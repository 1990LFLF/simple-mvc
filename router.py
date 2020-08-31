#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:40:51 2020

@author: luizf
"""
from dogs_controller import DogsController

class Router:
    def __init__(self, controller):
        self.controller = controller
        self.running = True

    def run(self):
        while self.running == True:
            action = int(input('1 - Create a dog\n2 - All\n3 - Stop\n'))
            self.router(action)

    def router(self, action):
        if action == 1:
            self.controller.create()
        elif action == 2:
            self.controller.all()
        else:
            self.running = False
