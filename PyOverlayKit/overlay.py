from PyQt6.QtCore import Qt, QRect, QPoint
from PyQt6.QtGui import QPainter, QColor, QMouseEvent
from PyQt6.QtWidgets import *

class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.Tool, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.WindowDoesNotAcceptFocus, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

        # Default settings
        self.bg_color = QColor(0, 0, 0, 100)  # Black with 100 transparency

        # For dragging
        self._drag_start_position = None

        # Close Button
        self.close_button = QPushButton("X", self)
        self.close_button.setFixedSize(40, 20)
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("""
            QPushButton {
                background-color: #FF4C4C;
                color: white;
                border: none;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)
        self.close_button.setVisible(True)  # Show by default

    def set_background_color(self, color: QColor):
        self.bg_color = color
        self.update()  # Request a redraw to apply the new color

    def set_position(self, x: int, y: int):
        self.move(x, y)

    def set_geometry(self, x: int, y: int, width: int, height: int):
        self.setGeometry(QRect(x, y, width, height))
        self.position_close_button()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, False)
        painter.setBrush(self.bg_color)
        painter.setPen(Qt.PenStyle.NoPen)  # Disable the pen to avoid border lines
        painter.drawRect(0, 0, self.width() + 1, self.height() + 1)  # Slightly expand the rectangle

    def set_close_button_visibility(self, visible: bool):
        """Method to show or hide the close button."""
        self.close_button.setVisible(visible)
    
    def position_close_button(self):
        """Method to position the close button at the top-right corner."""
        self.close_button.move(self.width() - self.close_button.width() - 5, 5)

    def set_size(self, width: int, height: int):
        self.resize(width, height)

    def add_widget(self, widget):
        self.layout().addWidget(widget)
        widget.show()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_start_position = event.globalPosition()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._drag_start_position:
            delta = event.globalPosition() - self._drag_start_position
            self.move(self.pos() + delta.toPoint())
            self._drag_start_position = event.globalPosition()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_start_position = None
