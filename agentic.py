"""
Agentic workflow demonstration
"""

import subprocess

def agentic_workflow():
    print("Step 1: gather data")
    subprocess.run(["python", "fetch_data.py"])

    print("Step 2: analyze")
    subprocess.run(["python", "analyze.py"])

    print("Step 3: report")
    subprocess.run(["python", "send_report.py"])

if __name__ == "__main__":
    agentic_workflow()
