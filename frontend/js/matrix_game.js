/**
 * Matrix Game Engine - Boggle / Word Hunt Swipe Mechanics with Grammatical Order
 */

class MatrixGameEngine {
  constructor() {
    this.roundData = null;
    this.currentWordIndex = 0;
    this.selectedPath = []; // Array of {row, col, char, element}
    this.isDragging = false;
    this.mistakeCount = 0;
    this.learnedWordsInRound = new Set();
    this.wordHintsCount = {}; // Map of wordIndex -> count of hints requested
    
    // Timer state
    this.activeTimeSeconds = 0;
    this.timerInterval = null;
    this.isPaused = false;
    
    // DOM references
    this.gridContainer = document.getElementById("matrix-grid");
    this.svgOverlay = document.getElementById("svg-overlay");
    this.sourceSentenceEl = document.getElementById("source-sentence");
    this.assemblyBarEl = document.getElementById("assembly-bar");
    this.liveTrayEl = document.getElementById("live-swiped-text");
    this.timerDisplayEl = document.getElementById("timer-display");
    this.topicBadgeEl = document.getElementById("game-topic-badge");
    this.difficultyBadgeEl = document.getElementById("game-difficulty-badge");
    this.sourceBadgeEl = document.getElementById("game-source-badge");
    
    this.initGlobalListeners();
  }

  initGlobalListeners() {
    // End dragging when mouse leaves window or is released
    window.addEventListener("mouseup", () => this.handleDragEnd());
    window.addEventListener("touchend", () => this.handleDragEnd());
    window.addEventListener("touchcancel", () => this.handleDragEnd());

    // Prevent default touch gestures (scrolling) during grid drag
    const matrixWrapper = document.getElementById("matrix-wrapper");
    if (matrixWrapper) {
      matrixWrapper.addEventListener("touchmove", (e) => {
        if (this.isDragging) {
          e.preventDefault();
          this.handleTouchMove(e);
        }
      }, { passive: false });
    }
  }

  loadRound(roundData) {
    this.roundData = roundData;
    this.currentWordIndex = 0;
    this.selectedPath = [];
    this.isDragging = false;
    this.mistakeCount = 0;
    this.learnedWordsInRound.clear();
    this.wordHintsCount = {};
    this.activeTimeSeconds = 0;
    this.isPaused = false;

    this.renderHeaderInfo();
    this.renderAssemblyBar();
    this.renderGrid();
    this.clearLiveTray();
    this.startTimer();
  }

  renderHeaderInfo() {
    const srcEl = document.getElementById("source-sentence");
    if (srcEl && this.roundData) {
      srcEl.textContent = this.roundData.source_text;
    }

    const isAi = this.roundData && this.roundData.content_source === "ai";

    const sourceDot = document.getElementById("arena-source-dot");
    if (sourceDot) {
      sourceDot.className = isAi ? "ai-status-dot online" : "ai-status-dot offline";
      sourceDot.title = isAi ? "AI Online" : "AI Offline";
    }

    const headerLevel = document.getElementById("header-level-badge");
    if (headerLevel && this.roundData && this.roundData.level) {
      headerLevel.textContent = `🏆 ${this.roundData.level}`;
    }

    const gameLvlTag = document.getElementById("game-level-tag");
    if (gameLvlTag && this.roundData && this.roundData.level) {
      gameLvlTag.textContent = this.roundData.level;
    }
  }

  directExit() {
    this.stopTimer();
    this.roundData = null;
    this.selectedPath = [];
    this.clearSvgLines();
    this.clearLiveTray();
    document.body.classList.remove("in-game");

    if (this.gridContainer) this.gridContainer.innerHTML = "";
    if (this.assemblyBarEl) this.assemblyBarEl.innerHTML = "";

    // Close any active modal
    document.querySelectorAll(".modal-overlay").forEach(m => m.classList.remove("active"));

    if (window.app) {
      window.app.showScreen("dashboard");
      window.app.loadDashboardData();
    }
  }

  exitGame() {
    this.directExit();
  }

  showExitModal() {
    this.directExit();
  }

  cancelExit() {
    this.isPaused = false;
    const modal = document.getElementById("exit-confirm-modal");
    if (modal) modal.classList.remove("active");
  }

  confirmExit() {
    this.directExit();
  }

