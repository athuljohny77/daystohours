import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QDialog
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize, QFile, QTextStream

# Function to convert man days to hours
def man_days_to_hours():
    try:
        man_days = float(man_days_input.text())
        hours = man_days * 8
        result_label.setText(f"{man_days} man days = {hours} hours")
    except ValueError:
        result_label.setText("Please enter a number.")

# Function to convert hours to man days
def hours_to_man_days():
    try:
        hours = float(man_days_input.text())
        man_days = hours / 8
        result_label.setText(f"{hours} hours = {man_days} man days")
    except ValueError:
        result_label.setText("Please enter a number.")

# Function to toggle between man days and hours calculation
def toggle_calculation():
    if toggle_button.isChecked():
        label_man_days.setText("Enter Hours:")
        convert_button.clicked.disconnect()
        convert_button.clicked.connect(hours_to_man_days)
        window.setStyleSheet("background-color: #2f2045;")
        toggle_button.setIcon(QIcon(icon_path("man_to_hours.png")))
        toggle_button.setStyleSheet("background-color: transparent; border: none;")
    else:
        label_man_days.setText("Enter Man Days:")
        convert_button.clicked.disconnect()
        convert_button.clicked.connect(man_days_to_hours)
        window.setStyleSheet("background-color: #20452e;")
        toggle_button.setIcon(QIcon(icon_path("hours_to_man.png")))
        toggle_button.setStyleSheet("background-color: transparent; border: none;")

# Function to get the full path for icon and image files
def icon_path(file_name):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, file_name)

# Create the information window
def open_info_window():
    info_dialog = QDialog(window)
    info_dialog.setWindowTitle("About")
    info_dialog.setFixedSize(300, 150)  # Set the size of the information window

    # Pass the current background color from the main window to the information window
    info_dialog.setStyleSheet(f"background-color: {window.styleSheet().split(':')[1]};")

    layout = QVBoxLayout()
    version_label = QLabel("Ver 2.0.1")
    version_label.setStyleSheet("color: white; font-size: 14px;")
    developer_label = QLabel('<a href="https://www.athuljohny.in" style="color: #FFFF00; text-decoration: none; font-size: 16px;">www.athuljohny.in</a>')
    developer_label.setOpenExternalLinks(True)  # Enable opening links in a web browser
    copyright_label = QLabel("Copyright © 2024 Athul Johny")
    copyright_label.setStyleSheet("color: white; font-size: 16px;")
    close_button = QPushButton("Close")
    close_button.setStyleSheet(
        "color: white; background-color: #353535; border: 2px solid #FFFFFF; border-radius: 10px; font-size: 16px; padding: 5px;"
    )

    layout.addWidget(version_label)
    layout.addWidget(developer_label)
    layout.addWidget(copyright_label)
    layout.addWidget(close_button)

    info_dialog.setLayout(layout)

    # Connect the Close button to close the information window
    close_button.clicked.connect(info_dialog.close)

    info_dialog.exec_()

# Create the application
app = QApplication(sys.argv)

# Set the application icon
app_icon = QIcon(icon_path("icon.ico"))
app.setWindowIcon(app_icon)

# Set a dark color palette for dark mode
dark_palette = QPalette()
dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
dark_palette.setColor(QPalette.WindowText, Qt.white)
dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ButtonText, Qt.white)
dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
dark_palette.setColor(QPalette.ToolTipText, Qt.white)
dark_palette.setColor(QPalette.Text, Qt.white)
dark_palette.setColor(QPalette.BrightText, Qt.red)
dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
dark_palette.setColor(QPalette.HighlightedText, Qt.black)

# Create the main window
window = QWidget()
window.setWindowTitle("Work Time Converter")
window.setPalette(dark_palette)

# Set the fixed size of the window
window.setFixedSize(400, 150)

# Set the initial background color to #20452e
window.setStyleSheet("background-color: #20452e;")

# Create widgets
man_days_input = QLineEdit()
toggle_button = QPushButton()
convert_button = QPushButton("Convert")

# Set the initial result text to "Please enter a number."
result_label = QLabel("Please enter a number.")

label_man_days = QLabel("Enter Man Days:")

# Set widget styles for dark mode
widgets = [man_days_input, convert_button]
for widget in widgets:
    widget.setStyleSheet(
        "color: white; background-color: #353535; border: 2px solid #FFFFFF; border-radius: 10px; font-size: 16px; padding: 5px;"
    )

# Set the button as a toggle button and use hours_to_man.png initially
toggle_button.setIcon(QIcon(icon_path("hours_to_man.png")))
toggle_button.setCheckable(True)
toggle_button.setIconSize(QSize(40, 40))
toggle_button.setToolTip("Toggle Calculation Mode")

# Remove default style (border and background) from the input title text
label_man_days.setStyleSheet("color: white; background-color: transparent; border: none; font-size: 16px;")

# Remove default style (border and background) from the info button
toggle_button.setStyleSheet("background-color: transparent; border: none;")

# Set the same style for the info button as the toggle button
info_button = QPushButton()
info_button.setIcon(QIcon(icon_path("info.png")))  # Replace with the path to your info button icon
info_button.setFixedSize(40, 40)  # Set the size of the info button
info_button.setStyleSheet("background-color: transparent; border: none;")
info_button.setToolTip("About")

# Connect the button click to toggle calculation mode
toggle_button.clicked.connect(toggle_calculation)

# Connect the info button's click event to open_info_window
info_button.clicked.connect(open_info_window)

# Connect the Enter key press event to the convert_button click event
man_days_input.returnPressed.connect(convert_button.click)

# Connect the Convert button click event to the appropriate function
convert_button.clicked.connect(man_days_to_hours)

# Create layout
input_layout = QHBoxLayout()
input_layout.addWidget(label_man_days)
input_layout.addWidget(man_days_input)
input_layout.addWidget(toggle_button)

button_layout = QHBoxLayout()
button_layout.addWidget(convert_button)
button_layout.addWidget(info_button)  # Add the info button to the layout

main_layout = QVBoxLayout()
main_layout.addLayout(input_layout)
main_layout.addLayout(button_layout)

result_label.setFont(QFont("Arial", 12))  # Adjust font size to 12px
result_label.setStyleSheet("color: white; padding-top: 0px; padding-bottom: 0px;")  # Remove padding

main_layout.addWidget(result_label)

frame = QFrame()
frame.setLayout(main_layout)

# Set the layout for the window
window.setLayout(main_layout)

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())
