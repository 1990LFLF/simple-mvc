#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:28:09 2020

@author: luizf
"""

from dogs_view import DogsView
from dog import Dog

class DogsController:

    def __init__(self):
        self.view = DogsView()
        self.lst = []

    def create(self):
        name = self.view.ask_user_for_name()
        color = self.view.ask_user_for_color()
        dog = Dog(name, color)
        self.store(dog)

    def store(self, dog):
        self.lst.append(dog)

    def all(self):
        print(self.lst)
