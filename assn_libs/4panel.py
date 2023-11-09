import matplotlib.pyplot as plt
import pandas as pd
print('hello world')

agro = pd.read_csv('Agro_NA.csv',sep=',')
print(agro.head())
gdp = pd.read_csv('GDP_NA.csv',sep=',')
print(gdp.head())


agro_mainland_na_df = pd.read_csv('Agro_NA.csv')
                                  
gdp_mainland_na_df = pd.read_csv('GDP_NA.csv')
                                 

# Assuming mainland_na_df is the DataFrame with the North American subset
fig, ax = plt.subplots()

# List of country names in the North American subset
countries = agro_mainland_na_df['Area'].unique()

# Loop through each country and plot the Average Temperature vs year
for country in countries:
    country_data = agro_mainland_na_df[agro_mainland_na_df['Area'] == country]
    ax.plot(country_data['Year'], country_data['Average Temperature °C'], label=country)

ax.legend(loc='upper right')
ax.set_xlabel('Year')
ax.set_ylabel('Average Temperature (°C)')
plt.show()

import matplotlib.pyplot as plt

# Assuming mainland_na_df is the DataFrame with the North American subset
fig, ax = plt.subplots()

# List of country names in the North American subset
countries = agro_mainland_na_df['Area'].unique()

# Loop through each country and create a scatter plot for Total Emission vs Year
for country in countries:
    country_data = agro_mainland_na_df[agro_mainland_na_df['Area'] == country]
    ax.scatter(country_data['Year'], country_data['total_emission'], label=country, s=10)  # Adjust the size (s) as needed

ax.legend(loc='upper left')
ax.set_xlabel('Year')
ax.set_ylabel('Total Emission')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load and replace '-' and '...' values with NaN in the GDP data
gdp_data = gdp_mainland_na_df.replace(['-', '...'], np.nan)

# Load your agriculture data
agro_data = agro_mainland_na_df

# Merge the two datasets based on the common column, which appears to be the country name and year
merged_data = pd.merge(gdp_data, agro_data, left_on=['Country'], right_on=['Area'])

# Define the list of North American countries (including Guatemala)
north_american_countries = ['United States', 'Canada', 'Mexico', 'Guatemala']  # Add Guatemala to the list
filtered_data = merged_data[merged_data['Country'].isin(north_american_countries)]

years = [str(year) for year in range(1980, 2021)]
x_values = [filtered_data[year].str.replace(',', '', regex=False).astype(float) for year in years]
y = filtered_data['total_emission']
colors = filtered_data['Year']

plt.figure(figsize=(12, 8))
for i, year in enumerate(years):
    plt.scatter(x_values[i], y, c=colors, cmap='viridis', label=f'Year {year}')

plt.xlabel('GDP (1980-2020)')
plt.ylabel('total_emission')
plt.title('Scatter Plot of GDP vs Total emission (1980-2020)')

plt.legend()

plt.show()

import matplotlib.pyplot as plt

# Assuming mainland_na_df is the DataFrame with the North American subset
fig, ax = plt.subplots()

# List of country names in the North American subset
countries = agro_mainland_na_df['Area'].unique()

# Loop through each country and create a scatter plot for Total Emission vs Year
for country in countries:
    country_data = agro_mainland_na_df[agro_mainland_na_df['Area'] == country]
    ax.scatter(country_data['Rural population'], country_data['total_emission'], label=country, s=10)  # Adjust the size (s) as needed

ax.legend(loc='upper left')
ax.set_xlabel('Rural Population')
ax.set_ylabel('total_emission')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec



# Assuming mainland_na_df is the DataFrame with the North American subset
# List of country names in the North American subset
countries = agro_mainland_na_df['Area'].unique()

# Create a 2x2 grid for the subplots (a, b, c, d)
fig, axs = plt.subplots(2, 2, figsize=(12, 10), constrained_layout=True, gridspec_kw={'wspace': 0.2, 'hspace': 0.4})

# Set plot titles
titles = ['(a) Average Temperature', '(b) Total Emission vs Year', '(c) GDP vs Total Emission (1980-2020)', '(d) Rural Population vs Total Emission']

# Loop through each country and create the subplots
for i, ax in enumerate(axs.flat):
    if i == 0:
        # Subplot (a): Average Temperature vs Year
        for country in countries:
            country_data = agro_mainland_na_df[agro_mainland_na_df['Area'] == country]
            ax.plot(country_data['Year'], country_data['Average Temperature °C'], label=country)
        ax.legend(loc='upper right')
        ax.set_xlabel('Year')
        ax.set_ylabel('Average Temperature (°C)')
    elif i == 1:
        # Subplot (b): Total Emission vs Year
        for country in countries:
            country_data = agro_mainland_na_df[agro_mainland_na_df['Area'] == country]
            ax.scatter(country_data['Year'], country_data['total_emission'], label=country, s=10)
        ax.legend(loc='upper left')
        ax.set_xlabel('Year')
        ax.set_ylabel('Total Emission')
    elif i == 2:
        # Subplot (c): GDP vs Total Emission (1980-2020)
        for country in north_american_countries:
            country_data = filtered_data[filtered_data['Country'] == country]
            gdp_values = [country_data[year].str.replace(',', '', regex=False).astype(float) for year in years]  # Remove commas and convert to float for each year
            total_emissions = country_data['total_emission']

            for j, year in enumerate(years):
                ax.scatter(gdp_values[j], total_emissions, label=f'{year}', s=10)
        ax.legend(loc='upper left')
        ax.set_xlabel('GDP (1980-2020)')
        ax.set_ylabel('Total Emission')
    elif i == 3:
        # Subplot (d): Rural Population vs Total Emission
        for country in countries:
            country_data = agro_mainland_na_df[agro_mainland_na_df['Area'] == country]
            ax.scatter(country_data['Rural population'], country_data['total_emission'], label=country, s=10)
        ax.legend(loc='upper left')
        ax.set_xlabel('Rural Population')
        ax.set_ylabel('Total Emission')

    # Set subplot title
    ax.set_title(titles[i])
    # Remove right and top borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# Show the multipanel graph
plt.show()
fig.savefig('4_panel.png') 
