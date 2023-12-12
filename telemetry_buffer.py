from bit_converter import BitConverter


class TelemetryBuffer:

    @classmethod
    def to_buffer(cls, reading):
        buffer = [0x2]
        buffer += BitConverter.int16_to_bytes(reading)
        buffer += [0x0] * 6
        return buffer
