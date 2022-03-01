# Major Changes

- 20211105: Release CircuitPython 7.0 version
- 20211207: Add ATSAMD51P19A module
- 20220105: Adapt to CircuitPython 7.1
  - The size of the firmware becomes smaler; native is enabled.
  - [Concatenaton of f-string (like `f"abc" f"def"`) causes error.](https://docs.micropython.org/en/latest/genrst/core_language.html)
  - Adjustment is required for UART communication with RTL.
- 20220301: Adapt to CircuitPython 7.2
  - TileGrid has now width/height attributes.  Its subclass cannot have the attributes of the same name.
