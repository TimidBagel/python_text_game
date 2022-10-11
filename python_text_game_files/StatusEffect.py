# StatusEffect.py
# Contributors: Ben

from enum import Enum

class StatusEffect(Enum):
    POISON = 0
    BLEED = 1
    WEAK = 2 #We can use this later as a debuff. The counterpart will be RAGE ~Kit
    RAGE = 3

