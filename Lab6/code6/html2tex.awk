BEGIN {print "\\documentclass[11pt]{book}";print "\\usepackage{graphicx}";print "\\begin{document}"}
{

if ($0 ~/\<img/) {match($0,/\/.*\</,arr);split(arr[0],a,"\"")
print "\\begin{figure}"
print "\\begin{centering}"

print "\\includegraphics{5_sample_html_files"a[1]"}"
print "\\end{centering}"
print "\\end{figure}"
print " \\clearpage"
print ""
}

}

END {print "\\end{document}"}
