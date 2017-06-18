BEGIN {print "\\documentclass{article}\n"
 
 print "\\title{Sections and Chapters} \n"
 print "\\author{Anish Kumar Mishra}  \n"
 print "\\date{\\today} \n"
 print "\\begin{document} \n"
 
 print "\\maketitle  \n " 
  }
 
{  print $0; }

END { print "\\end{document}"}
