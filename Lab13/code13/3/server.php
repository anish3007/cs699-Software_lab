<html>
<style>
div{
	word-wrap:normal;
	width: 500px;
}
</style>
<body>
<h1>Gate Examination: City Select Form</h1> 	
<h3>Enter City choices:</h3>
<form action="choices.php" method="post">
	<?php
		ini_set('display_errors', 1);
		ini_set('display_startup_errors', 1);
		error_reporting(-1);
		echo "<table>";

		$cities=file("cities.txt");
		$cellcount=0;
		$row="";
		for($i=1;$i<=3;$i++){
			$row .="<tr>";
			$col="";
			for($j=1;$j<=3;$j++){
				$col.="<td> Choice ".++$cellcount.":";
				$options= '<option value="Not Chosen">--Not Chosen--</option>';
				foreach($cities as $city){
					if(strlen($city)>1){
					//echo $city;
					$options .='<option value="'.$city.'">'.$city.'</option>';
					}	
				}
				$select='<select name="city'.$cellcount.'">'.$options.'</select>';
				$col.=$select."</td>";
			}
			$row.=$col."</tr>";	
		}
		echo $row;	
		echo "</table>";
	?>
	<br><br>
	&nbsp&nbsp<input type="submit" value="Submit Choices" />
</form>
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