  getSlotText(item, index) {
    if (index < this.currentWordIndex) {
      return item.word;
    }
    const hints = this.wordHintsCount[index] || 0;
    const chars = item.word.split("");
    return chars.map((ch, i) => (i < hints ? ch : "_")).join(" ");
  }

  renderAssemblyBar() {
    if (!this.assemblyBarEl || !this.roundData) return;
    this.assemblyBarEl.innerHTML = "";

    this.roundData.words.forEach((item, index) => {
      const slot = document.createElement("div");
      slot.className = "word-slot";
      slot.id = `slot-word-${index}`;

      if (index < this.currentWordIndex) {
        slot.classList.add("completed");
      } else if (index === this.currentWordIndex) {
        slot.classList.add("active");
      } else {
        slot.classList.add("pending");
      }

      slot.textContent = this.getSlotText(item, index);
      this.assemblyBarEl.appendChild(slot);
    });
  }

  updateAssemblyBarSlots() {
    if (!this.roundData) return;
    this.roundData.words.forEach((item, index) => {
      const slot = document.getElementById(`slot-word-${index}`);
      if (!slot) return;

      slot.className = "word-slot";
      if (index < this.currentWordIndex) {
        slot.classList.add("completed");
      } else if (index === this.currentWordIndex) {
        slot.classList.add("active");
      } else {
        slot.classList.add("pending");
      }

      slot.textContent = this.getSlotText(item, index);
    });
  }

  renderGrid() {
    if (!this.gridContainer || !this.roundData) return;
    this.gridContainer.innerHTML = "";
    this.clearSvgLines();

    const dimension = this.roundData.grid_dimension || this.roundData.grid.length;
    this.gridContainer.style.gridTemplateColumns = `repeat(${dimension}, 1fr)`;
    this.gridContainer.style.gridTemplateRows = `repeat(${dimension}, 1fr)`;

    let gapSize = "6px";
    let fontSize = "22px";
    let borderRadius = "8px";

    if (dimension <= 6) {
      gapSize = "6px";
      fontSize = "clamp(16px, 4.4vw, 24px)";
      borderRadius = "8px";
    } else if (dimension === 7) {
      gapSize = "5px";
      fontSize = "clamp(14px, 3.8vw, 20px)";
      borderRadius = "7px";
    } else if (dimension === 8) {
      gapSize = "4px";
      fontSize = "clamp(12px, 3.2vw, 17px)";
      borderRadius = "6px";
    } else if (dimension === 9) {
      gapSize = "3px";
      fontSize = "clamp(11px, 2.7vw, 15px)";
      borderRadius = "5px";
    } else {
      gapSize = "2px";
      fontSize = "clamp(10px, 2.2vw, 13px)";
      borderRadius = "4px";
    }

    this.gridContainer.style.gap = gapSize;

    for (let r = 0; r < dimension; r++) {
      for (let c = 0; c < dimension; c++) {
        const char = this.roundData.grid[r][c] || "A";
        const tile = document.createElement("div");
        tile.className = "matrix-tile matrix-cell";
        tile.textContent = char;
        tile.dataset.row = r;
        tile.dataset.col = c;
        tile.dataset.char = char;
        tile.style.fontSize = fontSize;
        tile.style.borderRadius = borderRadius;

        // Mouse Listeners
        tile.addEventListener("mousedown", (e) => {
          e.preventDefault();
          this.handleDragStart(r, c, char, tile);
        });

        tile.addEventListener("mouseenter", () => {
          if (this.isDragging) {
            this.handleDragEnter(r, c, char, tile);
          }
        });

        // Touch Listeners
        tile.addEventListener("touchstart", (e) => {
          e.preventDefault();
          this.handleDragStart(r, c, char, tile);
        }, { passive: false });

        this.gridContainer.appendChild(tile);
      }
    }
  }

  playSound(action, param) {
    if (window.soundEngine) {
      try {
        if (action === "select" && typeof window.soundEngine.playTileSelect === "function") {
          window.soundEngine.playTileSelect(param || 0);
        } else if (action === "complete" && typeof window.soundEngine.playWordComplete === "function") {
          window.soundEngine.playWordComplete();
        } else if (action === "mistake" && typeof window.soundEngine.playMistake === "function") {
          window.soundEngine.playMistake();
        } else if (action === "victory" && typeof window.soundEngine.playVictory === "function") {
          window.soundEngine.playVictory();
        } else if (action === "hint" && typeof window.soundEngine.playHint === "function") {
          window.soundEngine.playHint();
        }
      } catch (e) {
        console.warn("Sound playback skipped:", e);
      }
    }
  }

