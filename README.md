# Stability AI Image Generation with Django & Celery

A Django application that generates images using Stability AI's Text-to-Image API, utilizing Celery for parallel processing to handle asynchronous tasks.

## Features

Asynchronous Image Generation: Generates multiple images in parallel using Celery.
Stability AI Integration: Connects to the Stability AI API to create images from text prompts.
Django Backend: Stores image URLs and prompts in the database.
User Interface: Simple web UI to input prompts and view generated images.

## Prerequisites

Before running the application, ensure you have the following installed:

Python 3.x
Redis: Required for Celery as a message broker.
Stability AI API Key: Obtain from Stability AI.

## Getting Started

1. ### Clone The Repository

   git clone <repository_url>
   cd your_project_name

2. ### Set Up a Virtual Environment

   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`

3. ### Install Dependencies

   pip install -r requirements.txt

4. ### Set Up Redis
   Start the Redis server on your system:
   redis-server

5. ### Configure Your API Key
   Create a .env file in the project root (same directory as manage.py) and add your Stability AI API key:
   STABILITY_API_KEY=your-api-key-here
   
6. ### Apply Migrations
   Apply the database migrations:
   python manage.py migrate

7. ### Start Celery Workers
   In a new terminal, start the Celery worker:
   celery -A your_project_name worker --loglevel=info

8. ### Run the Django Development Server
   Start the Django development server:
   
   python manage.py runserver

9. ### Access the Application
   Open your web browser and navigate to:
   Generate Images: http://127.0.0.1:8000/generate-images/

## Troubleshooting
### Common Issues
Redis Not Running: Ensure Redis is running before starting the Celery worker.
API Key Issues: Verify that your Stability AI API key is correctly set in the .env file.
Database Issues: Run python manage.py migrate to ensure the database schema is up-to-date.
   

   
