"""Tests for the client module."""


import pytest
import requests
from pytest_mock import MockerFixture

from acoriss_payment_gateway.client import PaymentGatewayClient
from acoriss_payment_gateway.errors import APIError
from acoriss_payment_gateway.signer import SignerInterface


class TestClientInitialization:
    """Test client initialization."""

    def test_init_with_api_secret(self) -> None:
        """Test client initialization with API secret."""
        client = PaymentGatewayClient(
            api_key="test-key",
            api_secret="test-secret",
        )
        assert client.api_key == "test-key"
        assert client.signer is not None
        assert client.base_url == "https://sandbox.checkout.rdcard.net/api/v1"

    def test_init_with_custom_signer(self) -> None:
        """Test client initialization with custom signer."""

        class CustomSigner(SignerInterface):
            def sign(self, data: str) -> str:
                return "custom-sig"

        signer = CustomSigner()
        client = PaymentGatewayClient(
            api_key="test-key",
            signer=signer,
        )
        assert client.signer is signer

    def test_init_with_live_environment(self) -> None:
        """Test client initialization with live environment."""
        client = PaymentGatewayClient(
            api_key="test-key",
            api_secret="test-secret",
            environment="live",
        )
        assert client.base_url == "https://checkout.rdcard.net/api/v1"

    def test_init_with_custom_base_url(self) -> None:
        """Test client initialization with custom base URL."""
        client = PaymentGatewayClient(
            api_key="test-key",
            api_secret="test-secret",
            base_url="https://custom.example.com/api",
        )
        assert client.base_url == "https://custom.example.com/api"

    def test_init_without_secret_or_signer(self) -> None:
        """Test client initialization without secret or signer."""
        client = PaymentGatewayClient(api_key="test-key")
        assert client.signer is None


class TestCreateSession:
    """Test create_session method."""

    def test_create_session_success(self, mocker: MockerFixture) -> None:
        """Test successful session creation."""
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "sess_123",
            "amount": 5000,
            "currency": "USD",
            "checkoutUrl": "https://checkout.example.com/sess_123",
            "customer": {
                "email": "john@example.com",
                "name": "John Doe",
            },
            "createdAt": "2025-11-15T12:00:00Z",
        }
        mock_post = mocker.patch("requests.post", return_value=mock_response)

        client = PaymentGatewayClient(
            api_key="test-key",
            api_secret="test-secret",
        )

        session = client.create_session(
            amount=5000,
            currency="USD",
            customer={
                "email": "john@example.com",
                "name": "John Doe",
            },
        )

        assert session["id"] == "sess_123"
        assert session["amount"] == 5000
        assert session["checkout_url"] == "https://checkout.example.com/sess_123"
        assert mock_post.called

    def test_create_session_with_all_fields(self, mocker: MockerFixture) -> None:
        """Test session creation with all optional fields."""
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "sess_123",
            "amount": 5000,
            "currency": "USD",
            "checkoutUrl": "https://checkout.example.com/sess_123",
            "customer": {
                "email": "john@example.com",
                "name": "John Doe",
                "phone": "+1234567890",
            },
            "createdAt": "2025-11-15T12:00:00Z",
        }
        mocker.patch("requests.post", return_value=mock_response)

        client = PaymentGatewayClient(
            api_key="test-key",
            api_secret="test-secret",
        )

        session = client.create_session(
            amount=5000,
            currency="USD",
            customer={
                "email": "john@example.com",
                "name": "John Doe",
                "phone": "+1234567890",
            },
            description="Test payment",
            callback_url="https://example.com/callback",
            cancel_url="https://example.com/cancel",
            success_url="https://example.com/success",
            transaction_id="tx_123",
            services=[
                {
                    "name": "Service 1",
                    "price": 1000,
                    "description": "Test service",
                    "quantity": 2,
                }
            ],
        )

        assert session["id"] == "sess_123"

    def test_create_session_without_signature_raises(self) -> None:
        """Test that creating session without signature raises ValueError."""
        client = PaymentGatewayClient(api_key="test-key")

        with pytest.raises(ValueError, match="No signature available"):
            client.create_session(
                amount=5000,
                currency="USD",
                customer={"email": "test@example.com", "name": "Test"},
            )

    def test_create_session_with_signature_override(self, mocker: MockerFixture) -> None:
        """Test session creation with signature override."""
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "sess_123",
            "amount": 5000,
            "currency": "USD",
            "checkoutUrl": "https://checkout.example.com/sess_123",
            "customer": {"email": "test@example.com", "name": "Test"},
            "createdAt": "2025-11-15T12:00:00Z",
        }
        mock_post = mocker.patch("requests.post", return_value=mock_response)

        client = PaymentGatewayClient(api_key="test-key")

        session = client.create_session(
            amount=5000,
            currency="USD",
            customer={"email": "test@example.com", "name": "Test"},
            signature_override="custom-signature",
        )

        assert session["id"] == "sess_123"
        # Verify signature header was set
        call_kwargs = mock_post.call_args[1]
        assert call_kwargs["headers"]["X-SIGNATURE"] == "custom-signature"

    def test_create_session_api_error(self, mocker: MockerFixture) -> None:
        """Test API error handling in create_session."""
        mock_response = mocker.Mock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Invalid request"}
        mock_response.headers = {"content-type": "application/json"}

        http_error = requests.HTTPError()
        http_error.response = mock_response

        mock_post = mocker.patch("requests.post", return_value=mock_response)
        mock_post.return_value.raise_for_status.side_effect = http_error

        client = PaymentGatewayClient(
            api_key="test-key",
            api_secret="test-secret",
        )

        with pytest.raises(APIError) as exc_info:
            client.create_session(
                amount=5000,
                currency="USD",
                customer={"email": "test@example.com", "name": "Test"},
            )

        assert exc_info.value.status == 400
        assert exc_info.value.message == "Invalid request"


