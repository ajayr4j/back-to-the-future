"""
Model Context Protocol demonstration
"""

import requests

def call_tool():
    response = requests.get("https://api.github.com")
    return response.json()

print(call_tool())

# Historical name: API call