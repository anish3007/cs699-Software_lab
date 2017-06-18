#run this file as:
#awk -f test.awk -v A=2 -v B=3 data 
BEGIN {print "A:"A " B:" B}
{print A " " B " " $0}

END{print ARGC; for (i=0; i<ARGC;i++) print i ":" ARGV[i]}

#variables are passed each with -v var=val  as parameter as given above
#ARGC and ARGV refer to files and not to variables, which are used directly

