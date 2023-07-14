from empire_commons.date_util.date_util import current_yyyy_mm_dd_hh_ii_ss_ffff

from src.ereport.level import Level


class Report:
    __slots__ = (
        'date_time',
        'level',
        'module',
        'function',
        'line',
        'message',
        'reporter_name'
    )

    def __init__(
            self,
            level: Level,
            module: str,
            function: str,
            line: int,
            message: str,
            reporter_name: str,
            date_time: str = None,
    ):
        self.date_time: str = date_time if date_time else current_yyyy_mm_dd_hh_ii_ss_ffff()
        self.level: Level = level
        self.module: str = module
        self.function: str = function
        self.line: int = line
        self.message: str = message
        self.reporter_name: str = reporter_name
