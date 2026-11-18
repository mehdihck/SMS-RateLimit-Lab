"""Local-only simulator. It does not make network requests."""
from dataclasses import dataclass
from .rate_limiter import SlidingWindowLimiter


@dataclass
class SimulatedRequest:
    server_client_id: str
    headers: dict[str, str]


def handle_request(
    request: SimulatedRequest,
    limiter: SlidingWindowLimiter,
    *,
    trust_forwarded_header: bool,
    now: float,
) -> int:
    """Return a simulated HTTP status code; no HTTP server or network is involved."""
    if trust_forwarded_header:
        identity = request.headers.get("X-Forwarded-For", request.server_client_id)
    else:
        identity = request.server_client_id

    return limiter.check(identity, now=now).status_code


def run_demo() -> None:
    print("SMS Rate Limit Lab — local simulation only\n")

    print("[1] Demonstration: trusting an unverified forwarding header")
    weak_limiter = SlidingWindowLimiter(limit=2, window_seconds=60)
    for index, header_value in enumerate(("198.51.100.10", "198.51.100.10", "203.0.113.20"), start=1):
        request = SimulatedRequest(
            server_client_id="client-A",
            headers={"X-Forwarded-For": header_value},
        )
        status = handle_request(
            request, weak_limiter, trust_forwarded_header=True, now=float(index)
        )
        print(f"  simulated request {index}: HTTP {status}")

    print("\n[2] Demonstration: using server-controlled identity")
    strong_limiter = SlidingWindowLimiter(limit=2, window_seconds=60)
    for index, header_value in enumerate(("198.51.100.10", "198.51.100.10", "203.0.113.20"), start=1):
        request = SimulatedRequest(
            server_client_id="client-A",
            headers={"X-Forwarded-For": header_value},
        )
        status = handle_request(
            request, strong_limiter, trust_forwarded_header=False, now=float(index)
        )
        print(f"  simulated request {index}: HTTP {status}")

    print("\nFinished. No SMS was sent and no network connection was made.")


if __name__ == "__main__":
    run_demo()
