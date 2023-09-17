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

    def get_by_id(self, student_id):
        with self.Session() as session:
            stmt = select(Student).where(Student.id == student_id)
            student = session.execute(stmt).one_or_none()
            if student:
                lesson = student[0]
            return lesson

    def add_grade(self, student_id, lesson_id, grade):
        with self.Session() as session:
            grade = int(grade)
            stmt = select(Student).where(Student.id == student_id)
            student = session.execute(stmt).one_or_none()[0]
            d = student.grades
            d[lesson_id] = grade
            student.grades = d
            session.commit()

    def create(self, telegram_id, name, lastname, **kwargs) -> Student:
        with self.Session() as session:
            student = Student(
                telegram_id=telegram_id,
                name=name,
                lastname=lastname,
            )
            session.add(student)
            session.commit()
        return student

    def get_by_tg_id(self, telegram_id):
        with self.Session() as session:
            stmt = select(Student).where(Student.telegram_id == telegram_id)
            teacher = session.execute(stmt).one_or_none()
            if teacher:
                return teacher[0]
            return teacher


class TeacherCRUD:
    def __init__(self, sessionmaker: sessionmaker):
        self.Session = sessionmaker

    def get_by_tg_id(self, telegram_id):
        with self.Session() as session:
            stmt = select(Teacher).where(Teacher.telegram_id == telegram_id)
            teacher = session.execute(stmt).one_or_none()
            if teacher:
                return teacher[0]
            return teacher

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

