"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from pathlib import Path
import os


with open("texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    print(f"First record of texts: {texts[0][0]}")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    print(f"Last record of calls: {calls[-1][-1]}")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

