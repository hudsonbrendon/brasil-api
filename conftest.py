import pytest

from brasil_api.brasilapi import BrasilAPI


@pytest.fixture
def brasil_api():
    return BrasilAPI()
