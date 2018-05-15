#Author:Santi
#coding:utf-8
#请使用python2.7.12，pyenv里已安装

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("你好，世界")

settings = {
    'static_path':'static',
    # 'static_url_prefix':'/ppp/',
            }

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/cn", TestHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()