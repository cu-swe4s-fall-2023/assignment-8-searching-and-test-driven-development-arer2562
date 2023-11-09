import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

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

def get_fire_gdp_year_data(fire_file_name,
                           gdp_file_name,
                           target_country,
                           fire_year_col,
                           fire_savanna_col,
                           fire_forest_col,
                           fire_Co2_col):
    
    fire_datas = get_data(fire_file_name, 
                         query_value=target_country, 
                         query_col=0)

    gdp_datas, header = get_data(gdp_file_name,
                                 query_value=target_country,
                                 query_col=0,
                                 get_header=True)
    
    fires = []
    gdps = []
    years = []
    co2 = []
    
    for fire_data in fire_datas:
        year = fire_data[fire_year_col]
        year_idx = search(header, year)
        if gdp_datas[0][year_idx] != '...' and fire_data[29] != '...':
            fires.append(float(fire_data[fire_savanna_col]) + float(fire_data[fire_forest_col]))
            years.append(int(year))
            gdps.append(float(clean_str(gdp_datas[0][year_idx])))
            co2.append(float(fire_data[fire_Co2_col]))  
    
    ofn = f"{target_country}.txt"
    with open(ofn, 'w') as file:
        for i in range(len(fires)):
            file.write('\t'.join([str(fires[i]), str(gdps[i])]) + '\n')
    
    return [fires, gdps, years, co2]

def scat(country, infile, out_file):
    # Scatter plot
    data = np.genfromtxt(infile, delimiter='\t', names=['TotalFires', 'GDP'])
    title = "GDP vs Fires for " + country
    x_label = "Total Fires"
    y_label = "GDP"

    X = data['TotalFires']
    Y = data['GDP']

    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    filename = f"{country}.png"
    plt.savefig(out_file, bbox_inches='tight')


