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
# import json
import datetime


class Py3status:
    """Placeholder for running status command."""

    format = 'Number {number}'
    cache_timeout = 30

    def run(self):
        """Runner method."""
        now = datetime.datetime.now()
        if now.hour > 19 or now.hour < 10:
            return {
                'full_text': "-",
                'color': self.py3.COLOR_HIGH,
                'cached_until': self.py3.time_in(self.cache_timeout)
            }
        # result = subprocess.run(['date', '+%S'],
        result = subprocess.run(['/home/saa/.config/i3/py3status/motriex-proto-lens'],
                                capture_output=True,
                                text=True)

        number = float(result.stdout.strip())
        # full_text = self.py3.safe_format(self.format, {'number': number})

        if number < 60.0:
            color = self.py3.COLOR_LOW
        else:
            color = self.py3.COLOR_HIGH

        return {
            'full_text': str(number),
            'color': color,
            'cached_until': self.py3.time_in(self.cache_timeout)
        }

    def on_click(self, event):
        """Exec run function onClick."""
        pass

    # def prn():
    #     """Exec debug shell command."""
    #     result = subprocess.run(['./motriex-proto-lens'],
    #                             capture_output=True,
    #                             text=True)
    #     # jsonData = json.loads(json.loads(result.stdout.strip()))
    #     # print(jsonData['code'])
    #     number2 = float(result.stdout.strip())
    #     return {
    #         "out": number2
    #     }
