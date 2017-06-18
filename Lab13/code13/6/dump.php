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
	color:white;
}
td{
	height: 30px;
	vertical-align: bottom;
	padding:5px;
}

tr.d0 td{
	background-color: white;
}
tr.d1 td{
	background-color: lightgrey;
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

		//	echo "Inside dump<br>";
	//	$file=fopen("directory.txt","r");
		$query='SELECT name, phone_no from `153059003`';
		$result= $connect->query($query);

		$table="<table>";
		$table.="<th>Name</th><th>Phone</th>";
	//	$list=fgetcsv($file);
		$list = $result->fetch_row();
		$i=0;

		while ($list!=NULL) {
			$table.="<tr class=\"d".($i&1)."\"><td>".$list[0]."</td><td>".$list[1]."</td></tr>";
			$list = $result->fetch_row();
			$i++;
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
