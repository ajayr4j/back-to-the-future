"""
AI reasoning demonstration
"""

temperature = 32

def think(temp):
    if temp > 30:
        return "turn_on_ac"
    else:
        return "do_nothing"

decision = think(temperature)
print("Decision:", decision)

