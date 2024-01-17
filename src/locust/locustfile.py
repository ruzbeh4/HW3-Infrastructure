from locust import HttpUser, between, task

HOST_NAME = 'localhost:80'


class LoadTest(HttpUser):
    @task
    def api(self):
        self.client.get('/api/')