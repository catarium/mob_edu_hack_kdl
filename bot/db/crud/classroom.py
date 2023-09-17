from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from bot.db.models.classroom import Classroom
from bot.db.models.user import Teacher, Student
from bot.db.models.way import Way, Lesson


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

    def add_student(self, classroom_id: int, student: Student):
        with self.Session() as session:
            classroom = select(Classroom).where(Classroom.id == classroom_id)
            classroom = session.execute(classroom).one_or_none()[0]
            classroom.students.append(student)
            session.commit()

    def change_lesson_status(self, classroom: Classroom, lesson: Lesson):
        with self.Session() as session:
            # session.add(classroom)
            # session.add(lesson)
            lessons_ids = [l.id for l in classroom.way.lessons]
            completed_lessons_ids = [l.id for l in classroom.completed_lessons]
            if lesson.id not in lessons_ids:
                return False
            classroom = select(Classroom).where(Classroom.id == classroom.id)
            classroom = session.execute(classroom).one_or_none()[0]
            lesson = select(Lesson).where(Lesson.id == classroom.id)
            lesson = session.execute(lesson).one_or_none()[0]
            if lesson.id in completed_lessons_ids:
                classroom.completed_lessons.remove(lesson)
            else:
                classroom.completed_lessons.append(lesson)
            session.commit()
            return True

