#!/bin/awk

BEGIN	{  }

	{
			printf "%c%c\n", 0x0938, 0x094B
			gsub(/\baa/, "आ");
			gsub(/\ba/, "अ");
			gsub(/b/, "ब");
	}

END	{
	}
