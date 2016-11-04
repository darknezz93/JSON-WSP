from ladon.ladonizer import ladonize
from ladon.types.attachment import attachment
from os.path import dirname, abspath, join
import os

upload_dir = join(dirname(abspath(__file__)), 'clipboard')

class ClipboardService(object):
    @ladonize(attachment, rtype=bool)
    def upload(self, attachment):
        global upload_dir
        if not os.path.exists(upload_dir):
            os.mkdir(upload_dir)

        f = open(join(upload_dir, "currentImage.jpg"), 'wb')
        f.write(attachment.read())
        f.close()
        return True

    @ladonize(rtype=attachment)
    def download(self):
        global upload_dir
        return attachment(open(join(upload_dir, "currentImage.jpg"), 'rb'))