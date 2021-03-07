from flask import Flask, render_template, Response
import subprocess

app = Flask(__name__)

#/にアクセスがあったときの処理
@app.route('/')
def index():
    return render_template('index.html')

#/システム起動ﾎﾞﾀﾝが押されたときの処理
@app.route('/system_on')
def system_run():
    subprocess.run("python human_detection.py",shell=True)
    return render_template('index.html')

#/システム停止ﾎﾞﾀﾝが押されたときの処理
@app.route('/system_off')
def system_stop():
    subprocess.run("./system_stop.sh")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='hostname', debug=True)
