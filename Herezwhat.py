from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm
from flask import flash, redirect
from datetime import datetime
app= Flask(__name__)

app.config['SECRET_KEY']='5a010e6170bd6627c422d94b9a2c1a46'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db' # relative path

db= SQLAlchemy(app)
class User(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    username= db.Column(db.String(20), unique=True, nullable= False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),  nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    # The "Post" here is the class name
    # one-many Relationship.
    posts= db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return  f"User('{self.username}', '{self.email}', '{self.image_file}')"



class Post(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    title= db.Column(db.String(100), nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content= db.Column(db.Text, nullable= False)
    # "user" is table name. so its  lowercase.
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post'{self.title}', '{self.date_posted}'_"

# Dummy posts
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",title="Home", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password':
            flash("You logged In!", "success")
            return redirect(url_for("home"))
        else:
            flash('login Not successful', "danger")
    return render_template("login.html", title="Login", form=form)

if __name__== "__main__":
    app.run(debug=True)

