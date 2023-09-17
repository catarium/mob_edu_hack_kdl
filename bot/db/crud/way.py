from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker

from bot.db.models.classroom import Classroom
from bot.db.models.user import Teacher, Student
from bot.db.models.way import Way, Lesson


class WayCRUD:
    def __init__(self, sessionmaker: sessionmaker):
        self.Session = sessionmaker

    def get_by_id(self, way_id):
        with self.Session() as session:
            stmt = select(Way).where(Way.id == way_id)
            way = session.execute(stmt).one_or_none()
            if way:
                way = way[0]
            return way

    def create(self, name: str, teacher: Teacher, lessons=[], **kwargs):
        with self.Session() as session:
            way = Way(name=name, teacher=teacher, lessons=[])
            session.add(way)
            session.commit()
            session.refresh(way)
        return way

    # def add_lessons(self, way: Way, lessons: List[Lesson]):
    #     with self.Session() as session:
    #         way.lessons += lessons
    #         session.commit()


class LessonCRUD:
    def __init__(self, sessionmaker: sessionmaker):
        self.Session = sessionmaker

    def create(self, name, way_id):
        with self.Session() as session:
            lesson = Lesson(name=name, way_id=way_id)
            session.add(lesson)
            session.commit()

    def get_by_id(self, lesson_id):
        with self.Session() as session:
            stmt = select(Lesson).where(Lesson.id == lesson_id)
            lesson = session.execute(stmt).one_or_none()
            if lesson:
                lesson = lesson[0]
            return lesson

    def get_all_lessons(self):
        with self.Session() as session:
            select(Lesson)
