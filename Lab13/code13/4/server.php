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
			$file= fopen("directory.txt","a");
			$list=array();
			$list[0] = $name;
			$list[1] = $phone;
			fputcsv($file, $list);
			fclose($file);
			echo "Information Saved.";
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
