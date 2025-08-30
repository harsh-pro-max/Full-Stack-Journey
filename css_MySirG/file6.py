from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
import sqlite3

app = Flask(__name__)
CORS(app)

# Database setup
def init_db():
    conn = sqlite3.connect('typing_results.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wpm INTEGER,
            accuracy INTEGER,
            cpm INTEGER,
            total_chars INTEGER,
            duration INTEGER,
            timestamp DATETIME,
            ip_address TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('file6.html')

@app.route('/api/save-result', methods=['POST'])
def save_result():
    try:
        data = request.get_json()
        
        # Validate data
        required_fields = ['wpm', 'accuracy', 'cpm', 'totalChars', 'duration']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Save to database
        conn = sqlite3.connect('typing_results.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO results (wpm, accuracy, cpm, total_chars, duration, timestamp, ip_address)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['wpm'],
            data['accuracy'],
            data['cpm'],
            data['totalChars'],
            data['duration'],
            datetime.now().isoformat(),
            request.remote_addr
        ))
        
        conn.commit()
        conn.close()
        
        return jsonify({'message': 'Result saved successfully'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/leaderboard')
def get_leaderboard():
    try:
        conn = sqlite3.connect('typing_results.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT wpm, accuracy, cpm, total_chars, duration, timestamp
            FROM results
            ORDER BY wpm DESC
            LIMIT 10
        ''')
        
        results = cursor.fetchall()
        conn.close()
        
        leaderboard = []
        for result in results:
            leaderboard.append({
                'wpm': result[0],
                'accuracy': result[1],
                'cpm': result[2],
                'totalChars': result[3],
                'duration': result[4],
                'timestamp': result[5]
            })
        
        return jsonify(leaderboard), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stats')
def get_stats():
    try:
        conn = sqlite3.connect('typing_results.db')
        cursor = conn.cursor()
        
        # Get total tests
        cursor.execute('SELECT COUNT(*) FROM results')
        total_tests = cursor.fetchone()[0]
        
        # Get average WPM
        cursor.execute('SELECT AVG(wpm) FROM results')
        avg_wpm = cursor.fetchone()[0] or 0
        
        # Get highest WPM
        cursor.execute('SELECT MAX(wpm) FROM results')
        max_wpm = cursor.fetchone()[0] or 0
        
        # Get average accuracy
        cursor.execute('SELECT AVG(accuracy) FROM results')
        avg_accuracy = cursor.fetchone()[0] or 0
        
        conn.close()
        
        stats = {
            'total_tests': total_tests,
            'avg_wpm': round(avg_wpm, 1),
            'max_wpm': max_wpm,
            'avg_accuracy': round(avg_accuracy, 1)
        }
        
        return jsonify(stats), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
