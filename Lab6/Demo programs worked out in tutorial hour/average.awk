BEGIN {sum1=0; sum2=0; sum3=0; c1=0; c2=0; c3=0}
{sum1=sum1+$2; c1+=1}
{sum2=sum2+$3; c2+=1}
{sum3=sum3+$4; c3+=1}
END {print sum1/c1 "\t"  sum2/c2 "\t" sum3/c3}

