from telemetry_buffer import TelemetryBuffer


class TestToBuffer:

    def test_unsigned_short(self):
        expected = [0x2, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]
        assert TelemetryBuffer.to_buffer(5) == expected
