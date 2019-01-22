import os, csv

from flask import Flask, render_template, request
app = Flask(__name__) #parm인자로 넘겨줌

@app.route('/')
def index():
    return 'Hello World!'
    
    
@app.route('/greeting/<name>')
def greeting(name):
    return f'반갑습니다! {name}님!'
    

@app.route('/cube/<int:num>')
def cube(num):
    result=num**3
    return str(result)
    

@app.route('/html_file')
def html_file():
    return render_template('html_file.html')
    
    
@app.route('/hi/<name>') #페이지 만들기
def hi(name):
    return render_template('hi.html',name_in_html=name)
    
    
@app.route('/fruits')
def fruits():
    fruits=['apple','banana','mango','melon']
    return render_template('fruits.html',fruits=fruits)
    

@app.route('/send')
def send():
    return render_template('send.html')
    
    
@app.route('/receive')
def receive():
    name_p = request.args.get('name_s') #요청에 대한 정보를 얻음. args는 dict형태
    #request.args: {'name_s':'minho', 'message'='hello'}, 변수이름은 key값으로 input은 value값으로
    message = request.args.get('message') #name과 message라는 변수에 저장
    
    # csv에 input 저장
    with open('guestbook.csv','a',encoding='utf8',newline='') as f: #csv에 input 저장
        writer = csv.DictWriter(f,fieldnames=['name_c','message'])
        writer.writerow({
            'name_c':name_p,
            'message':message
        })
    
    return render_template('receive.html',name_r=name_p, message=message)
    
    
    
@app.route('/guestbook')
def guestbook():
    
    # csv에 저장값 불러오기
    messages=[]
    with open('guestbook.csv','r',encoding='utf8',newline='') as f:
        reader=csv.DictReader(f) #리더에  csv의 전체를 읽어서 저장
        for row in reader: #리더에서 한줄씩 불러옴
            messages.append(row)
    
    return render_template('guestbook.html',messages=messages)





if __name__=='__main__': #항상 마지막 줄에 유지
    app.run(host=os.getenv('IP'),port=os.getenv('PORT'), debug=True)