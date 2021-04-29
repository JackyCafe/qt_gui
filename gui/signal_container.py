from PySide2.QtCore import QObject, Signal


class SignalConatiner(QObject):
    label_update = Signal(int)