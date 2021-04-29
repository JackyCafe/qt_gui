from PySide2 import QtWidgets, QtCore


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 800)
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.image_label.setObjectName("image_label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OpenCV"))
        self.image_label.setText(_translate("Form", "TextLabel"))
