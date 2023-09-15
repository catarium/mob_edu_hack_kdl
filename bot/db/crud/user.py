from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker, with_polymorphic

from bot.db.models.classroom import Classroom
from bot.db.models.user import Teacher, Student, User


class UserCRUD:
    def __init__(self, session: sessionmaker):
        self.Session = session

    def get_user_by_tg_id(self, telegram_id):
        with self.Session() as session:
            stmt = select(with_polymorphic(User, [Teacher, Student])).where(User.telegram_id == telegram_id)
            user = session.execute(stmt).one_or_none()
            if user:
                return user[0]
            return user


class StudentCRUD:
    def __init__(self, sessionmaker: sessionmaker):
        self.Session = sessionmaker

    def create(self, telegram_id, name, lastname, rating=0, class_=None, **kwargs) -> Student:
        with self.Session() as session:
            student = Student(
                telegram_id=telegram_id,
                name=name,
                lastname=lastname,
                rating=rating,
                class_=class_
            )
            session.add(student)
            session.commit()
        return student


class TeacherCRUD:
    def __init__(self, sessionmaker: sessionmaker):
        self.Session = sessionmaker

    def create(self, telegram_id, name, lastname, classes=[], **kwargs):
        with self.Session() as session:
            teacher = Teacher(
                telegram_id=telegram_id,
                name=name,
                lastname=lastname,
                classes=classes,
            )
            session.add(teacher)
            session.commit()
        return teacher

    def add_classes(self, teacher: Teacher, classes):
        with self.Session() as session:
            teacher.classes += classes
            session.commit()

