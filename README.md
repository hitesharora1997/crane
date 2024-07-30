# Crane Control System

A FastAPI-based application demonstrating crane control with a client-server architecture and a web UI for user interaction.

## Features

- Real-time crane control through WebSocket
- Client-server architecture with FastAPI backend and web frontend
- Docker support for containerization
- Web UI for easy interaction
- RESTful API for crane operations

## Getting Started

### Prerequisites

- Python 3.6 or later
- `virtualenv` or `venv` for creating virtual environments
- Docker (for containerization)

### Project Structure

```plaintext
.
├── backend/                # FastAPI backend code
│   ├── crane/
│   │   ├── crane.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── state_manager.py
│   ├── __init__.py
│   ├── main.py
│   ├── tests/
│   │   ├── test_crane.py
│   │   ├── test_endpoints.py
│   │   ├── test_state_manager.py
│   │   └── test_websocket.py
│   └── venv/               # Virtual environment for backend
├── static/                 # Static files for the frontend
│   └── index.html
├── Dockerfile              # Dockerfile for building the container
├── Makefile                # Makefile for building and running the project
├── README.md               # Project README file
└── requirements.txt        # Python dependencies
```

### API Endpoints
The API endpoints are defined in the backend application. Main endpoints include:
* `GET /`: Serves the frontend application.
* `POST /update_state`: Updates the crane state.
* `POST /solve_ik`: Solves inverse kinematics for the crane.
* `POST /update_origin`: Updates the origin of the crane.
* WebSocket endpoint `/ws` for real-time crane control.

### Installing and Running

Clone the repository:
   ```bash
    git clone https://github.com/hitesharora1997/crane.git
    cd crane
   ```
Create a virtual environment and install dependencies:
   ```bash
   make setup
   ```
Run the application:
   ```bash
   make run
   ```
To run the test:
   ```bash
   make test
   ```
Building Docker Image
   ```bash
   make docker
   ```
Cleaning up the virtual environment and other generated files:
   ```bash
   make clean
   ```
Help
   ```bash
   make help
   ```

### Caveats and Limitations
* Concurrency Handling: Currently handles basic concurrency. Future versions could aim to improve this for high-load scenarios with benchmark tests.
* Error Handling: Basic error handling implemented; can be improved with more contextual errors.
* Testing Coverage: Good coverage for major functionalities. Edge cases and stress conditions can be further improved.
* Code Maintainability: The code is structured for maintainability, with ongoing efforts to improve documentation and code clarity.
* Data Persistence: Currently, data is stored in memory during runtime and is not persisted after the application stops.