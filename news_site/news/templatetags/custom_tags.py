import re
from django import template


register = template.Library()

@register.filter
def hex_to_rgba(hex_color, opacity=1):
    hex_pattern = r'^#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$'
    match = re.match(hex_pattern, hex_color)
    if match:
        value = match.group(1)
        if len(value) == 3:
            value = value * 2
        r, g, b = [int(value[i:i+2], 16) for i in range(0, 6, 2)]
        return f'rgba({r}, {g}, {b}, {opacity})'
    else:
        raise ValueError(f'Invalid hex color value: {hex_color}')


