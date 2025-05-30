# Flask "Hello Pickle Rick" App

A simple Flask web application that displays "hello Pickle Rick" on the home page.

## Running Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
python app.py
```

The app will be available at http://localhost:8000

## Running with Docker

1. Build the Docker image:
```bash
docker build -t flask-pickle-rick .
```

2. Run the Docker container:
```bash
docker run -p 8000:8000 flask-pickle-rick
```

The app will be available at http://localhost:8000 