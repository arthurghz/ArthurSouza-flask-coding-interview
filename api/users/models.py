from sqlalchemy.orm import Mapped, mapped_column

from api.db import Base


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[str] = mapped_column(nullable=False)
    updated_at: Mapped[str] = mapped_column(nullable=False)
    last_login: Mapped[str] = mapped_column(nullable=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)


class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    enrollment_date: Mapped[str] = mapped_column(nullable=False)
    min_course_credits: Mapped[int] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(nullable=False)


class Course(Base):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    max_students: Mapped[int] = mapped_column(nullable=False)
    num_credits: Mapped[int] = mapped_column(nullable=False)
    professor_name: Mapped[int] = mapped_column(nullable=False)
