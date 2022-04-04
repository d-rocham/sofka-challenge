from flask_sqlalchemy import SQLAlchemy

from app import db


class Level(db.Model):
    __tablename__ = "levels"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    level_name = db.Column(db.String(10), nullable=False, unique=True)


class Questions(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    level_id = db.Column(db.ForeignKey("levels.id"), index=True, nullable=False)
    question_text = db.Column(db.String(140), nullable=False)

    @classmethod
    def create_question(cls, question, answers):
        """Inserts a question inside Questions table and its associated answers inside Answers table
        Args:
            question: `dictionary` where the key is a `string` question_text
            and the value is an `int` representing the level_id

            answers: `dictionary`with 4 key, value pairs where each key is a `string` representing
            `Answers.answer_text` and the value is an `int` representing Answers.correct`

        Returns: TODO:
        """
        new_question = cls(
            level_id=question["level_id"], question_text=question["question_text"]
        )

        db.session.add(new_question)
        db.session.commit()

        for key, value in answers.items():
            new_answer = Answers(
                question_id=new_question.id, answer_text=key, correct=value
            )
            db.session.add(new_answer)
            db.session.commit()


class Answers(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    question_id = db.Column(db.ForeignKey("questions.id"), index=True, nullable=False)
    answer_text = db.Column(db.String(25), nullable=False)
    correct = db.Column(db.Integer, nullable=False)
