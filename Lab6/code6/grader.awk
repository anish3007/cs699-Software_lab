

BEGIN{
	FS = ";";	
	print "roll no \t total \t grade";
	count=0;
	sum=0;
}

NR>1{
	q1=$2 *(10 / 20);	
	q2=$3*10/20;	
	mid=$4*15/50;
	end=$5*50/100;
	proj=$6*15/15;
		
		total[$1] = q1+q2+mid+end+proj;
        actualTotal[$1] = $2+$3+$4+$5+$6;       
        avg[$1]=total[$1]/100*100;

        if(avg[$1]>90 && avg[$1]<=100)
        	grade[$1]="AA";
        else if(avg[$1]>81 && avg[$1]<=90)
        	grade[$1]="AB";
        else if(avg[$1]>71 && avg[$1]<=80)
        	grade[$1]="BB";	
        else if(avg[$1]>61 && avg[$1]<=70)
        	grade[$1]="BC";
        else if(avg[$1]>51 && avg[$1]<=60)
        	grade[$1]="CC";
        else if(avg[$1]>41 && avg[$1]<=50)
        	grade[$1]="CD";
        else
        	grade[$1]="DD";
    count++;

    print $1 " \t " avg[$1] " \t"grade[$1];
    } 

END{	

	#Calculating Averages
	for (student in total) {           
            sum+=avg[student];
        }
    totalAvg=sum/count;
    totalGrade
    if(totalAvg>90 && totalAvg<=100)
        	totalGrade="AA";
        else if(totalAvg>81 && totalAvg<=90)
        	totalGrade="AB";
        else if(totalAvg>71 && totalAvg<=80)
        	totalGrade="BB";	
        else if(totalAvg>61 && totalAvg<=70)
        	totalGrade="BC";
        else if(totalAvg>51 && totalAvg<=60)
        	totalGrade="CC";
        else if(totalAvg>41 && totalAvg<=50)
        	totalGrade="CD";
        else
        	totalGrade="DD";


    print "Averages \t " totalAvg " \t "totalGrade;

    #Calculating standanrd deviation

    sum=0;
    for (student in total) {           
            sum+=(totalAvg-avg[student])^2;            
        }

    stdDeviation=sqrt(sum/count);

    print "StdDev \t " stdDeviation;

}
