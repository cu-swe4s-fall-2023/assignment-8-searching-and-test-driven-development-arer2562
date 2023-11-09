test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest
# Define test cases

file1='Agrofood_co2_emission.csv'
file2='IMF_GDP.csv'
sub1='Agro_NA.csv'
sub2='GDP_NA.csv'


run "Test " python clean.py ${file1} ${file2} 
assert_equal Agro_NA.csv $( ls Agro_NA.csv )
assert_stdout

run "Test graphs" python main.py ${sub1} ${sub2}
assert_equal 4_panel.png  $( ls 4_panel.png )
assert_exit_code 0