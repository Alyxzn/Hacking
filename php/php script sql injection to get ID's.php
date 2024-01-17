<?php
// cabe aclarar que el los parametros username, y password tiene que estar el usuario de la base de datos con los mayores privilegios

$server = "localhost";
$username = "CHANGE THIS";
$password = "CHANGE THIS";
$database = "CHANGE THIS";

// Conexion a la base de datos

$conn = new mysqli($server, $username, $password, $database);

$id = $_GET['id'];

$data = mysqli_query($conn, "select username from users where id = '$id'") or die (mysqli_error($conn));

$response = mysqli_fetch_array($data);

echo $response['username'];

?>
