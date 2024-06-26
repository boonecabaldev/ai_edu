
from . import db


class EntityBase(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    creation_dt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_dt = db.Column(db.DateTime, default=db.func.current_timestamp())
    note = db.Column(db.String(255))

class Contact(EntityBase):
    __tablename__ = 'contacts'

    contact_full_name = db.Column(db.String(255))
    contact_phone = db.Column(db.String(255))
    contact_email = db.Column(db.String(255))
    street1 = db.Column(db.String(255))
    street2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zip_code = db.Column(db.String(255))

class Solution(EntityBase):
    __tablename__ = 'solutions'
    
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    per = db.Column(db.String(255))

    features = db.relationship('SolutionFeature', backref='solution', lazy=True)

class Feature(EntityBase):
    __tablename__ = 'features'
    
    tag = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255))
    video_url = db.Column(db.String(255))
    website_url = db.Column(db.String(255))

    solutions = db.relationship('SolutionFeature', backref='feature', lazy=True)

class Institution(EntityBase):
    __tablename__ = 'institutions'

    name = db.Column(db.String(255), nullable=False)
    contact = db.Relationship("Contact", backref="institution")

    solutions = db.relationship('Solution', backref='institution', lazy=True)
    products = db.relationship('Solution', backref='institution', lazy=True)

class SolutionFeature(EntityBase):
    __tablename__ = 'solutionfeatures'
    
    solution = db.relationship("Solution", backref='features', lazy=True)
    feature = db.relationship("Feature", backref='solutions', lazy=True)

    score = db.Column(db.Float)
    automate = db.Column(db.Boolean)




class HatComposite(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    img_src = db.Column(db.String)
    img_file_path = db.Column(db.String)

class HatComponent(HatComposite):
    __tablename__ = 'hatcomponents'

    url = db.Column(db.String)

    leaves = db.Relationship("HatLeaf", backref="hatcomponent")

    text_id = ""

class HatLeaf(HatComposite):
    __tablename__ = 'hatleafs'

    node_id = db.Column(db.Integer, db.ForeignKey('hatcomponents.id'))
    h3_title = db.Column(db.String)
    date_string = db.Column(db.String)