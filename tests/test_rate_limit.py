import unittest
from src.rate_limiter import SlidingWindowLimiter
from src.simulator import SimulatedRequest, handle_request


class RateLimiterTests(unittest.TestCase):
    def test_limit_returns_429_after_quota(self):
        limiter = SlidingWindowLimiter(limit=2, window_seconds=60)
        self.assertEqual(limiter.check("client", now=1).status_code, 200)
        self.assertEqual(limiter.check("client", now=2).status_code, 200)
        self.assertEqual(limiter.check("client", now=3).status_code, 429)

    def test_window_expires_old_events(self):
        limiter = SlidingWindowLimiter(limit=1, window_seconds=10)
        self.assertEqual(limiter.check("client", now=1).status_code, 200)
        self.assertEqual(limiter.check("client", now=12).status_code, 200)

    def test_untrusted_header_does_not_change_server_identity(self):
        limiter = SlidingWindowLimiter(limit=1, window_seconds=60)
        first = SimulatedRequest("client-A", {"X-Forwarded-For": "198.51.100.1"})
        second = SimulatedRequest("client-A", {"X-Forwarded-For": "203.0.113.9"})
        self.assertEqual(handle_request(first, limiter, trust_forwarded_header=False, now=1), 200)
        self.assertEqual(handle_request(second, limiter, trust_forwarded_header=False, now=2), 429)

    def test_header_trust_demo_uses_distinct_supplied_values(self):
        limiter = SlidingWindowLimiter(limit=1, window_seconds=60)
        first = SimulatedRequest("client-A", {"X-Forwarded-For": "198.51.100.1"})
        second = SimulatedRequest("client-A", {"X-Forwarded-For": "203.0.113.9"})
        self.assertEqual(handle_request(first, limiter, trust_forwarded_header=True, now=1), 200)
        self.assertEqual(handle_request(second, limiter, trust_forwarded_header=True, now=2), 200)


if __name__ == "__main__":
    unittest.main()
