BEGIN {FS="@"}
{print "new record:"; print $0,"::"; for (i=1; i<=NF; i++) print $i}

#field separator is reset to @
# in print $0 we get the whole record printed, and newline is also a part of
#text that matched !
# the records are not being split on newline now
