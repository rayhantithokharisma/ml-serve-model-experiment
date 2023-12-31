# ml-serve-model-experiment
This project tested how much difference performance of Recommendation System when it's served with Nginx and 4 duplicated gunicorn deployed apps; compared to when it's deployed only with plain flask. It's tested with locust with 50k simulated user and 5000 spawn rate per second.

The recommendation model uses [implicit](https://github.com/benfred/implicit)https://github.com/benfred/implicit library.
For necessary files to run this project, please refer to my [recommender-learning](https://github.com/rayhantithokharisma/recommender-learning)https://github.com/rayhantithokharisma/recommender-learning repo. You can also read data-driven approach when I build this recommender model.

The result of this experiment is pretty obvious, the response time of nginx-served model is way better than plainly served model. Also, the failure rate is below 1% for nginx-served model, while plainly served model has high failure rate (41%).

This repo inspired by https://philchen.com/2019/07/15/scaling-a-python-flask-app-with-nginx-using-multiple-containers-with-docker-compose
