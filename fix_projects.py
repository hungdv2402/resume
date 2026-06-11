import re

with open('/Users/hung.duongviet/Documents/MyDocs/resume/sourabh_bajaj_resume.tex', 'r') as f:
    content = f.read()

# We want to replace:
# Technologies: [some text].
# \end{tabular*}\vspace{-4pt}
#
# with:
# \multicolumn{2}{p{0.97\textwidth}}{Technologies: [some text].} \\
# \noalign{\vspace{3pt}\color[gray]{0.8}\hrule height 0.4pt\normalcolor\vspace{3pt}}
# \end{tabular*}\vspace{-4pt}

def replacer(match):
    tech_line = match.group(1).strip()
    return f"\\multicolumn{{2}}{{p{{0.97\\textwidth}}}}{{{tech_line}}} \\\\\n        \\noalign{{\\vspace{{3pt}}\\color[gray]{{0.8}}\\hrule height 0.4pt\\normalcolor\\vspace{{3pt}}}}\n      \\end{{tabular*}}\\vspace{{-4pt}}"

# Regex to match the Technologies line and the \end{tabular*} that follows it
# Need to make sure we don't double-replace the one that already has \multicolumn
new_content = re.sub(r'([ \t]*Technologies:[^\n]+)\n[ \t]*\\end\{tabular\*}\\vspace\{-4pt\}', replacer, content)

with open('/Users/hung.duongviet/Documents/MyDocs/resume/sourabh_bajaj_resume.tex', 'w') as f:
    f.write(new_content)

print("Done")
