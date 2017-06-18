#!/bin/awk

function rev(str)
{
	if (str == "")
		return ""

	return (rev(substr(str, 2)) substr(str, 1, 1))
}

BEGIN	{ 
		RS="[ \t\n]+";
		REVSUB=rev(SUB)
	}


{	
	word=$0;
	revword=rev(word);

	ind1 = match(word, SUB);
	ind2 = match(revword, REVSUB);

	if(ind1==1 || ind2==1)
	{
		print word;
	}
}
