# ml-serve-model-experiment
This project tested how much difference performance of Recommendation System when it's served with Nginx and 4 duplicated gunicorn deployed apps; compared to when it's deployed only with plain flask. It's tested with locust with 50k simulated user and 5000 spawn rate per second.
