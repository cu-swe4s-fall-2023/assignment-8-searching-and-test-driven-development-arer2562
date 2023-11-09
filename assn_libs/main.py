import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def main(agro_filename, gdp_filename):
    print('hello world')

    # Load the agriculture data
    agro_mainland_na_df = pd.read_csv(agro_filename)
    print(agro_mainland_na_df.head())

    # Load the GDP data
    gdp_mainland_na_df = pd.read_csv(gdp_filename)
    print(gdp_mainland_na_df.head())

    # Replace '...' with NaN and melt the GDP data to long format
    gdp_mainland_na_df.replace('...', np.nan, inplace=True)
    gdp_long_df = gdp_mainland_na_df.melt(id_vars=['Country'], var_name='Year', value_name='GDP')

    # Convert 'Year' to int and remove commas from 'GDP' then convert to float
    gdp_long_df['Year'] = gdp_long_df['Year'].astype(int)
    gdp_long_df['GDP'] = gdp_long_df['GDP'].str.replace(',', '').astype(float)

    print(gdp_long_df.head())

    # Merge the agriculture data with the transformed GDP data
    merged_data = pd.merge(agro_mainland_na_df, gdp_long_df, left_on=['Area', 'Year'], right_on=['Country', 'Year'])
    print(merged_data.head())

    # Create a 2x2 grid for the subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10), constrained_layout=True)
    countries = merged_data['Area'].unique()  # Updated to use the 'Area' from merged data
    titles = ['(a) Average Temperature', '(b) Total Emission vs Year', 
              '(c) GDP vs Total Emission', '(d) Rural Population vs Total Emission']

    # Loop through each subplot to set specific plots
    for i, ax in enumerate(axs.flat):
        for country in countries:
            country_data = merged_data[merged_data['Area'] == country]
            if i == 0:  # Subplot (a): Average Temperature vs Year
                ax.plot(country_data['Year'], country_data['Average Temperature °C'], label=country)
            elif i == 1:  # Subplot (b): Total Emission vs Year
                ax.scatter(country_data['Year'], country_data['total_emission'], label=country, s=10)
            elif i == 2:  # Subplot (c): GDP vs Total Emission
                ax.scatter(country_data['GDP'], country_data['total_emission'], label=country, s=10)
            elif i == 3:  # Subplot (d): Rural Population vs Total Emission
                ax.scatter(country_data['Rural population'], country_data['total_emission'], label=country, s=10)
        
        # Set common features for subplots
        ax.legend(loc='upper left')
        ax.set_title(titles[i])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    # Adjust labels for all axes
    for ax in axs.flat:
        ax.set(xlabel='Year', ylabel='Value')

    # Adjust y-axis labels for the first column of subplots
    axs[0, 0].set(ylabel='Average Temperature (°C)')
    axs[1, 0].set(ylabel='Total Emission')

    # Adjust x-axis labels for the bottom row of subplots
    axs[1, 0].set(xlabel='Year')
    axs[1, 1].set(xlabel='Rural Population')

    # Show the plot
    plt.show()
    fig.savefig('4_panel.png') 

# Call the main function
if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python main.py Agro_NA.csv GDP_NA.csv")