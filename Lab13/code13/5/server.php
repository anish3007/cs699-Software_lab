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

		function searchPhone($name){
			$file=fopen("directory.txt", "r");
			$list=fgetcsv($file);
			while (!feof($file)) {
				if ($list[0]==$name) {
					fclose($file);
					return $list[1];
				}
				$list=fgetcsv($file);
			}
			fclose($file);
			return -1;
		}

		function searchName($phone){
			$file=fopen("directory.txt", "r");
			$list=fgetcsv($file);
			while (!feof($file)) {
				if ($list[1]==$phone) {
					fclose($file);
					return $list[0];
				}
				$list=fgetcsv($file);
			}
			fclose($file);
			return -1;
		}

		$namereg="/^[a-zA-Z]+(\s[a-zA-Z]+)*$/";
		$phonereg="/^\+?[0-9]+$/";
		$val= $_POST["search"];

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
				$phone = searchPhone($name);
				if ($phone==-1){
					echo "<b>Search Result</b>: Phone Number not found in the directory";
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
				$name = searchName($phone);
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
	</div>

	<br>
	&nbsp&nbsp<input type="button" value ="Main Page" onclick="window.location.href='client.html';"/>
	<br>
	<br>
	The server side script is on: 
	<?php
	$name =gethostname();
	print_r($name);
	?>


</body>
</html> 
