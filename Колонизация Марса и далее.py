from flask import Flask

app = Flask(__name__)


@app.route('/')
def index1():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index2():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    Человечество вырастает из детства.<br>
                    Человечеству мала одна планета.<br>
                    Мы сделаем обитаемыми безжизненные пока планеты.<br>
                    И начнем с Марса!<br>
                    Присоединяйся!
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
