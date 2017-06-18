#nf is no of fields
#FNR is no of records per file
#NR  is total no of records, try with multiple files
/R/	{print $0; print "\nNF:" NF  "\t" "FNR:" FNR "\t" "NR:" NR}
