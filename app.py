from flask import Flask , redirect,url_for

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

@app.route('/blog/<name>')
def blog_post(name):
    return 'This is blog post of %s' % name

@app.route('/student/<int:stuID>')
def student(stuID):
    return 'This is the Rahuls student id number %d' % stuID

@app.route('/avg/<float:salary>')
def avg_salary(salary):
    return 'This is the average salary of 20 emp %f' % salary

@app.route("/admin")
def hii_admin():
    return 'Hello admin'

@app.route("/user/<name1>")
def check(name1):
    if name1=='admin':
        return redirect(url_for('hii_admin'))
    else:
        return redirect(url_for('blog_post',name=name1))

if __name__ == '__main__':
    app.run(debug=True)
