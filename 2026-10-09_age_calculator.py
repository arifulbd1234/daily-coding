"""
Day 3 - 2026-10-09
Tool: Age Calculator
What it does: Works out someone's exact age in years, months and days
from their date of birth, plus the total days lived and how many days
are left until their next birthday.
Who it helps: Anyone filling in a form, applying for a job, an exam or
an ID card, or just checking an exact age for a birthday.
"""

import calendar
from datetime import date


def _same_day_or_last_day(year, month, day):
    """That month's date for `day`, or its last day if shorter."""
    last_day = calendar.monthrange(year, month)[1]
    return date(year, month, min(day, last_day))


def calculate_age(birth_date, today=None):
    """Return the exact age as a (years, months, days) tuple."""
    if today is None:
        today = date.today()
    if birth_date > today:
        raise ValueError("Date of birth cannot be in the future.")

    # Full years: this year's birthday (29 February birthdays are
    # counted on 28 February in non-leap years).
    years = today.year - birth_date.year
    anchor = _same_day_or_last_day(
        birth_date.year + years, birth_date.month, birth_date.day
    )
    if anchor > today:
        years -= 1
        anchor = _same_day_or_last_day(
            birth_date.year + years, birth_date.month, birth_date.day
        )

    # Full months after that birthday.
    months = 0
    while months < 11:
        month_index = anchor.month - 1 + months + 1
        next_anchor = _same_day_or_last_day(
            anchor.year + month_index // 12,
            month_index % 12 + 1,
            birth_date.day,
        )
        if next_anchor > today:
            break
        months += 1

    anchor = _same_day_or_last_day(
        anchor.year + (anchor.month - 1 + months) // 12,
        (anchor.month - 1 + months) % 12 + 1,
        birth_date.day,
    ) if months else anchor

    # Whatever is left is whole days.
    days = (today - anchor).days
    return years, months, days


def total_days_lived(birth_date, today=None):
    """Return how many days have passed since the birth date."""
    if today is None:
        today = date.today()
    if birth_date > today:
        raise ValueError("Date of birth cannot be in the future.")
    return (today - birth_date).days


def days_until_next_birthday(birth_date, today=None):
    """Return the number of days until the next birthday (0 = today)."""
    if today is None:
        today = date.today()

    def birthday_in(year):
        # People born on 29 February celebrate on 28 February
        # in years that are not leap years.
        try:
            return date(year, birth_date.month, birth_date.day)
        except ValueError:
            return date(year, 2, 28)

    next_birthday = birthday_in(today.year)
    if next_birthday < today:
        next_birthday = birthday_in(today.year + 1)
    return (next_birthday - today).days


def format_age(birth_date, today=None):
    """Return the age as one easy-to-read line."""
    years, months, days = calculate_age(birth_date, today)
    return f"{years} years, {months} months, {days} days"


if __name__ == "__main__":
    # Example 1: exact age of someone born on 15 May 2000,
    # checked against a fixed date so the answer is clear
    dob1 = date(2000, 5, 15)
    fixed_day = date(2026, 10, 9)
    print("Born 2000-05-15, age on 2026-10-09:", format_age(dob1, fixed_day))
    print("Total days lived:", total_days_lived(dob1, fixed_day))

    # Example 2: a child born on 1 December 2023 — useful for
    # school admission forms that ask for the exact age
    dob2 = date(2023, 12, 1)
    print("Born 2023-12-01, age on 2026-10-09:", format_age(dob2, fixed_day))

    # Example 3: age and next-birthday countdown using today's real date
    dob3 = date(1998, 3, 20)
    print("Born 1998-03-20, age today:", format_age(dob3))
    print("Days until next birthday:", days_until_next_birthday(dob3))
