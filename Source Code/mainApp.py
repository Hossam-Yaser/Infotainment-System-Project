from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QDateTime, QUrl
from PyQt5.QtGui import QDesktopServices, QPixmap  # Import QPixmap for displaying images
import requests
from PyQt5.QtCore import QProcess
import webbrowser
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import os



class Ui_MainWindow(object):
    a = 0  # Horizontal offset for positioning
    b = 0  # Vertical offset for positioning
    x = 1280  # Window width
    y = 720   # Window height
    counter = 0  # Initialize counter starting from 1

    def update_counter_display(self):
        # Update the label with the current counter value
        self.counter_label.setText(f"{self.counter}")
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.x, self.y)  # Set initial window size
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("""
        *{ color:#000000; }
        #MainSide{ background-color:#000000; }
        #LeftSide{ background-color:#000000; }
        #RightSide{ background-color:#000000; }
        """)
        self.centralwidget.setObjectName("centralwidget")

        self.MainSide = QtWidgets.QWidget(self.centralwidget)
        self.MainSide.setGeometry(QtCore.QRect(int(self.a), int(self.b), int(self.x), int(self.y)))  # Full window size
        self.MainSide.setObjectName("MainSide")

        self.RightSide = QtWidgets.QWidget(self.MainSide)
        self.RightSide.setGeometry(QtCore.QRect(int(self.a + 960), int(self.b + 60), int(self.x / 4), int(self.y / 1.20)))  # Adjust size relative to main window
        self.RightSide.setObjectName("RightSide")
 


        # 🔒 Lock Button
        self.Lock = QtWidgets.QPushButton(self.RightSide)
        self.Lock.setGeometry(QtCore.QRect(int(self.a + 20), int(self.b + 120), int(self.x / 4.5), int(self.y / 12)))  # Adjust button size
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(14)  
        self.Lock.setFont(font)

        self.lock_icon_locked = QtGui.QIcon("lock.png")  # Locked state icon
        self.lock_icon_unlocked = QtGui.QIcon("lock-open-alt.png")  # Unlocked state icon
        self.lock_state = False  # Default: Unlocked state


        self.Lock.setIcon(self.lock_icon_unlocked)
        self.Lock.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.Lock.setObjectName("Lock")
        self.Lock.clicked.connect(self.toggle_lock)  # Connect button to function

        self.Home = QtWidgets.QPushButton(self.RightSide)
        self.Home.setGeometry(QtCore.QRect(int(self.a + 20), int(self.b + 20), int(self.x / 4.5), int(self.y / 12)))  # Adjust button size
        font.setBold(True)
        self.Home.setFont(font)
        self.Home.setIcon(QtGui.QIcon("home.png"))
        self.Home.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.Home.setObjectName("Home")
        self.Home.clicked.connect(self.return_home)  # Connect Home button to return_home method

        self.Media = QtWidgets.QPushButton(self.RightSide)
        self.Media.setGeometry(QtCore.QRect(int(self.a + 20), int(self.b + 220), int(self.x / 4.5), int(self.y / 12)))  # Adjust button size
        font.setBold(True)
        self.Media.setFont(font)
        self.Media.setIcon(QtGui.QIcon("bluetooth-alt.png"))
        self.Media.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.Media.setObjectName("Media")
        self.Media.clicked.connect(self.open_media)

        self.Navigation = QtWidgets.QPushButton(self.RightSide)
        self.Navigation.setGeometry(QtCore.QRect(int(self.a + 20), int(self.b + 320), int(self.x / 4.5), int(self.y / 12)))  # Adjust button size
        self.Navigation.setFont(font)
        self.Navigation.setIcon(QtGui.QIcon("map-marker.png"))
        self.Navigation.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.Navigation.setObjectName("Navigation")
        self.Navigation.clicked.connect(self.show_map)
        

        self.SignDetection = QtWidgets.QPushButton(self.RightSide)
        self.SignDetection.setGeometry(QtCore.QRect(int(self.a + 20), int(self.b + 420), int(self.x / 4.5), int(self.y / 12)))  # Adjust button size
        self.SignDetection.setFont(font)
        self.SignDetection.setIcon(QtGui.QIcon("road-sign.png"))
        self.SignDetection.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.SignDetection.setObjectName("SignDetection")
        self.SignDetection.clicked.connect(self.run_sign_detection)


        self.Radio = QtWidgets.QPushButton(self.RightSide)
        self.Radio.setGeometry(QtCore.QRect(int(self.a + 20), int(self.b + 520), int(self.x / 4.5), int(self.y / 12)))  # Adjust button size
        self.Radio.setFont(font)
        self.Radio.setIcon(QtGui.QIcon("radio.png"))
        self.Radio.setIconSize(QtCore.QSize(40, 40))  # Adjust icon size
        self.Radio.setObjectName("Radio")
        self.Radio.clicked.connect(self.open_radio) # Connect to the open radio function

        self.LeftSide = QtWidgets.QWidget(self.MainSide)
        self.LeftSide.setGeometry(QtCore.QRect(int(self.a), int(self.b + 10), int(self.x / 1.33), int(self.y)))  # Adjust size relative to main window
        self.LeftSide.setObjectName("LeftSide")
        self.LeftSide.setStyleSheet("background-color: black;")



        self.label = QtWidgets.QLabel(self.LeftSide)
        self.label.setGeometry(QtCore.QRect(int(self.a + 30), int(self.b), int(self.x / 1.42), int(self.b / 1.0589)))  # Adjust label size
        self.label.setText("")
        self.label.setObjectName("label")


        # ⏰ Time Label (Position top right corner)
        self.Time = QtWidgets.QLabel(self.MainSide)
        self.Time.setGeometry(QtCore.QRect(int(self.a + 970), int(self.b + 10), int(self.x / 13), int(self.y / 18)))  # Adjust time label position
        self.Time.setStyleSheet("font-size: 16px; color: gray;")
        self.Time.setFont(font)
        self.Time.setObjectName("Time")

        # 🌡 Temperature Label (Below Time)
        self.temp = QtWidgets.QLabel(self.MainSide)
        self.temp.setGeometry(QtCore.QRect(int(self.a + 1150), int(self.b + 10), 150, 40))  # Position below time
        self.temp.setStyleSheet("font-size: 16px; color: gray;")
        self.temp.setFont(font)
        self.temp.setAlignment(QtCore.Qt.AlignCenter)
        self.temp.setObjectName("temp")

        # Lock Message Label (Popup on Left Side)
        self.lock_message = QtWidgets.QLabel(self.LeftSide)
        self.lock_message.setGeometry(QtCore.QRect(int(self.a + 300), int(self.b + 300), 400, 100))
        self.lock_message.setStyleSheet("font-size: 30px; color: white; background-color: gray; padding: 10px; border-radius: 10px;")
        self.lock_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lock_message.setVisible(False)

        self.home_image_label = QtWidgets.QLabel(self.LeftSide)
        self.home_image_label.setGeometry(QtCore.QRect(30, 0, 900, 680))
        self.home_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_image_label.setPixmap(QPixmap("car2.png"))  # Set the home image
        
        # Create the lightonimage (initially visible)
        self.lightonimage = QtWidgets.QLabel(self.LeftSide)
        self.lightonimage.setGeometry(QtCore.QRect(800, 50, 60, 60))
        self.lightonimage.setAlignment(QtCore.Qt.AlignCenter)
        self.lightonimage.setPixmap(QPixmap("car-lights.png"))  # Set the image
        self.lightonimage.setVisible(False)


        self.lighton = QtWidgets.QPushButton(self.LeftSide)
        self.lighton.setGeometry(QtCore.QRect(800, 500, 200, 50))  # Position below the home image (adjust as needed)
        self.lighton.setFixedSize(50, 50)  # Width: 150px, Height: 50px
        self.lighton.setIcon(QtGui.QIcon("car-lights(2).png"))
        self.lighton.setIconSize(QtCore.QSize(40, 40))
        self.lighton.setFont(font)
        self.lighton.setObjectName("lighton")
        self.lighton.clicked.connect(self.toggle_light)  # Connect button to toggle_light function
        self.lighton.setStyleSheet("""
         QPushButton {
        background-color: gray;  /* Green background */
            }
            QPushButton:hover {
         background-color: #D3D3D3;  /* Lighter green when hovered */
            }
            """)

        
        self.fan = QtWidgets.QLabel(self.LeftSide)
        self.fan.setGeometry(QtCore.QRect(80, 400, 60, 50))
        self.fan.setAlignment(QtCore.Qt.AlignCenter)

        # Load and scale the image to the desired size
        pixmap = QPixmap("fan.png")
        scaled_pixmap = pixmap.scaled(200, 50, QtCore.Qt.KeepAspectRatio)  # Resize to 400x100, maintaining aspect ratio

        # Set the scaled pixmap on the label
        self.fan.setPixmap(scaled_pixmap)

        self.up_button = QtWidgets.QPushButton(self.LeftSide)
        self.up_button.setGeometry(QtCore.QRect(80, 300, 200, 50))  # Position below the home image (adjust as needed)
        self.up_button.setFixedSize(50, 50)  # Width: 150px, Height: 50px
        self.up_button.setIcon(QtGui.QIcon("plus.png"))
        self.up_button.setIconSize(QtCore.QSize(40, 40))
        self.up_button.setFont(font)
        self.up_button.setObjectName("UpButton")
        self.up_button.clicked.connect(self.scroll_up)  # Connect to scroll_down function
        self.up_button.setStyleSheet("""
         QPushButton {
        background-color: gray;  /* Green background */
            }
            QPushButton:hover {
         background-color: #D3D3D3;  /* Lighter green when hovered */
            }
            """)


        # Down Button (Positioned below the home image)
        self.down_button = QtWidgets.QPushButton(self.LeftSide)
        self.down_button.setGeometry(QtCore.QRect(80, 500, 200, 50))  # Position below the home image (adjust as needed)
        self.down_button.setFixedSize(50, 50)  # Width: 150px, Height: 50px
        self.down_button.setIcon(QtGui.QIcon("minuss.png"))
        self.down_button.setIconSize(QtCore.QSize(40, 40))
        self.down_button.setFont(font)
        self.down_button.setObjectName("DownButton")
        self.down_button.clicked.connect(self.scroll_down)  # Connect to scroll_down function
        self.down_button.setStyleSheet("""
         QPushButton {
        background-color: gray;  /* Green background */
            }
            QPushButton:hover {
         background-color: #D3D3D3;  /* Lighter green when hovered */
            }
            """)
        self.counter_label = QtWidgets.QLabel(self.LeftSide)
        self.counter_label.setGeometry(QtCore.QRect(80, 450, 60, 50))  # Position of counter label
        self.counter_label.setStyleSheet("font-size: 20px; color: white; background-color: rgba(0, 0, 0, 0.5);")
        self.counter_label.setFont(font)
        self.counter_label.setAlignment(QtCore.Qt.AlignCenter)
        self.counter_label.setObjectName("counter_label")
        self.update_counter_display()  # Initial display of counter


        # Lock Message Label (Popup on Left Side)
        self.lock_message = QtWidgets.QLabel(self.LeftSide)
        self.lock_message.setGeometry(QtCore.QRect(int(self.a + 300), int(self.b + 300), 400, 100))
        self.lock_message.setStyleSheet("font-size: 30px; color: white; background-color: gray; padding: 10px; border-radius: 10px;")
        self.lock_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lock_message.setVisible(False)
        
        # Add this label definition in the setupUi method
        self.ac_off_message = QtWidgets.QLabel(self.LeftSide)
        self.ac_off_message.setGeometry(QtCore.QRect(int(self.a + 300), int(self.b + 300), 400, 100))
        self.ac_off_message.setStyleSheet("font-size: 30px; color: white; background-color: gray; padding: 10px; border-radius: 10px;")
        self.ac_off_message.setAlignment(QtCore.Qt.AlignCenter)
        self.ac_off_message.setVisible(False)
        self.ac_off_message.setText("AC is Off")
        

        self.lightonmessage = QtWidgets.QLabel(self.LeftSide)
        self.lightonmessage.setGeometry(QtCore.QRect(int(self.a + 300), int(self.b + 300), 400, 100))
        self.lightonmessage.setStyleSheet("font-size: 30px; color: white; background-color: gray; padding: 10px; border-radius: 10px;")
        self.lightonmessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lightonmessage.setVisible(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ⏳ Timer to update time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()  # Initial update

        # Timer for Temperature
        self.temp_timer = QTimer()
        self.temp_timer.timeout.connect(self.update_temperature)
        self.temp_timer.start(60000)
        self.update_temperature()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Media.setText(_translate("MainWindow", "     Media"))
        self.Home.setText(_translate("MainWindow", "     HOME"))
        self.Lock.setText(_translate("MainWindow", "     Lock"))
        self.Navigation.setText(_translate("MainWindow", "     Navigation"))
        self.SignDetection.setText(_translate("MainWindow", "   Sign Detection"))
        self.Radio.setText(_translate("MainWindow", "     Radio"))
        self.Time.setText(_translate("MainWindow", "00:00"))
        self.temp.setText(_translate("MainWindow", "Temp"))
        
    def toggle_light(self):
        """ Toggle the visibility of the lightonimage and show a popup message """
        if self.lightonimage.isVisible():
            self.lightonimage.setVisible(False)
            message = "Light is OFF"
        else:
            self.lightonimage.setVisible(True)
            message = "Light is ON"
    
        self.lightonmessage.setText(message)
        self.lightonmessage.setVisible(True)

        # Hide the message after 2 seconds
        QtCore.QTimer.singleShot(2000, lambda: self.lightonmessage.setVisible(False))

    def update_time(self):
        """ Update the time label with the current time """
        current_time = QDateTime.currentDateTime().toString("hh:mm")
        self.Time.setText(current_time)

    def toggle_lock(self):
        """ Toggle the lock icon between locked and unlocked and show a message """
        if self.lock_state:
            self.Lock.setIcon(self.lock_icon_unlocked)  # Unlock icon
            self.Lock.setText("     Unlock")
            message = "🔓 Unlocked"
        else:
            self.Lock.setIcon(self.lock_icon_locked)  # Lock icon
            self.Lock.setText("     Lock")
            message = "🔒 Locked"
    
        self.lock_state = not self.lock_state  # Toggle state
    
        # Show message in the Left Side
        self.lock_message.setText(message)
        self.lock_message.setVisible(True)
    
        # Hide message after 2 seconds
        QtCore.QTimer.singleShot(2000, lambda: self.lock_message.setVisible(False))
        
    def open_media(self):
        """ Open and play a media file when the Media button is clicked """
        # Example: Open a local audio or video file
        media_path = "/path/to/media/file.mp4"  # Replace with the path to your media file
        if not os.path.exists(media_path):
            print(f"Media file {media_path} does not exist.")
            return
        
        # Create a QMediaPlayer instance to play the media
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        media_content = QMediaContent(QUrl.fromLocalFile(media_path))

        # Set the media to be played
        self.media_player.setMedia(media_content)

        # Start playback
        self.media_player.play()

        # Optional: Update UI to indicate media is playing
        self.lock_message.setText("Media Playing")
        self.lock_message.setVisible(True)
        QtCore.QTimer.singleShot(2000, lambda: self.lock_message.setVisible(False))

    # [Your other methods like toggle_lock, update_time, etc. stay the same]
        
    def show_map(self):
        """ Show the map when Navigation button is clicked """
        # Use a map URL to load in the QWebEngineView (Google Maps example)
        self.close_sign_detection()
        map_url = "https://www.google.com/maps"
        webbrowser.open(map_url)  # Open Google Maps in the default browser  # Load the URL into the map viewer
        self.home_image_label.setVisible(False)  # Hide the home image
        self.down_button.setVisible(False)  # Hide the home image
        self.up_button.setVisible(False)  # Hide the home image
        self.counter_label.setVisible(False)  # Hide the home image
        self.fan.setVisible(False)  # Hide the home image
        self.lighton.setVisible(False)  # Hide the home image 
        self.lighton.setVisible(False)  # Hide the home image 
        self.lightonimage.setVisible(False)  # Hide the home image 

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Wheel:
            if event.angleDelta().y() > 0:  # Scroll up
                self.scroll_up()
            else:  # Scroll down
                self.scroll_down()
            return True
        return super().eventFilter(obj, event)

    def scroll_up(self):
        # Increase the counter when scrolling up
        self.counter += 1
        if self.counter > 4:  # Loop the counter back to 1 after reaching 4
            self.counter = 0
        self.update_counter_display()
        self.check_ac_status()

    def scroll_down(self):
        # Decrease the counter when scrolling down
        self.counter -= 1
        if self.counter < 0:  # Loop the counter back to 4 after reaching 1
            self.counter = 0
        self.update_counter_display()
        self.check_ac_status()
        
    def check_ac_status(self):
        """ Check if the counter is 0 and show AC off message """
        if self.counter == 0:
            self.ac_off_message.setVisible(True)
            QtCore.QTimer.singleShot(2000, lambda: self.ac_off_message.setVisible(False))
        else:
            self.ac_off_message.setVisible(False)

    def open_radio(self):
        """ Open the radio URL inside the QWebEngineView """
        self.close_sign_detection()
        radio_url = "https://radio.garden/visit/cairo/vtWTDbUW"
        webbrowser.open(radio_url)   # Load the radio URL in the web viewer
        self.home_image_label.setVisible(False)  # Hide the home image
        self.counter_label.setVisible(False)  # Hide the home image
        self.fan.setVisible(False)  # Hide the home image
        self.down_button.setVisible(False)  # Hide the home image
        self.up_button.setVisible(False)  # Hide the home image
        self.lighton.setVisible(False)  # Hide the home image
        self.lighton.setVisible(False)  # Hide the home image
        self.lightonimage.setVisible(False)  # Hide the home image

    
    def run_sign_detection(self):
        """ Run the sign detection Python script and display output in LeftSide """
        self.home_image_label.setVisible(False)  # Hide home image
    
        # Create a text display area for output
        if not hasattr(self, "output_display"):
            self.output_display = QtWidgets.QTextEdit(self.LeftSide)
            self.output_display.setGeometry(QtCore.QRect(30, 0, 900, 680))
            self.output_display.setStyleSheet("background-color: black; color: white; font-size: 14px;")
            self.output_display.setReadOnly(True)

        self.output_display.setVisible(True)

        # Run the sign detection script
        self.process = QProcess()
        self.process.setProgram("python3")  # Use "python" on Windows
        self.process.setArguments(["/home/muhamed/ODC/ai/test2models/test.py"])
        self.process.readyReadStandardOutput.connect(self.update_output)
        self.process.readyReadStandardError.connect(self.update_output)
        self.process.start()

    def update_output(self):
        """ Update the output display with real-time process output """
        output = self.process.readAllStandardOutput().data().decode()
        error = self.process.readAllStandardError().data().decode()
        self.output_display.append(output + error)

    def close_sign_detection(self):
        """ Close the Sign Detection output and return to the previous state """
        if hasattr(self, "output_display"):
            self.output_display.setVisible(False)  # Hide output display

    def update_temperature(self):
        """ Fetch temperature from OpenWeatherMap API """
        API_KEY = "764ace33f1778d77731a5f44453469f2"  
        CITY = "Cairo"
        URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(URL)
            data = response.json()
            
            if response.status_code == 200:
                temp_value = data["main"]["temp"]
                self.temp.setText(f"🌡 {temp_value}°C")  
            else:
                self.temp.setText("❌ Error")
        except Exception as e:
            print("Error fetching temperature:", e)
            self.temp.setText("❌ Error")

    def return_home(self):
        """ Return to the home screen, close any app, and display an image """
        self.close_sign_detection()  # Hide Sign Detection when returning home
        self.home_image_label.setVisible(True)
        self.down_button.setVisible(True)  # Hide the home image
        self.up_button.setVisible(True)  # Hide the home image
        self.counter_label.setVisible(True)  # Hide the home image
        self.fan.setVisible(True)  # Hide the home image
        self.lighton.setVisible(True)  # Hide the home image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
