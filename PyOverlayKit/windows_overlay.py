import ctypes
from ctypes import wintypes
from overlay import Overlay
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QWindow

class WindowsOverlay(Overlay):
    def __init__(self):
        super().__init__()
        self.hwnd = self.winId()  # Get the window ID
        self.setWindowAlwaysOnTop()

    def setWindowAlwaysOnTop(self):
        # Convert QWindow ID to integer
        hwnd = int(self.hwnd)
        SetWindowPos = ctypes.windll.user32.SetWindowPos
        HWND_TOPMOST = -1
        SWP_NOSIZE = 0x0001
        SWP_NOMOVE = 0x0002
        SWP_NOACTIVATE = 0x0010
        SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE | SWP_NOACTIVATE)
