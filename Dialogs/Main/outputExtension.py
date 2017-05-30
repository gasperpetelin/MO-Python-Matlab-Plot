from PyQt5.QtWidgets import QDialog
from Dialogs.Main import output

class OutputExtension(QDialog, output.Ui_Form):
    def __init__(self):
        super().__init__()

    def display_generation_number(self, number=None):
        if number == 0 or number is None:
            self.lblCurrentGeneration.setText("All")
        else:
            self.lblCurrentGeneration.setText(str(number))

    def display_front_number(self, number=None):
        if number == -1 or number is None:
            self.lblCurrentFront.setText("All")
        else:
            self.lblCurrentFront.setText(str(number))

    def get_generation(self):
        g = self.sldGenerations.value()
        if g == 0:
            return None
        return g

    def get_front(self):
        f = self.sldFront.value()
        if f == -1:
            return None
        return f

    def enable_sliders_after_file_loaded(self):
        self.sldFront.setEnabled(True)
        self.sldGenerations.setEnabled(True)

    def default_control_values_setup(self):
        self.display_generation_number()
        self.display_front_number()
        self.sldFront.setValue(-1)
        self.sldGenerations.setValue(0)