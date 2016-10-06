<?php

$servername = "db-iwantix2";
$username = "iwantix2";
$password = "iwantix22";
$dbname = "iwantix2";

$conn = new mysqli($servername, $username, $password,$dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

# Get POST Request..
$secret_key = $_POST['secret_key'];

$sql = "SELECT * from secret_key where secretkey = '$secret_key'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
    	echo 'Nice! You can generate as many tickets as you want now!!<br />';
    	echo "Here's your flag! You're most welcome.<br />";
    	echo "GCTF{7unn3l_4nd_1nj3c7}";
    }
} else {
    echo "Hahahahaha! No! You cannot generate ticket!";
}


?>


