from sqlalchemy.orm import Session
from typing import Optional
from database.models.User import User

class UserRepository:
    @staticmethod
    def get_by_id(db: Session, id: str) -> Optional[User]:
        return db.query(User).filter(User.id == id).first()

    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def create(db: Session, email: str, google_id: str):
        user = User(email=email, google_id=google_id)

        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user
    

    @staticmethod
    def update_points(db: Session, id: str, points: int):
        user = db.query(User).filter(User.id == id).first()
 
        user.points = points
 
        db.commit()
        db.refresh(user)
 
        return user



