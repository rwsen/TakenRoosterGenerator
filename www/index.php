<!DOCTYPE html>
<html>
<head>
<title>Roosterpagina Gang3.4</title>
</head>
<body>


<!--
<?php
$servername = "localhost";
$username = "root";
$password = "wortel";
$dbname = "test";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$weekNumber = date("W");
$yearNumber = date("o");
$sql = "SELECT taakID, personID FROM rooster WHERE weeknummer={$weekNumber} AND jaarnummer={$yearNumber}";
echo $sql
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["taakID"]. " - Name: " . $row["personID"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
-->

<?php echo '<p>Hello World</p>'; ?> 




</body>
</html> 