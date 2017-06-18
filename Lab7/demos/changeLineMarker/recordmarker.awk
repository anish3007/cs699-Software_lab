BEGIN {RS="@"}
{print "new record:"; print $0}

#record separator is reset to @
# in print $0 we get the whole record printed, and newline is also a part of
#text that matched !
# the records are not being split on newline now
