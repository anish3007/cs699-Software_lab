BEGIN{print "\\documentclass[11pt]{article}\n\\begin{document}\n\\tableofcontents"}
#($0 !~/\\section /||/\\subsection /) {print $0} 

{if ($0 ~ /^[0-9].[0-9]\./) 
{gsub(/^[0-9].[0-9].[0-9]\s/,"\\subsubsection{"); printf( "%s}\n", $0)} 

else if ($0 ~ /^[0-9].*/) 
{gsub(/^[0-9].[0-9]\s/,"\\subsection{");printf( "%s}\n", $0)} 

else if ($0 ~/^Chapter.*\./)
{gsub(/^Chapter.*\.\s/,"\\section{") ;gsub(/\r$/ ,"") ;printf( "%s}\n", $0)}

else
{gsub("\\$0","\\$0"); printf("%s\n",$0)}}

END {print "\\end{document}"}

