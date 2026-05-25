from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import DB_Table
from app.schemas.user import AuthUserCreate, AuthUserResponse, AuthToken
from app.core.security import verify_password, hash_password, create_access_token



router = APIRouter(prefix="/auth", tags=["Auth"])
#auth2_scheme = OAuth2PasswordBearer(tokenUrl=["auth/login"])

@router.post("/register", response_model=AuthUserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: AuthUserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(DB_Table).filter(DB_Table.username == user_data.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário já registrado!"
        )
    
    existing_email = db.query(DB_Table).filter(DB_Table.email == user_data.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já utilizado!"
        )
    
    existing_register = db.query(DB_Table).filter(DB_Table.register == user_data.register).first()
    if existing_register:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CPF já cadastrado!"
        )
    
    hashed_password = hash_password(user_data.password)

    new_user = DB_Table(
        username=user_data.username,
        email=user_data.email,
        register=user_data.register,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=AuthToken)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(DB_Table).filter(DB_Table.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password!",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    access_token = create_access_token(data={"sub": user.username})

    return{"token": access_token, "type": "bearer"}