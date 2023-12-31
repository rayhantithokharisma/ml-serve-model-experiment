import json
import random
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(0.01, 2)  # Time between requests

    options_list = [
        1515915625355805313,
        1515915625379210214,
        1515915625385482819,
        1515915625425059411
    ]

    @task
    def access_single_flask_app(self):
        payload = {"user_id": self.generate_random_data()}
        self.client.post("http://localhost:5000/recommend_items", json=payload)

    # @task
    # def access_multiple_flask_apps(self):
    #     payload = {"user_id": self.generate_random_data()}
    #     self.client.post("http://localhost:82/recommend_items", json=payload)

    def generate_random_data(self):
        # Select a random item from the options_list
        return random.choice(self.options_list)
