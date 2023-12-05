from bit_converter import BitConverter


class TelemetryBuffer:

    @classmethod
    def to_buffer(cls, reading):
        return [0x2] + BitConverter.get_bytes(reading) + [0x0] * 7
