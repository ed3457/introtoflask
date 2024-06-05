from flask import Flask     
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return 'HELLO'

@app.route('/page1')       
def page1function(): 
    return 'Page 1 Data'
  
if __name__=='__main__': 
   app.run() 
