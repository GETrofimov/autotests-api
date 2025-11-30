from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, ExerciseSchema, GetExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        resposne: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на создание задания соответствует данным из запроса.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными созданного задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(resposne.exercise.title, request.title, "title")
    assert_equal(resposne.exercise.course_id, request.course_id, "course_id")
    assert_equal(resposne.exercise.max_score, request.max_score, "maxScore")
    assert_equal(resposne.exercise.min_score, request.min_score, "minScore")
    assert_equal(resposne.exercise.order_index, request.order_index, "orderIndex")
    assert_equal(resposne.exercise.description, request.description, "description")
    assert_equal(resposne.exercise.estimated_time, request.estimated_time, "estimatedTime")


def assert_exercise(
        actual: ExerciseSchema,
        expected: ExerciseSchema):
    """
    Проверяет, что ответ на получение задания соответствует ожидаемым данным.

    :param actual: Фактические данные задания.
    :param expected: Ожидаемые данные задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "maxScore")
    assert_equal(actual.min_score, expected.min_score, "minScore")
    assert_equal(actual.order_index, expected.order_index, "orderIndex")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimatedTime")


def assert_get_exercise_response(
        get_exercises_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema
):
    """
    Проверяет, что ответ на получение списка заданий соответствует ответу на его создание.

    :param  get_exercises_response: Ответ API при запросе задания.
    :param create_course_responses: Список API ответов при создании задания.
    :raises AssertionError: Если данные заданий не совпадают.
    """
    assert_exercise(get_exercises_response.exercise, create_exercise_response.exercise)