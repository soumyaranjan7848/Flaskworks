from flask import Flask

app=Flask(__name__)
@app.route('/')
def home():
    return "This is my first Flask webpage!"

@app.route('/about')
def about():
    return "This is my about Page !"

@app.route('/contact')
def contact():
    return "This is contact page !"

if __name__ == '__main__':
    app.run(debug=True)