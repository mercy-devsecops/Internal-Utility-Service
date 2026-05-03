# 🚀 Production-Ready Containerized Web Application with Secure CI/CD

## 🌐 Live Application

🔗 View Live App: https://internal-utility-app.duckdns.org

## 📌 Overview

This project transforms a locally developed Flask application into a secure, production-ready system using Docker, AWS EC2, and automated CI/CD pipelines.

It focuses on reliability, security, and zero-downtime deployment strategies.


## 🧱 Architecture

* **GitHub** → Source control & CI/CD pipeline
* **Docker Hub** → Image registry
* **AWS EC2** → Application hosting
* **Nginx** → Reverse proxy layer
* **Let’s Encrypt** → HTTPS encryption
* **DuckDNS** → Domain management


## 🐳 Containerization Strategy

* Multi-stage Docker build to reduce image size
* Runs as non-root user for improved security
* HEALTHCHECK configured for runtime validation


## 🔁 CI/CD Pipeline

Automated using GitHub Actions:

Steps:

1. Run tests (pytest)
2. Build Docker image
3. Push image to Docker Hub
4. Deploy automatically to EC2

✅ Deployment triggered on push to `main`
🚫 Failed tests block deployment


## 🔐 Secrets Management

* GitHub Secrets → CI/CD credentials
* AWS EC2 environment variables → runtime secrets
* No secrets stored in source code, Dockerfile, or history


## 🌐 Deployment

* Application runs inside Docker container on EC2
* Nginx routes traffic to the container
* HTTPS enabled using Let’s Encrypt
* HTTP automatically redirects to HTTPS


## 🔄 Deployment Strategy

Rolling update simulation:

1. Pull new image
2. Stop old container
3. Start new container


## ❤️ Health Monitoring

* Docker HEALTHCHECK configured
* Auto-restart enabled (`--restart always`)
* Container recovers automatically from failure


## ⚠️ Failure Handling

* Test failures block deployment
* Missing secrets prevent startup
* Container crash triggers auto-restart


## 📈 Future Improvements

* Kubernetes-based deployment
* Load balancing across multiple instances
* Horizontal scaling


## 📄 Documentation

Detailed engineering decisions, architecture diagrams, and security reasoning:
https://docs.google.com/document/d/1Fj4snFdcg6vaajU0M576k8Ms6SdF9mC9hSNSbmcr5HA/edit?usp=sharing


## 🎯 Key Outcomes

* Fully automated CI/CD pipeline
* Secure secrets management
* Production-grade deployment on AWS
* HTTPS-enabled system with reverse proxy
* Fault-tolerant container behavior






