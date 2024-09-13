
---

# Lexer C - Backend (FastAPI)

This is the backend of the Lexer C application, built with FastAPI. It processes the C code sent from the frontend and returns the result of the lexical analysis.

## Requirements

- Python 3.8 or higher
- pip

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repository/lexer-c-backend.git
   ```

2. Navigate to the project directory:
   ```bash
   cd lexer-c-backend
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. If you don't have the `requirements.txt` file, you can create one with the following content:
   ```bash
   fastapi
   uvicorn
   pydantic
   ```

## Usage

Start the FastAPI server with Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```

The server will be running at http://127.0.0.1:8000. You can view the API documentation at http://127.0.0.1:8000/docs.

## Project Structure

- `main.py`: Main file that contains the API routes and the logic to process the C code.
- `lexer.py`: Contains the lexical analyzer code that processes the C code.
- `requirements.txt`: List of dependencies required to run the project.

## Connecting with the Frontend

Ensure that the frontend (Next.js) is running at http://localhost:3000 and is making requests to the backend at http://127.0.0.1:8000.

--- 

