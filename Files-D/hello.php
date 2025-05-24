// small chapter 1 code for PHP

<?php
echo "Hello, World!<br>";

// Variables
$name = "John";
$age = 30;
echo "My name is $name and I am $age years old.<br>";

// Arrays
$fruits = array("Apple", "Banana", "Cherry");
echo "My favorite fruits are: " . implode(", ", $fruits) . ".<br>";

// Associative Arrays
$person = array("name" => "Alice", "age" => 25);
echo "Person's name is " . $person['name'] . " and age is " . $person['age'] . ".<br>";

// Loops
for ($i = 0; $i < count($fruits); $i++) {
    echo "Fruit $i: " . $fruits[$i] . "<br>";
}

// Functions
function greet($name) {
    return "Hello, $name!";
}