# Variables
VENV_NAME = venv
PYTHON = $(VENV_NAME)/bin/python
PIP = $(VENV_NAME)/bin/pip
PYTEST = $(VENV_NAME)/bin/pytest
FLAKE8 = $(VENV_NAME)/bin/flake8
AUTOPEP8 = $(VENV_NAME)/bin/autopep8

.PHONY: setup install run test lint fix-lint clean docker help

# Default target
all: clean setup install lint test run

# Create virtual environment and install dependencies
setup:
	@echo "Setting up the virtual environment and installing dependencies."
	python3 -m venv $(VENV_NAME)
	$(PIP) install -r requirements.txt
	$(PIP) install flake8 autopep8

# Install dependencies
install: $(VENV_NAME)
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

# Lint the code with flake8
lint: setup
	@echo "Linting the code..."
	$(FLAKE8) backend/crane backend/tests --count --select=E9,F63,F7,F82 --show-source --statistics
	$(FLAKE8) backend/crane backend/tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Fix linting issues automatically with autopep8
fix-lint: setup
	@echo "Fixing linting issues..."
	$(AUTOPEP8) --in-place --aggressive --aggressive -r backend/crane backend/tests

# Run the application
run:
	@echo "Running the application..."
	PYTHONPATH=$(PWD) $(VENV_NAME)/bin/uvicorn backend.main:app --reload

# Run tests
test: install
	@echo "Running tests..."
	PYTHONPATH=$(PWD) $(PYTEST) backend/tests

# Build Docker image
docker:
	@echo "Building Docker image..."
	docker build -t crane .

# Clean up
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_NAME)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

# Display help information
help:
	@echo "Usage: make [TARGET]"
	@echo ""
	@echo "Targets:"
	@echo "  setup     - Create virtual environment and install dependencies"
	@echo "  install   - Install dependencies"
	@echo "  lint      - Lint the code"
	@echo "  fix-lint  - Fix linting issues"
	@echo "  run       - Run the application"
	@echo "  test      - Run tests"
	@echo "  clean     - Clean up"
	@echo "  docker    - Build Docker image"
	@echo "  help      - Show this help message"
