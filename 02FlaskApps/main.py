from flask import Flask, render_template, request
from flask import redirect, session, url_for
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def root():
  return 'Hello Flask Apps' 

@app.route('/image')
def image():
  return render_template('static.html')

@app.route('/jinda2')
def jinja2():
  return render_template('jinja2.html',
                         title = 'Jinja2',
                         home_str = 'Jinja2를 알아봅시다.',
                         home_list = [1, 2, 3, 4, 5])
@app.route('/form')
def info():
  return render_template('form.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
  if request.method == 'GET':
    args_dict = request.args.to_dict()
    print('args_dict (GET):', args_dict)
    userid = request.args["userid"]
    name = request.args.get("name")
    email = request.args.get('email')
    fail = request.form.get("name")
    print("실패예시 request.form.get(name):", fail)
    return render_template(
      'get.html',
      userid=userid,
      name=name,
      email=email,
      fail=fail
    )
    
  else:
    form_dict = request.form.to_dict()
    print("form_dict (POST):",form_dict)
    userid = request.form["userid"]
    name = request.form.get("name")
    email = request.form.get('email')
    fail = request.form.get("name")
    print("실패예시 request.form.get(name):", fail)
    return render_template(
      'post.html',
      userid=userid,
      name=name,
      email=email,
      fail=fail
    )

@app.route('/hello/<name>')  
def hello(name):
  return "내 이름은 {}".format(name)

@app.route('/input/<int:num>')  
def input(num):
  name = ''
  if num == 1:
    name = '홍길동'
  elif num == 2:
    name = '전우치'
  elif num == 3:
    name = '손오공'
  return "내 선택은{}".format(name)
    
@app.route('/daum')
def daum():
  return redirect("https://www.daum.net/")

@app.route('/naver')
def naver():
  return redirect("https://www.naver.com/")

@app.errorhandler(404)
def page_not_found(error):
  print("오류로그:",error)
  return "페이지가 없습니다. url을 확인하세요", 404

app.secret_key = 'A0Zr98j/3yx R~XHH!jmN]LWX/,?RT'

users = {
  'admin' : '1234',
  'user' : '9876'
}

@app.route('/mypage')
def mypage():
  if 'username' in session:
    return render_template('welcome.html',
                           username=escape(session['username']))
  return redirect(url_for('login'))

@app.route('/login', methods=['GET', "POST"])
def login():
  if request.method == "POST":
    input_id = request.form['username'] 
    input_pw = request.form['password']
    
    if input_id in users and users[input_id] == input_pw:
      session['username'] = input_id
      return redirect(url_for('mypage'))
    else:
      return render_template('login.html',
                             error='아이디 또는 비밀번호가 틀렸습니다.')  
  return render_template('login.html')
@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('root'))
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
  
  
  