# Hybrid Anime Recommendation System

A production-ready Anime Recommendation System integrating hybrid filtering strategies, automated CI/CD, and containerized microservice deployment on a simulated Kubernetes (Minikube) cluster.

## Key Features
- **Hybrid Recommender** using Content-Based + Collaborative Filtering
- Lightweight Flask-based API for real-time recommendations
- Fully containerized microservices using Docker
- CI/CD automated using **Jenkins** + **ArgoCD** pipelines
- Kubernetes Deployment tested locally using **Minikube**
- Version-controlled experiments + pipeline via GitHub

## System Architecture
**User Request** → **Flask API** → **Hybrid Recommendation Engine** (Content-Based + Collaborative Filtering) → **Ranked Anime Results**

## Tech Stack
| Layer | Tools |
|-------|-------|
| ML / Recommender | Python, Pandas, Scikit-learn |
| API Serving | Flask |
| CI/CD | Jenkins CI, ArgoCD CD |
| Containers | Docker |
| Cluster Orchestration | Minikube (Kubernetes) |
| Version Control | GitHub |

## How To Run Locally
```bash
git clone <repo_url>
cd Hybrid-Anime-Recommendation-System
pip install -r requirements.txt
python app.py
docker build -t anime-rec .
docker run -p 8000:8000 anime-rec
