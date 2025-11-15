# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-11-15

### Added
- Initial release of the Acoriss Payment Gateway Python SDK
- `PaymentGatewayClient` for creating sessions and retrieving payments
- HMAC-SHA256 signature support via `HmacSha256Signer`
- Custom signer interface via `SignerInterface`
- Comprehensive type hints using TypedDict
- Full test suite with pytest
- Support for Python 3.8+
- Automatic camelCase to snake_case conversion for API responses
- `APIError` exception for API error handling
- Environment support (sandbox/live)
- Configurable timeouts and base URLs

[0.1.0]: https://github.com/Acoriss-RDC/payment-gateway-python-sdk/releases/tag/v0.1.0
