/**
 * API Client for Adaptive English Sentence Reconstruction Game
 */

const API_BASE = window.API_BASE || localStorage.getItem("custom_api_base") || "";

class ApiClient {
  static getToken() {
    return localStorage.getItem("token") || null;
  }

  static setToken(token) {
    localStorage.setItem("token", token);
  }

  static removeToken() {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
  }

  static getUsername() {
    return localStorage.getItem("username") || "Guest";
  }

  static setUsername(username) {
    localStorage.setItem("username", username);
  }

  static async request(endpoint, options = {}) {
    const url = `${API_BASE}${endpoint}`;
    const headers = {
      "Content-Type": "application/json",
      ...(options.headers || {})
    };

    const token = this.getToken();
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }

    try {
      const response = await fetch(url, {
        ...options,
        headers
      });

      if (response.status === 401 && !endpoint.includes("/auth/")) {
        this.removeToken();
        window.location.reload();
        throw new Error("Sessiya tugadi. Iltimos qaytadan kiring.");
      }

      const text = await response.text();
      let data;
      try {
        data = JSON.parse(text);
      } catch {
        data = { detail: text };
      }

      if (!response.ok) {
        throw new Error(data.detail || data.message || `Server xatosi (${response.status})`);
      }

      return data;
    } catch (err) {
      console.error(`API Error on ${endpoint}:`, err);
      throw err;
    }
  }

  // Auth Endpoints
  static async register(username, password) {
    const res = await this.request("/api/auth/register", {
      method: "POST",
      body: JSON.stringify({ username, password })
    });
    this.setToken(res.access_token);
    this.setUsername(res.username);
    return res;
  }

  static async login(username, password) {
    const res = await this.request("/api/auth/login", {
      method: "POST",
      body: JSON.stringify({ username, password })
    });
    this.setToken(res.access_token);
    this.setUsername(res.username);
    return res;
  }

  static async getProfile() {
    return await this.request("/api/auth/me");
  }

  // Game Endpoints
  static async generateGame(level = null, topic = null, matrix_size = null) {
    return await this.request("/api/game/generate", {
      method: "POST",
      body: JSON.stringify({ level, topic, matrix_size })
    });
  }

  static async submitRound(round_id, active_time, mistake_count, is_correct = true, learned_words = []) {
    return await this.request("/api/game/submit-round", {
      method: "POST",
      body: JSON.stringify({
        round_id,
        active_time,
        mistake_count,
        is_correct,
        learned_words
      })
    });
  }

  // Progress Endpoints
  static async getProgressSummary() {
    return await this.request("/api/progress/summary");
  }

  static async getWeakWords() {
    return await this.request("/api/progress/weak-words");
  }

  static async markWordWeak(word) {
    return await this.request(`/api/progress/words/${encodeURIComponent(word)}/mark`, {
      method: "POST"
    });
  }

  static async unmarkWordWeak(word) {
    return await this.request(`/api/progress/words/${encodeURIComponent(word)}/mark`, {
      method: "DELETE"
    });
  }

  // Settings Endpoints
  static async getSettings() {
    return await this.request("/api/settings");
  }

  static async updateSettings(settingsData) {
    return await this.request("/api/settings", {
      method: "PUT",
      body: JSON.stringify(settingsData)
    });
  }
}

window.ApiClient = ApiClient;
