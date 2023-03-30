# FastAPI To-Do List
## Description

This is a FastAPI-based API for a To-Do List application. The API allows users to create to-do items with three different statuses: "to-do", "in-progress", and "done". Users can update the status and other information for each item, as well as delete them. The API is backed by a MongoDB database for data storage. The application is designed to be simple and easy to use.

In addition to the main application code, the repository includes a suite of tests using Pytest to ensure that the API is working as intended.

## Installation

1. Clone the repository

```bash
git clone https://github.com/viniciusenari/fastapi-to-do.git
```
or
```
git clone git@github.com:viniciusenari/fastapi-to-do.git
```

2. Create a and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
To activate the virtual environment on Windows:
```
venv\Scripts\activate
```

4. Install poetry and the dependencies

```bash
pip install poetry
poetry install
```

6. Create a .env file with the following variables:

```bash
MONGO_CONNECTION_STRING = "<your_mongo_connection_string>"
```

7. Run the app
```bash
uvicorn main:app --reload
```

## Usage

With the API running locally, you can find the API documentation at http://localhost:8000/docs or http://localhost:8000/redoc.

## Tests

To run the tests, run the following command:
```bash
pytest .
```

## Formatting and Linting

To format the code, run the following command:
```bash
black .
```

To check the code for formatting errors, run the following command:
```bash
flake8 .
```

## License

[MIT License](https://github.com/viniciusenari/fastapi-to-do/blob/main/LICENSE)