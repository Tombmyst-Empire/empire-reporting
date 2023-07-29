from __future__ import annotations

from datetime import datetime


def current_yyyy_mm_dd_hh_ii_ss_ffff(
        date_separator: str = '-',
        datetime_separator: str = ' ',
        time_separator: str = ':',
        sub_second_separator: str = ','
) -> str:
    return datetime.now().strftime(f'%Y{date_separator}%m{date_separator}%d'
                                   f'{datetime_separator}'
                                   f'%H{time_separator}%M{time_separator}%S{sub_second_separator}%f')
