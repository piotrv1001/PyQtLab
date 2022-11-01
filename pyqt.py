from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# Create the main app class inheriting from QMainWindow


class Window(QMainWindow):
    #Add a constructor extending the parent window
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('PyQt6 Lab')
        self.setGeometry(100, 100, 400, 300)
        self.createMenu()
        self.createTabs()

        self.task1()
        self.task2()
        self.task3()

   # Method adding the menu panel
    def createMenu(self):
        # Create a menu bar
        self.menu = self.menuBar()
        # Add a drop-down list of the name File
        self.fileMenu = self.menu.addMenu("File")
        self.menuTask1 = self.menu.addMenu("Task 1")
        self.menuTask2 = self.menu.addMenu("Task 2")
        self.menuTask3 = self.menu.addMenu("Task 3")
        # Extend the file menu with exit position
        self.actionExit = QAction('Exit', self)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.triggered.connect(self.close)
        self.fileMenu.addAction(self.actionExit)

        self.menuTask1.addAction('Open', self.openPicture)
        self.menuTask2.addAction('Clear', self.clearText)
        self.menuTask2.addAction('Save', self.quickSave)
        self.menuTask2.addAction('Save as', self.normalSave)
        self.menuTask2.addAction('Open', self.openText)
        self.menuTask3.addAction('Clear', self.clearLines)
        self.menuTask3.addAction('A+B+C', self.merge)

    def quickSave(self):
        with open('TextFile.txt', 'w') as f:
            my_text = self.text_box.toPlainText()
            f.write(my_text)
    
    def normalSave(self):
        name , selectedFilter = QFileDialog.getSaveFileName(self.tab_2, "Select an image file",  "Initial file name", "All Files (*);;Python Files (*.py);; PNG (*.png)")
        file = open(name, 'w')
        text = self.text_box.toPlainText()
        file.write(text)

    def openText(self):  
        textName , selectedFilter = QFileDialog.getOpenFileName(self.tab_2, "Select an image file",  "Initial file name", "All Files (*);;Python Files (*.py);; PNG (*.png)")
        textFile = open(textName, 'r')
        data = textFile.read()
        self.text_box.setText(data)

    def merge(self):
        self.text_4.setText(self.text_1.text()+self.text_2.text()+self.text_3.text())

    def clearLines(self): 
        self.text_1.clear()
        self.text_2.clear()
        self.text_3.clear()
        self.text_4.clear()

    def clearText(self):
        self.text_box.clear()
    
    def openPicture(self):
        fileName , selectedFilter = QFileDialog.getOpenFileName(self.tab_1, "Select an image file",  "Initial file name", "All Files (*);;Python Files (*.py);; PNG (*.png)")
        if fileName:
            pixmap = QPixmap(fileName)
            self.t1Label.setPixmap(pixmap)   

    # Method adds an internal widget to the window
    def createTabs(self):
        # Create a tab widget
        self.tabs = QTabWidget()
        
        # Create seperate widgets for tabs
        self.tab_1 = QWidget()
        self.tab_2 = QWidget()
        self.tab_3 = QWidget()
        
        # Add tabs to the tab widget
        self.tabs.addTab(self.tab_1, "Task 1")        
        self.tabs.addTab(self.tab_2, "Task 2")        
        self.tabs.addTab(self.tab_3, "Task 3")
        self.setCentralWidget(self.tabs)

    def task1(self):
        self.tab_1.layout =  QVBoxLayout(self)
        self.t1Label = QLabel("Image will be displayed here once added")
        self.tab_1.layout.addWidget(self.t1Label)
        # Create a button
        self.button = QPushButton("Add a pic")
        # Attach the on_button_clicked function to the button 
        self.button.clicked.connect(self.openPicture)
        self.tab_1.layout.addWidget(self.button)
        self.tab_1.setLayout(self.tab_1.layout)    

    def task2(self):
        self.tab_2.layout = QGridLayout(self)
        self.text_box = QTextEdit()
        self.save_button = QPushButton("Save")
        self.clear_button = QPushButton("Clear")
        self.tab_2.layout.addWidget(self.text_box,0,0,1,2)
        self.tab_2.layout.addWidget(self.save_button,1,0)
        self.tab_2.layout.addWidget(self.clear_button,1,1)
        self.clear_button.clicked.connect(self.clearText)
        self.save_button.clicked.connect(self.normalSave)
        self.tab_2.setLayout(self.tab_2.layout) 

    def task3(self):
        self.tab_3.layout = QGridLayout(self)
        
        self.label_1 = QLabel("Field A")
        self.label_2 = QLabel("Field B")
        self.label_3 = QLabel("Field C")
        self.label_4 = QLabel("Joint fields")

        self.text_1 = QLineEdit()
        self.text_2 = QLineEdit()
        self.text_3 = QSpinBox()
        self.text_4 = QLineEdit()

        self.tab_3.layout.addWidget(self.label_1,1,0)
        self.tab_3.layout.addWidget(self.label_2,2,0)
        self.tab_3.layout.addWidget(self.label_3,3,0)
        self.tab_3.layout.addWidget(self.label_4,4,0)

        self.tab_3.layout.addWidget(self.text_1,1,1)
        self.tab_3.layout.addWidget(self.text_2,2,1)
        self.tab_3.layout.addWidget(self.text_3,3,1)
        self.tab_3.layout.addWidget(self.text_4,4,1)
        # Create a button
        self.buttont3 = QPushButton("Execute")
        # Attach the on_button_clicked function to the button 
        self.buttont3.clicked.connect(self.merge)
        self.tab_3.layout.addWidget(self.buttont3)

        self.tab_3.setLayout(self.tab_3.layout)   

# Run the window

app = QApplication([])
win = Window()
win.show()
app.exec()
