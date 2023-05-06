# imports

import sys
from prettytable import PrettyTable

# days of the week in whatever language

WEEK_DAYS_EN = [ 'Monday',  'Tuesday', 'Wednesday', 'Thursday', 'Friday',  'Saturday', 'Sunday'  ]
WEEK_DAYS_ES = [ 'Lunes',   'Martes',  'Miercoles', 'Jueves',   'Viernes', 'Sábado',   'Domingo' ]
WEEK_DAYS_PT = [ 'Segunda', 'Terça',   'Quarta',    'Quinta',   'Sexta',   'Sábado',   'Domingo' ]

WEEK_DAYS = WEEK_DAYS_ES

# define base templated dishes, i.e, dishes with variables
# each item is in general a list so that certain days may return different dishes

BASE01 = [ 'guisado de VARIABLE'                    ]
BASE02 = [ 'pasta con VARIABLE + ensalada verde'    ]
BASE03 = [ 'couscous', 'wraps de verduras y pollo'  ]
BASE04 = [ 'huevos revueltos + VARIABLE'            ]
BASE05 = [ 'asado de patatas, verduras y VARIABLE'  ]
BASE06 = [ 'BARRA LIBRE'                            ]
BASE07 = [ 'arroz español'                          ]

# define an ordered list dish templates

TEMPLATES = [ BASE01, BASE02, BASE03, BASE04, BASE05, BASE06, BASE07 ]

# relate each dish with the corresponding variables

t_VARIABLES = {
              BASE01[0]: [ 'alubias', 'lentejas', 'garbanzos'                   ],
              BASE02[0]: [ 'bolognesa', 'pollo y aguacate', 'gusmix'            ],
              BASE04[0]: [ 'ensalada de tomate', 'crema de verduras'            ],
              BASE05[0]: [ 'pollo', 'lomo sapiens', 'ternera', 'tofu', 'seitan' ],
            },

# convert tuple to dict (...)
VARIABLES = t_VARIABLES[0]


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
