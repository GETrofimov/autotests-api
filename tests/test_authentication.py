import pytest
from http import HTTPStatus
from clients.authentication.authentication_client import AuthenticationClient

from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema

from tests.conftest import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.authentication import assert_login_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login(function_user: UserFixture, authentication_client: AuthenticationClient):
    authenticate_user_request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )

    # Авторизуемся под созданным юзером
    response = authentication_client.login_api(authenticate_user_request)
    response_data = LoginResponseSchema.model_validate_json(response.text)

    # Проверяем статус код
    assert_status_code(response.status_code, HTTPStatus.OK)

    # Проверяем ответ
    assert_login_response(response_data)

    # Проверяем, что ответ соответствует JSON схеме
    validate_json_schema(response.json(), response_data.model_json_schema())