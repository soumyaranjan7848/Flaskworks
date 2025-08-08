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

@app.route('/blog/<name>')
def blog_post(name):
    return 'This is blog post of %s' % name

@app.route('/student/<int:stuID>')
def student(stuID):
    return 'This is the Rahuls student id number %d' % stuID

@app.route('/avg/<float:salary>')
def avg_salary(salary):
    return 'This is the average salary of 20 emp %f' % salary

if __name__ == '__main__':
    app.run(debug=True)