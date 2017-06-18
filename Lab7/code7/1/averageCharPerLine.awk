@include "lib.awk"
BEGIN {count =0 ;line =0}
{
#ARGV[i]
abc = $0;
count = count + myprint(abc)
line++;
}

#END {print int (count/line) }
END {print (count+line)/line }
