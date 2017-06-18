

BEGIN{print "\\documentclass[11pt]{book}\n\\begin{document}\n\\frontmatter\n";RS="\n"}

{if ($0 ~/^CHAPTER I\./)
{gsub(/^CHAPTER I\.\s/, "\\tableofcontents\n\\mainmatter\n\\chapter{"); gsub(/\r$/,"}");print $0}

else if ($0 ~/^CHAPTER.*\./) 
{gsub(/^CHAPTER.*\.\s/,"\\chapter{") ;gsub(/\r$/ ,"}") ;print $0} 

else 
{sub("_I_","\\_I\\_");gsub("\\$5,000","\\$5,000");gsub("\\$1","\\$1");gsub("20%","20\\%");sub("#","\\#");printf "%s",$0}}

END {print "\\end{document}"}
