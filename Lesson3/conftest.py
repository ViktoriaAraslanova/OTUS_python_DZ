import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        help="Request base url",
        default='https://jsonplaceholder.typicode.com/todos'
    )


@pytest.fixture(scope='module')
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='module')
def session():
    return requests.Session()
