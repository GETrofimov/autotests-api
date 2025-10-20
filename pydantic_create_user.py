from pydantic import BaseModel, EmailStr

# Модель данных пользователя
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str

#Модель данных запроса на создание пользователя
class CreateUserRequestSchema(BaseModel):
      email: EmailStr
      password: str
      lastName: str
      firstName: str
      middleName: str

# Модель данных ответа на запрос создания пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema