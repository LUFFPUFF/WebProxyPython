from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            try:
                response = requests.get(url)
                print(f'Request URL: {url}, Response Status: {response.status_code}')
                return response.content
            except requests.RequestException as e:
                print(f'Error: {e}')
                return str(e), 500
    return '', 400

if __name__ == '__main__':
    app.run(debug=True)
