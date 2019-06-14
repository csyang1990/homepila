# #-*- coding:utf-8 -*-
# import sys
#
# # reload(sys)
# # sys.setdefaultencoding('utf-8')

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    if not session.get('logged_in'): #로그인 되어 있지 않으면 로그인 페이지로 이동
        # return render_template('login.html')
        return "Login !!!"
    else:
        # return render_template('logout.html') #임시
        return "Logout !!!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    #폼에서 넘어온 데이터를 가져와 정해진 유저네임과 암호를 비교하고 참이면 세션을 저장한다.
    #회원정보를 DB구축해서 추출하서 비교하는 방법으로 구현 가능 - 여기서는 바로 적어 줌
    if request.form['password'] == 'password' and request.form['username'] == 'admin' :
        session['logged_in'] = True #세선 해제는 어떻게?
    else:
        flash('유저네임이나 암호가 맞지 않습니다.')
    return index()

@app.route('/logout')
def logout():
    session.clear()
    #return redirect(url_for('index'))
    return index()

if __name__ == '__main__':
    app.secret_key = os.urandom(12) #좀 더 알아 볼것. 시크릿키는 세션등의 기능을 위해 반드시 필요하다.
    app.run(debug=True)
    # app.run(debug=True, host='0.0.0.0')