  handleDragStart(row, col, char, tile) {
    if (this.isPaused) return;
    if (window.soundEngine && typeof window.soundEngine.ensureContext === "function") {
      try { window.soundEngine.ensureContext(); } catch (e) {}
    }

    this.isDragging = true;
    this.selectedPath = [{ row, col, char, element: tile }];
    tile.classList.add("selected");
    
    this.playSound("select", 0);
    this.updateLiveTray();
    this.drawSvgLines();
  }

  handleDragEnter(row, col, char, tile) {
    if (!this.isDragging || this.isPaused) return;

    const last = this.selectedPath[this.selectedPath.length - 1];

    // Check if backtracking to previous tile (undo last step)
    if (this.selectedPath.length > 1) {
      const prev = this.selectedPath[this.selectedPath.length - 2];
      if (prev.row === row && prev.col === col) {
        const removed = this.selectedPath.pop();
        removed.element.classList.remove("selected");
        this.updateLiveTray();
        this.drawSvgLines();
        this.playSound("select", this.selectedPath.length - 1);
        return;
      }
    }

    // Check if cell already in path (prevent looping on itself)
    const alreadyVisited = this.selectedPath.some(p => p.row === row && p.col === col);
    if (alreadyVisited) return;

    // Check adjacency (4 orthogonal directions only: Up, Down, Left, Right - NO diagonals)
    const dr = Math.abs(row - last.row);
    const dc = Math.abs(col - last.col);

    if (dr + dc === 1) {
      this.selectedPath.push({ row, col, char, element: tile });
      tile.classList.add("selected");
      this.playSound("select", this.selectedPath.length - 1);
      this.updateLiveTray();
      this.drawSvgLines();
    }
  }

  handleTouchMove(e) {
    if (!this.isDragging || this.isPaused) return;
    const touch = e.touches[0];
    const targetEl = document.elementFromPoint(touch.clientX, touch.clientY);
    
    if (targetEl && targetEl.classList.contains("matrix-tile")) {
      const row = parseInt(targetEl.dataset.row);
      const col = parseInt(targetEl.dataset.col);
      const char = targetEl.dataset.char;
      this.handleDragEnter(row, col, char, targetEl);
    }
  }

