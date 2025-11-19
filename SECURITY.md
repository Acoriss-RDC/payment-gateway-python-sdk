# Security Policy

## Supported Versions

We release security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1.0 | :x:                |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them responsibly by emailing: **security@acoriss.com**

Include the following information:

- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact
- Suggested fix (if any)

### What to Expect

1. **Acknowledgment**: We'll acknowledge receipt within 48 hours
2. **Assessment**: We'll assess the vulnerability and confirm if it's valid
3. **Fix Timeline**: We'll provide an estimated timeline for a fix
4. **Update**: We'll keep you informed of progress
5. **Disclosure**: We'll coordinate disclosure timing with you

### Security Best Practices

When using this SDK:

1. **Never commit API keys or secrets** to version control
2. **Use environment variables** for sensitive configuration:
   ```python
   import os
   client = PaymentGatewayClient(
       api_key=os.getenv('ACORISS_API_KEY'),
       api_secret=os.getenv('ACORISS_API_SECRET')
   )
   ```

3. **Validate webhook signatures** on your callback endpoints
4. **Use HTTPS** for all callback and redirect URLs
5. **Keep the SDK updated** to the latest version
6. **Use secrets management** in production (e.g., AWS Secrets Manager, HashiCorp Vault)
7. **Review permissions** - only grant necessary access

### Known Security Considerations

- **HMAC-SHA256 Signatures**: All API requests are signed using HMAC-SHA256 to prevent tampering
- **HTTPS Required**: Always use HTTPS for production environments
- **No Sensitive Data in Logs**: The SDK does not log sensitive information

### Security Updates

Security updates will be released as patch versions (e.g., 0.1.3) and documented in:
- [CHANGELOG.md](CHANGELOG.md)
- GitHub Security Advisories
- Release notes

### Bug Bounty

We currently do not offer a bug bounty program, but we greatly appreciate responsible disclosure of security issues.

---

Thank you for helping keep Acoriss Payment Gateway SDK secure!
