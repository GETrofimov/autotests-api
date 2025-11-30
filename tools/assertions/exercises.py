from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
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
