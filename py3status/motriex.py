# -*- coding: utf-8 -*-
"""
Example module that says 'Hello World!' that can be customised.

This demonstrates how to use configuration parameters.

Configuration parameters:
    format: Display format (default 'Hello World!')

docs:
https://py3status.readthedocs.io/en/latest/dev-guide/writing-modules/

example:
https://programtalk.com/vs2/python/13516/py3status/py3status/modules/volume_status.py/
"""


import subprocess


class Py3status:
    """Placeholder for running status command."""

    format = 'Number {number}'
    cache_timeout = 10

    def run(self):
        """Runner method."""
        result = subprocess.run(['date', '+%S'],
                                capture_output=True,
                                text=True)

        number = int(result.stdout.strip())
        full_text = self.py3.safe_format(self.format, {'number': number})

        if number < 30:
            color = self.py3.COLOR_LOW
        else:
            color = self.py3.COLOR_HIGH

        return {
            'full_text': full_text,
            'color': color,
            'cached_until': self.py3.time_in(self.cache_timeout)
        }

    def on_click(self, event):
        """Exec run function onClick."""
        pass
