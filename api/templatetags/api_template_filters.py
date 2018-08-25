from django import template


register = template.Library()


def humantime(value):
    value = int(value)
    if value <= 60:
        return '{} seconds'.format(value)
    elif value < 3600:
        if value % 60 == 0:
            return '{} minutes'.format(value // 60)
        minutes = value // 60
        seconds = value % 60

        return '{} minutes {} seconds'.format(minutes, seconds)
    elif value < 86400:
        if value % 60 == 0:
            return '{} hours'.format(value // 60 // 60)
        hours = value // 60 // 60
        minutes = value // 60 % 60
        seconds = value % 60

        humantime = '{} hours {} minutes'
        if seconds > 0:
            humantime += ' {} seconds'
            return humantime.format(hours, minutes, seconds)
        return humantime.format(hours, minutes)
    elif value < 604800:
        return 'days'
    elif value < 2419200:
        return 'weeks'
    elif value < 29030400:
        return 'months'
    else:
        return 'years'
