from flask import Flask

app = Flask(__name__)

@app.route('/')
def menu():
    return "** Game of Life **"

if __name__ == '__main__':
    app.run(debug=true)
