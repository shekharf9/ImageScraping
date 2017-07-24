from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/tdg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)


class Extraction(db.Model):
    __tablename__ = "ImageScraping"
    flickr_height = db.Column(db.Integer, primary_key = True, nullable=True)
    flickr_width = db.Column(db.Integer, nullable=True)
    flickr_title = db.Column(db.String(100), nullable=True)
    flickr_url = db.Column(db.String(300), nullable=True)
    googleScraper_url = db.Column(db.String(300), nullable=True)

    def __init__(self, flickr_height, flickr_width, flickr_title, flickr_url, googleScraper_url):
        self.flickr_height = flickr_height	
        self.flickr_width = flickr_width
        self.flickr_title = flickr_title
        self.flickr_url = flickr_url
        self.googleScraper_url = googleScraper_url
        

    def __repr__(self):
        return '<User %r>' % self.flickr_title

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
