from __future__ import annotations

from enum import Enum


class Color4Bits(Enum):
    BLACK = (30, 40)
    DARK_RED = (31, 41)
    GREEN = (32, 42)
    DARK_YELLOW = (33, 43)
    DARK_BLUE = (34, 44)
    PURPLE = (35, 45)
    TURQUOISE = (36, 46)
    SILVER = (37, 47)
    GRAY = (90, 100)
    RED = (91, 101)
    LIME = (92, 102)
    YELLOW = (93, 103)
    BLUE = (94, 104)
    PINK = (95, 105)
    CYAN = (96, 106)
    WHITE = (97, 107)


class ConsoleCharacters:
    @staticmethod
    def reset() -> str:
        return "\u001b[0m"

    @staticmethod
    def set_bold() -> str:
        return "\u001b[1m"

    @staticmethod
    def set_thin() -> str:
        return "\u001b[2m"

    @staticmethod
    def set_italic() -> str:
        return "\u001b[3m"

    @staticmethod
    def set_underline() -> str:
        return "\u001b[4m"

    @staticmethod
    def set_slow_blink() -> str:
        return "\u001b[5m"

    @staticmethod
    def set_fast_blink() -> str:
        return "\u001b[6m"

    @staticmethod
    def swap_colors() -> str:
        return "\u001b[7m"

    @staticmethod
    def set_conceal() -> str:
        return "\u001b[8m"

    @staticmethod
    def set_strike_out() -> str:
        return "\u001b[9m"

    @staticmethod
    def set_font(n: int = 0) -> str:
        """
        :param n: An integer between 0 and 9. 0 is the default font.
        """
        if 0 > n > 9:
            raise ValueError(f"n must be between 0 and 9. Actual: {n}")
        else:
            return f"\u001b[{n + 10}m"

    @staticmethod
    def set_fraktur() -> str:
        return "\u001b[20m"

    @staticmethod
    def reset_bold() -> str:
        return "\u001b[21m"

    @staticmethod
    def set_double_underline() -> str:
        return "\u001b[21m"

    @staticmethod
    def reset_font_weight() -> str:
        return "\u001b[22m"

    @staticmethod
    def reset_italic() -> str:
        return "\u001b[23m"

    @staticmethod
    def reset_fraktur() -> str:
        return "\u001b[23m"

    @staticmethod
    def reset_underline() -> str:
        return "\u001b[24m"

    @staticmethod
    def reset_blink() -> str:
        return "\u001b[25m"

    @staticmethod
    def reset_swap_colors() -> str:
        return "\u001b[27m"

    @staticmethod
    def reset_conceal() -> str:
        return "\u001b[28m"

    @staticmethod
    def reset_strike_out() -> str:
        return "\u001b[29m"

    @staticmethod
    def set_foreground_4bits(code: Color4Bits | int | str) -> str:
        if isinstance(code, Color4Bits):
            code: str = str(code.value[0])

        return f"\u001b[{code}m"

    @staticmethod
    def set_foreground_8bits(value: int) -> str:
        if 0 > value > 255:
            raise ValueError(f"Value must be between 0 and 255, not {value}")
        else:
            return f"\u001b[38;5{value}m"

    @staticmethod
    def set_foreground_32bits(r: int, g: int, b: int) -> str:
        ConsoleCharacters._validate_rgb(r, g, b)
        return f"\u001b[38;2;{r};{g};{b}m"

    @staticmethod
    def reset_foreground() -> str:
        return "\u001b[39m"

    @staticmethod
    def set_background_4bits(code: Color4Bits | int | str) -> str:
        if isinstance(code, Color4Bits):
            code: str = str(code.value[1])

        return f"\u001b[{code}m"

    @staticmethod
    def set_background_8bits(value: int) -> str:
        if 0 > value > 255:
            raise ValueError(f"Value must be between 0 and 255, not {value}")
        else:
            return f"\u001b[48;5{value}"

    @staticmethod
    def set_background_32bits(r: int, g: int, b: int) -> str:
        ConsoleCharacters._validate_rgb(r, g, b)
        return f"\u001b[48;2;{r};{g};{b}m"

    @staticmethod
    def reset_background() -> str:
        return "\u001b[49m"

    @staticmethod
    def set_framed() -> str:
        return "\u001b[51m"

    @staticmethod
    def set_encircled() -> str:
        return "\u001b[52m"

    @staticmethod
    def set_overlined() -> str:
        return "\u001b[53m"

    @staticmethod
    def reset_framed_encircled() -> str:
        return "\u001b[54m"

    @staticmethod
    def reset_overlined() -> str:
        return "\u001b[55m"

    @staticmethod
    def set_ideogram_underlined() -> str:
        return "\u001b[60m"

    @staticmethod
    def set_ideogram_double_underlined() -> str:
        return "\u001b[61m"

    @staticmethod
    def set_ideogram_overlined() -> str:
        return "\u001b[62m"

    @staticmethod
    def set_ideogram_double_overlined() -> str:
        return "\u001b[63m"

    @staticmethod
    def set_ideogram_stress_marking() -> str:
        return "\u001b[64m"

    @staticmethod
    def reset_ideogram() -> str:
        return "\u001b[65m"

    @staticmethod
    def clear_from_cursor_to_end_of_line() -> str:
        return "\u001b[K"

    @staticmethod
    def clear_from_line_start_to_cursor() -> str:
        return "\u001b[1K"

    @staticmethod
    def clear_line() -> str:
        return "\u001b[2K"

    @staticmethod
    def clear_below() -> str:
        return "\u001b[J"

    @staticmethod
    def clear_above() -> str:
        return "\u001b[1J"

    @staticmethod
    def clear_all() -> str:
        return "\u001b[2J"

    @staticmethod
    def clear_saved_lines() -> str:
        return "\u001b[3J"

    @staticmethod
    def move_cursor_at_absolute(x: int, y: int) -> str:
        return f"\u001b[{x};{y}H"

    @staticmethod
    def move_cursor_at_column_relative(columns: int = 1) -> str:
        if columns < 0:
            return f"\u001b[{abs(columns)}C"
        elif columns > 0:
            return f"\u001b[{columns}D"
        return ""

    @staticmethod
    def move_cursor_at_row_relative(rows: int = 1) -> str:
        if rows < 0:
            return f"\u001b[{abs(rows)}A"
        elif rows > 0:
            return f"\u001b[{rows}B"
        return ""

    @staticmethod
    def scroll_up(n: int = 1) -> str:
        return f"\u001b[{n}S"

    @staticmethod
    def scroll_down(n: int = 1) -> str:
        return f"\u001b[{n}T"

    @staticmethod
    def move_cursor_at_00() -> str:
        return "\u001b[H"

    @staticmethod
    def save_cursor_position() -> str:
        return "\u001b[7"

    @staticmethod
    def restore_cursor_position() -> str:
        return "\u001b[8"

    @staticmethod
    def move_cursor_back_one_space() -> str:
        return "\b"

    @staticmethod
    def make_cursor_invisible() -> str:
        return "\u001b[?25l"

    @staticmethod
    def make_cursor_visible() -> str:
        return "\u001b[?25h"

    @staticmethod
    def save_screen() -> str:
        return "\u001b[?47h"

    @staticmethod
    def restore_screen() -> str:
        return "\u001b[?47l"

    @staticmethod
    def print_screen() -> str:
        return "\u001b[?0i"

    @staticmethod
    def dump_screen_to_html() -> str:
        return "\u001b[?10i"

    @staticmethod
    def dump_screen_to_svg() -> str:
        return "\u001b[?11i"

    @staticmethod
    def bell() -> str:
        return "\a"

    @staticmethod
    def set_autowrap() -> str:
        return "\u001b[?7h"

    @staticmethod
    def unset_autowrap() -> str:
        return "\u001b[?7l"

    @staticmethod
    def set_cursor_blink() -> str:
        return "\u001b[?14h"

    @staticmethod
    def unset_cursor_blink() -> str:
        return "\u001b[?14l"

    @staticmethod
    def set_tektronix() -> str:
        return "\u001b[?38h"

    @staticmethod
    def unset_tektronix() -> str:
        return "\u001b[?38l"

    @staticmethod
    def set_slow_scroll() -> str:
        return "\u001b[?4h"

    @staticmethod
    def unset_slow_scroll() -> str:
        return "\u001b[?4l"

    @staticmethod
    def set_margin_bell() -> str:
        return "\u001b[?44h"

    @staticmethod
    def unset_margin_bell() -> str:
        return "\u001b[?44l"

    @staticmethod
    def insert_n_lines(n: int = 1) -> str:
        return f"\u001b[{n}L"

    @staticmethod
    def insert_n_blank_chars(n: int = 1) -> str:
        return f"\u001b[{n}@"

    @staticmethod
    def delete_n_lines(n: int = 1) -> str:
        return f"\u001b[{n}M"

    @staticmethod
    def delete_n_chars(n: int = 1, forward: bool = True) -> str:
        if forward:
            return f"\u001b[{n}P"
        else:
            return f"\u001b[{n}X"

    @staticmethod
    def never_hide_mouse() -> str:
        return "\u001b[0p"

    @staticmethod
    def hide_mouse_if_tracking_mode_enabled() -> str:
        return "\u001b[1p"

    @staticmethod
    def hide_mouse_except_leaving_window() -> str:
        return "\u001b[2p"

    @staticmethod
    def hide_mouse() -> str:
        return "\u001b[3p"

    @staticmethod
    def set_scrolling_region(top: int, bottom: int) -> str:
        return f"\u001b[{top};{bottom}r"

    @staticmethod
    def reset_scrolling_region() -> str:
        return "\u001b[r"

    @staticmethod
    def fill_rectangle(with_char: str, top: int, left: int, bottom: int, right: int) -> str:
        return f"\u001b[{with_char};{top};{left};{bottom};{right}$x"

    @staticmethod
    def erase_rectangle_area(top: int, left: int, bottom: int, right: int) -> str:
        return f"\u001b[{top};{left};{bottom};{right}$z"

    @staticmethod
    def _validate_rgb(r: int, g: int, b: int):
        if 0 > r > 255:
            raise ValueError(f'"r" must be between 0 and 255, not {r}')
        if 0 > g > 255:
            raise ValueError(f'"g" must be between 0 and 255, not {g}')
        if 0 > b > 255:
            raise ValueError(f'"b" must be between 0 and 255, not {b}')


