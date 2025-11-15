# Getting Started with Acoriss Payment Gateway Python SDK

## Installation

### From PyPI (once published)

```bash
pip install acoriss-payment-gateway
```

### From Source (Development)

```bash
# Clone the repository
cd /path/to/acoriss/payment-gateway/sdks/python

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e .

# Or install with dev dependencies
pip install -r requirements-dev.txt
```

## Quick Start

### Basic Usage

```python
from acoriss_payment_gateway import PaymentGatewayClient

# Initialize the client
client = PaymentGatewayClient(
    api_key="your-api-key",
    api_secret="your-api-secret",
    environment="sandbox"  # or "live"
)

# Create a payment session
session = client.create_session(
    amount=5000,  # $50.00 in cents
    currency="USD",
    customer={
        "email": "customer@example.com",
        "name": "John Doe",
        "phone": "+1234567890"
    },
    description="Order #1234",
    success_url="https://yoursite.com/success",
    cancel_url="https://yoursite.com/cancel",
)

# Redirect user to checkout
print(f"Checkout URL: {session['checkout_url']}")

# Later, retrieve payment status
payment = client.get_payment(session['id'])
print(f"Payment Status: {payment['status']}")
```

### With Custom Signer

```python
from acoriss_payment_gateway import PaymentGatewayClient
from acoriss_payment_gateway.signer import SignerInterface

class CustomSigner(SignerInterface):
    def sign(self, data: str) -> str:
        # Your custom signing logic
        return custom_hmac(data)

client = PaymentGatewayClient(
    api_key="your-api-key",
    signer=CustomSigner()
)
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=acoriss_payment_gateway --cov-report=html

# Run specific test file
pytest tests/test_client.py

# Run with verbose output
pytest -v
```

### Type Checking

```bash
mypy acoriss_payment_gateway
```

### Linting

```bash
# Check code
ruff check acoriss_payment_gateway tests

# Auto-fix issues
ruff check --fix acoriss_payment_gateway tests

# Format code
ruff format acoriss_payment_gateway tests
```

### Using Makefile

```bash
# Install dev dependencies
make install-dev

# Run tests
make test

# Run tests with coverage
make test-cov

# Type check
make typecheck

# Lint
make lint

# Format
make format

# Clean build artifacts
make clean

# Build package
make build
```

## Building for Distribution

```bash
# Build the package
python -m build

# This creates:
# - dist/acoriss_payment_gateway-0.1.0.tar.gz
# - dist/acoriss_payment_gateway-0.1.0-py3-none-any.whl
```

## Publishing to PyPI

```bash
# Install twine if not already installed
pip install twine

# Upload to TestPyPI first (recommended)
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*
```

## Project Structure

```
acoriss-payment-gateway/
├── acoriss_payment_gateway/     # Main package
│   ├── __init__.py              # Package exports
│   ├── client.py                # Main client implementation
│   ├── errors.py                # Exception classes
│   ├── signer.py                # Signature implementations
│   ├── types.py                 # Type definitions
│   └── py.typed                 # PEP 561 marker
├── tests/                       # Test suite
│   ├── __init__.py
│   ├── test_client.py
│   ├── test_errors.py
│   ├── test_signer.py
│   └── test_types.py
├── example.py                   # Example usage
├── pyproject.toml               # Project metadata & config
├── setup.py                     # Setup script
├── requirements.txt             # Runtime dependencies
├── requirements-dev.txt         # Development dependencies
├── README.md                    # Package documentation
├── CHANGELOG.md                 # Version history
├── LICENSE                      # MIT License
├── Makefile                     # Development commands
└── .gitignore                   # Git ignore rules
```

## Environment Variables

You can also configure the SDK using environment variables:

```python
import os
from acoriss_payment_gateway import PaymentGatewayClient

client = PaymentGatewayClient(
    api_key=os.getenv("ACORISS_API_KEY"),
    api_secret=os.getenv("ACORISS_API_SECRET"),
    environment=os.getenv("ACORISS_ENV", "sandbox")
)
```

## Features

✅ Full type hints with Python 3.8+ support
✅ HMAC-SHA256 signature support
✅ Custom signer interface
✅ Automatic camelCase ↔ snake_case conversion
✅ Comprehensive error handling
✅ 96% test coverage
✅ Zero required dependencies (only `requests`)
✅ Environment support (sandbox/live)
✅ Fully typed with mypy
✅ Linted with ruff

## API Reference

See [README.md](README.md) for full API documentation.

## Support

For issues and questions:
- GitHub Issues: https://github.com/Acoriss-RDC/payment-gateway-python-sdk/issues
- Documentation: https://github.com/Acoriss-RDC/payment-gateway-python-sdk#readme
