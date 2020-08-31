#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:31:16 2020

@author: luizf
"""

class DogsView:
    def ask_user_for_name(self):
        name = input('Enter a name:')
        return name

    def ask_user_for_color(self):
       color = input('Enter a color:')
       return color

    def display(self, dogs):
        print('---------------DOGS LIST--------------------')
        print('ID  | NAME      |  COLOR     ')
        for i in range(len(dogs)):
            print("{}   |  {}   | {}".format(i+1, dogs[i].name, dogs[i].color))
        print('--------------------------------------------')
