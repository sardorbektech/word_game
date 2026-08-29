/**
 * Synthesized Web Audio API Sound Effects Engine
 */

class SoundEngine {
  constructor() {
    this.ctx = null;
    this.enabled = true;
  }

  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
      }
    }
  }

  ensureContext() {
    this.init();
    if (this.ctx && this.ctx.state === "suspended") {
      this.ctx.resume();
    }
  }

  playTileSelect(index = 0) {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    // Scale pitch based on chain length
    const baseFreq = 380;
    const freq = baseFreq + (index * 45);

    osc.type = "sine";
    osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(freq + 40, this.ctx.currentTime + 0.08);

    gain.gain.setValueAtTime(0.12, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.08);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.08);
  }

  playWordComplete() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    // Harmonic triad (C major: C5, E5, G5)
    const notes = [523.25, 659.25, 783.99];
    notes.forEach((freq, i) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = "triangle";
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime + (i * 0.05));

      gain.gain.setValueAtTime(0.15, this.ctx.currentTime + (i * 0.05));
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + (i * 0.05) + 0.25);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(this.ctx.currentTime + (i * 0.05));
      osc.stop(this.ctx.currentTime + (i * 0.05) + 0.25);
    });
  }

  playMistake() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = "sawtooth";
    osc.frequency.setValueAtTime(140, this.ctx.currentTime);
    osc.frequency.linearRampToValueAtTime(90, this.ctx.currentTime + 0.2);

    gain.gain.setValueAtTime(0.18, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.2);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start();
    osc.stop(this.ctx.currentTime + 0.2);
  }

  playVictory() {
    if (!this.enabled) return;
    this.ensureContext();
    if (!this.ctx) return;

    const melody = [
      { freq: 440.00, delay: 0.00, dur: 0.12 }, // A4
      { freq: 554.37, delay: 0.12, dur: 0.12 }, // C#5
      { freq: 659.25, delay: 0.24, dur: 0.14 }, // E5
      { freq: 880.00, delay: 0.38, dur: 0.35 }  // A5
    ];

    melody.forEach(note => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = "triangle";
      osc.frequency.setValueAtTime(note.freq, this.ctx.currentTime + note.delay);

      gain.gain.setValueAtTime(0.2, this.ctx.currentTime + note.delay);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + note.delay + note.dur);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(this.ctx.currentTime + note.delay);
      osc.stop(this.ctx.currentTime + note.delay + note.dur);
    });
  }
}

window.soundEngine = new SoundEngine();
