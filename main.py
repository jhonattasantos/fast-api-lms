from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users, sections, courses

app = FastAPI(
    tiitle="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Jhonatta Santos",
        "email": "jhow@email.com",
    },
    license_info={
        "name": "MIT",
    },
)
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
