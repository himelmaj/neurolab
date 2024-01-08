from fastapi import HTTPException, status
from sqlmodel import Session, select
from fastapi_pagination.ext.sqlmodel import paginate
from ..models.models import Course, CourseCreate, CourseUpdate

def get_all_courses_or_404(session: Session):
    courses = paginate(session, select(Course))
    
    if not courses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Courses not found")
    
    return courses

def get_course_by_id_or_404(session: Session, course_id: int):
    course = session.get(Course, course_id)
    
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    return course

def create_course_or_404(session: Session, course: CourseCreate):
    course = Course.model_validate(course)
    session.add(course)
    session.commit()
    session.refresh(course)
    
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not created")
    
    return course

def update_course_or_404(session: Session, course_id: int, course: CourseUpdate):
    db_course = session.get(Course, course_id)
    
    if not db_course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    course_data = course.model_dump(exclude_unset=True)
    
    for key, value in course_data.items():
        setattr(db_course, key, value)
        
    session.add(db_course)
    session.commit()
    session.refresh(db_course)
    return db_course

def delete_course_or_404(session: Session, course_id: int):
    course = session.get(Course, course_id)
    
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    session.delete(course)
    session.commit()
    return course

def get_students_of_course_or_404(session: Session, course_id: int):
    course = session.get(Course, course_id)
    
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    return course

def get_course_by_name_or_404(session: Session, course_name: str):
    course = paginate(session, select(Course).where(Course.course_name.contains(course_name)))
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    
    return course