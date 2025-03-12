from flask import Flask, render_template,request
app = Flask(__name__)
global display

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/page2', methods=['GET','POST'])
def page2():
    #value1 = float(request.form['value1'])
    htmlDisplay = ""
    if request.method == 'POST':
        select_option = request.form.get('weight')
        userValue = request.form['value1']
        print("the type wants the user to pick",select_option)
        print(request.form['value1'],"this is the amount the user input")
        # convert userValue to fix flask ValueError 
       
        print(type(userValue))
        if userValue.isdigit():
            if "milligramtoGram" == select_option:
                totalUserValue = float(userValue) * 0.001
                htmlDisplay = totalUserValue
            if "gramtoMilligram" == select_option:
                totalUserValue = float(userValue) * 1000
                htmlDisplay = totalUserValue
                #need to show fix this bug :C
            if "kilogramtoOunce" == select_option:
                totalUserValue = float(userValue) * 35.274
                #numbers=int(userValue) * 35.274
                print(type(userValue))
                htmlDisplay = totalUserValue
            if "ouncetoKilogram" == select_option:
                totalUserValue = float(userValue) * 0.0283495231
                htmlDisplay = totalUserValue
            if "poundstoGrams" == select_option:
                totalUserValue = float(userValue) * 453.59237
                htmlDisplay = totalUserValue
            if "poundstoGrams" == select_option:
                totalUserValue = float(userValue) * 453.59237
                htmlDisplay = totalUserValue
            if "gramstoPounds" == select_option:
                totalUserValue = float(userValue) / 453.59290944
                htmlDisplay = round(totalUserValue,5)
        else:
           htmlDisplay = "This is not a number please input a number"
        if  userValue  == '' :
            htmlDisplay = "please input a number"
        
    return render_template("page2.html", display = str(htmlDisplay))

@app.route('/page3', methods=['GET','POST'])
def page3():
    htmlDisplay = ""
    
    if request.method == 'POST':
        userValue = request.form['value2']
        select_option = request.form.get('length')
        print(type(userValue))
        if userValue.isdigit():
            if select_option == "millimetertoCentimeter":
                 htmlDisplay = float(userValue)
                 print("test")
    else:
        htmlDisplay = "This is not a number please input a number"
    if  userValue  == '' :
        htmlDisplay = "please input a number"
    
        
    return render_template("page3.html",display = str(htmlDisplay))



@app.route('/page4')
def page4():
    return render_template("page4.html")

if __name__ == "__main__":
    app.run(debug=True)