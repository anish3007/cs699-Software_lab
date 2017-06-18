BEGIN 	{sum=0}
#sum=0   # remove this line to make it work, else this happens on every line
$2==20 {sum=sum+$3; print $0}
END 	{print sum}
