<?php

// Declaración de variables
$numero = 10;
$texto = "Hola mundo";
$verdadero = true;
$falso = false;

// Declaración de una función
function saludar($nombre) {
    echo "¡Hola, $nombre!";
}

// Llamada a la función
saludar("Juan");

// Estructura condicional
if ($numero > 5) {
    echo "El número es mayor que 5";
} else {
    echo "El número es menor o igual que 5";
}

// Bucle while
$i = 0;
while ($i < 5) {
    echo $i;
    $i++;
}

?>