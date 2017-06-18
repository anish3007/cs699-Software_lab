<html>
<title>
	Complete Phone Directory
</title>
<style>
body{
	background-color: skyblue;
}
table{
	border-spacing: 20px;
	border-collapse: collapse;
	width:100%;
}
table,th,td{
	border: 1px solid blue;
}
th{
	height: 50px;
	text-align: left;
	padding: 5px;
	background-color: blue;
}
td{
	height: 30px;
	vertical-align: bottom;
	padding:5px;
}
div{
	word-wrap:normal;
	width: 500px;
}
</style>
<body>
	<h1>Complete Phone Directory</h1>
	<div>
	<?php
		ini_set('display_errors', 1);
		ini_set('display_startup_errors', 1);
		error_reporting(-1);

		//	echo "Inside dump<br>";
		$file=fopen("directory.txt","r");
		$table="<table>";
		$table.="<th>Name</th><th>Phone</th>";
		$list=fgetcsv($file);
		while (! feof($file)) {
			$table.="<tr><td>".$list[0]."</td><td>".$list[1]."</td></tr>";
			$list=fgetcsv($file);
		}
		$table.="</table>";
		echo $table;	
		fclose($file);
		echo '<br><br>&nbsp&nbsp<input type="button" value="Go Back" onclick="history.go(-1);">';

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
