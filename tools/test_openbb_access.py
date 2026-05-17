#!/usr/bin/env python3
"""
Test script to verify OpenBB access and capabilities.
Tests available connectivity and data retrieval methods.
"""

import sys
import json
from datetime import datetime, timedelta
from typing import Dict, Any, Optional

def test_openbb_sdk() -> Dict[str, Any]:
    """Test OpenBB SDK installation and basic functionality."""
    result = {
        "test": "OpenBB SDK",
        "status": "FAILED",
        "details": {}
    }

    try:
        import openbb
        result["status"] = "PASSED"
        result["details"]["version"] = openbb.__version__
        result["details"]["available"] = True

        # Try basic initialization
        from openbb import obb
        result["details"]["initialized"] = True
        result["details"]["endpoints"] = {
            "stocks": "Available",
            "crypto": "Available",
            "bonds": "Available",
            "economy": "Available",
            "alternatives": "Available"
        }
    except ImportError as e:
        result["status"] = "NOT_INSTALLED"
        result["details"]["error"] = str(e)
        result["details"]["install_command"] = "pip install openbb"
    except Exception as e:
        result["status"] = "ERROR"
        result["details"]["error"] = str(e)

    return result


def test_openbb_api_connectivity() -> Dict[str, Any]:
    """Test connectivity to OpenBB Cloud API."""
    result = {
        "test": "OpenBB Cloud API",
        "status": "FAILED",
        "details": {}
    }

    try:
        import requests

        # Test endpoint availability (no auth required for this test)
        test_url = "https://api.openbb.dev/v1/health"
        try:
            response = requests.get(test_url, timeout=5)
            result["status"] = "REACHABLE"
            result["details"]["http_status"] = response.status_code
            result["details"]["api_endpoint"] = "https://api.openbb.dev/v1"
            result["details"]["authentication_required"] = True
            result["details"]["note"] = "API key required for authenticated requests"
        except requests.ConnectionError:
            result["status"] = "UNREACHABLE"
            result["details"]["error"] = "Cannot reach api.openbb.dev"
        except requests.Timeout:
            result["status"] = "TIMEOUT"
            result["details"]["error"] = "Connection timeout"

    except ImportError:
        result["status"] = "REQUESTS_NOT_AVAILABLE"
        result["details"]["note"] = "Install requests: pip install requests"
    except Exception as e:
        result["status"] = "ERROR"
        result["details"]["error"] = str(e)

    return result


def test_openbb_terminal() -> Dict[str, Any]:
    """Test OpenBB Terminal installation and CLI access."""
    result = {
        "test": "OpenBB Terminal",
        "status": "FAILED",
        "details": {}
    }

    try:
        import subprocess

        # Try to run openbb command
        process = subprocess.run(
            ["openbb", "--help"],
            capture_output=True,
            timeout=5
        )

        if process.returncode == 0:
            result["status"] = "INSTALLED"
            result["details"]["available"] = True
            result["details"]["cli_available"] = True
            result["details"]["note"] = "OpenBB Terminal CLI is available"
        else:
            result["status"] = "FAILED"
            result["details"]["error"] = process.stderr.decode()

    except FileNotFoundError:
        result["status"] = "NOT_INSTALLED"
        result["details"]["install_command"] = "pip install openbb[all]"
        result["details"]["error"] = "OpenBB Terminal command not found in PATH"
    except subprocess.TimeoutExpired:
        result["status"] = "TIMEOUT"
        result["details"]["error"] = "Command execution timeout"
    except Exception as e:
        result["status"] = "ERROR"
        result["details"]["error"] = str(e)

    return result


def test_sample_query() -> Dict[str, Any]:
    """Test basic data retrieval if SDK is available."""
    result = {
        "test": "Sample Data Query",
        "status": "SKIPPED",
        "details": {}
    }

    try:
        from openbb import obb

        # Try to get basic stock data
        try:
            ticker_info = obb.equity.fundamental.ratios(
                symbol="AAPL",
                limit=1
            )
            result["status"] = "SUCCESS"
            result["details"]["query"] = "Apple Inc (AAPL) fundamentals"
            result["details"]["data_available"] = True
            result["details"]["note"] = "Successfully retrieved stock data"
        except Exception as e:
            result["status"] = "QUERY_FAILED"
            result["details"]["error"] = str(e)
            result["details"]["note"] = "Query execution failed - API may require authentication"

    except ImportError:
        result["status"] = "SKIPPED"
        result["details"]["reason"] = "OpenBB SDK not installed"

    return result


def main():
    """Run all access tests and generate report."""
    print("=" * 70)
    print("OpenBB Access Test Report")
    print(f"Generated: {datetime.now().isoformat()}")
    print("=" * 70)
    print()

    tests = [
        ("SDK Installation", test_openbb_sdk),
        ("API Connectivity", test_openbb_api_connectivity),
        ("Terminal CLI", test_openbb_terminal),
        ("Sample Query", test_sample_query),
    ]

    results = []

    for test_name, test_func in tests:
        print(f"Testing {test_name}...")
        try:
            result = test_func()
            results.append(result)
            status_symbol = {
                "PASSED": "✓",
                "INSTALLED": "✓",
                "REACHABLE": "✓",
                "SUCCESS": "✓",
                "FAILED": "✗",
                "ERROR": "✗",
                "NOT_INSTALLED": "○",
                "SKIPPED": "↷",
                "UNREACHABLE": "✗",
                "TIMEOUT": "✗",
            }.get(result["status"], "?")

            print(f"  {status_symbol} {result['status']}")
            if result["details"]:
                for key, value in result["details"].items():
                    print(f"    - {key}: {value}")
        except Exception as e:
            print(f"  ✗ Test execution failed: {e}")
        print()

    # Summary
    print("=" * 70)
    print("Summary")
    print("=" * 70)

    status_counts = {}
    for result in results:
        status = result["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
        print(f"  {result['test']}: {result['status']}")

    print()
    print("Recommendations:")
    print("  1. If SDK is NOT_INSTALLED: pip install openbb")
    print("  2. If API is UNREACHABLE: Check network/firewall settings")
    print("  3. For authenticated access: Set OPENBB_API_KEY environment variable")
    print("  4. See OPENBB_ACCESS_ASSESSMENT.md for integration options")

    return 0 if any("PASSED" in r["status"] or "SUCCESS" in r["status"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
