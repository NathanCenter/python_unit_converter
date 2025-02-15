from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/page2', methods=['GET','POST'])
def page2():
    #value1 = float(request.form['value1'])
    if request.method == 'POST':
        print(float(request.form['value1']))
    return render_template("page2.html")

@app.route('/page3')
def page3():
    return render_template("page3.html")
@app.route('/page4')
def page4():
    return render_template("page4.html")

if __name__ == "__main__":
    app.run(debug=True)