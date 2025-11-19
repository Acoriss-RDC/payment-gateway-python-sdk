# Contributing to Acoriss Payment Gateway Python SDK

Thank you for your interest in contributing! We welcome contributions from the community.

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/payment-gateway-python-sdk.git
   cd payment-gateway-python-sdk
   ```
3. **Set up your development environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements-dev.txt
   pip install -e .
   ```
4. **Install pre-commit hooks** (recommended):
   ```bash
   pre-commit install
   ```

## 💻 Development Workflow

### Making Changes

1. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our code style guidelines

3. **Run tests** to ensure everything works:
   ```bash
   make test
   ```

4. **Run all quality checks**:
   ```bash
   make lint        # Run linting
   make typecheck   # Run type checking
   make security    # Run security checks
   make format      # Format code
   ```

5. **Commit your changes** with a descriptive message:
   ```bash
   git commit -m "feat: add new feature X"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request** on GitHub

### Commit Message Convention

We follow conventional commits:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Adding or updating tests
- `refactor:` - Code refactoring
- `style:` - Code style changes (formatting, etc.)
- `chore:` - Maintenance tasks

Example: `feat: add retry logic for network failures`

## 📝 Code Style

### Python Style Guide

- **PEP 8** compliance (enforced by ruff)
- **Type hints** on all public functions (checked by mypy)
- **Docstrings** for all public classes and methods
- **Line length**: 120 characters max

### Pre-commit Hooks

We use pre-commit hooks to ensure code quality:

```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=acoriss_payment_gateway --cov-report=html

# Run specific test file
pytest tests/test_client.py

# Run specific test
pytest tests/test_client.py::TestPaymentGatewayClient::test_create_session
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Use pytest fixtures for common setup
- Aim for **90%+ code coverage**
- Test both success and error cases

Example:
```python
def test_create_session_success(mocker):
    """Test successful session creation."""
    # Arrange
    mock_post = mocker.patch('requests.post')
    mock_post.return_value.json.return_value = {...}
    
    # Act
    client = PaymentGatewayClient(api_key="test", api_secret="secret")
    result = client.create_session(...)
    
    # Assert
    assert result['checkout_url'] == "https://..."
```

## 🔍 Type Checking

We use mypy for static type checking:

```bash
mypy acoriss_payment_gateway
```

All public APIs must have complete type annotations.

## 🔒 Security

- Run security checks before submitting: `make security`
- Never commit API keys or secrets
- Report security vulnerabilities privately (see [SECURITY.md](SECURITY.md))

## 📚 Documentation

- Update `README.md` for user-facing changes
- Update docstrings for API changes
- Add examples for new features
- Update `CHANGELOG.md` following [Keep a Changelog](https://keepachangelog.com/)

## 🎯 Pull Request Guidelines

### Before Submitting

- ✅ All tests pass
- ✅ Code is formatted (run `make format`)
- ✅ Linting passes (run `make lint`)
- ✅ Type checking passes (run `make typecheck`)
- ✅ Security checks pass (run `make security`)
- ✅ Coverage is maintained or improved
- ✅ Documentation is updated
- ✅ CHANGELOG.md is updated

### PR Description

Include:
- What changed and why
- How to test the changes
- Any breaking changes
- Related issue numbers (e.g., "Fixes #123")

### Review Process

1. Automated CI checks must pass
2. At least one maintainer approval required
3. Address review comments
4. Keep PR focused and reasonably sized

## 🏗️ Project Structure

```
acoriss_payment_gateway/
├── __init__.py          # Package exports
├── client.py            # Main client
├── errors.py            # Exceptions
├── signer.py            # Signature implementations
├── types.py             # Type definitions
└── retry.py             # Retry logic
```

## 🔄 Release Process

(For maintainers)

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create a git tag: `git tag -a v0.x.x -m "Release v0.x.x"`
4. Push tag: `git push origin v0.x.x`
5. GitHub Actions will automatically publish to PyPI

## ❓ Questions?

- Open an issue for bug reports or feature requests
- Check existing issues and PRs first
- Join discussions for general questions

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉
