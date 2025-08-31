Ubicación óptima: (5, 3)
Código MiniZinc:
var int: x;
var int: y;
constraint x >= 0;
constraint y >= 0;
constraint x <= 12;
constraint y <= 12;
set of int: CIUDADES = 1..5;
function var int: distancia_manhattan(var int: x1,var int: y1,var int: x2,var int: y2) = abs(x1 - x2) + abs(y1 - y2);
var int: distancia1 = distancia_manhattan(2, 3, x, y);
var int: distancia2 = distancia_manhattan(10, 2, x, y);
var int: distancia3 = distancia_manhattan(11, 0, x, y);
var int: distancia4 = distancia_manhattan(0, 3, x, y);
var int: distancia5 = distancia_manhattan(1, 2, x, y);
solve minimize distancia1;
output["x=",show(x),"y=",show(y)];
