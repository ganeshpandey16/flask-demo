#we are making a server which will print the data of my form on the command line
from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
    f=open("data.txt", "a")
    
    if request.method=='POST':
        first_name = request.form['username']
        last_name = request.form['usernamelast']
        a=str(first_name)+' '+str(last_name)
        f.write(a)
        f.write('\n')
    # f=open("data.txt",)
    return render_template('index.html')
app.run()