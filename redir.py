from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def index():
        return redirect("http://127.0.0.1:1337/login?username=admin&password=erywithalice", code=302)

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8000)
