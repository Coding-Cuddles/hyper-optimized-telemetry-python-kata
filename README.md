# Hyper-optimized telemetry kata in Python

[![CI](https://github.com/Coding-Cuddles/hyper-optimized-telemetry-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/hyper-optimized-telemetry-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

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

Setup is complete when the existing test suite passes.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/hyper-optimized-telemetry-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd hyper-optimized-telemetry-python-kata
   ```

3. Run the existing tests. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `65 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

Implement `TelemetryBuffer.to_buffer()` and `TelemetryBuffer.from_buffer()` in
`telemetry_buffer.py`. `bit_converter.py` contains the integer conversion helpers.

Run the tests after each change. Use Make when it is installed:

```console
make test
```

Otherwise, run pytest through `uv` directly:

```console
uv run pytest
```

Continue when the test run passes.

## Run the sample entry point

Use Make when it is installed:

```console
make run
```

Otherwise, run `main.py` through `uv` directly:

```console
uv run python main.py
```

The command prints `Hello World!`.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the command reference              |
| `make run`          | Run the sample entry point              |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |

## Credits and references

* <https://exercism.org/tracks/csharp/exercises/hyper-optimized-telemetry>
