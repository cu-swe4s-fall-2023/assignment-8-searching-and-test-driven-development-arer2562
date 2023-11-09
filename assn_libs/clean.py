import pandas as pd
import sys

def read_and_clean(in_file):
    read_file = pd.read_csv(in_file, sep=',')

    mainland_north_american_countries = [
        'United States of America', 'Canada', 'Mexico', 'Guatemala'
    ]
    years_to_include = [year for year in range(1980, 2021)]


    if 'Area' in read_file.columns:
        agro_mainland_na_df = read_file[read_file['Area'].isin(mainland_north_american_countries)]
        # Assuming you want to filter by years and 'Year' is a column
        print(agro_mainland_na_df)
        print(agro_mainland_na_df['Year'].unique())
        # This shows you the data type of each column
        print(agro_mainland_na_df.dtypes)
        agro_mainland_na_df = agro_mainland_na_df[agro_mainland_na_df['Year'].isin(years_to_include)]
        print(agro_mainland_na_df)
        agro_mainland_na_df.to_csv('Agro_NA.csv', index=False)
      
    elif 'Country' in read_file.columns:
        mainland_north_american_countries = [
        'United States', 'Canada', 'Mexico', 'Guatemala']
        gdp_mainland_na_df = read_file[read_file['Country'].isin(mainland_north_american_countries)]
        gdp_mainland_na_df = gdp_mainland_na_df.replace('United States', 'United States of America')
        # Assuming you want to filter by years and 'Year' is a column
        gdp_mainland_na_df.to_csv('GDP_NA.csv', index=False)

        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean.py <input_file.csv>")
        sys.exit(1)
    
    # Call the function with the provided argument
    else:
        input_filename = sys.argv[1]
        read_and_clean(input_filename)

