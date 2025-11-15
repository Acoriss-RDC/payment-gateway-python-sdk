"""Tests for the errors module."""


from acoriss_payment_gateway.errors import APIError


def test_api_error_basic() -> None:
    """Test basic APIError creation."""
    error = APIError("Something went wrong")
    assert str(error) == "APIError: Something went wrong"
    assert error.message == "Something went wrong"
    assert error.status is None
    assert error.data is None
    assert error.headers is None


def test_api_error_with_status() -> None:
    """Test APIError with status code."""
    error = APIError("Not found", status=404)
    assert str(error) == "APIError(404): Not found"
    assert error.status == 404


def test_api_error_with_all_fields() -> None:
    """Test APIError with all fields."""
    error = APIError(
        "Validation failed",
        status=400,
        data={"errors": ["field required"]},
        headers={"content-type": "application/json"},
    )
    assert error.message == "Validation failed"
    assert error.status == 400
    assert error.data == {"errors": ["field required"]}
    assert error.headers == {"content-type": "application/json"}


def test_api_error_repr() -> None:
    """Test APIError repr."""
    error = APIError("Test", status=500, data={"error": "internal"})
    repr_str = repr(error)
    assert "APIError" in repr_str
    assert "Test" in repr_str
    assert "500" in repr_str
