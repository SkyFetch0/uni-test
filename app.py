from flask import Flask, jsonify
import subprocess
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World2</title>
        <style>
            body { font-family: Arial; margin: 50px; background: #f5f5f5; }
            .container { max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; }
            .status { background: #e8f5e9; padding: 15px; border-radius: 5px; margin: 20px 0; }
            button { background: #2196F3; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; margin: 5px; }
            button:hover { background: #1976D2; }
            .info { font-family: monospace; background: #f0f0f0; padding: 10px; border-radius: 3px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 GitHub Demo Website</h1>
            <div class="status" id="status">Sistem durumu yükleniyor...</div>
            <button onclick="checkStatus()">Durumu Kontrol Et</button>
            <button onclick="updateCode()">Kodu Güncelle</button>
            <div class="info" id="info"></div>
        </div>
        
        <script>
            async function checkStatus() {
                try {
                    const response = await fetch('/api/status');
                    const data = await response.json();
                    document.getElementById('status').innerHTML = 
                        `✅ Sistem Çalışıyor<br>Son Güncelleme: ${new Date(data.timestamp).toLocaleString()}`;
                    document.getElementById('info').innerHTML = 
                        `Git Hash: ${data.git_hash}<br>Branch: ${data.git_branch}`;
                } catch (error) {
                    document.getElementById('status').innerHTML = '❌ Hata: ' + error.message;
                }
            }
            
            async function updateCode() {
                document.getElementById('status').innerHTML = '🔄 Güncelleniyor...';
                try {
                    const response = await fetch('/api/update');
                    const data = await response.json();
                    document.getElementById('status').innerHTML = 
                        data.status === 'success' ? '✅ Kod güncellendi!' : '❌ Güncelleme hatası!';
                    document.getElementById('info').innerHTML = data.output || data.error || '';
                } catch (error) {
                    document.getElementById('status').innerHTML = '❌ Hata: ' + error.message;
                }
            }
            
            // Sayfa yüklendiğinde durumu kontrol et
            checkStatus();
        </script>
    </body>
    </html>
    '''

@app.route('/api/status')
def status():
    try:
        git_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], 
                                         stderr=subprocess.DEVNULL).decode().strip()
        git_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], 
                                           stderr=subprocess.DEVNULL).decode().strip()
    except:
        git_hash = 'N/A'
        git_branch = 'N/A'
    
    return jsonify({
        'status': 'running',
        'timestamp': datetime.datetime.now().isoformat(),
        'git_hash': git_hash,
        'git_branch': git_branch
    })

@app.route('/api/update')
def update():
    try:
        result = subprocess.run(['git', 'pull', 'origin', 'main'], 
                              capture_output=True, text=True)
        
        return jsonify({
            'status': 'success' if result.returncode == 0 else 'error',
            'output': result.stdout + result.stderr
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)