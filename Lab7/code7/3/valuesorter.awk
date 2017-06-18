{myarr[$1]=$2}
END{n=asort(myarr);for (i=1; i<=n;i++) print myarr[i]}
