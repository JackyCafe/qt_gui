from PySide2.QtCore import QTimer, Slot

from gui import MainWindow, SignalConatiner


class LabelUpdateThread:
    label: int
    window: MainWindow
    signal: SignalConatiner

    def __init__(self, window: MainWindow):
        super().__init__()
        self.label = 0
        self.window = window
        self.signal = SignalConatiner()
        self.signal.label_update.connect(window.set_label)
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_label)
        self.timer.start()

    @Slot(int)
    def update_label(self):
        self.signal.label_update.emit(self.label)
        self.label += 1
