LATEX = """ 
\\documentclass[12pt]{{article}}
\\setlength{{\\textwidth}}{{16.5cm}}
\\setlength{{\\textheight}}{{22.2cm}}
\\setlength{{\\hoffset}}{{-.25in}}
\\setlength{{\\voffset}}{{-.9in}}

\\usepackage{{fancyhdr, graphicx}}
\\renewcommand{{\\headrulewidth}}{{0pt}}
\\fancyhead[L]{{}}
\\fancyhead[R]{{
\\includegraphics[width=4cm]{{/home/ubuntu/webapp/logo.png}}
}}

\\pagestyle{{plain}}
\\date{{}}
\\pagenumbering{{gobble}}

\\fancyfoot[R]{{\\today}}

\\usepackage[dvipsnames]{{xcolor}}
\\definecolor{{InsBlue}}{{HTML}}{{0079c2}}
\\color{{InsBlue}}

\\usepackage{{hyperref}}
\\hypersetup{{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,
}}
 
\\urlstyle{{same}}

\\begin{{document}}
\\thispagestyle{{fancy}}

The following are the prerequisites on your end before we can integrate and hand over the external service environment for your testing

\\section{{SSL}}
We will need your authorization to add the domains to one of our service SSL certificates and it can be done by adding a special DNS TXT record that has the following key-value

\\end{{document}}
"""
