from config import db

class User(db.Model):
    __tablename__ = 'user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(200),nullable=False)
    projects=db.relationship('Projects',backref='user')
    personal_details=db.relationship('PersonalDetails',backref='user')
    experiences=db.relationship('Experiences',backref='user')
    education=db.relationship('Educations',backref='user')
    certificates=db.relationship('Certificates',backref='user')
    skills=db.relationship('Skills',backref='user')
    
