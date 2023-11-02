test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
# Define test cases

country1='Argentina'
country2='Nexico'
graphdir=scats
datadir=data
sourcedir=scr

run "Test read_data with valid data" python ${sourcedir}/get_fire.py 'Agrofood_co2_emission.csv' 1 2 3 29 'IMF_GDP.csv' ${country1} ${datadir}/${country1}.txt ${graphdir}/${country1}.png
assert_equal $file_name $( ls ${country1}.png )
assert_exit_code 0

run "Test read_data with typo" python ${sourcedir}/get_fire.py 'Agrofood_co2_emission.csv' 1 2 3 29 'IMF_GDP.csv' ${country2} ${datadir}/${country2}.txt ${graphdir}/${country2}.png
assert_equal $file_name $( ls ${country2}.png )
assert_stderr