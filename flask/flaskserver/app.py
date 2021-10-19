from flask import Flask, request
from flask_restful import Resource,Api



app = Flask(__name__)
api = Api(app)


@app.route('/')
def User():
    Userlist = MyTbl().getTbls();
    return render_template('index.html', Userlist=Userlist)


if __name__ == "__main__":
    app.run(debug=True)


