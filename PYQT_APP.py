# """ SIMPLE FILE DOWNLOADER APPLICATION"""

from PyQt4 QtCore import*
from PyQt4 QtGui import*
import sys
import urllib.request

class Downloader(QDialog):

    def __init__(self):
        QDialog.__init__(self)
         layout = QVBOXLayout()

         self.url = QLineEdit()
         self.save_location = QLineEdit()
         self.progress = QProgressBar()
         download = QPushButton("Download")
         browse= QpushButton("Browse")

         url.setPlaceholderText("URL")
         save_location.setPlaceholderText("File save location")

         progress.setvalue(0)
         progress.SetAlighment(Qt.AlignHcenter)

         layout.addWidget(self.url)
         layout.addWidget(self.save_location)
         layout.addWidget(self.browse)
         layout.addWidget(self.progress)
         layout.addWidget(download)

         self.SetLayout(layout)

         self.SertWindowTitle("PyDownloader")
         self.SetFocus()

         download.Clicked.connect(self.download)
         browse.Clicked.connect(self.browse_file)

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self,caption="save File as",directory='.'
                                                Filter="All Files(*.*)")
        self.save_location.SetText(QDir.toNativeSeparators(save_file))
        

    def download(self):
        url = self.url.text()
        save_location=self.save_location.text()
        try:
            urllib.request.urlretrieve(url,save_location,self.report)
        except Exception:
            QMessageBox.Warning(self,"warning","Failed")
            return
        QMessageBox.information(self,"information","The download is complete")
        self.url.SetText("")
        self.progress.SetValue(0)
        self.save_location.SetText("")

    def report(self,blocknum,blocksize,totalsize):
        readsofar=blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100/totalsize
            self.progress.SetValue(int(percent))
    
