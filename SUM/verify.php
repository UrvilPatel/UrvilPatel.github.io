<?php
	//values from .html file
	$u11=$_POST["Email"];
	$p11=$_POST["Password"];

	$con=mysqli_connect("localhost","root","","login");

	$result=mysqli_query($con,"SELECT * FROM user where email='$u11' && password='$p11'");

	$row = mysqli_num_rows($result);

	if ($row==1) 
	{	
		echo "Welcome ".$u11;
	}
	else
	{
		echo "Invalid Input";
	}
	
	/*
		while ($row = $result->fetch_assoc()) 
		{
	    echo $row['pwd']."<br>";
		}
	*/
?>

<!DOCTYPE html>
<html>
<head>
	<title>Successfully Login</title>
</head>
<body>
	<br>
	<a href="index.html">Home</a>
</body>
</html>