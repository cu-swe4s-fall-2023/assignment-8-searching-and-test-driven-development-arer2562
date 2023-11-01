import csv

def clean_str(string):
    return string.replace(",", "")

def search(L, k):
    for i, value in enumerate(L):
        if k == value:
            return i
    return None


