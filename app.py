from flask import Flask,render_template, request,Response, send_from_directory, jsonify,session,make_response,flash
import os
import pandas as pd
import uuid
app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'SOME KEY'


@app.route('/')
def index():
    return render_template('index.html', message="Index")

@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'
    return render_template('index.html', message='Session data set.')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        data = session['other']
        return render_template('index.html', message=f" Name: {name} data : {data}")
    else:
        return render_template('index.html', message="no session found")

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message="session cleared")

@app.route('/set_cookie')
def set_cookie():
    # instruct the browser to set the cookie on the client side
    # 当用户点击 <a href="/set_cookie">：
    # 浏览器向服务器发请求；
    # Flask 生成一个 response，里面除了 HTML 还有一个 Set-Cookie 指令；
    # 浏览器收到后会在客户端存下这个 cookie；
    # 之后浏览器访问你的服务器时，会自动带上这个 cookie
    response = make_response(render_template('index.html', message='Cookie set.'))
    response.set_cookie('cookie_name', 'cookie_response')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message=f'cookie_value : {cookie_value}')


@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message ='cookie removed'))
    response.set_cookie('cookie_name',expire=0)
    return response

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Angel' and password == '828':
            flash("successful login")
            return render_template('index.html', message = '')
        else:
            flash("login failed")
            return render_template('login.html', message = '')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5555, debug=True)



# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "GET":
#         return render_template('index.html')
#     elif request.method == "POST":
#         # print(request.form)
#         username= request.form.get('username')
#         password = request.form.get('password')

#         if username == 'angel' and password == '123':
#             return "success"
#         return "Failure"

# @app.route('/file_upload', methods=["POST"])
# def file_upload():
#     print(request.files)
#     file = request.files['file']
#     if file.content_type == 'text/plain':
#         return file.read().decode()
#     elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == "application/vnd.ms-excel":
#         df = pd.read_excel(file)
#         return df.to_html()

# @app.route('/convert_csv', methods=["POST"])
# def convert_csv():
#     file = request.files['file']
#     df = pd.read_excel(file)
#     response = Response(df.to_csv(), mimetype='text/csv',
#     headers={'Content-Disposition': 'attachment; filename=result.csv'})
#     return response


# @app.route('/convert_csv_two', methods=["POST"])
# def convert_csv_two():
#     file = request.files['file']
#     df = pd.read_excel(file)

#     if not os.path.exists('downloads'):
#         os.makedirs('downloads')
    
#     filename = f'{uuid.uuid4()}.csv'
#     df.to_csv(os.path.join('downloads', filename))
#     return render_template("download.html", filename = filename)



# @app.route('/download/<filename>')
# def download(filename):
#     return send_from_directory("downloads", filename, download_name="res.csv")

# @app.route('/handle_post', methods = ["POST"])
# def handle_post():
#     name = request.get_json()['name']
#     greeting = request.get_json()['greeting']
#     with open('file.txt', 'w') as f:
#         f.write(f'I {greeting} {name}')
#     return jsonify({'message':'successfully written !'})






# course II
# @app.route('/')
# def index():
#     myValue = 10
#     myFood = "dessert"
#     mylist = [1,11,111,1111]
#     return render_template('index.html', mv=myValue, mf = myFood, ml = mylist)

# @app.route('/other')
# def other():
#     s = "Hello World"
#     return render_template("other.html", str = s)


# @app.template_filter("reverse_string")
# def reverse_string(s):
#     return s[::-1]





# in Index.html course II:
# <!-- <p>{{mf}}</p>
#     <p>Rating {{mv}}</p> -->
# <!-- <ul> -->
# <!-- {% for item in ml %}
#       <li {%if item == 111%} style="color:red" {%endif%}>{{item}}</li>
#       {% endfor %} -->
# <!-- </ul> -->
# <!-- <a href="{{url_for('other')}}">Other</a> -->




# basics
# @app.route('/hello', methods=['GET'])
# def hello():
#     return "Hello world\n", 201
#     # if request.method == 'GET':
#     #     return "you made a get request\n", 202
#     # elif request.method == 'POST':
#     #     return "you made a post request\n"
#     # return "you will never see this message\n"

# @app.route('/greet/<name>')
# def greet(name):
#     return f"hello {name}"

# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1, num2):
#     return f"{num1} + {num2} = {num1+num2}"

# @app.route('/urlParam')
# def getUrlParam():
#     greeting = request.args["greeting"] #是一个 dictionary key value pair string
#     name = request.args.get('name')
#     return f'{greeting}, {name}'
#     # return str(request.args)



