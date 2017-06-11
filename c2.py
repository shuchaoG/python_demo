# -*- encodind=UTF-8 -*-

from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/index/')
@app.route('/')
def index():
    return 'hello'

@app.route('/profile/<int:uid>/',methods=['get','post'])
def profile(uid):
    return 'profile:'+str(uid)




if __name__ == '__main__':
    app.run(debug=True)