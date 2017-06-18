<html>
<style>
div{
	word-wrap:normal;
	width: 500px;
}
</style>
<body>
<h1>Gate Examination: City Validation</h1> 	

<h3>Validating choices entered</h3>

<?php
	ini_set('display_errors', 1);
	ini_set('display_startup_errors', 1);
	error_reporting(-1);

	/*foreach ($_POST as $key=>$value){
		echo $key ."=>". $value."<br>";
	}*/
	function isNOTChosen($city_val){
		if($city_val == "Not Chosen"){
			return TRUE;
		}
		else{
			return FALSE;
		}

	}
	function isDuplicate($city_val, $i){
		for($j=1; $j<=9;$j++){
			if($j!=$i){
				if($_POST["city".$j]==$city_val){
					return TRUE;
				}
			}
		}
		return FALSE;
	}
	$errflag=FALSE;
	for ($i=1;$i<=9;$i++){
		$city_val=$_POST["city".$i];
		//echo $city_val." ";
		if(isNotChosen($city_val)){
			$errflag=TRUE;
			echo "Choice ".$i." not provided. Please provide the same<br>";
			break;
		}
	}

	if(!$errflag){
		for ($i=1;$i<=9;$i++){
			$city_val=$_POST["city".$i];
			if(isDuplicate($city_val,$i)){
				$errflag=TRUE;
				echo "Choice ".$i." is not unique. You have provided duplicate cities. Please change your choices<br>";
				break;
			}
		}
	}
	if($errflag){
		echo '<br><br>&nbsp&nbsp<input type="button" value="Go Back" onclick="history.go(-1);">';
	}
	else{
		echo 'Cities provided is found to be correct. The options entered are:<br><br>';
		$count=1;
		foreach ($_POST as $key=>$value){
		echo "City".$count++." : ". $value."<br>";
		}
	}


?>
<br>
<br>
&nbsp&nbsp<input type="button" value ="Main Page" onclick="window.location.href='client.html';"/>
<br>
<br>
<p1>The server side script is on:</p1> 
<?php
$name =gethostname();
print_r($name);
?>
</footer>

</body>
</html> 
