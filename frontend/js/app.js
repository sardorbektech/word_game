/**
 * Application Main Controller
 */

window.exitCurrentGame = function() {
  if (window.matrixGame && typeof window.matrixGame.directExit === "function") {
    window.matrixGame.directExit();
  } else if (window.app && typeof window.app.showScreen === "function") {
    if (window.matrixGame && typeof window.matrixGame.stopTimer === "function") {
      window.matrixGame.stopTimer();
    }
    window.app.showScreen("dashboard");
    window.app.loadDashboardData();
  } else {
    window.location.reload();
  }
};

class AppController {
  constructor() {
    this.currentScreen = "dashboard";
    this.userProfile = null;
    this.progressSummary = null;
    this.userSettings = null;
    this.activeGameLevel = "A1";

    this.initEventListeners();
  }

  async init() {
    // Check if token exists
    const token = ApiClient.getToken();
    if (token) {
      try {
        await this.loadUserProfile();
        await this.loadDashboardData();
        this.showScreen("dashboard");
      } catch (e) {
        console.warn("Auto-login failed:", e);
        this.openModal("auth-modal");
      }
    } else {
      this.openModal("auth-modal");
    }
  }

  initEventListeners() {
    // Brand click returns to dashboard
    const brand = document.getElementById("brand-logo");
    if (brand) {
      brand.addEventListener("click", () => {
        window.matrixGame.stopTimer();
        this.loadDashboardData();
        this.showScreen("dashboard");
      });
    }

    // Auth Form Tabs
    const tabLogin = document.getElementById("tab-login");
    const tabRegister = document.getElementById("tab-register");
    const formLogin = document.getElementById("form-login");
    const formRegister = document.getElementById("form-register");

    if (tabLogin && tabRegister) {
      tabLogin.addEventListener("click", () => {
        tabLogin.classList.add("btn-primary");
        tabLogin.classList.remove("btn-secondary");
        tabRegister.classList.add("btn-secondary");
        tabRegister.classList.remove("btn-primary");
        formLogin.style.display = "flex";
        formRegister.style.display = "none";
      });

      tabRegister.addEventListener("click", () => {
        tabRegister.classList.add("btn-primary");
        tabRegister.classList.remove("btn-secondary");
        tabLogin.classList.add("btn-secondary");
        tabLogin.classList.remove("btn-primary");
        formRegister.style.display = "flex";
        formLogin.style.display = "none";
      });
    }

    // Login Submit
    if (formLogin) {
      formLogin.addEventListener("submit", async (e) => {
        e.preventDefault();
        const u = document.getElementById("login-username").value.trim();
        const p = document.getElementById("login-password").value;
        const errEl = document.getElementById("auth-error");
        errEl.textContent = "";

        try {
          await ApiClient.login(u, p);
          this.closeModal("auth-modal");
          await this.loadUserProfile();
          await this.loadDashboardData();
          this.showScreen("dashboard");
        } catch (err) {
          errEl.textContent = err.message || "Kirishda xatolik yuz berdi.";
        }
      });
    }

    // Register Submit
    if (formRegister) {
      formRegister.addEventListener("submit", async (e) => {
        e.preventDefault();
        const u = document.getElementById("reg-username").value.trim();
        const p = document.getElementById("reg-password").value;
        const errEl = document.getElementById("auth-error");
        errEl.textContent = "";

        try {
          await ApiClient.register(u, p);
          this.closeModal("auth-modal");
          await this.loadUserProfile();
          await this.loadDashboardData();
          this.showScreen("dashboard");
        } catch (err) {
          errEl.textContent = err.message || "Ro'yxatdan o'tishda xatolik yuz berdi.";
        }
      });
    }

    // Game Action Buttons
    const btnPause = document.getElementById("btn-pause");
    if (btnPause) {
      btnPause.addEventListener("click", () => window.matrixGame.togglePause());
    }

    const btnResume = document.getElementById("btn-resume");
    if (btnResume) {
      btnResume.addEventListener("click", () => window.matrixGame.togglePause());
    }

    const btnLearn = document.getElementById("btn-learn-word");
    if (btnLearn) {
      btnLearn.addEventListener("click", () => window.matrixGame.markCurrentWordAsLearned());
    }

    const btnNextRound = document.getElementById("btn-next-round");
    if (btnNextRound) {
      btnNextRound.addEventListener("click", () => {
        this.closeModal("result-modal");
        this.startNewGame(this.activeGameLevel);
      });
    }

    const btnExitGame = document.getElementById("btn-exit-game");
    if (btnExitGame) {
      btnExitGame.addEventListener("click", () => window.matrixGame.showExitModal());
    }

    // Header buttons
    const btnWeakWords = document.getElementById("btn-weak-words");
    if (btnWeakWords) {
      btnWeakWords.addEventListener("click", () => this.openWeakWordsModal());
    }

    const btnSettings = document.getElementById("btn-settings");
    if (btnSettings) {
      btnSettings.addEventListener("click", () => this.openSettingsModal());
    }

    // Settings Save Form
    const formSettings = document.getElementById("form-settings");
    if (formSettings) {
      formSettings.addEventListener("submit", async (e) => {
        e.preventDefault();
        const topic = document.getElementById("settings-topic").value;
        const sound = document.getElementById("settings-sound").checked;

        try {
          await ApiClient.updateSettings({
            preferred_matrix_size: "auto",
            preferred_topic: topic,
            sound_enabled: sound
          });
          window.soundEngine.enabled = sound;
          this.closeModal("settings-modal");
          alert("Sozlamalar saqlandi!");
        } catch (err) {
          alert("Sozlamalarni saqlashda xatolik: " + err.message);
        }
      });
    }

    // Logout
    const btnLogout = document.getElementById("btn-logout");
    if (btnLogout) {
      btnLogout.addEventListener("click", () => {
        ApiClient.removeToken();
        window.location.reload();
      });
    }
  }

