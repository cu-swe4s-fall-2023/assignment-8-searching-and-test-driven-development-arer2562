import csv

def clean_str(string):
    return string.replace(",", "")

def search(L, k):
    for i, value in enumerate(L):
        if k == value:
            return i
    return None

def get_data(file_name, query_value=None, query_col=None, get_header=False):
    header = []
    data = []
    
    with open(file_name) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if query_value is None or query_col is None:
                data.append(row)
            else:
                if get_header and len(header) == 0:
                    header = row
                    continue
                if row[query_col] == query_value:
                    data.append(row)
    if get_header:
        return data, header
    else:
        return data




