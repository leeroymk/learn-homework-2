import locale
from datetime import date, timedelta, datetime


def print_days():

    locale.setlocale(locale.LC_TIME, 'ru_RU')

    date_td = date.today()
    delta = timedelta(days=1)
    date_ystd = date_td - delta
    date_mon_ago = date_td - (30 * delta)

    lst_dates = [date_td, date_ystd, date_mon_ago]

    tod, ystd, mon_ago = [i.strftime('%A %d %B %Y').lower() for i in lst_dates]

    print(f"Вчера: {ystd} г.")
    print(f"Сегодня: {tod} г.")
    print(f"30 дней назад: {mon_ago} г.")


def str_2_datetime(date_string):
    res = datetime.strptime(date_string, ("%d/%m/%y %H:%M:%S.%f"))
    return f'Функция возвращает {type(res)}'


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
