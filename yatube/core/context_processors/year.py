import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    today = datetime.datetime.today()
    return {
        'year': int(today.strftime('%Y'))
    }
