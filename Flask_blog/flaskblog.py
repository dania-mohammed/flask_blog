from flask import Flask , render_template , url_for
app = Flask(__name__)
posts = [
    {'author': 'mohammedelhassan',
     'title': 'Blog Post 1',
     'content': 'first post content',
     'date_posted': 'October 26,2023'},
     {'author': 'Amal Abdalaziz',
     'title': 'Blog Post 2',
     'content': 'second post content',
     'date_posted': 'november 26,2023'}
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts =posts )

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
