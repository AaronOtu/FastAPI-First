from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session

from typing import List


router = APIRouter(
  prefix="/blog",
  tags=["BLOGS"]
)
get_db = database.get_db


# Get all blog
@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blog(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# Create new blog
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Delete blog
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

# Get blog by id
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog

# Update blog
@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    else:
        blog.update(request.model_dump())
        db.commit()
        return 'updated'
