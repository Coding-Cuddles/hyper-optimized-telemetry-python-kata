def _int_to_bytes_helper(value, length, *, signed=False):
    return list(value.to_bytes(length, byteorder="little", signed=signed))


class BitConverter:

    @staticmethod
    def int16_to_bytes(value):
        """Convert the specified 16-bit signed integer value to bytes."""
        return _int_to_bytes_helper(value, 2, signed=True)

    @staticmethod
    def uint16_to_bytes(value):
        """Convert the specified 16-bit unsigned integer value to bytes."""
        return _int_to_bytes_helper(value, 2)

    @staticmethod
    def int32_to_bytes(value):
        """Convert the specified 32-bit signed integer value to bytes."""
        return _int_to_bytes_helper(value, 4, signed=True)

    @staticmethod
    def uint32_to_bytes(value):
        """Convert the specified 32-bit unsigned integer value to bytes."""
        return _int_to_bytes_helper(value, 4)

    @staticmethod
    def int64_to_bytes(value):
        """Convert the specified 64-bit signed integer value to bytes."""
        return _int_to_bytes_helper(value, 8, signed=True)

    @staticmethod
    def uint64_to_bytes(value):
        """Convert the specified 64-bit unsigned integer value to bytes."""
        return _int_to_bytes_helper(value, 8)

    @staticmethod
    def bytes_to_int64(byte_list):
        """Convert a list of bytes to a 64-bit signed integer."""
        return int.from_bytes(bytes(byte_list), "little", signed=True)
