import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer, QTime
from PyQt6.QtGui import QFont

class MinimalistApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Apply a strict monochrome, contemporary aesthetic
        self.setStyleSheet("""
            QWidget {
                background-color: #050505;
                color: #F0F0F0;
            }
        """)
        self.setWindowTitle('VEM Studio')
        self.resize(350, 180)

        # Set up the layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(10)

        # Brand / Title Label
        title_label = QLabel("VERITAS EX MACHINA")
        title_font = QFont("Helvetica", 10, QFont.Weight.Bold)
        title_font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 2.0)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #888888;") # Subtle gray for hierarchy

        # Functional Element: The Clock
        self.time_label = QLabel("00:00:00")
        self.time_label.setFont(QFont("Helvetica", 42, QFont.Weight.Light))
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add widgets to layout
        layout.addWidget(title_label)
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        # Initialize and start the timer for the clock
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) # Update every 1000 milliseconds (1 second)

        # Call once immediately to prevent initial "00:00:00" flash
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == '__main__':
    # Initialize the Qt Application
    app = QApplication(sys.argv)

    # Create and display the main window
    window = MinimalistApp()
    window.show()

    # Execute the application loop
    sys.exit(app.exec())
