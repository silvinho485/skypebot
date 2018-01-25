from datetime import datetime, timedelta


def ponto(entry, working, rest_hours, format='%H:%M', exit=None, verbose=True):
    entrytime = datetime.strptime(entry, format)
    working_hours = _get_timedelta_from_hours(working, format)
    rest_hours = _get_rest_hours_timedelta(rest_hours, format)

    if exit:
        worked_hours = _get_worked_hours(exit, entrytime, rest_hours, format)
        msg = '{} horas trabalhadas e {} de descanso'
        return _return_message(msg, [worked_hours, rest_hours], verbose)
    else:
        expected_exittime = entrytime + working_hours + rest_hours
        msg = 'Você deve sair as {} para descansar {} e completar {} horas'
        params = [
            datetime.strftime(expected_exittime, format),
            rest_hours,
            working_hours,
        ]
        return _return_message(msg, params, verbose)


def _return_message(msg, params, verbose):
    if verbose:
        return msg.format(*params)
    else:
        return params[0]


def _get_timedelta_from_hours(hours, format):
    h = datetime.strptime(hours, format)
    return timedelta(hours=h.hour, minutes=h.minute)


def _get_worked_hours(exit, entrytime, rest_hours, format):
    exittime = datetime.strptime(exit, format)
    return exittime - entrytime - rest_hours


def _get_rest_hours_timedelta(rest_hours, format):
    if ',' in str(rest_hours):
        exit, regress = rest_hours.split(',')
        exittime = datetime.strptime(exit, format)
        regresstime = datetime.strptime(regress, format)
        return regresstime - exittime
    else:
        return _get_timedelta_from_hours(rest_hours, format)
