from flask import Flask,render_template,request,render_template_string
from flask import Flask,render_template,request,render_template_string
app = Flask(__name__)

@app.route('/',methods=["get","post"])
def main(): 
    return render_template('index1.html')

if __name__ == "__main__":
    app.run()
    
