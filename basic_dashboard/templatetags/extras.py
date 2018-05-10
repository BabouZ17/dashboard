#! /usr/bin/env python

from django import template
from time import ctime

register = template.Library()


def to_celsius(value):
    """
    Convert the value from Fahrenheit to Celsius
    """
    to_celsius = ''
    try:
        to_celsius = (int(value) - 32) * 5/9
    except ValueError:
        pass
    return to_celsius

def to_human_date(value):
    """
    Convert an epoch time to human readable date
    """
    time = ''
    try:
        time = ctime(int(value))
    except ValueError:
        time = None
    return time

def to_human_value(value):
    """
    Convert to a human readable value
    """
    new_value = ''
    try:
        transit = str(int(value))
        # Million or more
        if value / 1000000 > 0 and len(transit) < 10:
            new_value = transit[0:len(transit)-6] + '.' + \
            transit[len(transit)-6:len(transit)-3] + '.' + \
            transit[len(transit)-3:len(transit)] + ' -> ' + \
            transit[0:len(transit)-6] + ',' + \
            transit[len(transit)-6:len(transit)-5] + ' Millions'
        # Billion or more
        elif value / 1000000000 > 0 and len(transit) < 13:
            new_value = transit[0:len(transit)-9] + '.'  + \
            transit[len(transit)-9:len(transit)-6] + '.' + \
            transit[len(transit)-6:len(transit)-3] + '.' + \
            transit[len(transit)-3:len(transit)] + ' -> ' + \
            transit[0:len(transit)-9] + ',' + \
            transit[len(transit)-9:len(transit)-8] + ' Billions'
        # Trillion or more
        elif value / 1000000000000 > 0:
            new_value = transit[0:len(transit)-12] + '.'  + \
            transit[len(transit)-12:len(transit)-9] + '.' + \
            transit[len(transit)-9:len(transit)-6] + '.' + \
            transit[len(transit)-6:len(transit)-3] + '.' + \
            transit[len(transit)-3:len(transit)] + ' -> ' + \
            transit[0:len(transit)-12] + ',' + \
            transit[len(transit)-12:len(transit)-11] + ' Trillions'
        else:
            new_value = transit
    except (TypeError, ValueError):
        new_value = value
    return new_value


register.filter('to_human_value', to_human_value)
register.filter('to_celsius', to_celsius)
register.filter('to_human_date', to_human_date)