  handleDragEnd() {
    if (!this.isDragging) return;
    this.isDragging = false;

    if (this.selectedPath.length === 0) return;

    const swipedWord = this.selectedPath.map(p => p.char).join("").toUpperCase();
    const expectedTarget = this.roundData.words[this.currentWordIndex];

    if (!expectedTarget) return;

    const expectedCleanWord = expectedTarget.word.replace(/[^a-zA-Z0-9'-]/g, "").toUpperCase();

    if (swipedWord === expectedCleanWord) {
      // SUCCESS: Correct grammatical word found!
      this.handleWordSuccess(expectedTarget.word);
    } else {
      // MISTAKE: Incorrect word or out of grammatical sequence
      this.handleWordMistake(swipedWord);
    }
  }

  handleWordSuccess(wordText) {
    this.playSound("complete");

    // Flash green on path tiles
    this.selectedPath.forEach(p => {
      p.element.classList.remove("selected");
      p.element.classList.add("correct-flash");
      setTimeout(() => p.element.classList.remove("correct-flash"), 400);
    });

    this.clearSvgLines();
    this.selectedPath = [];

    this.currentWordIndex++;
    this.updateAssemblyBarSlots();
    this.clearLiveTray();

    // Check if entire sentence is completed
    if (this.currentWordIndex >= this.roundData.words.length) {
      this.completeRound();
    }
  }

  handleWordMistake(swipedWord) {
    this.mistakeCount++;
    this.playSound("mistake");

    // Flash red on path tiles
    this.selectedPath.forEach(p => {
      p.element.classList.remove("selected");
      p.element.classList.add("wrong-flash");
      setTimeout(() => p.element.classList.remove("wrong-flash"), 400);
    });

    this.clearSvgLines();
    this.selectedPath = [];
    this.clearLiveTray();
  }

  updateLiveTray() {
    if (!this.liveTrayEl) return;
    this.liveTrayEl.innerHTML = "";
    this.selectedPath.forEach(p => {
      const span = document.createElement("span");
      span.textContent = p.char;
      this.liveTrayEl.appendChild(span);
    });
  }

  clearLiveTray() {
    if (this.liveTrayEl) {
      this.liveTrayEl.innerHTML = "";
    }
  }

  drawSvgLines() {
    if (!this.svgOverlay || this.selectedPath.length <= 1) {
      this.clearSvgLines();
      return;
    }

    const wrapperRect = this.svgOverlay.getBoundingClientRect();
    const points = this.selectedPath.map(p => {
      const rect = p.element.getBoundingClientRect();
      const x = rect.left + rect.width / 2 - wrapperRect.left;
      const y = rect.top + rect.height / 2 - wrapperRect.top;
      return `${x},${y}`;
    }).join(" ");

    this.svgOverlay.innerHTML = `
      <polyline
        points="${points}"
        fill="none"
        stroke="#00f2fe"
        stroke-width="5"
        stroke-linecap="round"
        stroke-linejoin="round"
        style="filter: drop-shadow(0 0 8px rgba(0, 242, 254, 0.8)); opacity: 0.85;"
      />
    `;
  }

  clearSvgLines() {
    if (this.svgOverlay) {
      this.svgOverlay.innerHTML = "";
    }
  }

  giveHint() {
    if (!this.roundData || this.currentWordIndex >= this.roundData.words.length) return;
    const currentItem = this.roundData.words[this.currentWordIndex];
    if (!currentItem) return;

    const wordLen = currentItem.word.length;
    const currentHints = this.wordHintsCount[this.currentWordIndex] || 0;

    if (currentHints >= wordLen) {
      return;
    }

    const nextHints = currentHints + 1;
    this.wordHintsCount[this.currentWordIndex] = nextHints;

    // Rule: "so'zni esa zaif so'zlar 2-harfni ham so'ragandan keyin qo'shilsin"
    if (nextHints >= 2 && !this.learnedWordsInRound.has(currentItem.word)) {
      this.learnedWordsInRound.add(currentItem.word);
      ApiClient.markWordWeak(currentItem.word).catch(console.error);
    }

    // Update the assembly slot display
    this.updateAssemblyBarSlots();

    // Highlight matrix tile for the revealed letter
    if (currentItem.path && currentItem.path[nextHints - 1]) {
      const [r, c] = currentItem.path[nextHints - 1];
      const tile = document.querySelector(`.matrix-tile[data-row="${r}"][data-col="${c}"]`);
      if (tile) {
        tile.classList.add("hint-flash");
        setTimeout(() => tile.classList.remove("hint-flash"), 1200);
      }
    }

    this.playSound("hint");
  }

  markCurrentWordAsLearned() {
    this.giveHint();
  }

  startTimer() {
    this.stopTimer();
    this.timerInterval = setInterval(() => {
      if (!this.isPaused) {
        this.activeTimeSeconds += 0.1;
        this.updateTimerDisplay();
      }
    }, 100);
  }

  stopTimer() {
    if (this.timerInterval) {
      clearInterval(this.timerInterval);
      this.timerInterval = null;
    }
  }

  updateTimerDisplay() {
    if (!this.timerDisplayEl) return;
    const totalSec = Math.floor(this.activeTimeSeconds);
    const mins = String(Math.floor(totalSec / 60)).padStart(2, "0");
    const secs = String(totalSec % 60).padStart(2, "0");
    this.timerDisplayEl.textContent = `${mins}:${secs}`;
  }

  togglePause() {
    this.isPaused = !this.isPaused;
    const modal = document.getElementById("pause-modal");
    if (modal) {
      if (this.isPaused) {
        modal.classList.add("active");
      } else {
        modal.classList.remove("active");
      }
    }
  }

  async completeRound() {
    this.stopTimer();
    this.playSound("victory");

    try {
      const response = await ApiClient.submitRound(
        this.roundData.round_id,
        parseFloat(this.activeTimeSeconds.toFixed(1)),
        this.mistakeCount,
        true,
        Array.from(this.learnedWordsInRound)
      );

      // Open victory / result modal
      window.app.showRoundResult(response, this.roundData);
    } catch (err) {
      console.error("Error submitting round:", err);
      alert("Natijani saqlashda xatolik yuz berdi.");
    }
  }
}

window.matrixGame = new MatrixGameEngine();

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
