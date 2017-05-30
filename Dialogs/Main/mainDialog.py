import os

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from Dialogs.Main.helperMethods import generate_2d_or_3d_subplot, generate_checkboxes, \
    disable_checkboxes_if_only_2_are_checked, limit_name_lenght, plot_objectives, enable_checkboxes, \
    delete_all_widgets_from_holder, add_all_widgets_to_holder
from Dialogs.Main.outputExtension import OutputExtension
from FileParsers.fileParser import FileParser


class MainDialog(OutputExtension):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.x_limit, self.y_limit, self.z_limit = None, None, None

    def set_file_name(self, full_path):
        fileName = os.path.basename(full_path)
        self.lblCurrentFile.setText(limit_name_lenght(fileName))

    def axis_changed(self, rbtn):
        if rbtn.isChecked():
            if rbtn == self.rbtnDynamic:
                self.x_limit, self.y_limit, self.z_limit = None, None, None
            if rbtn == self.rbtnFixed:
                if len(self.selectedObjectives)>=1:
                    self.x_limit = self.data.get_objective_limits(self.selectedObjectives[0])
                if len(self.selectedObjectives) >= 2:
                    self.y_limit = self.data.get_objective_limits(self.selectedObjectives[1])
                if len(self.selectedObjectives) >= 3:
                    self.z_limit = self.data.get_objective_limits(self.selectedObjectives[2])
        self.canvas_update()

    def file_opened(self):
        name, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if name != "":
            self.set_file_name(name)
            p = FileParser(name)
            self.data = p.read_data()
            self.figure.delaxes(self.ax)
            self.ax = generate_2d_or_3d_subplot(self.figure, self.data.number_of_objectives())
            self.slider_range_setup()
            self.default_control_values_setup()
            delete_all_widgets_from_holder(self.checkboxHolderLayout)
            self.objectives_selection_checkboxes_setup()
            self.canvas_update()
            self.enable_sliders_after_file_loaded()

    def canvas_update(self):
        generation = self.get_generation()
        front = self.get_front()

        self.display_generation_number(generation)
        self.display_front_number(front)

        var, obj = self.data.filter(generation, front)
        plot_objectives(self.ax, obj, self.selectedObjectives, self.x_limit, self.y_limit, self.z_limit)
        self.canvas.draw()

    def checkbox_objective_changed(self, objective):
        cb = self.objectiveSelectionCheckboxes[objective]

        if cb.isChecked():
            self.selectedObjectives.append(objective)
            enable_checkboxes(self.objectiveSelectionCheckboxes)
        else:
            self.selectedObjectives.remove(objective)
            disable_checkboxes_if_only_2_are_checked(self.objectiveSelectionCheckboxes, len(self.selectedObjectives))

        self.figure.delaxes(self.ax)
        self.selectedObjectives = sorted(self.selectedObjectives)
        self.ax = generate_2d_or_3d_subplot(self.figure, min(self.data.number_of_objectives(), len(self.selectedObjectives)))
        self.canvas_update()

    def slider_range_setup(self):
        self.sldGenerations.setRange(0, self.data.number_of_generations())
        self.sldFront.setRange(-1, self.data.number_of_fronts())

    def event_connections_setup(self):
        self.sldGenerations.valueChanged.connect(self.canvas_update)
        self.sldFront.valueChanged.connect(self.canvas_update)
        self.btnOpenFile.clicked.connect(self.file_opened)
        self.rbtnDynamic.toggled.connect(lambda:self.axis_changed(self.rbtnDynamic))
        self.rbtnFixed.toggled.connect(lambda:self.axis_changed(self.rbtnFixed))

    def objectives_selection_checkboxes_setup(self):
        number_of_objectives_to_display = min(3, self.data.number_of_objectives())
        self.objectiveSelectionCheckboxes = generate_checkboxes(self.data.number_of_objectives(), number_of_objectives_to_display, self.checkbox_objective_changed)
        add_all_widgets_to_holder(self.checkboxHolderLayout, self.objectiveSelectionCheckboxes)
        self.selectedObjectives = [x for x in range(number_of_objectives_to_display)]

    def setupUi(self, form):
        super().setupUi(form)
        self.slider_range_setup()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.graphHolderGridLayout.addWidget(self.canvas)

        self.ax = generate_2d_or_3d_subplot(self.figure, self.data.number_of_objectives())

        self.default_control_values_setup()
        self.objectives_selection_checkboxes_setup()
        self.canvas_update()
        self.event_connections_setup()
