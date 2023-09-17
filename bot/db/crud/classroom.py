from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from bot.db.models.classroom import Classroom
from bot.db.models.user import Teacher, Student
from bot.db.models.way import Way


class ClassroomCRUD:
    def __init__(self, sessionmaker: sessionmaker):
        self.Session = sessionmaker

    def get_all(self):
        with self.Session() as session:
            classrooms = session.query(Classroom).all()
            return classrooms

    def get_by_id(self, class_id):
        with self.Session() as session:
            stmt = select(Classroom).where(Classroom.id == class_id)
            classroom = session.execute(stmt).one_or_none()
            if classroom:
                classroom = classroom[0]
            return classroom


    def create(self, name: str, teacher: Teacher, way_id: int, **kwargs):
        with self.Session() as session:
            classroom = Classroom(name=name, teacher=teacher, students=[], way_id=way_id)
            session.add(classroom)
            session.commit()

    def add_students(self, classroom: Classroom, students: List[Student]):
        with self.Session() as session:
            classroom.students += students
            session.commit()
