#### Menu customization ####

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

#### Misc definitions ####

# days of the week in whatever language

WEEK_DAYS_EN = [ 'Monday',  'Tuesday', 'Wednesday', 'Thursday', 'Friday',  'Saturday', 'Sunday'  ]
WEEK_DAYS_ES = [ 'Lunes',   'Martes',  'Miercoles', 'Jueves',   'Viernes', 'Sábado',   'Domingo' ]
WEEK_DAYS_PT = [ 'Segunda', 'Terça',   'Quarta',    'Quinta',   'Sexta',   'Sábado',   'Domingo' ]

# language definition for days of the week

WEEK_DAYS = WEEK_DAYS_ES