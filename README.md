Manual de usuario
1. Preparación del espacio de trabajo
Kwok está codificado en lenguaje Python, por lo que lo primero que debemos hacer es verificar que tengamos instalado Python en nuestro equipo, para ello debemos ejecutar el comando en la línea de comandos:
python --version

En caso de no tener instalado python podemos instalarlo en la siguiente liga: https://www.python.org/downloads/. Una vez instalado python debemos verificar que tengamos todas las librerías necesarias instaladas para poder usar el lenguaje. Para empezar a codificar en Kwok debes tener instaladas las librerías de lex y yacc, para ello debemos ejecutar los siguientes comandos:

pip install lex
pip install yacc

En caso de que se requiera instalar alguna otra librería de python recuerde que los comandos son:
pip install nombreDeLibrería

Para usar el lenguaje debemos crear un archivo “main.kwok” y empezar a codificar. Para correr el programa debemos ejecutar el comando:

python PLY.py
2. Empezar a programar
2.1 Estructura
Cualquier programa en Kwok debe llevar primero un nombre que se le quiera asignar al programa seguido de la palabra reservada “program”. Después se declaran las variables locales y funciones que se usarán en el programa. Estas dos últimas son opcionales pero lo que sí debe llevar el programa es un main( ). Para ilustrar más la estructura del lenguaje pongamos el ejemplo de un “Hola Mundo” en Kwok:

program holaMundo;
main(){
    print("Hola Mundo");
}

Como podemos ver en el ejemplo anterior no se declaran variables locales ni se definieron funciones, esto sucede porque recordemos que en Kwok los únicos elementos indispensables son el program nombreDePrograma; y el main( ).
2.2 Declaración de variables globales
La declaración de variables globales debe hacerse seguidamente después del program nombreDePrograma;. Debemos usar la palabra var para definir el inicio de la declaración de variables locales. Seguido debemos indicar el tipo de variable. En Kwok se manejan tres tipos de variables: int, float y char. 

program holaMundo;
var int numero, numero2;
float decimales;
char caracter;
main(){
    print("Hola Mundo");
}

Como podemos ver en el ejemplo anterior Kwok nos permite declarar variables del mismo tipo si las separamos por una “ , ” y variables de diferente tipo si las separamos por un “ ; ”.
2.3 Declaración de funciones
Para declarar funciones en Kwok debemos indicar con la palabra function que se va a declarar una función. Las funciones siguen la siguiente estructura:

function tipo nombreFuncion(tipo nombreParametro1, tipo nombreParametro2){            código de la función}

Para las funciones podemos tener el tipo void, el cual nos indica que la función no retorna ningún valor. En Kwok las funciones pueden tener cualquier cantidad de parámetros siempre y cuando se define el tipo, su nombre y se separe por comas.
2.4 Declaración de variables locales
La declaración de variables locales puede hacerse en cualquier sección del código, ya sea en el main( ) o dentro de alguna función. La estructura es la misma a la de la declaración de variables globales pero omitiendo la palabra var.

2.5 Expresiones
2.5.1 Expresiones Aritméticas
A continuación se presentan las expresiones aritméticas que se pueden usar en Kwok con su respectiva prioridad. Cabe mencionar que la asociatividad en Kwok es de izquierda a derecha y es de suma importancia que los operandos hayan sido declarados previamente a su uso, esto porque no todos los tipos de operandos son compatibles entre sí.

Operadores de mayor a menor precedencia
( )   *   /   +   -   ==    <     >     >=    <=    !=   =     &&     ||

2.5.2 Read
Para la lectura de variables debemos usar la palabra read antes de la variable a usar. Recuerda declarar la variable a usar previamente a su uso y de ingresar valores que coincidan con el tipo de dato que se declaró la variable.

read variable;
2.5.3 Print
Para desplegar valores en consola debemos usar la palabra print seguido de lo que se desee imprimir entre paréntesis. En Kwok podemos imprimir variables, constantes o strings dentro de comillas. De igual manera podemos imprimir varios elementos seguidos separándolos por “ , “.

print(“Esto es un ejemplo de print”);
2.6 Llamadas a funciones
Las llamadas a funciones tienen una estructura sencilla, debemos colocar el nombre de la función que queremos mandar a llamar y dentro de paréntesis mandar los parámetros que queremos que la función use. Debemos tener en cuenta que los tipos de datos de las funciones y la cantidad de los parámetros tienen mucha importancia, ya que si la función está declarada con dos parámetros enteros y al mandarla a llamar le mandamos uno entero y uno flotante se producirá un error.

nombreDeFuncion(parámetro)
2.7 Condicionales
Para el manejo de condicionales en Kwok se implementa un estatuto If, el cuál lleva la siguiente forma:

if(condición){
	código si la condición es verdadera
}

Es importante que la condición sea una expresión cuyo resultado sea de tipo booleano, ya que de no ser así se marcará un error. En Kwok se manejan igual condicionales if-else, en donde si la expresión es Verdadera se ejecuta el fragmento de código que esté antes del else, si la condición es falsa solo se ejecuta el fragmento de código ubicado en el else. Veamos un ejemplo de implemente todo lo que hemos visto hasta ahora:

program holaMundo;
var int a;
function void suma(int a, int b){
	print(“La suma es: “, a+b);
}
main(){
    int b;
    read b;
    if(b > 9){
      a = 8;
      suma(a,b)
 }
    print("Hasta Luego!");
}

En el código anterior se va a leer la variable b por consola (lo que el usuario desee darle de valor) y si es mayor que 9 entrará en el if mandando a llamar a la función suma, pero si b es menor que 9 no entrará al if.
2.8 Ciclos
Los ciclos se manejan con el estatuto cíclico while, este recibe contiene la misma estructura que un if sin else con la diferencia de que se va a estar ejecutando el código que se encuentra dentro del while de manera cíclica hasta que la expresión se deje de cumplir. 

program holaMundo;
var int a;
function void suma(int a, int b){
	print(“La suma es: “, a+b);
}
main(){
    int b;
   b = 10;
    while(b > 9){
      read b;
      suma(a,b)
 }
    print("Hasta Luego!");
}

El código anterior va a estar ejecutando lo que está dentro del while siempre y cuando la variable b siga siendo mayor a 9.

2.9 Funciones especiales
2.9.1 Plot 
Kwok maneja la función Plot que genera una gráfica lineal dado una variable, para poder graficar lo único que debemos hacer es usar la palabra plot seguido de la variable a graficar.

plot(calificaciones);
2.9.2 Distribución Normal
Kwok permite obtener la distribución normal dados los parámetros n, p y size. Para usarla solo se debe usar normal seguido de los tres valores a usar para dichos parámetros.

normal(9, 0.1, 20000);

2.9.3 Distribución Poisson
Kwok permite obtener la distribución poisson dados los parámetros lambda y size. Para usarla solo se debe usar poisson seguido de los dos valores a usar para dichos parámetros.

poisson(5, 1000);
2.9.4 Distribución Binomial
Kwok de igual forma permite obtener la distribución binomial dado los parámetros n, p y size. Para usarla solo se debe usar binomial seguido de los tres valores a usar para dichos parámetros.

binomial(9, 0.1, 20000);

2.9.5 Distribución Uniforme
Y la última distribución que Kwok nos permite obtener es la distribución uniforme con los parámetros low, high y size. Para usarla solo se debe usar uniforme seguido de los tres valores a usar para dichos parámetros.

uniforme(-1, 0, 1000);
