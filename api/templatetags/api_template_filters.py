from dateutil.relativedelta import relativedelta
from django import template


register = template.Library()


def pluarlize_unit(value, unit):
    if value == 1:
        return unit

    return unit + 's'


@register.filter(name='humantime')
def humantime(value):
    value = int(value)
    rd = relativedelta(seconds=value)

    # seconds
    if value <= 60:
        humantime = '{} {}'.format(value, pluarlize_unit(value, 'second'))
    # minutes
    elif value < 3600:
        humantime = '{} {}'.format(rd.minutes,
                                   pluarlize_unit(rd.minutes, 'minute'))
        if rd.seconds > 0:
            humantime += ' {} {}'.format(rd.seconds,
                                         pluarlize_unit(rd.seconds, 'second'))
    # hours
    elif value < 86400:
        humantime = '{} {}'.format(rd.hours,
                                   pluarlize_unit(rd.hours, 'hour'))
        if rd.minutes > 0:
            humantime += ' {} {}'.format(rd.minutes,
                                         pluarlize_unit(rd.minutes, 'minute'))
        elif rd.seconds > 0:
            humantime += ' 0 minutes'

        if rd.seconds > 0:
            humantime += ' {} {}'.format(rd.seconds,
                                         pluarlize_unit(rd.seconds, 'second'))
    # days
    elif value < 604800:
        humantime = '{} {}'.format(rd.days, pluarlize_unit(rd.days, 'day'))
        if rd.hours > 0:
            humantime += ' {} {}'.format(rd.hours,
                                         pluarlize_unit(rd.hours, 'hour'))
        elif rd.minutes > 0 or rd.seconds > 0:
            humantime += ' 0 hours'

        if rd.minutes > 0:
            humantime += ' {} {}'.format(rd.minutes,
                                         pluarlize_unit(rd.minutes, 'minute'))
        elif rd.seconds > 0:
            humantime += ' 0 minutes'

        if rd.seconds > 0:
            humantime += ' {} {}'.format(rd.seconds,
                                         pluarlize_unit(rd.seconds, 'second'))
    # weeks
    elif value < 2419200:
        humantime = '{} {}'.format(rd.weeks,
                                   pluarlize_unit(rd.weeks, 'week'))

        num_days = rd.days - (rd.weeks * 7) if rd.days % 7 > 0 else 0
        if num_days > 0:
            humantime += ' {} {}'.format(num_days,
                                         pluarlize_unit(num_days, 'day'))
        elif rd.hours > 0 or rd.minutes > 0 or rd.seconds > 0:
            humantime += ' 0 days'

        if rd.hours > 0:
            humantime += ' {} {}'.format(rd.hours,
                                         pluarlize_unit(rd.hours, 'hour'))
        elif rd.minutes > 0 or rd.seconds > 0:
            humantime += ' 0 hours'

        if rd.minutes > 0:
            humantime += ' {} {}'.format(rd.minutes,
                                         pluarlize_unit(rd.minutes, 'minute'))
        elif rd.seconds > 0:
            humantime += ' 0 minutes'

        if rd.seconds > 0:
            humantime += ' {} {}'.format(rd.seconds,
                                         pluarlize_unit(rd.seconds, 'second'))
    # months
    elif value < 29030400:
        humantime = '{} {}'.format(rd.months,
                                   pluarlize_unit(rd.months, 'month'))
        if rd.weeks > 0:
            humantime += ' {} {}'.format(rd.weeks,
                                         pluarlize_unit(rd.weeks, 'week'))

        num_days = rd.days - (rd.weeks * 7) if rd.days % 7 > 0 else 0
        if num_days > 0:
            humantime += ' {} {}'.format(num_days,
                                         pluarlize_unit(num_days, 'day'))
        elif rd.hours > 0 or rd.minutes > 0 or rd.seconds > 0:
            humantime += ' 0 days'

        if rd.hours > 0:
            humantime += ' {} {}'.format(rd.hours,
                                         pluarlize_unit(rd.hours, 'hour'))
        elif rd.minutes > 0 or rd.seconds > 0:
            humantime += ' 0 hours'

        if rd.minutes > 0:
            humantime += ' {} {}'.format(rd.minutes,
                                         pluarlize_unit(rd.minutes, 'minute'))
        elif rd.seconds > 0:
            humantime += ' 0 minutes'

        if rd.seconds > 0:
            humantime += ' {} {}'.format(rd.seconds,
                                         pluarlize_unit(rd.seconds, 'second'))
    # years
    else:
        humantime = '{} {}'.format(rd.years,
                                   pluarlize_unit(rd.years, 'year'))
        if rd.months > 0:
            humantime += ' {} {}'.format(rd.months,
                                         pluarlize_unit(rd.months, 'month'))

        if rd.weeks > 0:
            humantime += ' {} weeks'.format(rd.weeks,
                                            pluarlize_unit(rd.weeks, 'week'))

        num_days = rd.days - (rd.weeks * 7) if rd.days % 7 > 0 else 0
        if num_days > 0:
            humantime += ' {} {}'.format(num_days,
                                         pluarlize_unit(num_days, 'day'))
        elif rd.hours > 0 or rd.minutes > 0 or rd.seconds > 0:
            humantime += ' 0 days'

        if rd.hours > 0:
            humantime += ' {} {}'.format(rd.hours,
                                         pluarlize_unit(rd.hours, 'hour'))
        elif rd.minutes > 0 or rd.seconds > 0:
            humantime += ' 0 hours'

        if rd.minutes > 0:
            humantime += ' {} {}'.format(rd.minutes,
                                         pluarlize_unit(rd.minutes, 'minute'))
        elif rd.seconds > 0:
            humantime += ' 0 minutes'

        if rd.seconds > 0:
            humantime += ' {} {}'.format(rd.seconds,
                                         pluarlize_unit(rd.seconds, 'second'))

    return humantime
