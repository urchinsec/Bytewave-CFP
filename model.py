from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    phone_number = db.Column(db.String())
    paper_title = db.Column(db.String())
    paper_category = db.Column(db.String())
    paper_summary = db.Column(db.String())

    def __init__(self, id, first_name, last_name, email, phone_number, paper_title, paper_category, paper_summary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.paper_title = paper_title
        self.paper_category = paper_category
        self.paper_summary = paper_summary

    def __repr__(self):
        return f"{self.id}:{self.first_name}:{self.last_name}:{self.email}:{self.phone_number}:{self.paper_title}:{self.paper_category}:{self.paper_summary}"
