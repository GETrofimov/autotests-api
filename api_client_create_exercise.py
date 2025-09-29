from clients.courses.courses_client import CreateCourseRequestDict, get_courses_client
from clients.exercises.exercises_client import CreateExerciseRequestDict, get_exercises_client
from clients.files.files_client import CreateFileRequestDict, get_files_client
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import CreateUserRequest, get_public_users_client
from tools.fakers import get_random_email

# Получаем public client
public_user_client = get_public_users_client()

# Тело дляя запроса создания юзера
create_user_request = CreateUserRequest(
    email = get_random_email(),
    password = "123456789",
    lastName = "Иванов",
    firstName = "Иван",
    middleName = "Иванович"
)

# Создаем юзера
create_user_response = public_user_client.create_user(create_user_request)

# Тело для аутентификации
authentication_user = AuthenticationUserDict(
    email = create_user_request["email"],
    password = create_user_request["password"]
)

# Получаем клиенты для файлов и курсов
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Тело для создания файла
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)

# Создаем файлик 
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Тело для создания курса
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

# Создаем курс
create_course_response = courses_client.create_course(create_course_request)
print('Create course data: ', create_course_response)

# Получаем клиент для заданий
exercises_client = get_exercises_client(authentication_user)

# Тело для создания задания
create_exercise_request = CreateExerciseRequestDict(
    title = "test exercise",
    courseId = create_course_response['course']['id'],
    maxScore = 10,
    minScore = 1,
    orderIndex = 0,
    description = "some basic description",
    estimatedTime = "10 minutes"
)

# Создаем задание
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise data: ", create_exercise_response)