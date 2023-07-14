from abc import ABC, abstractmethod

from ereport.library.formatter import DefaultFormatter, BaseFormatter
from ereport.library.report import Report


class ReporterOutlet(ABC):
    __slots__ = ('formatter',)

    def __init__(self, formatter: BaseFormatter = None):
        self.formatter: BaseFormatter = formatter or DefaultFormatter()

    def set_formatter(self, formatter):
        self.formatter = formatter

    @abstractmethod
    def emit(self, report: Report):
        raise NotImplementedError()


class ReporterOutletStdOut(ReporterOutlet):
    def __init__(self, formatter: BaseFormatter = None):
        super().__init__(formatter)

    def emit(self, report: Report):
        print(self.formatter.format(report))


class ReporterOutletFile(ReporterOutlet):
    __slots__ = (
        '_file',
        '_file_opened'
    )

    def __init__(self, file: str, formatter: BaseFormatter = None, *, truncate: bool = True):
        super().__init__(formatter or DefaultFormatter())
        self._file = open(file, 'w' if truncate else 'a', encoding='utf8', buffering=1)
        self._file_opened = True

    def close_file(self):
        if self._file_opened:
            self._file.close()

    def emit(self, report: Report):
        self._file.write(f'{self.formatter.format(report)}\n')


if __name__ == '__main__':
    from ereport.library.level import Levels
    from ereport.library.formatter import AdaptativeColoredFormatter
    outlet = ReporterOutletStdOut(AdaptativeColoredFormatter())
    outlet.emit(Report(Levels.WARN, 'module', 'func', 123, 'message', 'reporter'))
    outlet.emit(Report(Levels.ERROR, 'string_creation_vs_reuse', 'diff_json_different_values', 123, 'message', 'reporter'))
