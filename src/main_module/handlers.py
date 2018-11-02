import logging
import tornado
from main_module.main import LOGGER_MODULE_NAME

class MainHandler(tornado.web.RequestHandler):
    """ 暂时用于测试上传图片 """

    def get(self):
        logger = logging.getLogger(LOGGER_MODULE_NAME)
        logger.info("get Main request!!!")
        self.write('''
                    <html>
                      <head><title>Upload File</title></head>
                      <body>
                        <form action='kousuan' enctype="multipart/form-data" method='post' target="sub_iframe">
                        <input type='file' name='uploadfile'/><br/>
                        <input type='submit' value='submit'/>
                        </form>

                        <iframe name="sub_iframe"></iframe>
                      </body>
                    </html>
                    ''')