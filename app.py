from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return 'This is Mypage!'

if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)