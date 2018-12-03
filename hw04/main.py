import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,m,n):
        m = int(m)
        n = int(n) if n is not None else m

        html='''
        <html>
          <body>
            <table>
        '''
        for a in range(1,m+1):
            html += '<TR>'
            for b in range(1,n+1):
                html += '<TD>%d</TD>' % (str(a)+'*'+str(b)+'='+str(a*b))
            html +='</TR>' 

        html+='''
           </table>
          </body>
        </html>
        '''
    self.write(html)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
