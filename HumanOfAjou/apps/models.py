from apps import db

class Humans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    q_month = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=db.func.now())
    photo = db.Column(db.Text())


class Managers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())


class Ajou(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=db.func.now())
    photographer = db.Column(db.String(255))
    title = db.Column(db.String(255))


class Epilogues(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    text = db.Column(db.Text())
    date_created = db.Column(db.DateTime(),default=db.func.now())


# class Q_month(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     Q_month_human_id = db.Column(db.Integer, db.ForeignKey('Humans.id'))
#     human = db.relationship('Humans', backref=db.backref('comments', cascade='all, delete-orphan', lazy='dynamic'))
#     Q_month_other_id = db.Column(db.Integer)
