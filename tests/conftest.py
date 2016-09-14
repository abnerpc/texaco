import pytest

from texaco import create_app


@pytest.fixture
def app_client():
    app = create_app('configtest')
    return app.test_client()


@pytest.fixture
def fake_reader():
    def gen_lines():
        for i in range(3):
            yield str(i)
    return gen_lines
