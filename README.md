# weekly-meal-planner

Generates a week of meal suggestions based on daily options and variables inside each option.

Executing

```
python3 wmp.py X
```
where X is the index of the week, results in a plan based on the predefined variables:

```
+-----------+--------------------------------------+
| Day       | Dish                                 |
+-----------+--------------------------------------+
| Monday    | guisado de alubias                   |
| Tuesday   | pasta con bolognesa + ensalada verde |
| Wednesday | wraps de verduras y pollo            |
| Thursday  | huevos revueltos + crema de verduras |
| Friday    | asado de patatas, verduras y tofu    |
| Saturday  | BARRA LIBRE                          |
| Sunday    | arroz español                        |
+-----------+--------------------------------------+
```
For different values of X different plans are generated:

```
+-----------+---------------------------------------------+
| Day       | Dish                                        |
+-----------+---------------------------------------------+
| Monday    | guisado de lentejas                         |
| Tuesday   | pasta con pollo y aguacate + ensalada verde |
| Wednesday | couscous                                    |
| Thursday  | huevos revueltos + ensalada de tomate       |
| Friday    | asado de patatas, verduras y seitan         |
| Saturday  | BARRA LIBRE                                 |
| Sunday    | arroz español                               |
+-----------+---------------------------------------------+
```

Generating a 8 week plan is as simple as executing
```
for j in `seq 1 8`; do echo "week $j"; python3 wmp.py $j ; done
```

In order to customize the menu options all that is needed is editing [config.py](config.py).
