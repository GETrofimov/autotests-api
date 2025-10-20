from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

# Получаем public client
public_user_client = get_public_users_client()

# Тело дляя запроса создания юзера
create_user_request = CreateUserRequestSchema(
    email = get_random_email(),
    password = "123456789",
    last_name = "Иванов",
    first_name = "Иван",
    middle_name = "Иванович"
)

# Создаем юзера
create_user_response = public_user_client.create_user(create_user_request)

# Тело для аутентификации
authentication_user = AuthenticationUserSchema(
    email = create_user_request.email,
    password = create_user_request.password
)

# Получаем клиенты для файлов и курсов
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)

# Тело для создания файла
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)

# Создаем файлик 
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Тело для создания курса
create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score=100,
    min_score=10,
    description="Python API course",
    estimated_time="2 weeks",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)

# Создаем курс
create_course_response = courses_client.create_course(create_course_request)
print('Create course data: ', create_course_response)

# Получаем клиент для заданий
exercises_client = get_exercises_client(authentication_user)

# Тело для создания задания
create_exercise_request = CreateExerciseRequestSchema(
    title = "test exercise",
    course_id = create_course_response.course.id,
    max_score = 10,
    min_score = 1,
    order_index = 0,
    description = "some basic description",
    estimated_time = "10 minutes"
)

# Создаем задание
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise data: ", create_exercise_response)