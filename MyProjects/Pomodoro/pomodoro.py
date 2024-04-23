'''
Thank's ChatGPT for help
'''

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QSpinBox
from PyQt6.QtCore import QTimer
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl
import winsound

class PomodoroTimer(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pomodoro Timer")
        self.setGeometry(100, 100, 285, 180)

        self.timer_label = QLabel("25:00", self)
        self.timer_label.setGeometry(110, 120, 100, 50)

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(50, 80, 75, 30)
        self.start_button.clicked.connect(self.start_timer)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(150, 80, 75, 30)
        self.stop_button.clicked.connect(self.stop_timer)
        self.stop_button.setEnabled(False)

        self.work_time_label = QLabel("Work Time:", self)
        self.work_time_label.setGeometry(50, 20, 100, 20)

        self.work_time_spinbox = QSpinBox(self)
        self.work_time_spinbox.setGeometry(160, 20, 50, 20)
        self.work_time_spinbox.setValue(25)

        self.break_time_label = QLabel("Break Time:", self)
        self.break_time_label.setGeometry(50, 50, 100, 20)

        self.break_time_spinbox = QSpinBox(self)
        self.break_time_spinbox.setGeometry(160, 50, 50, 20)
        self.break_time_spinbox.setValue(5)

        self.work_time = 25 * 60 * 1000  # Default work time is 25 minutes
        self.break_time = 5 * 60 * 1000  # Default break time is 5 minutes
        self.current_time = self.work_time

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.timer_status = ("Stop", "Work", "Break")
        self.timer_state = 0


    def start_timer(self):
        self.work_time = self.work_time_spinbox.value() * 60 * 1000
        self.break_time = self.break_time_spinbox.value() * 60 * 1000
        self.current_time = self.work_time
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.timer_state = 1
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.timer_state = 0
        self.timer_label.setText(f"{self.timer_status[self.timer_state]}")

    def update_timer(self):
        minutes = self.current_time // 60000
        seconds = (self.current_time % 60000) // 1000
        
        self.timer_label.setText(f"{self.timer_status[self.timer_state]} {minutes:02d}:{seconds:02d}")
        print(self.current_time)
        
        if self.work_time != 0 or self.break_time != 0:
            if self.current_time == 0 :
                self.work_time = 0
                if self.timer_state == 1:
                    self.current_time = self.break_time
                    self.timer_state = 2
                else:
                    self.break_time = 0
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
                print(f"self.work_time =", {self.work_time})
                print(f"self.break_time =", {self.break_time})
            else:
                self.current_time -= 1000
        else:
            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS | winsound.SND_ASYNC)
            self.stop_timer()
                
def main():
    app = QApplication(sys.argv)
    window = PomodoroTimer()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()