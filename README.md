# Internal Utility Service

Run locally:

pip install -r requirements.txt
python app.py

Runs on port 5000.


Internal Utility Service – Production Deployment
📌 Overview

This project transforms a locally-run Flask application into a production-ready system using Docker, CI/CD, and AWS EC2 with HTTPS.


🧱 Architecture

1 GitHub → CI/CD pipeline
2 Docker Hub → Image storage
3 AWS EC2 → Hosting
4 Nginx → Reverse proxy
5 Let’s Encrypt → HTTPS
8 DuckDNS → Domain


🐳 Docker Strategy

1 Multi-stage build for smaller image size
2 Non-root user for security

3 HEALTHCHECK implemented:

HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1


🔁 CI/CD Pipeline

Implemented using GitHub Actions:

Steps:

1 Run tests (pytest)
2 Build Docker image
3 Push to Docker Hub
4 Deploy to EC2 via SSH

Deployment is fully automated on push to main.


🔐 Secrets Management

1 GitHub Secrets → CI/CD credentials
2 AWS EC2 runtime → environment variables
3 No secrets stored in:
    i. source code
    ii. Dockerfile
    iii. Git history


🌐 Deployment
1 App runs inside Docker on EC2 (port 5000)
2 Nginx proxies traffic → container
3 HTTPS enabled using Let’s Encrypt
4 Domain: internal-utility-app.duckdns.org


🔄 Update Strategy

Rolling update simulation:

1 Pull new image
2 Stop old container
3 Start new container


❤️ Health Checks
1 Docker HEALTHCHECK configured
2 Verified using: docker ps


🔁 Auto Restart
--restart always

Ensures container recovers from crashes.


⚠️ Failure Simulation
1 Test failure → blocks deployment
2 Container stop → auto restart
3 Missing secret → deployment fails


📈 Future Improvements
1 Kubernetes deployment
2 Load balancer
3 Multiple EC2 instances





THIS MY SECOND PROJECT BY THE WAY, I'M DOING GREAT.





