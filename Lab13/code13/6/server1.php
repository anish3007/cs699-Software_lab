<html>
<title>
	Form Validation
</title>
<style>
div{
	word-wrap:normal;
	width: 500px;
}
</style>
<body>
	<h1>Form Validation</h1>
	<div>
	<form action="dump.php" method="post">
	<?php
		ini_set('display_errors', 1);
		ini_set('display_startup_errors', 1);
		error_reporting(-1);

		$namereg="/^[a-zA-Z]+(\s[a-zA-Z]+)*$/";
		$phonereg="/^\+?[0-9]+$/";
	
		$name= $_POST["name"];
		$phone=$_POST["phone"];

		$nameflag=FALSE;
		$phoneflag=FALSE;
		//echo "$name";
		//echo "$namereg"
		if ($name == ''){
			echo "<b>Incorrect:</b> Name field blank, please provide the name.<br><br>";
			$nameflag=TRUE;
		}
		elseif (!preg_match_all($namereg, $name)){
			//echo "Inside if";
			echo "<b>Incorrect:</b> Name should only contain alphabets separated by single space.<br><br>";
			$nameflag=TRUE;
		}

		if ($phone == ''){
			echo "<b>Incorrect:</b> Phone Number field blank, please provide the phone number.<br><br>";
			$phoneflag=TRUE;
		}
		elseif (!preg_match_all($phonereg, $phone)){
			//echo "Inside if";
			echo "<b>Incorrect:</b> Phone field can contain single'+' followed by any no. of numerals.<br><br>";
			$phoneflag=TRUE;
		}

		if ($nameflag||$phoneflag){
			echo '<br><br>&nbsp&nbsp<input type="button" value="Go Back" onclick="history.go(-1);">';
		}
		else{
			echo 'Form found to be correct. The options entered are:<br><br>';
			echo "Name: "."$name"."<br><br>";
			echo "Phone: "."$phone"."<br><br>";
			$file= fopen("dbdetails.txt","r") or die("\"dbdetails.txt\" file not found");
			$count=1;	
			$server="";
			$uname="";
			$pass="";
			$dbname="";
			while(!feof($file)){
				$filestr =fgets($file);
				$filearr=explode(':', $filestr);
				//print_r(explode(':', $filestr));
				switch ($count) {
					case '1':
						$server=$filearr[1];
						break;
					case '2':
						$uname=$filearr[1];
						break;
					case '3':
						$pass=$filearr[1];
						break;
					case '4':
						$dbname=$filearr[1];
						break;
				}
				$count++;
			}
			//echo $server.$uname.$pass.$dbname;
			$uname = rtrim($uname);
			$pass = rtrim($pass);
			$dbname = rtrim($dbname);	
			//Create Connection
			$connect= new mysqli($server, $uname, $pass, $dbname);

			//Check Connection
			if ($connect->connect_error) {
				die("Connection failed:".$connect->connect_error);
			}

			echo "Connected to database succesfully <br><br>";
			$stmt=$connect->prepare("INSERT INTO `153059003`(name, phone_no) values (?,?)");
			$stmt->bind_param("ss",$username, $userphone);

			$username = $name;
			$userphone = $phone;
			$stmt->execute();
	
			fclose($file);
			$stmt->close();
			$connect->close();
			echo "Information Saved.";

		}
	?>
		<input type="submit" value="View Directory"\>
	</form>
		<input type="button" value ="Main Page" onclick="window.location.href='client.html';"/>
	</div>
	<br>
	<br>
	The server side script is on: 
	<?php
	$name =gethostname();
	print_r($name);
	?>


</body>
</html> 
