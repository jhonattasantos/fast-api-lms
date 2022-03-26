from typing import Optional, List
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

courses = []


class Course(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/courses")
async def get_courses():
    return {
        "courses": []
    }


@router.post("/courses")
async def create_courses_api(course: Course):
    courses.append(course)
    return "Success"


@router.get('/courses/{id}')
async def get_course(id: int):
    return {"course": []}


@router.patch('/courses/{id}')
async def update_course(id: int):
    return {"course": []}


@router.delete('/courses/{id}')
async def delete_course(id: int):
    return {"course": []}


@router.get('/courses/{id}/sections')
async def read_course_sections(id: int):
    return {"course": []}
