from typing import Optional

from flask_openapi3 import APIBlueprint
from pydantic import BaseModel
from sqlalchemy import select

from api.users.models import Users, Student , Course
from database import db

users_app = APIBlueprint("users_app", __name__)
students_app = APIBlueprint("students_app", __name__)
courses_app = APIBlueprint("courses_app", __name__)


class UserSchema(BaseModel):
    password: str
    email: str
    created_at: str
    updated_at: str
    last_login: Optional[str]
    first_name: str
    last_name: str

    class Config:
        orm_mode = True

class StudentSchema(BaseModel):
    id: int
    enrollment_date: str
    min_course_credits: str
    first_name: str
    last_name: str
    user_id:  int

    class Config:
        orm_mode = True


class CourseSchema(BaseModel):
    id: int
    max_students: int
    num_credits: str
    professor_name: str

    class Config:
        orm_mode = True

class UserList(BaseModel):
    users: list[UserSchema]


class StudentList(BaseModel):
    students: list[StudentSchema]


class CourseList(BaseModel):
    courses: list[CourseSchema]

@users_app.get("/users", responses={"200": UserList})
def get_users():
    with db.session() as session:
        users_query = session.execute(select(Users)).scalars().all()
        users_list = [
            UserSchema.from_orm(user).dict()
            for user
            in users_query
        ]
        return {"users": users_list}


# LIST ENDPOINTS
@students_app.get("/students", responses={"200": StudentList}) #
def get_students():
    pass

@courses_app.get("/courses", responses={"200": CourseList})
def get_courses():
    pass

# Retriever by ID
@students_app.get("/student/{user_id}", responses={"200": StudentSchema})  # Get user By User ID
def get_student_by_user_id(user_id):
    pass

# Courses By ID
@courses_app.get("/courses/{course_id}", responses={"200": CourseSchema})  # Get user By User ID
def get_course_by_id(course_id):
    pass

# Patch Data
@courses_app.patch("/courses/{course_id}", responses={"200": CourseSchema})
def update_course_by_id(course):
    pass

@students_app.patch("/students/{student_id}", responses={"200": StudentSchema})
def update_course_by_id(course):
    pass

