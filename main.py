from flask import Flask,render_template,request
app=Flask(__name__)










@app.route("/")
def start ():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("user_name")
        password=request.form.get("user_password")
        phone=request.form.get("user_phone")
        print(name,phone,password)

    return render_template("register.html")






























if __name__=="__main__":
    app.run(debug=True)