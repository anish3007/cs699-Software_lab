<html>
<style>
div{
	word-wrap:normal;
	width: 500px;
}
</style>
<body>
<p1>Information Entered:</p1><br><br>
<div>
<?php
	ini_set('display_errors', 1);
	ini_set('display_startup_errors', 1);
	error_reporting(-1);
	$namereg="/^[a-zA-Z]+(\s[a-zA-Z]+)*$/";
	$agereg="/^-?[0-9]+(\.[0-9]*)?$/";
	$rollreg="/^[a-zA-Z]{2}15[0-9]{4}$/";
	$name= $_POST["name"];
	$age=$_POST["age"];
	$roll=$_POST["roll"];
	$nameflag=FALSE;
	$ageflag=FALSE;
	$rollflag=FALSE;
	//echo "$name";
	//echo "$namereg"
	if ($name == ''){
		echo "Incorrect: Name field blank, please provide the name.<br>";
		$nameflag=TRUE;
	}
	elseif (!preg_match_all($namereg, $name)){
		//echo "Inside if";
		echo "Incorrect: Name should only contain alphabets separated by single space.<br>";
		$nameflag=TRUE;
	}
	else {
		//echo "Inside else";
		echo "Name: "."$name"."<br>";
	}

	if ($age == ''){
		echo "Incorrect: Age field blank, please provide the age.<br>";
		$ageflag=TRUE;
	}
	elseif (!preg_match_all($agereg, $age)){
		//echo "Inside if";
		echo "Incorrect: Age field cannot contain non-numerals.<br>";
		$ageflag=TRUE;
	}
	elseif ($age<=0) {
		echo "Incorrect: Age provided cannot be less than 0.<br>";
		$ageflag=TRUE;
	}
	else {
		//echo "Inside else";
		echo "Age: "."$age"."<br>";
	}

	if ($roll == ''){
		echo "Incorrect: Roll No. field blank, please provide the roll number.<br>";
		$rollflag=TRUE;
	}
	elseif (!preg_match_all($rollreg, $roll)){
		//echo "Inside if";
		echo "Incorrect: Roll No. should be in the format 'AA15NNNN'.{A=Alphabets, N=Numerals}<br>";
		$rollflag=TRUE;
	}
	else {
		//echo "Inside else";
		echo "Roll: "."$roll"."<br>";
	}
	if ($nameflag||$ageflag||$rollflag){
		echo '<br><br>&nbsp&nbsp<input type="button" value="Go Back" onclick="history.go(-1);">';
	}
	else{
		
	}
?>
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
