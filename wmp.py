# import standard libraries

import sys
from prettytable import PrettyTable

# import configuration variables

from config import TEMPLATES, VARIABLES, WEEK_DAYS


# functions

def exit_with_usage():
    print('usage: wmp.py WEEK_INDEX')
    exit()


#### main ####

if len(sys.argv) == 1:
    exit_with_usage()

# must be an integer

try:
    week_index = int(sys.argv[1])
except e:
    exit_with_usage()

# generate the weekly plan

weekly_table = PrettyTable()
weekly_table.field_names = ['Day', 'Dish']
weekly_table.align = 'l'

for j in range(0, 7):
    selected_base   = TEMPLATES[j]
    option_index    = week_index % len(selected_base)
    selected_option = selected_base[option_index]
    if selected_option in VARIABLES:
        variable_index = week_index % len(VARIABLES[selected_option])
        selected_variable = VARIABLES[selected_option][variable_index]
        my_food = selected_option.replace('VARIABLE', selected_variable)
    else:
        my_food = selected_option

    weekly_table.add_row( [ WEEK_DAYS[j], my_food ])

print(weekly_table)