class TestGetPayment:
    """Test get_payment method."""

    def test_get_payment_success(self, mocker: MockerFixture) -> None:
        """Test successful payment retrieval."""
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "pay_123",
            "amount": 5000,
            "currency": "USD",
            "description": "Test payment",
            "transactionId": "tx_123",
            "customer": {
                "email": "john@example.com",
                "phone": "+1234567890",
            },
            "createdAt": "2025-11-15T12:00:00Z",
            "expired": False,
            "services": [
                {
                    "id": "srv_1",
                    "name": "Service 1",
                    "description": "Test service",
                    "quantity": 1,
                    "price": 1000,
                    "currency": "USD",
                    "sessionId": "sess_123",
                    "createdAt": "2025-11-15T12:00:00Z",
                }
            ],
            "status": "P",
        }
        mock_get = mocker.patch("requests.get", return_value=mock_response)

        client = PaymentGatewayClient(
            api_key="test-key",
            api_secret="test-secret",
        )

        payment = client.get_payment("pay_123")

        assert payment["id"] == "pay_123"
        assert payment["amount"] == 5000
        assert payment["status"] == "P"
        assert payment["expired"] is False
        assert len(payment["services"]) == 1
        assert mock_get.called

    def test_get_payment_without_signature_raises(self) -> None:
        """Test that getting payment without signature raises ValueError."""
        client = PaymentGatewayClient(api_key="test-key")

        with pytest.raises(ValueError, match="No signature available"):
            client.get_payment("pay_123")

    def test_get_payment_with_signature_override(self, mocker: MockerFixture) -> None:
        """Test payment retrieval with signature override."""
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "pay_123",
            "amount": 5000,
            "currency": "USD",
            "transactionId": "tx_123",
            "customer": {"email": "test@example.com", "phone": None},
            "createdAt": "2025-11-15T12:00:00Z",
            "expired": False,
            "services": [],
            "status": "S",
        }
        mock_get = mocker.patch("requests.get", return_value=mock_response)

        client = PaymentGatewayClient(api_key="test-key")

        payment = client.get_payment("pay_123", signature_override="custom-signature")

        assert payment["status"] == "S"
        # Verify signature header was set
        call_kwargs = mock_get.call_args[1]
        assert call_kwargs["headers"]["X-SIGNATURE"] == "custom-signature"

    def test_get_payment_api_error(self, mocker: MockerFixture) -> None:
        """Test API error handling in get_payment."""
        mock_response = mocker.Mock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"message": "Payment not found"}
        mock_response.headers = {"content-type": "application/json"}

        http_error = requests.HTTPError()
        http_error.response = mock_response

        mock_get = mocker.patch("requests.get", return_value=mock_response)
        mock_get.return_value.raise_for_status.side_effect = http_error

        client = PaymentGatewayClient(
            api_key="test-key",
            api_secret="test-secret",
        )

        with pytest.raises(APIError) as exc_info:
            client.get_payment("pay_123")

        assert exc_info.value.status == 404
        assert exc_info.value.message == "Payment not found"


class TestUtilityMethods:
    """Test utility methods."""

    def test_to_snake_case(self) -> None:
        """Test camelCase to snake_case conversion."""
        client = PaymentGatewayClient(api_key="test", api_secret="secret")

        assert client._to_snake_case("checkoutUrl") == "checkout_url"
        assert client._to_snake_case("createdAt") == "created_at"
        assert client._to_snake_case("transactionId") == "transaction_id"
        assert client._to_snake_case("id") == "id"
        assert client._to_snake_case("amount") == "amount"

    def test_convert_keys_to_snake_case(self) -> None:
        """Test recursive key conversion."""
        client = PaymentGatewayClient(api_key="test", api_secret="secret")

        data = {
            "checkoutUrl": "https://example.com",
            "createdAt": "2025-11-15T12:00:00Z",
            "customer": {
                "firstName": "John",
                "lastName": "Doe",
            },
            "services": [
                {"serviceName": "Service 1", "servicePrice": 1000}
            ],
        }

        converted = client._convert_keys_to_snake_case(data)

        assert converted["checkout_url"] == "https://example.com"
        assert converted["created_at"] == "2025-11-15T12:00:00Z"
        assert converted["customer"]["first_name"] == "John"
        assert converted["customer"]["last_name"] == "Doe"
        assert converted["services"][0]["service_name"] == "Service 1"
        assert converted["services"][0]["service_price"] == 1000
