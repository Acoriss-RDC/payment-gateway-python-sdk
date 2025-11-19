"""Tests for the signer module."""

from acoriss_payment_gateway.signer import HmacSha256Signer, SignerInterface


def test_hmac_sha256_signer_sign() -> None:
    """Test HMAC-SHA256 signature generation."""
    signer = HmacSha256Signer("test-secret")
    data = '{"amount":5000,"currency":"USD"}'
    signature = signer.sign(data)

    # Verify it's a hex string
    assert isinstance(signature, str)
    assert len(signature) == 64  # SHA256 produces 64 hex characters
    assert all(c in "0123456789abcdef" for c in signature)


def test_hmac_sha256_signer_consistency() -> None:
    """Test that the same input produces the same signature."""
    signer = HmacSha256Signer("test-secret")
    data = "test-data"

    sig1 = signer.sign(data)
    sig2 = signer.sign(data)

    assert sig1 == sig2


def test_hmac_sha256_signer_different_secrets() -> None:
    """Test that different secrets produce different signatures."""
    signer1 = HmacSha256Signer("secret1")
    signer2 = HmacSha256Signer("secret2")
    data = "test-data"

    sig1 = signer1.sign(data)
    sig2 = signer2.sign(data)

    assert sig1 != sig2


def test_hmac_sha256_signer_different_data() -> None:
    """Test that different data produces different signatures."""
    signer = HmacSha256Signer("test-secret")

    sig1 = signer.sign("data1")
    sig2 = signer.sign("data2")

    assert sig1 != sig2


def test_custom_signer_implementation() -> None:
    """Test that custom signers can implement SignerInterface."""

    class CustomSigner(SignerInterface):
        def sign(self, data: str) -> str:
            return "custom-signature"

    signer = CustomSigner()
    assert signer.sign("any-data") == "custom-signature"
