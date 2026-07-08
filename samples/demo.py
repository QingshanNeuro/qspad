# demo.py — a quick look at QSpad in action
# Every token here is the same flat color on purpose: no rainbow syntax,
# no italics, no bracket confetti. Just calm, readable code.

from dataclasses import dataclass


@dataclass
class Reading:
    label: str
    value: float
    unit: str = "mV"

    def __repr__(self) -> str:
        return f"{self.label}: {self.value:.2f} {self.unit}"


class SignalBuffer:
    """Rolling buffer that flags readings above a threshold."""

    def __init__(self, capacity: int = 128, threshold: float = 2.5):
        self.capacity = capacity
        self.threshold = threshold
        self.readings: list[Reading] = []

    def add(self, reading: Reading) -> None:
        if len(self.readings) >= self.capacity:
            self.readings.pop(0)
        self.readings.append(reading)

    def flagged(self) -> list[Reading]:
        return [r for r in self.readings if r.value > self.threshold]


def summarize(buffer: SignalBuffer) -> str:
    total = len(buffer.readings)
    hits = len(buffer.flagged())
    rate = (hits / total * 100) if total else 0.0
    return f"{hits}/{total} readings above threshold ({rate:.1f}%)"


if __name__ == "__main__":
    buffer = SignalBuffer(capacity=64, threshold=3.0)
    for i, value in enumerate([1.2, 3.8, 2.9, 4.1, 0.5, 3.3]):
        buffer.add(Reading(label=f"ch{i}", value=value))

    for reading in buffer.flagged():
        print(reading)

    print(summarize(buffer))
