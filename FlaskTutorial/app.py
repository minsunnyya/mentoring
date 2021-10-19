from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    if request.method == "POST":
        print(request.form.get('user'))
        user = request.form.get('user')
        data = {'age': 27, 'birth': 950625, 'phone': 4871}
        return render_template('index.html', user=user, data=data)
    elif request.method == "GET":
        user = "써니"
        data = {'age': 27, 'birth': 950625, 'phone': 4871}
        return render_template('index.html', user=user, data=data)

if __name__== "__main__":
    app.run(debug=True)




