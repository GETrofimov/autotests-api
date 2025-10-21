import httpx
from tools.fakers import fake

# Константы
BASE_URL = 'http://127.0.0.1:8000'
USER_EMAIL = 'test_user@example.com'
USER_NEW_EMAIL = fake.email()
USER_PASSWORD = '123456789'

# Данные для тела запроса /api/v1/users
create_user_payload = {
    "email": USER_EMAIL,
    "password": USER_PASSWORD,
    "lastName": "Иванов",
    "firstName": "Иван",
    "middleName": "Иванович"
}

# Данные для тела запроса /api/v1/authentication/login
login_user_payload = {
    "email": USER_EMAIL,
    "password": USER_PASSWORD
}

# Данные для тела запроса /api/v1/users/{user_id}
update_user_payload = {
  "email": USER_NEW_EMAIL,
  "lastName": "Свалов",
  "firstName": "Семен",
  "middleName": "Иванович"
}

# Создаем юзера
user_create_response = httpx.post(BASE_URL + '/api/v1/users', json=create_user_payload)
parsed_user_create_response = user_create_response.json()

print(f"Создали юзера: {parsed_user_create_response}")
print(user_create_response.status_code)

# Сохраняем id юзера на будущее
user_id = parsed_user_create_response['user']['id']

# Логинимся
user_login_response = httpx.post(BASE_URL + '/api/v1/authentication/login', json=login_user_payload)
parsed_user_login_response = user_login_response.json()

print(user_login_response.status_code)

# Сохраняем accssToken в хэдер
auth_header = {"Authorization": f"Bearer {parsed_user_login_response['token']['accessToken']}"}

# Обновляем юзера
user_update_response = httpx.patch(BASE_URL + f'/api/v1/users/{user_id}', json=update_user_payload, headers=auth_header)
parsed_user_update_response = user_update_response.json()

print(f"Обновили юзера: {parsed_user_update_response}")
print(user_update_response.status_code)


