#!/usr/bin/python
'''
A basic bottle app skeleton
'''
import bottle
from bottle import template
from poc import LATEX
import md5,base64,os,tempfile,subprocess
app = application = bottle.Bottle()

@app.route('/static/<filename:path>')
def static(filename):
    return bottle.static_file(filename, root='./static')

@app.route('/')
def show_index():
    return template("form.tpl", message="Please enter this info") 

@app.route('/genpdf', method='POST')
def generate_pdf():
    domain = bottle.request.forms.get('domain')
    cname = 'a001.'+bottle.request.forms.get('cust')+'.inscname.net'
    dig = md5.md5(domain).digest() 
    did = base64.urlsafe_b64encode(dig) 
    texfile = open("/tmp/"+did+'.tex','wb')
    latex = LATEX.format(goo_domain="*.g00."+ domain, tld=domain,cname=cname)
    texfile.write(latex)
    texfile.seek(0)
    texfile.close()
    texfile = os.path.abspath(texfile.name)
    logfd,logname = tempfile.mkstemp()
    outfile=os.fdopen(logfd)
    ret = subprocess.call(['pdflatex',
                '-interaction=nonstopmode',
                '-output-format', 'pdf',
                '-output-directory', "/tmp",
                texfile],
                cwd=os.path.dirname(texfile), stdout=outfile,
                stderr=subprocess.PIPE)

    bottle.response.headers['Content-Type'] = 'application/pdf; charset=UTF-8'
    bottle.response.headers['Content-Disposition'] = 'attachment; filename="' + did + '.pdf'
    return bottle.static_file(did+".pdf", root='/tmp')

@app.route('/page/<page_name>')
def show_page(page_name):
    '''
    Return a page that has been rendered using a template
    '''
    return template('page', page_name=page_name)

if __name__ == '__main__':
    bottle.run(app=app,
        host='0.0.0.0',
        port=8080)
