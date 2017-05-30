from PyQt5.QtWidgets import QApplication, QDialog

from DataHolders.nullDataHolder import NullDataHolder
from Dialogs.Main.mainDialog import MainDialog


def main():
    import sys
    app = QApplication(sys.argv)
    window = QDialog()
    ui = MainDialog(NullDataHolder())
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
