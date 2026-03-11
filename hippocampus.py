"""
AI memory demonstration
"""

memory = {}

def remember(key, value):
    memory[key] = value

def recall(key):
    return memory.get(key)

remember("user_name", "Ajay")

print(recall("user_name"))

