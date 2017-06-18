<html>
<title>
	Phone Directory Search
</title>
<style>
div{
	word-wrap:normal;
	width: 500px;
}
</style>
<body>
	<h1>Search Result</h1>
	<div>
	<form action="dump.php" method="post">	
	<?php
		ini_set('display_errors', 1);
		ini_set('display_startup_errors', 1);
		error_reporting(-1);


		function searchPhone($connect, $name){
			$query='SELECT phone_no from `153059003` where name ="'.$name.'"';
			$result= $connect->query($query);
			if($result->num_rows >0){
				$rowarr = $result->fetch_row();
				$phone=$rowarr[0];
				return $phone;
			}
			else
				return -1;
		}

		function searchName($connect, $phone){
			$query='SELECT name from `153059003` where phone_no ="'.$phone.'"';
			$result= $connect->query($query);
			if($result->num_rows >0){
				$rowarr = $result->fetch_row();
				$name=$rowarr[0];
				return $name;
			}
			else
				return -1;
		}

		$namereg="/^[a-zA-Z]+(\s[a-zA-Z]+)*$/";
		$phonereg="/^\+?[0-9]+$/";
		$val= $_POST["search"];

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

		if($val =="name"){
			$name = $_POST["nameval"];
			//echo $name;
			$nameflag=FALSE;
			if ($name == ''){
				echo "<b>Incorrect:</b> Name field blank, please provide the name.<br><br>";
				$nameflag=TRUE;
			}
			elseif (!preg_match_all($namereg, $name)){
				echo "<b>Incorrect:</b> Name should only contain alphabets separated by single space.<br><br>";
				$nameflag=TRUE;
			}

			if ($nameflag){
				echo '<br><br>&nbsp&nbsp<input type="button" value="Go Back" onclick="history.go(-1);">';
			}
			else{
				$phone = searchPhone($connect, $name);
				if ($phone==-1){
					echo "<b>Search Result</b>: Phone not found in the directory";
				}
				else{
					echo "<b>Search Result</b>:<br> Name-".$name."<br> Phone-".$phone;
				}
			}
		}
		elseif ($val == "phone") {
			$phone = $_POST["phoneval"];
			//echo $phone;
			$phoneflag=FALSE;
			if ($phone == ''){
				echo "<b>Incorrect:</b> Phone field blank, please provide the phone number.<br><br>";
				$phoneflag=TRUE;
			}
			elseif (!preg_match_all($phonereg, $phone)){
				echo "<b>Incorrect:</b> Phone field can contain single '+' followed by any no. of numerals.<br><br>";
				$phoneflag=TRUE;
			}

			if ($phoneflag){
				echo '<br><br>&nbsp&nbsp<input type="button" value="Go Back" onclick="history.go(-1);">';
			}
			else{
				$name = searchName($connect, $phone);
				if ($name==-1) {
					echo "<b>Search Result</b>: Name not found in the directory";
				}
				else{
					echo "<b>Search Result</b>:<br> Phone-".$phone."<br> Name-".$name;
				}		
			}
			
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
