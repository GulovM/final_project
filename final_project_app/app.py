from flask import Flask, request, render_template_string

app = Flask(__name__)

# Главная страница с формой для ввода имени
@app.route('/')
def index():
    return render_template_string('''
        <form action="/greet" method="post">
            <label for="name">Введите ваше имя:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Отправить</button>
        </form>
    ''')

# Страница, которая приветствует пользователя по имени
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

