# My Overlay Package

This package provides a customizable overlay for PyQt applications, allowing you to create always-on-top windows with adjustable background colors, transparency, and layouts. Specifically, this package allows these overlays to stay on top of full-screened applications.

## Installation

You can install the package using pip:
`pip install my_overlay_package`

## Example Usage
```
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout
from my_overlay_package.overlay import Overlay
from PyQt6.QtGui import QColor

app = QApplication([])

overlay = Overlay()
overlay.set_background_color(QColor(0, 255, 0, 150))  # Green with 150 transparency
overlay.set_geometry(100, 100, 400, 200)

grid_layout = QGridLayout()
overlay.setLayout(grid_layout)

label1 = QLabel("Label 1")
button1 = QPushButton("Button 1")
grid_layout.addWidget(label1, 0, 0)
grid_layout.addWidget(button1, 0, 1)

overlay.show()
app.exec()
```
