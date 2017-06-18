#BEGIN{PROCINFO["sorted_in"] = "@ind_str_asc"}

{myarr[$1]=$2}
END{n=asorti(myarr);for (i=1; i<=n;i++) print myarr[i]}
