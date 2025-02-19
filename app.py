from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/page2', methods=['GET','POST'])
def page2():
    #value1 = float(request.form['value1'])
    
    if request.method == 'POST':
        global htmlDisplay
        select_option = request.form.get('weight')
        userValue = float(request.form['value1'])
        print("the type wants the user to pick",select_option)
        print(request.form['value1'],"this is the amount the user inputed")

        if "milligramtoGram" == select_option:
            totalUserValue = userValue * 0.001
            htmlDisplay = totalUserValue

        if "gramtoMilligram" == select_option:
            totalUserValue = userValue * 1000
            htmlDisplay = totalUserValue
        
    return render_template("page2.html",display = str(htmlDisplay) )

@app.route('/page3')
def page3():
    return render_template("page3.html")
@app.route('/page4')
def page4():
    return render_template("page4.html")

if __name__ == "__main__":
    app.run(debug=True)