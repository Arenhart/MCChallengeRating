# -*- coding: utf-8 -*-
"""
01/03/2021
@author: Rafael Arenhart
"""

import numpy as np

from MCChallengeRating.utils import roll, ATTRIBUTES


class Character():

    def __init__(self, name="", attribute_roll=""):
        self.properties = {}
        self.properties['name'] = name
        self.roll_attributes(attribute_roll)
        self.templates = []
        self.professions = []
        self.feats = []
        self.conditions = []
        self.damage = 0
        self.properties['bab'] = 0
        self.properties['ca'] = 10
        self.properties['hp'] = 0
        self.properties['speed'] = 0
        
    def roll_attributes(self, attribute_roll):
        if ';' in attribute_roll:
            self.properties = dict(zip(
                ATTRIBUTES,
                (int(i) for i in attribute_roll.split(';'))))
        elif 'd' in attribute_roll:
            self.properties = {}
            for attribute in ATTRIBUTES:
                self.properties[attribute] = roll(attribute_roll)
        elif len(attribute_roll) > 0:
            for attribute in ATTRIBUTES:
                self.properties[attribute] = int(attribute_roll)
        else:
            for attribute in ATTRIBUTES:
                self.properties[attribute] = 10

    def get_property(self, prop):
        base = self.properties.get
                
    def print_sheet(self, mode='simple'):
        print(self.properties)
                
        