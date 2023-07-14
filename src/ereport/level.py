from __future__ import annotations
from typing import Final


class Level:
    """
    Reporter level implementation
    """
    __slots__ = (
        'weight',
        'name'
    )

    def __init__(self, weight: int, name: str):
        self.weight = weight
        self.name = name

    def __eq__(self, other) -> bool:
        return isinstance(other, Level) and other.weight == self.weight

    def __ne__(self, other) -> bool:
        return not self == other

    def __gt__(self, other) -> bool:
        return self.weight > other.weight

    def __ge__(self, other) -> bool:
        return self.weight >= other.weight

    def __lt__(self, other) -> bool:
        return self.weight < other.weight

    def __le__(self, other) -> bool:
        return self.weight <= other.weight

    def __repr__(self) -> str:
        return f'Level(weight={self.weight}, name="{self.name}")'

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash((self.weight, self.name))

    def can_log(self, required_level: Level) -> bool:
        return required_level.weight >= self.weight


class Levels:
    """
    List of levels
    """
    ALL: Final[Level] = Level(0, 'ALL')
    TRACE: Final[Level] = Level(10, 'TRACE')
    DEBUG: Final[Level] = Level(20, 'DEBUG')
    SUCCESS: Final[Level] = Level(30, 'SUCCESS')
    INFO: Final[Level] = Level(40, 'INFO')
    WARN: Final[Level] = Level(50, 'WARN')
    ERROR: Final[Level] = Level(60, 'ERROR')
    SEVERE: Final[Level] = Level(70, 'SEVERE')
    FATAL: Final[Level] = Level(80, 'FATAL')

    @staticmethod
    def parse_from_string(level: str) -> Level:
        return _STRING_TO_LEVEL[level.lower()]


_STRING_TO_LEVEL = {
    'all': Levels.ALL,
    'trace': Levels.TRACE,
    'debug': Levels.DEBUG,
    'success': Levels.SUCCESS,
    'info': Levels.INFO,
    'warn': Levels.WARN,
    'error': Levels.ERROR,
    'severe': Levels.SEVERE,
    'fatal': Levels.FATAL
}