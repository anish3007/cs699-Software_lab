{ if ($2>30) myarr[$1]=$2;}
END	{for (key in myarr) print key ":" myarr[key]}
