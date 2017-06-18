#nf is no of fields
#FNR is no of records per file
#NR  is total no of records, try with multiple files
/R/	{for (i=0; i<NF; i++) {print i ":" $i}; print "**" }
