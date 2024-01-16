# Hyper-optimized telemetry kata in Python

[![CI](https://github.com/Coding-Cuddles/hyper-optimized-telemetry-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/hyper-optimized-telemetry-python-kata/actions/workflows/main.yml)
[![Replit](https://img.shields.io/badge/Try%20with%20Replit-black?logo=replit)](https://replit.com/new/github/Coding-Cuddles/hyper-optimized-telemetry-python-kata)

## Overview

This kata complements [Clean Code: Advanced TDD, Ep. 20](https://cleancoders.com/episode/clean-code-episode-20)
and [Clean Code: Advanced TDD, Ep. 21](https://cleancoders.com/episode/clean-code-episode-21).

This repository contains two exercises designed to improve your skills in
test-driven development.

## Instructions

We will work on a telemetry system for a remote control car project. Bandwidth
in the telemetry system is at a premium and you have been asked to implement a
message protocol for communicating telemetry data.

Data is transmitted in a buffer (byte array). When integers are sent, the size
of the buffer is reduced by employing the protocol described below.

Each value should be represented in the smallest possible C integral type
(types of `char` and `unsigned char` are not included as the saving would be
trivial):

| From                       | To                        | Type             |
|:---------------------------|:------------------------- |:-----------------|
| 4_294_967_296              | 9_223_372_036_854_775_807 | `long`           |
| 2_147_483_648              | 4_294_967_295             | `unsigned int`   |
| 65_536                     | 2_147_483_647             | `int`            |
| 0                          | 65_535                    | `unsigned short` |
| -32_768                    | -1                        | `short`          |
| -2_147_483_648             | -32_769                   | `int`            |
| -9_223_372_036_854_775_808 | -2_147_483_649            | `long`           |

The value should be converted to the appropriate number of bytes for its
assigned type. The complete internal 9-byte buffer comprises three parts:
* _prefix byte_: a byte indicating the number of the payload bytes in the
  buffer;
* _payload bytes_: the bytes holding the integer;
* _trailing bytes_: the zero-fill bytes to complete the buffer.

To distinguish between signed and unsigned types, the protocol introduces a
little trick: for signed types, their _prefix byte_ value is `256` minus the
number of _payload bytes_ in the buffer.

### Exercise 1

Implement the static method `TelemetryBuffer.to_buffer()` to encode a buffer
taking an integer value passed to the method.

```python
# Type: unsigned short, bytes: 2, signed: no, prefix byte: 2
TelemetryBuffer.to_buffer(5)
# => [0x2, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0]

# Type: int, bytes: 4, signed: yes, prefix byte: 256 - 4
TelemetryBuffer.to_buffer(2_147_483_647)
# => [0xfc, 0xff, 0xff, 0xff, 0x7f, 0x0, 0x0, 0x0, 0x0]
```

> **Hint**
>
> The `BitConverter` class provides a convenient way of converting integer
> types to and from arrays of bytes.

### Exercise 2

Implement the static method `TelemetryBuffer.from_buffer()` to decode the
buffer received, and return the value in the form of an integer.

```python
TelemetryBuffer.from_buffer([0xfc, 0xff, 0xff, 0xff, 0x7f, 0x0, 0x0, 0x0, 0x0])
# => 2_147_483_647
```

If the prefix byte is of unexpected value, then return `0`.

## Integral numbers in C

> **Note**
>
> For type sizes, we assume a typical 64-bit system.

The C language provides a number of types that represent integers, each with
its own range of values. The ranges are determined by the storage width of the
type as allocated by the system:

| Type             | Width  | Minimum                    | Maximum                     |
|:-----------------|:-------|:---------------------------|:--------------------------- |
| `char`           | 8 bit  | -128                       | +127                        |
| `short`          | 16 bit | -32_768                    | +32_767                     |
| `int`            | 32 bit | -2_147_483_648             | +2_147_483_647              |
| `long`           | 64 bit | -9_223_372_036_854_775_808 | +9_223_372_036_854_775_807  |
| `unsigned char`  | 8 bit  | 0                          | +255                        |
| `unsigned short` | 16 bit | 0                          | +65_535                     |
| `unsigned int`   | 32 bit | 0                          | +4_294_967_295              |
| `unsigned long`  | 64 bit | 0                          | +18_446_744_073_709_551_615 |

## Usage

You can import this project into [Replit](https://replit.com), and it will
handle all dependencies automatically.

### Prerequisites

* [Python 3.8+](https://www.python.org/)
* [pytest](https://pytest.org)

### Run main

```console
make run
```

### Run tests

```console
make test
```

## Credits and references

* <https://exercism.org/tracks/csharp/exercises/hyper-optimized-telemetry>
