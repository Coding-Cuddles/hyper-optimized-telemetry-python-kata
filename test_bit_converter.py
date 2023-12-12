import pytest

from bit_converter import BitConverter


class TestBitConverter:

    @pytest.mark.parametrize("test_input,expected", [
        (0, [0x00, 0x00]),
        (15, [0x0F, 0x00]),
        (-15, [0xF1, 0xFF]),
        (10000, [0x10, 0x27]),
        (-10000, [0xF0, 0xD8]),
        (-32768, [0x00, 0x80]),
        (32767, [0xFF, 0x7F]),
    ])
    def test_int16_to_bytes(self, test_input, expected):
        assert BitConverter().int16_to_bytes(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (0, [0x00, 0x00]),
        (15, [0x0F, 0x00]),
        (1023, [0xFF, 0x03]),
        (10000, [0x10, 0x27]),
        (32767, [0xFF, 0x7F]),
        (65535, [0xFF, 0xFF]),
    ])
    def test_uint16_to_bytes(self, test_input, expected):
        assert BitConverter().uint16_to_bytes(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (0, [0x00, 0x00, 0x00, 0x00]),
        (15, [0x0F, 0x00, 0x00, 0x00]),
        (-15, [0xF1, 0xFF, 0xFF, 0xFF]),
        (1048576, [0x00, 0x00, 0x10, 0x00]),
        (-1048576, [0x00, 0x00, 0xF0, 0xFF]),
        (1000000000, [0x00, 0xCA, 0x9A, 0x3B]),
        (-1000000000, [0x00, 0x36, 0x65, 0xC4]),
        (-2147483648, [0x00, 0x00, 0x00, 0x80]),
        (2147483647, [0xFF, 0xFF, 0xFF, 0x7F]),
    ])
    def test_int32_to_bytes(self, test_input, expected):
        assert BitConverter().int32_to_bytes(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (0, [0x00, 0x00, 0x00, 0x00]),
        (15, [0x0F, 0x00, 0x00, 0x00]),
        (1023, [0xFF, 0x03, 0x00, 0x00]),
        (1048576, [0x00, 0x00, 0x10, 0x00]),
        (1000000000, [0x00, 0xCA, 0x9A, 0x3B]),
        (2147483647, [0xFF, 0xFF, 0xFF, 0x7F]),
        (4294967295, [0xFF, 0xFF, 0xFF, 0xFF]),
    ])
    def test_uint32_to_bytes(self, test_input, expected):
        assert BitConverter().uint32_to_bytes(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (0, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
        (16777215, [0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00]),
        (-16777215, [0x01, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]),
        (1000000000, [0x00, 0xCA, 0x9A, 0x3B, 0x00, 0x00, 0x00, 0x00]),
        (-1000000000, [0x00, 0x36, 0x65, 0xC4, 0xFF, 0xFF, 0xFF, 0xFF]),
        (4294967296, [0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00]),
        (-4294967296, [0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF]),
        (187649984473770, [0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0x00, 0x00]),
        (-187649984473770, [0x56, 0x55, 0x55, 0x55, 0x55, 0x55, 0xFF, 0xFF]),
        (1000000000000000000, [0x00, 0x00, 0x64, 0xA7, 0xB3, 0xB6, 0xE0, 0x0D]),
        (-1000000000000000000, [0x00, 0x00, 0x9C, 0x58, 0x4C, 0x49, 0x1F, 0xF2]),
        (-9223372036854775808, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80]),
        (9223372036854775807, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F]),
    ])
    def test_int64_to_bytes(self, test_input, expected):
        assert BitConverter().int64_to_bytes(test_input) == expected

    @pytest.mark.parametrize("test_input,expected", [
        (0, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
        (16777215, [0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00]),
        (1000000000, [0x00, 0xCA, 0x9A, 0x3B, 0x00, 0x00, 0x00, 0x00]),
        (4294967296, [0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00]),
        (187649984473770, [0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0x00, 0x00]),
        (1000000000000000000, [0x00, 0x00, 0x64, 0xA7, 0xB3, 0xB6, 0xE0, 0x0D]),
        (10000000000000000000, [0x00, 0x00, 0xE8, 0x89, 0x04, 0x23, 0xC7, 0x8A]),
        (9223372036854775807, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F]),
        (18446744073709551615, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]),
    ])
    def test_uint64_to_bytes(self, test_input, expected):
        assert BitConverter().uint64_to_bytes(test_input) == expected

    @pytest.mark.parametrize("byte_list,expected", [
        ([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00], 0),
        ([0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00], 16777215),
        ([0x01, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], -16777215),
        ([0x00, 0xCA, 0x9A, 0x3B, 0x00, 0x00, 0x00, 0x00], 1000000000),
        ([0x00, 0x36, 0x65, 0xC4, 0xFF, 0xFF, 0xFF, 0xFF], -1000000000),
        ([0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00], 4294967296),
        ([0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF], -4294967296),
        ([0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0x00, 0x00], 187649984473770),
        ([0x56, 0x55, 0x55, 0x55, 0x55, 0x55, 0xFF, 0xFF], -187649984473770),
        ([0x00, 0x00, 0x64, 0xA7, 0xB3, 0xB6, 0xE0, 0x0D], 1000000000000000000),
        ([0x00, 0x00, 0x9C, 0x58, 0x4C, 0x49, 0x1F, 0xF2], -1000000000000000000),
        ([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F], 9223372036854775807),
        ([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80], -9223372036854775808),
    ])
    def test_to_integer(self, byte_list, expected):
        assert BitConverter().bytes_to_int64(byte_list) == expected
