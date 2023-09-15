from typing import List

from sqlalchemy.orm import Session, sessionmaker

from bot.db.models.classroom import Classroom
from bot.db.models.user import Teacher, Student


class ClassroomCRUD:
    def __init__(self, sessionmaker: sessionmaker):
        self.Session = sessionmaker

    def create(self, name: str, teacher: Teacher, students=[], **kwargs):
        with self.Session() as session:
            classroom = Classroom(name=name, teacher=teacher, students=[])
            session.add(classroom)
            session.commit()

    def add_students(self, classroom: Classroom, students: List[Student]):
        with self.Session() as session:
            classroom.students += students
            session.commit()
