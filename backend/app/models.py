from flask_sqlalchemy import SQLAlchemy

from app import db


class Level(db.Model):
    __tablename__ = "level"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    level_name = db.Column(db.String(10), nullable=False, unique=True)


class Questions(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    level_id = db.Column(db.ForeignKey("level.id"), index=True, nullable=False)
    question_text = db.Column(db.String("140", nullable=False))


class Answers(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    level_id = db.Column(db.ForeignKey("questions.id"), index=True, nullable=False)
    answer_text = db.Column(db.String("15"), nullable=False)
    correct = db.Column(db.Integer, nullable=False)
