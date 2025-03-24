# ML Serve Model Experiment

This project explores the performance differences between two model-serving deployment strategies:

- **Nginx with 4 Gunicorn-replicated instances**
- **Plain Flask application**

The goal is to evaluate their scalability, response time, and throughput under high user loads.

## Experiment Overview

- **Scenario:** Serving a Recommendation System under high concurrent traffic.
- **Test Tool:** Locust, simulating 50,000 users with a 5,000 users/sec spawn rate.
- **Key Metrics:** Response time, throughput, and resource utilization.
- **Infrastructure:** Comparing Flask standalone vs. Nginx + Gunicorn for handling ML inference.

## Findings

### **Performance Comparison: Nginx + Gunicorn vs. Plain Flask**

#### **Key Findings**
1. **Request Handling**
   - **Plain Flask:** 39,586 requests, **16,493 failures** (~41.7% failure rate).
   - **Nginx + Gunicorn:** 42,230 requests, **only 219 failures** (~0.5% failure rate).
   - **Takeaway:** Nginx + Gunicorn handled slightly more requests and had a **drastically lower failure rate**.

2. **Response Times**
   - **Median Response Time**
     - Plain Flask: **94,000 ms** (~94 sec)
     - Nginx + Gunicorn: **16,000 ms** (~16 sec)
   - **Average Response Time**
     - Plain Flask: **82,513 ms** (~82 sec)
     - Nginx + Gunicorn: **20,765 ms** (~20 sec)
   - **Takeaway:** Nginx + Gunicorn significantly reduces response latency by ~76%.

3. **Peak Performance**
   - **Max Response Time**
     - Plain Flask: **168,688 ms** (~168 sec)
     - Nginx + Gunicorn: **189,862 ms** (~189 sec)
   - **Takeaway:** While Nginx performs better on average, some extreme cases still spike response times.

4. **Concurrency & Throughput**
   - **Requests per Second**
     - Plain Flask: **216.50 req/s**
     - Nginx + Gunicorn: **220.73 req/s**
   - **Takeaway:** Slightly higher throughput for Nginx, but the real win is in stability.

#### **Conclusion**
- **Plain Flask** struggles with high concurrency, resulting in **slow responses and a high failure rate**.
- **Nginx + Gunicorn** dramatically improves performance, reducing **failure rates, response times, and increasing scalability**.
- **For production-ready ML services, the Nginx + Gunicorn setup is the clear winner.**

## Why This Matters

Deploying ML models effectively is as important as training them. This experiment demonstrates an understanding of:

- **Performance optimization** for real-world ML applications.
- **Load balancing and concurrency** in production ML services.
- **Infrastructure considerations** when serving AI models at scale.

## About Me

I'm Rayhan Tito Kharisma, a Machine Learning Engineer with experience in building scalable ML solutions, optimizing inference pipelines, and deploying models in production environments. This project reflects my ability to architect efficient model-serving pipelines, but given time constraints, it's not designed as a plug-and-play solution.

For inquiries, collaborations, or discussions on ML deployment strategies, feel free to connect!

## Contact

- **GitHub:** [rayhantithokharisma](https://github.com/rayhantithokharisma)
- **Email:** [rayhantithokharisma@example.com](mailto:rayhantithokharisma@gmail.com)

