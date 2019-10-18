from Herezwhat import db
from datetime import datetime

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
