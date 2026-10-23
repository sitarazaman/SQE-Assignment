
import pytest
from requests.models import Response


@pytest.mark.models
def test_status_200_is_ok():
    response = Response()
    response.status_code = 200
    assert response.ok is True


@pytest.mark.models
def test_status_201_is_ok():
    response = Response()
    response.status_code = 201
    assert response.ok is True


@pytest.mark.models
def test_status_301_is_ok():
    response = Response()
    response.status_code = 301
    assert response.ok is True


@pytest.mark.models
def test_status_302_is_ok():
    response = Response()
    response.status_code = 302
    assert response.ok is True


@pytest.mark.models
def test_status_399_is_ok():
    response = Response()
    response.status_code = 399
    assert response.ok is True


@pytest.mark.models
def test_status_400_is_not_ok():
    response = Response()
    response.status_code = 400
    assert response.ok is False


@pytest.mark.models
def test_status_404_is_not_ok():
    response = Response()
    response.status_code = 404
    assert response.ok is False


@pytest.mark.models
def test_status_500_is_not_ok():
    response = Response()
    response.status_code = 500
    assert response.ok is False


@pytest.mark.models
def test_status_599_is_not_ok():
    response = Response()
    response.status_code = 599
    assert response.ok is False


@pytest.mark.models
def test_status_100_is_ok():
    response = Response()
    response.status_code = 100
    assert response.ok is True
