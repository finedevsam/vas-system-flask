from babel.numbers import format_currency


def currency_amount_format(value):
    return format_currency(value, 'USD', locale='en_US')