import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def restore_activities_state():
    original_activities = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client
