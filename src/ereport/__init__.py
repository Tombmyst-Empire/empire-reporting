import os

from ereport.library.level import Levels, Level
from ereport.library.report import Report
from ereport.library.reporter import Reporter


_DEFAULT_REPORTER = Reporter('MAIN', Levels.parse_from_string(os.getenv('LOGGING_LEVEL', 'INFO')))


def get_or_make_reporter(name: str = None, env_var_logging_level: str = None, default_level: str | Levels = Levels.INFO) -> Reporter:
    return Reporter.get_or_make(name or 'MAIN', env_var_logging_level, default_level)


def trace(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.TRACE):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.TRACE,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def debug(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.DEBUG):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.DEBUG,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def success(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.SUCCESS):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.SUCCESS,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def info(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.INFO):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.INFO,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def warn(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.WARN):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.WARN,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def error(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.ERROR):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.ERROR,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def severe(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.SEVERE):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.SEVERE,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


def fatal(message: str, module: str | None = None, function: str | None = None, line: int | None = None):
    if _DEFAULT_REPORTER._level.can_log(Levels.FATAL):
        _DEFAULT_REPORTER._log(Report(
            level=Levels.FATAL,
            module=module or _DEFAULT_REPORTER._find_module(),
            function=function or _DEFAULT_REPORTER._find_function(),
            line=line or _DEFAULT_REPORTER._find_line_number(),
            message=message,
            reporter_name=_DEFAULT_REPORTER._reporter_name
        ))


if __name__ == '__main__':
    trace('Ceci est un test')
    debug('Ceci est un debug')
    success('Ceci est success')
    info('Ceci est uin info')
    warn('Ceci est un wanring')
    error('Ceci est un error')
    severe('Ceci est un severe')
    fatal('Ceci est un fatal')
