from fastapi import APIRouter, HTTPException, Depends, status
from .. import database, schemas, models, hashing
from sqlalchemy.orm import Session

router = APIRouter(
  prefix="/user",
  tags=["USERS"]
)
get_db = database.get_db
hash = hashing.Hash.bcrypt



#Create a user
@router.post('/user', response_model= schemas.UserResponse)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name = request.name, email= request.email, password = hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#Get user by ID
@router.get('/user/{id}', status_code=status.HTTP_200_OK, response_model= schemas.UserResponse)
def show_user_by_id(id : int,db: Session = Depends(get_db) ):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not found')
        
    return user    