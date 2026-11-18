"""In-memory rate limiter for local security demonstrations."""
from collections import defaultdict, deque
from dataclasses import dataclass
from time import monotonic


@dataclass(frozen=True)
class Decision:
    allowed: bool
    status_code: int
    remaining: int


class SlidingWindowLimiter:
    def __init__(self, limit: int, window_seconds: float):
        if limit < 1 or window_seconds <= 0:
            raise ValueError("limit and window_seconds must be positive")
        self.limit = limit
        self.window_seconds = window_seconds
        self._events = defaultdict(deque)

    def check(self, identity: str, now: float | None = None) -> Decision:
        """Check a request against a sliding window using a server-chosen identity."""
        current = monotonic() if now is None else now
        events = self._events[identity]

        while events and current - events[0] >= self.window_seconds:
            events.popleft()

        if len(events) >= self.limit:
            return Decision(False, 429, 0)

        events.append(current)
        return Decision(True, 200, self.limit - len(events))
