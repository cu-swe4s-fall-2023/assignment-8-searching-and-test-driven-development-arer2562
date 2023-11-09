country1='Argentina'
country2='Mexico'
country3='Brazil'
graphdir=scats
datadir=data


python get_fire.py 'Agrofood_co2_emission.csv' 1 2 3 29 'IMF_GDP.csv' ${country1} ${datadir}/${country1}.txt ${graphdir}/${country1}.png
python get_fire.py 'Agrofood_co2_emission.csv' 1 2 3 29 'IMF_GDP.csv' ${country2} ${datadir}/${country2}.txt ${graphdir}/${country2}.png
python get_fire.py 'Agrofood_co2_emission.csv' 1 2 3 29 'IMF_GDP.csv' ${country3} ${datadir}/${country3}.txt ${graphdir}/${country3}.png


