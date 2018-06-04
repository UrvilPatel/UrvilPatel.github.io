<?php
	$con=mysqli_connect("localhost","root","","login");
	

	if($_SERVER['REQUEST_METHOD']=='POST')
	{
		if($_POST["Password"]==$_POST["ConfirmPassword"])
		{
			$user=$_POST["Username"];
			$u11=$_POST["Email"];
			$p11=$_POST["Password"];

			$result=mysqli_query($con,"INSERT INTO user VALUES('','$u11','$p11')");

			echo "Mr/Mrs. ".$user."<br>You are Successfully Registered<br>";
			echo '<a href="index.html">Home</a> | <a href="login.html">Login</a>';

		}
		else
		{
			echo "Invalid Input or Invalid Password";
		}

	}
?>