from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Прокси-сервер работает!'

@app.route('/proxy', methods=['GET', 'POST'])
def proxy():
    url = request.args.get('url')  # Получаем URL из параметра запроса

    if not url:
        return jsonify({'error': 'Не указан URL'}), 400

    try:
        # Отправляем запрос к указанному URL и возвращаем результат
        response = requests.get(url, params=request.args, headers=request.headers)
        return response.content, response.status_code, response.headers.items()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
