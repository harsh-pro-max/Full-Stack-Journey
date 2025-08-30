class TypingTest {
    constructor() {
        this.textDisplay = document.getElementById('text-display');
        this.textInput = document.getElementById('text-input');
        this.startBtn = document.getElementById('start-btn');
        this.resetBtn = document.getElementById('reset-btn');
        this.timeSelect = document.getElementById('time-select');
        this.timeElement = document.getElementById('time');
        this.wpmElement = document.getElementById('wpm');
        this.accuracyElement = document.getElementById('accuracy');
        this.resultsDiv = document.getElementById('results');
        this.leaderboardDiv = document.getElementById('leaderboard-list');
        this.saveResultBtn = document.getElementById('save-result');
        
        this.sampleTexts = [
            "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the alphabet and is commonly used for typing practice.",
            "In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat.",
            "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity.",
            "To be or not to be, that is the question. Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles.",
            "All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood."
        ];
        
        this.currentText = '';
        this.startTime = 0;
        this.endTime = 0;
        this.timerInterval = null;
        this.testDuration = 60;
        this.isTestActive = false;
        this.currentPosition = 0;
        this.errors = 0;
        this.totalChars = 0;
        
        this.initializeEventListeners();
        this.loadLeaderboard();
    }
    
    initializeEventListeners() {
        this.startBtn.addEventListener('click', () => this.startTest());
        this.resetBtn.addEventListener('click', () => this.resetTest());
        this.textInput.addEventListener('input', (e) => this.handleInput(e));
        this.textInput.addEventListener('keydown', (e) => this.handleKeydown(e));
        this.saveResultBtn.addEventListener('click', () => this.saveResult());
        this.timeSelect.addEventListener('change', (e) => {
            this.testDuration = parseInt(e.target.value);
            this.timeElement.textContent = this.testDuration + 's';
        });
    }
    
    startTest() {
        this.currentText = this.sampleTexts[Math.floor(Math.random() * this.sampleTexts.length)];
        this.textDisplay.innerHTML = this.highlightText();
        this.textInput.disabled = false;
        this.textInput.focus();
        this.textInput.value = '';
        this.startBtn.disabled = true;
        this.timeSelect.disabled = true;
        this.isTestActive = true;
        this.startTime = Date.now();
        this.currentPosition = 0;
        this.errors = 0;
        this.totalChars = 0;
        this.resultsDiv.style.display = 'none';
        
        this.startTimer();
    }
    
    resetTest() {
        this.isTestActive = false;
        this.textInput.disabled = true;
        this.textInput.value = '';
        this.startBtn.disabled = false;
        this.timeSelect.disabled = false;
        this.currentPosition = 0;
        this.errors = 0;
        this.totalChars = 0;
        this.timeElement.textContent = this.testDuration + 's';
        this.wpmElement.textContent = '0';
        this.accuracyElement.textContent = '100%';
        this.textDisplay.innerHTML = 'Click "Start Test" to begin typing';
        this.resultsDiv.style.display = 'none';
        
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }
    }
    
    startTimer() {
        let timeLeft = this.testDuration;
        this.timeElement.textContent = timeLeft + 's';
        
        this.timerInterval = setInterval(() => {
            timeLeft--;
            this.timeElement.textContent = timeLeft + 's';
            
            if (timeLeft <= 0) {
                this.endTest();
            }
        }, 1000);
    }
    
    handleInput(e) {
        if (!this.isTestActive) return;
        
        const inputText = e.target.value;
        this.currentPosition = inputText.length;
        this.totalChars = inputText.length;
        
        this.updateDisplay();
        this.calculateStats();
        
        if (inputText === this.currentText) {
            this.endTest();
        }
    }
    
    handleKeydown(e) {
        if (!this.isTestActive) return;
        
        // Prevent certain keys that might interfere with the test
        if (e.key === 'Tab' || e.key === 'Escape') {
            e.preventDefault();
        }
    }
    
    updateDisplay() {
        const inputText = this.textInput.value;
        let highlightedText = '';
        this.errors = 0;
        
        for (let i = 0; i < this.currentText.length; i++) {
            const char = this.currentText[i];
            
            if (i < inputText.length) {
                if (inputText[i] === char) {
                    highlightedText += `<span class="correct">${char}</span>`;
                } else {
                    highlightedText += `<span class="incorrect">${char}</span>`;
                    this.errors++;
                }
            } else if (i === inputText.length) {
                highlightedText += `<span class="current">${char}</span>`;
            } else {
                highlightedText += char;
            }
        }
        
        this.textDisplay.innerHTML = highlightedText;
    }
    
    highlightText() {
        return `<span class="current">${this.currentText[0]}</span>${this.currentText.slice(1)}`;
    }
    
    calculateStats() {
        const currentTime = Date.now();
        const timeElapsed = (currentTime - this.startTime) / 1000 / 60; // in minutes
        
        if (timeElapsed > 0) {
            const wordsTyped = this.totalChars / 5; // Average word length is 5 characters
            const wpm = Math.round(wordsTyped / timeElapsed);
            const accuracy = this.totalChars > 0 ? Math.round(((this.totalChars - this.errors) / this.totalChars) * 100) : 100;
            
            this.wpmElement.textContent = wpm;
            this.accuracyElement.textContent = accuracy + '%';
        }
    }
    
    endTest() {
        this.isTestActive = false;
        this.endTime = Date.now();
        this.textInput.disabled = true;
        this.startBtn.disabled = false;
        this.timeSelect.disabled = false;
        
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
        }
        
        this.showResults();
    }
    
    showResults() {
        const timeElapsed = (this.endTime - this.startTime) / 1000 / 60;
        const wordsTyped = this.totalChars / 5;
        const wpm = Math.round(wordsTyped / timeElapsed);
        const accuracy = this.totalChars > 0 ? Math.round(((this.totalChars - this.errors) / this.totalChars) * 100) : 100;
        const cpm = Math.round(this.totalChars / timeElapsed);
        
        document.getElementById('final-wpm').textContent = wpm;
        document.getElementById('final-accuracy').textContent = accuracy + '%';
        document.getElementById('final-cpm').textContent = cpm;
        document.getElementById('total-chars').textContent = this.totalChars;
        
        this.resultsDiv.style.display = 'block';
        this.resultsDiv.scrollIntoView({ behavior: 'smooth' });
        
        // Store current results for potential saving
        this.currentResults = {
            wpm: wpm,
            accuracy: accuracy,
            cpm: cpm,
            totalChars: this.totalChars,
            duration: this.testDuration,
            timestamp: new Date().toISOString()
        };
    }
    
    saveResult() {
        if (!this.currentResults) return;
        
        // Save to localStorage
        let savedResults = JSON.parse(localStorage.getItem('typingTestResults')) || [];
        savedResults.push(this.currentResults);
        savedResults.sort((a, b) => b.wpm - a.wpm); // Sort by WPM descending
        savedResults = savedResults.slice(0, 10); // Keep only top 10
        localStorage.setItem('typingTestResults', JSON.stringify(savedResults));
        
        // Also send to Python backend if available
        this.sendToBackend(this.currentResults);
        
        this.loadLeaderboard();
        alert('Result saved successfully!');
    }
    
    async sendToBackend(result) {
        try {
            const response = await fetch('/api/save-result', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(result)
            });
            
            if (response.ok) {
                console.log('Result saved to backend');
            }
        } catch (error) {
            console.log('Backend not available, using local storage only');
        }
    }
    
    loadLeaderboard() {
        let savedResults = JSON.parse(localStorage.getItem('typingTestResults')) || [];
        
        if (savedResults.length === 0) {
            this.leaderboardDiv.innerHTML = '<p>No results yet. Complete a test to see your scores!</p>';
            return;
        }
        
        let html = '';
        savedResults.forEach((result, index) => {
            const date = new Date(result.timestamp).toLocaleDateString();
            html += `
                <div class="leaderboard-item">
                    <div class="rank">#${index + 1}</div>
                    <div class="stats">
                        <span class="stat">WPM: ${result.wpm}</span>
                        <span class="stat">Accuracy: ${result.accuracy}%</span>
                        <span class="stat">Date: ${date}</span>
                    </div>
                </div>
            `;
        });
        
        this.leaderboardDiv.innerHTML = html;
    }
}

// Initialize the typing test when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new TypingTest();
});
