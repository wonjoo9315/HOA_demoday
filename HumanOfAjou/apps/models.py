from apps import db
from sqlalchemy import UniqueConstraint

class Humans(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    q_month = db.Column(db.Text())
    date_created = db.Column(db.DateTime(), default=db.func.now())
    photo = db.Column(db.Text())
    like_count = db.Column(db.Integer, default=0)
    view_count = db.Column(db.Integer, default=0)

    @classmethod
    def count(cls):
        return cls.query.all().count()


class LikeRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50))

    humans_id = db.Column(db.Integer, db.ForeignKey('humans.id'))
    humans = db.relationship('Humans', backref=db.backref('likeCounts', lazy='dynamic'))

    hash_code = db.Column(db.String(255))

    # multiple unique constraint
    __table_args__ = (UniqueConstraint('humans_id', 'ip', 'hash_code',  name='_like_humans'),)
    date_created = db.Column(db.DateTime(), default=db.func.now())

class ViewRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50))
    humans_id = db.Column(db.Integer, db.ForeignKey('humans.id'))
    humans = db.relationship('Humans', backref=db.backref('viewCounts', lazy='dynamic'))

    hash_code = db.Column(db.String(255))

    # multiple unique constraint
    __table_args__ = (UniqueConstraint('humans_id', 'ip', 'hash_code', name='_view_humans'),)
    date_created = db.Column(db.DateTime(), default=db.func.now())


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
