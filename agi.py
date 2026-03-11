"""
AGI demonstration
"""

import schedule
import time

def do_work():
    print("Executing autonomous task")

schedule.every().day.at("09:00").do(do_work)

while True:
    schedule.run_pending()
    time.sleep(1)