  showScreen(screenId) {
    document.querySelectorAll(".screen-view").forEach(el => el.classList.remove("active"));
    const target = document.getElementById(`screen-${screenId}`);
    if (target) {
      target.classList.add("active");
      this.currentScreen = screenId;
    }
  }

  openModal(modalId) {
    const m = document.getElementById(modalId);
    if (m) m.classList.add("active");
  }

  closeModal(modalId) {
    const m = document.getElementById(modalId);
    if (m) m.classList.remove("active");
  }

  async loadUserProfile() {
    try {
      this.userProfile = await ApiClient.getProfile();
      const userBadge = document.getElementById("user-name-badge");
      if (userBadge) {
        userBadge.textContent = `👤 ${this.userProfile.username}`;
      }
      this.userSettings = await ApiClient.getSettings();
      window.soundEngine.enabled = this.userSettings.sound_enabled;
    } catch (e) {
      console.error(e);
    }
  }

  async loadDashboardData() {
    try {
      this.progressSummary = await ApiClient.getProgressSummary();
      this.renderLevelCards();
      this.renderDashboardStats();
    } catch (e) {
      console.error("Failed to load progress summary:", e);
    }
  }

  renderDashboardStats() {
    if (!this.progressSummary) return;
    const gamesEl = document.getElementById("stat-total-games");
    const weakEl = document.getElementById("stat-weak-words");
    const activeLevelEl = document.getElementById("stat-current-level");

    if (gamesEl) gamesEl.textContent = this.progressSummary.total_games_played;
    if (weakEl) weakEl.textContent = this.progressSummary.total_weak_words;
    if (activeLevelEl) activeLevelEl.textContent = this.progressSummary.current_level;

    // Header badge
    const headerLevel = document.getElementById("header-level-badge");
    if (headerLevel) headerLevel.textContent = `🏆 ${this.progressSummary.current_level}`;
  }

  renderLevelCards() {
    const grid = document.getElementById("levels-grid");
    if (!grid || !this.progressSummary) return;
    grid.innerHTML = "";

    const levelDescriptions = {
      "A1": "Beginner (Boshlang'ich)",
      "A2": "Elementary (Oddiy muloqot)",
      "B1": "Intermediate (O'rta daraja)",
      "B2": "Upper-Intermediate (Mustaqil)",
      "C1": "Advanced (Yuqori daraja)"
    };

    this.progressSummary.levels.forEach(lvl => {
      const card = document.createElement("div");
      card.className = "level-card";
      if (lvl.level === this.progressSummary.current_level) {
        card.classList.add("selected");
      }

      card.innerHTML = `
        <div class="level-tag">${lvl.level}</div>
        <div class="level-name">${levelDescriptions[lvl.level] || ""}</div>
        <div class="level-meter">
          <div class="level-meter-fill" style="width: ${Math.round(lvl.difficulty_score * 100)}%;"></div>
        </div>
        <div class="level-meta">
          <div>Qiyinlik: <b>${lvl.difficulty_score.toFixed(2)}</b></div>
          <div>O'yinlar: <b>${lvl.total_games}</b> | Aniqlik: <b>${Math.round(lvl.accuracy)}%</b></div>
        </div>
        <button class="btn btn-primary" style="margin-top: 14px; width: 100%; font-size: 13px;">
          ▶ O'ynash
        </button>
      `;

      card.addEventListener("click", () => {
        this.selectLevelAndPlay(lvl.level);
      });

      grid.appendChild(card);
    });
  }

