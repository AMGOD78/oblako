from flask import Flask, render_template_string

app = Flask(__name__)

# Главная страница нашего сайта
@app.route("/")
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Моё Облачное Приложение</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f0f2f5; color: #333; text-align: center; padding-top: 100px; }
            .container { background-white: white; max-width: 500px; margin: 0 auto; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); background: #fff; }
            h1 { color: #007bff; }
            .status { display: inline-block; background-color: #28a745; color: white; padding: 5px 15px; border-radius: 20px; font-size: 14px; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Привет из облака! 🚀</h1>
            <p>Это веб-интерфейс нашего будущего приложения.
            ЧУПАПИ МУНЯНЯ</p>
            <div class="status">Статус: Работает локально</div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(debug=True)