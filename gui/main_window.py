from PySide2.QtCore import Slot
from PySide2.QtWidgets import QMainWindow
from . import Ui_Form


class MainWindow(QMainWindow,Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    @Slot(int)
    def set_label(self,label :int):
        self.image_label.setText(str(label))