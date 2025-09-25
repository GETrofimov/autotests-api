import httpx

# Базовый URL для запросов
BASE_URL = 'http://127.0.0.1:8000'

# Креды юзера
user_data = {
  "email": "user@example.com",
  "password": "123456789"
}

# Вызываем /api/v1/authentication/login и вытаскиваем из ответа accessToken
login_response = httpx.post(BASE_URL+'/api/v1/authentication/login', json=user_data)
parsed_login_response = login_response.json()

access_token = parsed_login_response['token']['accessToken']

# Добавляем acessToken в заголовки
auth_header = {'Authorization': f'Bearer {access_token}'}

# Вызываем /api/v1/users/me и выводим в консоль преобразованный в json ответ
users_me_response = httpx.get(BASE_URL+'/api/v1/users/me', headers=auth_header)
parsed_users_me_response = users_me_response.json()

print(parsed_users_me_response)
print(users_me_response.status_code)
