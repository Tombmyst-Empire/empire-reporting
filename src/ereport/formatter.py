from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Any, Final

from econsole.styles import Color4Bits, ConsoleCharacters
from edata.sun import SunData, Sun
from empire_commons.types_ import JsonType
from frozendict import frozendict

from ereport.level import Level, Levels
from ereport.report import Report


class BaseFormatter(ABC):
    """
    Base formatter class
    """
    @abstractmethod
    def format(self, report: Report) -> Any:
        """
        Produces a formatted result (usually a string or a dict) of the provided report
        :param report:
        :return:
        """
        raise NotImplementedError()


class DefaultFormatter(BaseFormatter):
    """
    Default formatter
    """

    def format(self, report: Report) -> str:
        effective_module: str = report.module[:30]
        effective_function: str = report.function[:30]

        return f'[{report.date_time}] ' \
               f'[{str(report.level):^7}] ' \
               f'[{report.reporter_name.upper():^8}] ' \
               f'[({report.line:0>4}) {effective_module:<30}::{effective_function:<30}] ' \
               f'{report.message}'


class ColoredFormatter(BaseFormatter):
    """
    A colored formatter.

    Each level has its own color.
    """
    COLORS: Final[frozendict[Level, Color4Bits]] = frozendict({
        Levels.TRACE: Color4Bits.GRAY,
        Levels.DEBUG: Color4Bits.BLACK,
        Levels.SUCCESS: Color4Bits.GREEN,
        Levels.INFO: Color4Bits.TURQUOISE,
        Levels.WARN: Color4Bits.DARK_YELLOW,
        Levels.ERROR: Color4Bits.DARK_RED,
        Levels.SEVERE: Color4Bits.DARK_BLUE,
        Levels.FATAL: Color4Bits.PURPLE
    })

    def format(self, report: Report) -> str:
        return ColoredFormatter.get_report_string(report, ColoredFormatter.COLORS)

    @staticmethod
    def get_report_string(report: Report, colors: frozendict[Level, Color4Bits]) -> str:
        color = ConsoleCharacters.set_foreground_4bits(colors[report.level])
        effective_module: str = report.module[:30]
        effective_function: str = report.function[:30]

        return f'{color}' \
               f'[{report.date_time}] ' \
               f'[{str(report.level):^8}] ' \
               f'[{report.reporter_name.upper():^8}] ' \
               f'[({report.line:0>4}) {effective_module:<30}::{effective_function:<30}] ' \
               f'{ConsoleCharacters.set_bold()}' \
               f'{report.message}' \
               f'{ConsoleCharacters.reset()}'


class AdaptativeColoredFormatter(BaseFormatter):
    """
    This is an augmented version of :class:`ColoredFormatter`.

    The colors will change upon sunset and sunrise for better visibility.

    .. note :: **empire-reporting** is not responsible for changing the console's background.

    .. warning :: Do not use this formatter if you need a fast logger. Use instead :class:`DefaultFormatter`.
    """
    NIGHT_COLORS: Final[frozendict[Level, Color4Bits]] = frozendict({
        Levels.TRACE: Color4Bits.SILVER,
        Levels.DEBUG: Color4Bits.WHITE,
        Levels.SUCCESS: Color4Bits.LIME,
        Levels.INFO: Color4Bits.CYAN,
        Levels.WARN: Color4Bits.YELLOW,
        Levels.ERROR: Color4Bits.RED,
        Levels.SEVERE: Color4Bits.BLUE,
        Levels.FATAL: Color4Bits.PINK
    })

    _SUNRISE_DATETIME: int | None = None
    _SUNSET_DATETIME: int | None = None

    def __init__(self):
        if not AdaptativeColoredFormatter._SUNRISE_DATETIME:
            AdaptativeColoredFormatter._SUNRISE_DATETIME = AdaptativeColoredFormatter._hour_minute_timestamp(
                Sun.get_sun_data_from_datetime(datetime.now()).sun_rise
            )

        if not AdaptativeColoredFormatter._SUNSET_DATETIME:
            AdaptativeColoredFormatter._SUNSET_DATETIME = AdaptativeColoredFormatter._hour_minute_timestamp(
                Sun.get_sun_data_from_datetime(datetime.now()).sun_set
            )

    def format(self, report: Report) -> Any:
        return ColoredFormatter.get_report_string(report, AdaptativeColoredFormatter._get_color_mapping())

    @staticmethod
    def _get_color_mapping() -> frozendict[Level, Color4Bits]:
        now_timestamp: int = AdaptativeColoredFormatter._hour_minute_timestamp(datetime.now())
        if AdaptativeColoredFormatter._SUNRISE_DATETIME <= now_timestamp < AdaptativeColoredFormatter._SUNSET_DATETIME:
            return ColoredFormatter.COLORS
        else:
            return AdaptativeColoredFormatter.NIGHT_COLORS

    @staticmethod
    def _hour_minute_timestamp(dt: datetime) -> int:
        return dt.hour * 60 + dt.minute


class DictFormatter(BaseFormatter):
    """
    Formats a provided report to a dictionary.

    Each key of the dictionary corresponds to the attribute name of :class:`ereport.report.Report`
    """
    __slots__ = (
        '_attributes',
    )

    def __init__(self, *report_attributes_to_keep: str):
        self._attributes: tuple[str, ...] = report_attributes_to_keep or Report.__slots__

    def format(self, report: Report) -> JsonType:
        return {
            attribute: getattr(report, attribute, None) for attribute in self._attributes
        }
