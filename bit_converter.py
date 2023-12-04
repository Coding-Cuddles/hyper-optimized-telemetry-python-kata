class BitConverter:

    @staticmethod
    def get_bytes(value):
        """Convert an integer to a list of integers representing bytes."""
        return list(value.to_bytes((value.bit_length() + 7) // 8, "little"))

    @staticmethod
    def to_integer(byte_list):
        """Convert a list of integers representing bytes to an integer."""
        return int.from_bytes(bytes(byte_list), "little")
