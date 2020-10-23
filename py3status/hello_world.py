# -*- coding: utf-8 -*-
"""
Example module that says 'Hello World!'

This demonstrates how to produce a simple custom module.
"""

import subprocess

class Py3status:

    def __init__(self):
        self.full_text = 'etc'
       
    def click_info(self):
        return {
            'full_text': self.full_text,
            'cached_until': self.py3.CACHE_FOREVER
        }

    def on_click(self, event):
        """
        event will be a dict like
        {'y': 13, 'x': 1737, 'button': 1, 'name': 'example', 'instance': 'first'}
        """
        # correct = subprocess.run(['notify-send', 'dddd'], check=True, text=True)
       
        

       

        button = event['button']
        if button == 1:
             correct = subprocess.run(['alacritty', '-e', 'htop', '&'], check=True, text=True)
             format_string = 'htop{button}'

        if button == 3:
             correct = subprocess.run(['/home/saa/src/js/simple-samples/prices/node_modules/electron/dist/electron', '/home/saa/src/js/simple-samples/prices/app.js', '&'], check=True, text=True)
             format_string = 'btn{button}'


        
            
        # update our output (self.full_text)

        data = {'button': button}
        self.full_text = self.py3.safe_format(format_string, data)
        # self.color = self.py3.COLOR_LOW -- dont work(
        # Our modules update methods will get called automatically.
        
