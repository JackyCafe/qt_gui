from PySide2.QtWidgets import QApplication
from gui import MainWindow
from gui import LabelUpdateThread


def main():
    app = QApplication()
    window = MainWindow()
    label_thread = LabelUpdateThread(window)
    window.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()