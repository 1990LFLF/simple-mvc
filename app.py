#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:46:25 2020

@author: luizf
"""

from dogs_controller import DogsController
from router import Router

ctr = DogsController()

router = Router(ctr)

router.run()

