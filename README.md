# 🛍️ Customer Segmentation & Targeting System

A cloud-native web application that uses unsupervised machine learning to segment customers into distinct groups based on their spending habits.

## Live Demo

-   **Frontend (User Interface):** https://huggingface.co/spaces/chatterjeerohit08/customer-segmentation-ui
-   **Backend (API Documentation):** https://segmentation-service-86215100553.us-central1.run.app/segment

---

## Overview

This project demonstrates a professional, end-to-end workflow for deploying a machine learning model. It takes customer data (annual income and spending score) and uses a **K-Means Clustering** algorithm to assign each customer to one of five distinct segments, such as "High-Spending Target" or "Frugal."

The application is built using a modern, decoupled architecture, making it scalable and maintainable.

### Key Features
-   **Unsupervised Learning:** Automatically discovers customer groups using K-Means clustering.
-   **Decoupled Architecture:** A standalone backend API is separate from the frontend user interface.
-   **Containerized Backend:** The FastAPI is packaged with Docker, making it portable and ready for any cloud environment.
-   **Cloud-Native Deployment:** The backend is deployed on a scalable, serverless platform (Google Cloud Run).
-   **Interactive UI:** A simple Gradio frontend allows users to input customer data and receive their segment in real-time.

---

## Architecture

This project consists of two main components that communicate over the internet:

1.  **Backend API:** A Python **FastAPI** service running in a **Docker** container on **Google Cloud Run**. It loads the trained K-Means model and exposes a `/segment` endpoint for predictions.
2.  **Frontend UI:** A **Gradio** application hosted on **Hugging Face Spaces**. It provides a user-friendly interface with sliders and calls the backend API to get results.



---

## Technology Stack

-   **Backend & Modeling:** Python, FastAPI, Scikit-learn, Docker
-   **Frontend:** Gradio, Requests
-   **Deployment:** Google Cloud Run, Google Artifact Registry, Hugging Face Spaces

---

## How to Run Locally

To run this project, you need two separate terminals. Ensure Docker Desktop is running first.

### 1. Run the Backend API

```bash
# Navigate to the project's root directory
cd customer-segmentation

# 1. Build the Docker image
docker build -t segmentation-api .

# 2. Run the Docker container
docker run -p 8000:8000 segmentation-api
