from flask import Flask, render_template, redirect
from WebApp4.views.register import register_blueprint
from WebApp4.views.list import list_blueprint

app = Flask(__name__)

# 블루프린트 모듈 등록
app.register_blueprint(register_blueprint)
app.register_blueprint(list_blueprint)

@app.route('/')
def index():
    return redirect('/register')


if __name__=='__main__':
    app.run()