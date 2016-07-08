import cherrypy
import cherrytemplate
import os
from tempfile import gettempdir
TMP_DIR = gettempdir()



class PythonRunner(object):
    title="Rodando codigos pela net"
    
    def header(self):
        return '''
               <html>
               <head>
                 <title>%s</title>
               </head>
               <body>
               <h2>%s</h2>
               '''%(self.title,self.title)
    
    def footer(self):
        return ''' 
                </body></html>
               '''      
    
    @cherrypy.expose()
    def index(self,code=None):
       output=''
       if code is None:
           output=''
       else:
           tmp_filename = os.path.join(TMP_DIR, 'myfile.dat')
           f = open(tmp_filename, 'w')
           f.write(code)
           f.close()
           f_in, f_out = os.popen4("python %s"%tmp_filename)
           output = "O codigo eh:"
           output += "<pre><font color='blue'>%s</font></pre>resultando: "%code
           output += "<pre><font color='green'>"
           for line in f_out.readlines():
             output += line
           output += "</font></pre>"     
       return self.header()+'''
            Digite seu codigo.
           <form action="index" method="GET">
           <textarea name="code" rows=5 cols=80></textarea><br/>
           <input type="submit" value="Execute em Python"/>
           </form>
           <br/>
           %s
           ''' % output + self.footer()                        
if __name__=="__main__":   
 cherrypy.quickstart(PythonRunner())                                      
                             