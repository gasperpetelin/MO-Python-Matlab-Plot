from PyQt5.QtWidgets import QCheckBox
from mpl_toolkits.mplot3d import Axes3D

def generate_2d_or_3d_subplot(figure, number_of_objectives):
    if number_of_objectives <= 2:
        return figure.add_subplot(1, 1, 1)
    else:
        return figure.add_subplot(1, 1, 1, projection='3d')

def generate_checkboxes(number_of_objectives, number_of_displayed_objectives, click_subscriber = None):
    checkbox_list = []
    for i in range(number_of_objectives):
        c = QCheckBox("Objective " + str(i))
        if i<number_of_displayed_objectives:
            c.setChecked(True)
        if click_subscriber is not None:
            c.stateChanged.connect(lambda checked, index=i: click_subscriber(index))
        checkbox_list.append(c)
    return checkbox_list

def disable_checkboxes_if_only_2_are_checked(checkbox_list, number_of_selected_objectives):
    if number_of_selected_objectives<=2:
        for cb in checkbox_list:
            if cb.isChecked():
                cb.setEnabled(False)

def enable_checkboxes(sheckbox_list):
    for enb in sheckbox_list:
        enb.setEnabled(True)

def limit_name_lenght(name):
    if len(name) < 15:
        return name
    else:
        return name[:12] + "..."

def plot_objectives(axis, data, selected_objectives, x_lim = None, y_lim = None, z_lim = None):
    axis.cla()
    if len(selected_objectives) == 2:
        axis.plot(data[:, selected_objectives[0]], data[:, selected_objectives[1]], ".")
        if x_lim is not None:
            axis.set_xlim(x_lim)
        if y_lim is not None:
            axis.set_ylim(y_lim)

    if len(selected_objectives) == 3:
        axis.plot(data[:, selected_objectives[0]], data[:, selected_objectives[1]], data[:, selected_objectives[2]], ".")
        if x_lim is not None:
            axis.set_xlim(x_lim)
        if y_lim is not None:
            axis.set_ylim(y_lim)
        if z_lim is not None:
            axis.set_zlim(z_lim)


def delete_all_widgets_from_holder(holder):
    for i in reversed(range(holder.count())):
        holder.itemAt(i).widget().deleteLater()

def add_all_widgets_to_holder(holder, widget_list):
    for w in widget_list:
        holder.addWidget(w)


