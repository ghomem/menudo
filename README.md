# weekly-meal-planner

Generates a week of meal suggestions based on daily options and variables inside each option.

Executing:

```
python3 wmp.py 1
```
results in a plan based on the predefined variables:

```
+-----------+---------------------------------------------+
| Day       | Dish                                        |
+-----------+---------------------------------------------+
| Lunes     | guisado de lentejas                         |
| Martes    | pasta con pollo y aguacate + ensalada verde |
| Miercoles | wraps de verduras y pollo                   |
| Jueves    | huevos revueltos + crema de verduras        |
| Viernes   | asado de patatas, verduras y lomo sapiens   |
| Sábado    | BARRA LIBRE                                 |
| Domingo   | arroz español                               |
+-----------+---------------------------------------------+
```

Generating a 8 week plan is as simple as executing
```
for j in `seq 1 8`; do echo "week $j"; python3 wmp.py $j ; done
```
