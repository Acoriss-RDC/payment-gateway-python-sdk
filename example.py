"""Example usage of the Acoriss Payment Gateway SDK."""

from acoriss_payment_gateway import PaymentGatewayClient
from acoriss_payment_gateway.errors import APIError


def main() -> None:
    """Main example function."""
    # Initialize the client
    client = PaymentGatewayClient(
        api_key="your-api-key",
        api_secret="your-api-secret",
        environment="sandbox",  # or "live"
    )

    # Create a payment session
    try:
        session = client.create_session(
            amount=5000,  # Amount in cents ($50.00)
            currency="USD",
            customer={
                "email": "john@example.com",
                "name": "John Doe",
                "phone": "+1234567890",
            },
            description="Payment for Order #1234",
            callback_url="https://example.com/api/callback",
            cancel_url="https://example.com/cancel",
            success_url="https://example.com/success",
            transaction_id="order_1234",
            services=[
                {
                    "name": "express_delivery",
                    "price": 1500,
                    "description": "Express delivery service",
                    "quantity": 1,
                }
            ],
        )

        print("Payment session created successfully!")
        print(f"Session ID: {session['id']}")
        print(f"Checkout URL: {session['checkout_url']}")
        print(f"Amount: {session['amount']} {session['currency']}")

        # Retrieve payment details
        payment = client.get_payment(session["id"])

        print("\nPayment details:")
        print(f"Status: {payment['status']}")
        print(f"Expired: {payment['expired']}")
        print(f"Customer Email: {payment['customer']['email']}")
        print(f"Services: {len(payment['services'])}")

    except APIError as e:
        print(f"API Error: {e}")
        print(f"Status: {e.status}")
        print(f"Data: {e.data}")


if __name__ == "__main__":
    main()
