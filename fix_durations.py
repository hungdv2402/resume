import re

with open('/Users/hung.duongviet/Documents/MyDocs/resume/Duong-Viet-Hung-RN.tex', 'r') as f:
    content = f.read()

# We only want to modify lines inside the Projects section
projects_start = content.find('\\section{Projects}')
projects_end = content.find('\\resumeSubHeadingListEnd', projects_start)

projects_content = content[projects_start:projects_end]

# For each project title line (starts with \textbf{...} and ends with \\), append " & \footnotesize\textit{4 months}"
# Skip if it already has "months" or "&"
def add_duration(match):
    line = match.group(0)
    if "&" in line or "months" in line:
        return line
    # Replace the trailing \\ with & \footnotesize\textit{4 months} \\
    return re.sub(r'\s*\\\\$', ' & \\\\footnotesize\\\\textit{4 months} \\\\\\\\', line)

# Match lines that have \textbf{ inside the tabular environment
new_projects_content = re.sub(r'^[ \t]*\\textbf\{.*\\\\$', add_duration, projects_content, flags=re.MULTILINE)

new_content = content[:projects_start] + new_projects_content + content[projects_end:]

with open('/Users/hung.duongviet/Documents/MyDocs/resume/Duong-Viet-Hung-RN.tex', 'w') as f:
    f.write(new_content)

print("Done")
