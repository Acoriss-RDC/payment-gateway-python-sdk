"""
Acoriss Payment Gateway Python SDK
===================================

This package provides a Python client for the Acoriss Payment Gateway API.
"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="acoriss-payment-gateway",
    version="0.1.0",
    author="Acoriss",
    author_email="info@acoriss.com",
    description="Python SDK for Acoriss Payment Gateway",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Acoriss-RDC/payment-gateway-python-sdk",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-mock>=3.11.0",
            "mypy>=1.5.0",
            "ruff>=0.0.292",
            "types-requests>=2.31.0",
        ],
    },
    keywords="payments sdk checkout acoriss",
    project_urls={
        "Documentation": "https://github.com/Acoriss-RDC/payment-gateway-python-sdk#readme",
        "Source": "https://github.com/Acoriss-RDC/payment-gateway-python-sdk",
        "Issues": "https://github.com/Acoriss-RDC/payment-gateway-python-sdk/issues",
    },
)
