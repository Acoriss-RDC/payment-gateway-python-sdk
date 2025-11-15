.PHONY: help install install-dev test test-cov lint typecheck format clean build publish

help:
	@echo "Available commands:"
	@echo "  install       - Install package dependencies"
	@echo "  install-dev   - Install package with dev dependencies"
	@echo "  test          - Run tests"
	@echo "  test-cov      - Run tests with coverage report"
	@echo "  lint          - Run linting"
	@echo "  typecheck     - Run type checking with mypy"
	@echo "  format        - Format code with ruff"
	@echo "  clean         - Remove build artifacts"
	@echo "  build         - Build distribution packages"
	@echo "  publish       - Publish to PyPI (requires credentials)"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pip install -e .

test:
	pytest

test-cov:
	pytest --cov=acoriss_payment_gateway --cov-report=html --cov-report=term

lint:
	ruff check acoriss_payment_gateway tests

typecheck:
	mypy acoriss_payment_gateway

format:
	ruff format acoriss_payment_gateway tests

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

publish: build
	python -m twine upload dist/*