  async selectLevelAndPlay(level) {
    this.activeGameLevel = level;
    try {
      await ApiClient.updateSettings({ current_level: level });
    } catch (e) {
      console.warn("Could not update settings:", e);
    }
    this.startNewGame(level);
  }

  async startNewGame(level = null) {
    const targetLevel = level || this.activeGameLevel || "A1";
    this.activeGameLevel = targetLevel;

    // Immediately reflect selected level in top header
    const headerLevel = document.getElementById("header-level-badge");
    if (headerLevel) headerLevel.textContent = `🏆 ${targetLevel}`;

    try {
      this.showScreen("game");
      const roundData = await ApiClient.generateGame(targetLevel);
      if (roundData && roundData.level) {
        this.activeGameLevel = roundData.level;
        if (headerLevel) headerLevel.textContent = `🏆 ${roundData.level}`;
      }
      window.matrixGame.loadRound(roundData);
    } catch (err) {
      alert("O'yinni yuklashda xatolik: " + err.message);
      this.showScreen("dashboard");
    }
  }

  showRoundResult(response, roundData) {
    const modal = document.getElementById("result-modal");
    if (!modal) return;

    document.getElementById("res-accuracy").textContent = `${Math.round(response.accuracy)}%`;
    document.getElementById("res-time").textContent = `${response.active_time}s`;
    document.getElementById("res-mistakes").textContent = response.mistakes;
    
    const deltaPrefix = response.difficulty_delta >= 0 ? "+" : "";
    document.getElementById("res-difficulty").textContent = 
      `${response.new_difficulty.toFixed(2)} (${deltaPrefix}${response.difficulty_delta.toFixed(2)})`;

    document.getElementById("res-feedback").textContent = response.message || "Ajoyib natija!";

    this.openModal("result-modal");
  }

  async openWeakWordsModal() {
    this.openModal("weak-words-modal");
    const container = document.getElementById("weak-words-container");
    if (!container) return;
    container.innerHTML = `<div style="text-align: center; color: var(--text-dim);">Yuklanmoqda...</div>`;

    try {
      const words = await ApiClient.getWeakWords();
      if (words.length === 0) {
        container.innerHTML = `<div style="text-align: center; color: var(--accent-emerald); padding: 20px;">Hozircha zaif so'zlar yo'q! Hammasi a'lo darajada.</div>`;
        return;
      }

      container.innerHTML = "";
      words.forEach(w => {
        const item = document.createElement("div");
        item.className = "weak-word-item";
        const trText = w.translation ? ` — <span style="color: var(--accent-cyan); font-weight: 600;">${w.translation}</span>` : "";
        item.innerHTML = `
          <div>
            <div style="font-weight: 700; font-size: 15px; color: #fff;">
              ${w.word}${trText}
            </div>
            <div style="font-size: 12px; color: var(--text-dim); margin-top: 2px;">
              Xatolar: <b>${w.wrong_count}</b> | To'g'ri: <b>${w.correct_count}</b>
            </div>
          </div>
          <div style="display: flex; align-items: center; gap: 12px;">
            <div class="word-strength-bar" title="O'zlashtirish: ${w.strength}%">
              <div class="word-strength-fill" style="width: ${w.strength}%;"></div>
            </div>
            <button class="btn btn-secondary" style="padding: 4px 8px; font-size: 11px;" onclick="window.app.removeWeakWord('${w.word}')">
              O'chirish
            </button>
          </div>
        `;
        container.appendChild(item);
      });
    } catch (e) {
      container.innerHTML = `<div style="color: var(--accent-red);">Yuklashda xatolik yuz berdi.</div>`;
    }
  }

  async removeWeakWord(word) {
    try {
      await ApiClient.unmarkWordWeak(word);
      this.openWeakWordsModal();
    } catch (e) {
      console.error(e);
    }
  }

  async openSettingsModal() {
    this.openModal("settings-modal");
    try {
      const settings = await ApiClient.getSettings();
      document.getElementById("settings-topic").value = settings.preferred_topic || "General";
      document.getElementById("settings-sound").checked = settings.sound_enabled;
    } catch (e) {
      console.error(e);
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  window.app = new AppController();
  window.app.init();
});
