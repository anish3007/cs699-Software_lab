<html>
<style>
div{
	word-wrap:normal;
	width: 300px;
}
</style>
<body>
<p1>The full address entered is:</p1><br><br>
<div>
<?php echo $_POST["addline1"].", ".$_POST["addline2"].", ".$_POST["city"].", ".$_POST["state"].", ".$_POST["pin"]; ?>
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
