{i=i+1; myarr[i]=$SORTKEY; myarr2[$SORTKEY]=$0}
END{n=asort(myarr);
for (i=1; i<=n;i++) {ind = myarr[i]; print myarr2[ind]}}
