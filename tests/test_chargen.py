# -*- coding: utf-8 -*-
"""
01/03/2021
@author: Rafael Arenhart

Run with 'python -m pytest tests\test.py' at root
"""

import pytest

from MCChallengeRating.utils import roll, ATTRIBUTES
import MCChallengeRating.character as character
import MCChallengeRating.races as races
import MCChallengeRating.professions as professions

def test_chargen():
    char = character.Character(name = "Alf")
    char.print_sheet()
    assert(True)