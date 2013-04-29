"""Solution for Task 1. The module contains a function that calculates
the horoscope sign by the date of birth."""


def what_is_my_sign(day, month):
    """Retrieve the name of the horoscope sign by day of birth.

    Keyword arguments:
    day -- the day of birth
    month -- the month of birth

    Returns string with the name of the horoscope sign.
    """

    signs = [
        # Name        Start     End
        ['Овен',      (21, 3),  (20, 4)],
        ['Телец',     (21, 4),  (20, 5)],
        ['Близнаци',  (21, 5),  (20, 6)],
        ['Рак',       (21, 6),  (21, 7)],
        ['Лъв',       (22, 7),  (22, 8)],
        ['Дева',      (23, 8),  (22, 9)],
        ['Везни',     (23, 9),  (22, 10)],
        ['Скорпион',  (23, 10), (21, 11)],
        ['Стрелец',   (22, 11), (21, 12)],
        ['Козирог',   (22, 12), (19, 1)],
        ['Водолей',   (20, 1),  (18, 2)],
        ['Риби',      (19, 2),  (20, 3)],
    ]

    for sign in signs:
        start_day = sign[1][0]
        start_month = sign[1][1]
        end_day = sign[2][0]
        end_month = sign[2][1]

        if day >= start_day and month == start_month or \
                day <= end_day and month == end_month:
            return sign[0]
