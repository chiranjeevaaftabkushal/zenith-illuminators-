from flask import Flask,render_template,request,url_for

app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    selected_city=None
    selected_time=None
    if request.method=="POST":
        selected_city=request.form.get('city')
        print(selected_city)
        selected_time=request.form.get('time')
        print(selected_time)
    return render_template('home.html',selected_city=selected_city)

if __name__ == '__main__':
    app.run(debug=True)

