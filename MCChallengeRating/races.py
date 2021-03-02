# -*- coding: utf-8 -*-
"""
01/03/2021
@author: Rafael Arenhart
"""


class Race():

    def __init__(self):
        self.modifiers = {}
        self.conditions = []
        self.actions = []
        self.name = ''
        

class Human(Race):

    def __init__(self):
        super().__init__()
        self.name = 'Human'
        self.modifiers['skills per level'] = 1
        self.modifiers['feats'] = 1
        self.modifiers['speed'] = 30