from pydantic import BaseModel, EmailStr, Field

# Модель данных пользователя
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

#Модель данных запроса на создание пользователя
class CreateUserRequestSchema(BaseModel):
      email: EmailStr
      password: str
      last_name: str = Field(alias="lastName")
      first_name: str = Field(alias="firstName")
      middle_name: str = Field(alias="middleName")

# Модель данных ответа на запрос создания пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema