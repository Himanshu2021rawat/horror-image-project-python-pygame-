# flask module mai se flask class define kari
from flask import Flask,render_template

app = Flask(__name__,template_folder='template')

@app.route("/")
def hello_world():
        return render_template('index.html')

@app.route("/about")
def hello():
    name = "himanshu"

    return render_template('about.html',name=name)


@app.route("/bootstrap")
def bootstrap():


    return render_template('bootstrapf.html')

app.run(debug=True)