from unittest import TestCase
from fastapi.testclient import TestClient
from api import app


class TestApi(TestCase):



    def test_health_check(self):
        self.assertTrue(
            TestClient(app).get('/api/healthz').status_code == 200
        )