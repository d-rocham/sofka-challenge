import random

from app import db


class Level(db.Model):
    __tablename__ = "levels"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    level_prize = db.Column(db.Integer, nullable=False)

    def assemble(self):
        """Builds & returns dictionary with level information, randomly chosen question
        and its answers"""

        random_question = random.choice(self.questions)

        return {
            "level_name": self.id,
            "prize": self.level_prize,
            "questions": random_question.assemble(),
        }

    @classmethod
    def get_all(cls):
        return cls.query.all()


class Questions(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    level_id = db.Column(db.ForeignKey("levels.id"), index=True, nullable=False)
    question_text = db.Column(db.String(140), nullable=False)

    levels = db.relationship(
        "Level",
        primaryjoin="Questions.level_id == Level.id",
        backref="questions",
    )

    @classmethod
    def create_question(cls, question, answers):
        """Inserts a question inside Questions table and its associated answers inside Answers table

        Args:
            question: `dictionary` where the key is a `string` question_text
            and the value is an `int` representing the level_id.

            answers: `dictionary`with 4 key, value pairs where each key is a `string`
            representing `Answers.answer_text` and each value is an
            `int` representing Answers.correct`.

        Returns:
            `ValueError` or `KeyError` if the provided arguments aren't
            formated as required.

            `SQLAlchemy.rowObject` if the question is succesfully added
        """
        keys = list(question.keys())
        values = list(answers.values())

        # Check for input errors
        if len(question) != 2:
            raise ValueError("Question dictionary must have 2 key, value pairs")

        elif len(answers) != 4:
            raise ValueError("Answers dictionary must have 4 key, value pairs")

        elif "question_text" not in keys or "level_id" not in keys:
            raise KeyError("Wrong keys in question dictionary")

        elif question["level_id"] not in [level.id for level in Level.get_all()]:
            raise ValueError("Requested level does not exist")

        elif 1 not in values:
            raise ValueError("A correct option must be provided")

        elif values.count(1) > 1:
            raise ValueError("Only 1 answer can be correct")

        # Once data is verified, add new question & answers to their respective tables
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

    def assemble(self):
        """Returns dictionary with question text and list with its answers"""

        return {
            "question_text": self.question_text,
            "answers": [answer.assemble() for answer in self.answers],
        }


class Answers(db.Model):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    question_id = db.Column(db.ForeignKey("questions.id"), index=True, nullable=False)
    answer_text = db.Column(db.String(50), nullable=False)
    correct = db.Column(db.Integer, nullable=False)

    questions = db.relationship(
        "Questions",
        primaryjoin="Answers.question_id == Questions.id",
        backref="answers",
    )

    def assemble(self):
        """Returns dictionary with answer text and correct status"""

        return {"answer_text": self.answer_text, "correct": self.correct}
