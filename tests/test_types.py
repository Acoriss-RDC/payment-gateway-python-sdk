"""Tests for type definitions."""

from acoriss_payment_gateway.types import (
    CustomerInfo,
    Environment,
    PaymentService,
    PaymentSessionRequest,
    PaymentSessionResponse,
    PaymentStatus,
    RetrievePaymentResponse,
    ServiceItem,
)


def test_environment_literal() -> None:
    """Test Environment literal type."""
    env1: Environment = "sandbox"
    env2: Environment = "live"
    assert env1 == "sandbox"
    assert env2 == "live"


def test_payment_status_literal() -> None:
    """Test PaymentStatus literal type."""
    status1: PaymentStatus = "P"
    status2: PaymentStatus = "S"
    status3: PaymentStatus = "C"
    assert status1 == "P"
    assert status2 == "S"
    assert status3 == "C"


def test_customer_info_typed_dict() -> None:
    """Test CustomerInfo TypedDict."""
    customer: CustomerInfo = {
        "email": "test@example.com",
        "name": "Test User",
        "phone": "+1234567890",
    }
    assert customer["email"] == "test@example.com"
    assert customer["name"] == "Test User"
    assert customer["phone"] == "+1234567890"


def test_service_item_typed_dict() -> None:
    """Test ServiceItem TypedDict."""
    service: ServiceItem = {
        "name": "Test Service",
        "price": 1000,
        "description": "A test service",
        "quantity": 2,
    }
    assert service["name"] == "Test Service"
    assert service["price"] == 1000


def test_payment_session_request_typed_dict() -> None:
    """Test PaymentSessionRequest TypedDict."""
    request: PaymentSessionRequest = {
        "amount": 5000,
        "currency": "USD",
        "customer": {
            "email": "test@example.com",
            "name": "Test User",
        },
        "description": "Test payment",
        "transaction_id": "tx_123",
    }
    assert request["amount"] == 5000
    assert request["currency"] == "USD"


def test_payment_session_response_typed_dict() -> None:
    """Test PaymentSessionResponse TypedDict."""
    response: PaymentSessionResponse = {
        "id": "sess_123",
        "amount": 5000,
        "currency": "USD",
        "description": "Test",
        "checkout_url": "https://example.com/checkout",
        "customer": {
            "email": "test@example.com",
            "name": "Test User",
        },
        "created_at": "2025-11-15T12:00:00Z",
    }
    assert response["id"] == "sess_123"
    assert response["checkout_url"] == "https://example.com/checkout"


def test_payment_service_typed_dict() -> None:
    """Test PaymentService TypedDict."""
    service: PaymentService = {
        "id": "srv_123",
        "name": "Test Service",
        "description": "A test service",
        "quantity": 1,
        "price": 1000,
        "currency": "USD",
        "session_id": "sess_123",
        "created_at": "2025-11-15T12:00:00Z",
    }
    assert service["id"] == "srv_123"
    assert service["session_id"] == "sess_123"


def test_retrieve_payment_response_typed_dict() -> None:
    """Test RetrievePaymentResponse TypedDict."""
    response: RetrievePaymentResponse = {
        "id": "pay_123",
        "amount": 5000,
        "currency": "USD",
        "description": "Test payment",
        "transaction_id": "tx_123",
        "customer": {
            "email": "test@example.com",
            "phone": "+1234567890",
        },
        "created_at": "2025-11-15T12:00:00Z",
        "expired": False,
        "services": [],
        "status": "P",
    }
    assert response["id"] == "pay_123"
    assert response["status"] == "P"
    assert response["expired"] is False
