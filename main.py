from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(843, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartingDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartingDateLabel.setGeometry(QtCore.QRect(40, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StartingDateLabel.setFont(font)
        self.StartingDateLabel.setObjectName("StartingDateLabel")
        self.StartingDateTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.StartingDateTextbox.setGeometry(QtCore.QRect(130, 30, 101, 20))
        self.StartingDateTextbox.setText("")
        self.StartingDateTextbox.setObjectName("StartingDateTextbox")
        self.DayXLabel = QtWidgets.QLabel(self.centralwidget)
        self.DayXLabel.setGeometry(QtCore.QRect(10, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.DayXLabel.setFont(font)
        self.DayXLabel.setObjectName("DayXLabel")
        self.TempLabel = QtWidgets.QLabel(self.centralwidget)
        self.TempLabel.setGeometry(QtCore.QRect(10, 120, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempLabel.setFont(font)
        self.TempLabel.setObjectName("TempLabel")
        self.TempTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.TempTextbox.setGeometry(QtCore.QRect(60, 120, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempTextbox.setFont(font)
        self.TempTextbox.setObjectName("TempTextbox")
        self.CelsiusLabel = QtWidgets.QLabel(self.centralwidget)
        self.CelsiusLabel.setGeometry(QtCore.QRect(120, 120, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CelsiusLabel.setFont(font)
        self.CelsiusLabel.setObjectName("CelsiusLabel")
        self.MedsLabel = QtWidgets.QLabel(self.centralwidget)
        self.MedsLabel.setGeometry(QtCore.QRect(10, 150, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.MedsLabel.setFont(font)
        self.MedsLabel.setAutoFillBackground(False)
        self.MedsLabel.setObjectName("MedsLabel")
        self.MedNameLabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_1.setGeometry(QtCore.QRect(10, 180, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_1.setFont(font)
        self.MedNameLabel_1.setObjectName("MedNameLabel_1")
        self.MedNameTextbox_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_1.setGeometry(QtCore.QRect(50, 180, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_1.setFont(font)
        self.MedNameTextbox_1.setObjectName("MedNameTextbox_1")
        self.MedDoseLabel_1 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_1.setGeometry(QtCore.QRect(10, 210, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_1.setFont(font)
        self.MedDoseLabel_1.setObjectName("MedDoseLabel_1")
        self.MedDoseTextbox_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_1.setGeometry(QtCore.QRect(50, 210, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_1.setFont(font)
        self.MedDoseTextbox_1.setObjectName("MedDoseTextbox_1")
        self.EndMedButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_1.setGeometry(QtCore.QRect(120, 210, 141, 23))
        self.EndMedButton_1.setDefault(False)
        self.EndMedButton_1.setFlat(False)
        self.EndMedButton_1.setObjectName("EndMedButton_1")
        self.AddDayButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddDayButton.setGeometry(QtCore.QRect(140, 110, 121, 41))
        self.AddDayButton.setObjectName("AddDayButton")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(0, 590, 131, 41))
        self.SaveButton.setObjectName("SaveButton")
        self.ExportButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExportButton.setGeometry(QtCore.QRect(130, 590, 141, 41))
        self.ExportButton.setObjectName("ExportButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 0, 561, 641))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.LoadPatientButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadPatientButton.setEnabled(True)
        self.LoadPatientButton.setGeometry(QtCore.QRect(140, 0, 131, 23))
        self.LoadPatientButton.setObjectName("LoadPatientButton")
        self.NewPatientButton = QtWidgets.QPushButton(self.centralwidget)
        self.NewPatientButton.setGeometry(QtCore.QRect(0, 0, 131, 23))
        self.NewPatientButton.setCheckable(False)
        self.NewPatientButton.setChecked(False)
        self.NewPatientButton.setAutoDefault(False)
        self.NewPatientButton.setDefault(False)
        self.NewPatientButton.setFlat(False)
        self.NewPatientButton.setObjectName("NewPatientButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 230, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.MedDoseLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_2.setGeometry(QtCore.QRect(10, 280, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_2.setFont(font)
        self.MedDoseLabel_2.setObjectName("MedDoseLabel_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 300, 271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.MedDoseTextbox_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_2.setGeometry(QtCore.QRect(50, 280, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_2.setFont(font)
        self.MedDoseTextbox_2.setObjectName("MedDoseTextbox_2")
        self.MedNameTextbox_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_2.setGeometry(QtCore.QRect(50, 250, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_2.setFont(font)
        self.MedNameTextbox_2.setObjectName("MedNameTextbox_2")
        self.MedNameLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_2.setGeometry(QtCore.QRect(10, 250, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_2.setFont(font)
        self.MedNameLabel_2.setObjectName("MedNameLabel_2")
        self.EndMedButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_2.setGeometry(QtCore.QRect(120, 280, 141, 23))
        self.EndMedButton_2.setDefault(False)
        self.EndMedButton_2.setFlat(False)
        self.EndMedButton_2.setObjectName("EndMedButton_2")
        self.MedDoseLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_3.setGeometry(QtCore.QRect(10, 350, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_3.setFont(font)
        self.MedDoseLabel_3.setObjectName("MedDoseLabel_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 370, 271, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.MedDoseTextbox_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_3.setGeometry(QtCore.QRect(50, 350, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_3.setFont(font)
        self.MedDoseTextbox_3.setObjectName("MedDoseTextbox_3")
        self.MedNameTextbox_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_3.setGeometry(QtCore.QRect(50, 320, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_3.setFont(font)
        self.MedNameTextbox_3.setObjectName("MedNameTextbox_3")
        self.MedNameLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_3.setGeometry(QtCore.QRect(10, 320, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_3.setFont(font)
        self.MedNameLabel_3.setObjectName("MedNameLabel_3")
        self.EndMedButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_3.setGeometry(QtCore.QRect(120, 350, 141, 23))
        self.EndMedButton_3.setDefault(False)
        self.EndMedButton_3.setFlat(False)
        self.EndMedButton_3.setObjectName("EndMedButton_3")
        self.MedDoseLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_4.setGeometry(QtCore.QRect(10, 420, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_4.setFont(font)
        self.MedDoseLabel_4.setObjectName("MedDoseLabel_4")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 440, 271, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.MedDoseTextbox_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_4.setGeometry(QtCore.QRect(50, 420, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_4.setFont(font)
        self.MedDoseTextbox_4.setObjectName("MedDoseTextbox_4")
        self.MedNameTextbox_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_4.setGeometry(QtCore.QRect(50, 390, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_4.setFont(font)
        self.MedNameTextbox_4.setObjectName("MedNameTextbox_4")
        self.MedNameLabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_4.setGeometry(QtCore.QRect(10, 390, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_4.setFont(font)
        self.MedNameLabel_4.setObjectName("MedNameLabel_4")
        self.EndMedButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_4.setGeometry(QtCore.QRect(120, 420, 141, 23))
        self.EndMedButton_4.setDefault(False)
        self.EndMedButton_4.setFlat(False)
        self.EndMedButton_4.setObjectName("EndMedButton_4")
        self.MedDoseLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_5.setGeometry(QtCore.QRect(10, 490, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_5.setFont(font)
        self.MedDoseLabel_5.setObjectName("MedDoseLabel_5")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 510, 271, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.MedDoseTextbox_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_5.setGeometry(QtCore.QRect(50, 490, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_5.setFont(font)
        self.MedDoseTextbox_5.setObjectName("MedDoseTextbox_5")
        self.MedNameTextbox_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_5.setGeometry(QtCore.QRect(50, 460, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_5.setFont(font)
        self.MedNameTextbox_5.setObjectName("MedNameTextbox_5")
        self.MedNameLabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_5.setGeometry(QtCore.QRect(10, 460, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_5.setFont(font)
        self.MedNameLabel_5.setObjectName("MedNameLabel_5")
        self.EndMedButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_5.setGeometry(QtCore.QRect(120, 490, 141, 23))
        self.EndMedButton_5.setDefault(False)
        self.EndMedButton_5.setFlat(False)
        self.EndMedButton_5.setObjectName("EndMedButton_5")
        self.MedDoseLabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.MedDoseLabel_6.setGeometry(QtCore.QRect(10, 560, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseLabel_6.setFont(font)
        self.MedDoseLabel_6.setObjectName("MedDoseLabel_6")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(0, 580, 271, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.MedDoseTextbox_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedDoseTextbox_6.setGeometry(QtCore.QRect(50, 560, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedDoseTextbox_6.setFont(font)
        self.MedDoseTextbox_6.setObjectName("MedDoseTextbox_6")
        self.MedNameTextbox_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.MedNameTextbox_6.setGeometry(QtCore.QRect(50, 530, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MedNameTextbox_6.setFont(font)
        self.MedNameTextbox_6.setObjectName("MedNameTextbox_6")
        self.MedNameLabel_6 = QtWidgets.QLabel(self.centralwidget)
        self.MedNameLabel_6.setGeometry(QtCore.QRect(10, 530, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MedNameLabel_6.setFont(font)
        self.MedNameLabel_6.setObjectName("MedNameLabel_6")
        self.EndMedButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.EndMedButton_6.setGeometry(QtCore.QRect(120, 560, 141, 23))
        self.EndMedButton_6.setDefault(False)
        self.EndMedButton_6.setFlat(False)
        self.EndMedButton_6.setObjectName("EndMedButton_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(260, 0, 20, 651))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.PatientNameTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientNameTextbox.setGeometry(QtCore.QRect(130, 50, 101, 20))
        self.PatientNameTextbox.setText("")
        self.PatientNameTextbox.setObjectName("PatientNameTextbox")
        self.PatientNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientNameLabel.setGeometry(QtCore.QRect(40, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PatientNameLabel.setFont(font)
        self.PatientNameLabel.setObjectName("PatientNameLabel")
        self.DaysIntervalLabel = QtWidgets.QLabel(self.centralwidget)
        self.DaysIntervalLabel.setGeometry(QtCore.QRect(40, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DaysIntervalLabel.setFont(font)
        self.DaysIntervalLabel.setObjectName("DaysIntervalLabel")
        self.DaysIntervalTextbox = QtWidgets.QLineEdit(self.centralwidget)
        self.DaysIntervalTextbox.setGeometry(QtCore.QRect(130, 70, 101, 20))
        self.DaysIntervalTextbox.setText("")
        self.DaysIntervalTextbox.setObjectName("DaysIntervalTextbox")
        self.vanitylabel = QtWidgets.QLabel(self.centralwidget)
        self.vanitylabel.setGeometry(QtCore.QRect(80, 630, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.vanitylabel.setFont(font)
        self.vanitylabel.setObjectName("vanitylabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patient Diagram Maker"))
        self.StartingDateLabel.setText(_translate("MainWindow", "Next Date:"))
        self.DayXLabel.setText(_translate("MainWindow", "Day 1"))
        self.TempLabel.setText(_translate("MainWindow", "Temp:"))
        self.CelsiusLabel.setText(_translate("MainWindow", "°C"))
        self.MedsLabel.setText(_translate("MainWindow", "Meds"))
        self.MedNameLabel_1.setText(_translate("MainWindow", "Name:"))
        self.MedDoseLabel_1.setText(_translate("MainWindow", "Dose:"))
        self.EndMedButton_1.setText(_translate("MainWindow", "End"))
        self.AddDayButton.setText(_translate("MainWindow", "Add Day"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.ExportButton.setText(_translate("MainWindow", "Export"))
        self.LoadPatientButton.setText(_translate("MainWindow", "Load"))
        self.NewPatientButton.setText(_translate("MainWindow", "New"))
        self.MedDoseLabel_2.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_2.setText(_translate("MainWindow", "Name:"))
        self.EndMedButton_2.setText(_translate("MainWindow", "End"))
        self.MedDoseLabel_3.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_3.setText(_translate("MainWindow", "Name:"))
        self.EndMedButton_3.setText(_translate("MainWindow", "End"))
        self.MedDoseLabel_4.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_4.setText(_translate("MainWindow", "Name:"))
        self.EndMedButton_4.setText(_translate("MainWindow", "End"))
        self.MedDoseLabel_5.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_5.setText(_translate("MainWindow", "Name:"))
        self.EndMedButton_5.setText(_translate("MainWindow", "End"))
        self.MedDoseLabel_6.setText(_translate("MainWindow", "Dose:"))
        self.MedNameLabel_6.setText(_translate("MainWindow", "Name:"))
        self.EndMedButton_6.setText(_translate("MainWindow", "End"))
        self.PatientNameLabel.setText(_translate("MainWindow", "Patient Name:"))
        self.DaysIntervalLabel.setText(_translate("MainWindow", "Days interval:"))
        self.vanitylabel.setText(_translate("MainWindow", "made by georgegrigs"))
        #Button calls
        self.LoadPatientButton.clicked.connect(self.Load_Button)
        self.AddDayButton.clicked.connect(self.Add_Day_Button)
        self.SaveButton.clicked.connect(self.Save_Button)
        self.DaysIntervalTextbox.textChanged.connect(self.Date_fixer)
        self.NewPatientButton.clicked.connect(self.New_Patient_Button)
        self.EndMedButton_1.clicked.connect(self.End_Med_1)
        self.EndMedButton_2.clicked.connect(self.End_Med_2)
        self.EndMedButton_3.clicked.connect(self.End_Med_3)
        self.EndMedButton_4.clicked.connect(self.End_Med_4)
        self.EndMedButton_5.clicked.connect(self.End_Med_5)
        self.EndMedButton_6.clicked.connect(self.End_Med_6)
        self.ExportButton.clicked.connect(self.Export_Button)
        self.TempTextbox.returnPressed.connect(self.Add_Day_Button)
        #Table Widget initialization
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        horHeaders = ["  Temp  "," Medication "," Date "]
        self.tableWidget.setHorizontalHeaderLabels(horHeaders)
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        i = 0


    def Load_Button(self):
        #File choosing dialog
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(initialdir=os.getcwd()+"/patients", title="Select patient file",filetypes=[("Excel files", "*.xlsx")])      
        if file_path != "":
            self.tableWidget.setRowCount(0)
            #change title to Patient Diagram Maker + Patient name
            patient_name = file_path.split(".xlsx",1)[0]
            patient_name = patient_name.rsplit("/",1)[1] 
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Patient Diagram Maker - "+ str(patient_name)))
            self.PatientNameTextbox.setText(_translate("MainWindow",str(patient_name)))
            self.DaysIntervalTextbox.setText(_translate("MainWindow",str("1")))
            #Read excel to panda dataframe
            excel = pd.read_excel(file_path)
            #print(excel.iloc[0,0])  #row , column
            count_row = excel.shape[0]
            #Populate table with pandas dataframe
            j=0
            while j<count_row:
                i=1
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                while i<4:
                    self.tableWidget.setItem(j,i-1, QTableWidgetItem(str(excel.iloc[j,i])))
                    i+=1
                j+=1
            self.tableWidget.resizeRowsToContents()
            #Populate textboxes with the last row data from pandas dataframe
            date = str(excel.iloc[count_row-1,3])
            s = date
            date = datetime.strptime(s, "%d/%m/%Y")
            interval = self.DaysIntervalTextbox.text()
            modified_date = date + timedelta(days=int(interval))
            date = datetime.strftime(modified_date, "%d/%m/%Y")
            self.StartingDateTextbox.setText(_translate("MainWindow",date))
            self.DayXLabel.setText(_translate("MainWindow", "Day " + str(count_row + int(interval))))
            meds_text = excel.iloc[count_row-1,2]
            meds_and_doses = []
            k = meds_text.count(";")
            while k>=1:
                med = meds_text.split(";",1)[0]
                meds_text = meds_text.split(";",1)[1]
                meds_and_doses.append(med)
                k-=1
            if meds_and_doses !=[]:
                q=1
                for medication in meds_and_doses:
                    med = medication.split("-",1)[0]
                    dose = medication.split("-",1)[1]
                    if q == 1: 
                        self.MedNameTextbox_1.setText(_translate("MainWindow",med))
                        self.MedDoseTextbox_1.setText(_translate("MainWindow",dose))
                    elif q==2: 
                        self.MedNameTextbox_2.setText(_translate("MainWindow",med))
                        self.MedDoseTextbox_2.setText(_translate("MainWindow",dose))
                    elif q==3: 
                        self.MedNameTextbox_3.setText(_translate("MainWindow",med))
                        self.MedDoseTextbox_3.setText(_translate("MainWindow",dose))
                    elif q==4: 
                        self.MedNameTextbox_4.setText(_translate("MainWindow",med))
                        self.MedDoseTextbox_4.setText(_translate("MainWindow",dose))
                    elif q==5: 
                        self.MedNameTextbox_5.setText(_translate("MainWindow",med))
                        self.MedDoseTextbox_5.setText(_translate("MainWindow",dose))
                    elif q==6: 
                        self.MedNameTextbox_6.setText(_translate("MainWindow",med))
                        self.MedDoseTextbox_6.setText(_translate("MainWindow",dose))
                    else:
                        return 
                    q+=1
   

    def Add_Day_Button(self):
        j = self.tableWidget.rowCount()
        _translate = QtCore.QCoreApplication.translate
        if self.TempTextbox.text() != "":  
            date = self.StartingDateTextbox.text()
            self.tableWidget.insertRow(j)
            self.tableWidget.setItem(j,0, QTableWidgetItem(str(self.TempTextbox.text()))) 
            self.tableWidget.setItem(j,2, QTableWidgetItem(str(date)))         
            s = date
            date = datetime.strptime(s, "%d/%m/%Y")
            interval = self.DaysIntervalTextbox.text()
            modified_date = date + timedelta(days=int(interval))
            date = datetime.strftime(modified_date, "%d/%m/%Y")
            self.StartingDateTextbox.setText(_translate("MainWindow",date))            
            self.DayXLabel.setText(_translate("MainWindow", "Day " + str(int(self.DayXLabel.text().split(" ")[1]) + int(interval))))
            
            if self.MedNameTextbox_1.text() != "":
                if self.MedDoseTextbox_1.text() != "":
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.MedNameTextbox_1.text() + "-" + self.MedDoseTextbox_1.text() + ";" )))
                else:
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.MedNameTextbox_1.text() + ";" )))
            if self.MedNameTextbox_2.text() != "":
                if self.MedDoseTextbox_2.text() != "":
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_2.text() + "-" + self.MedDoseTextbox_2.text() + ";" )))
                else:
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_2.text() + ";" )))
            if self.MedNameTextbox_3.text() != "":
                if self.MedDoseTextbox_3.text() != "":
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_3.text() + "-" + self.MedDoseTextbox_3.text() + ";" )))
                else:
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_3.text() + ";" )))
            if self.MedNameTextbox_4.text() != "":
                if self.MedDoseTextbox_4.text() != "":
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_4.text() + "-" + self.MedDoseTextbox_4.text() + ";" )))
                else:
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_4.text() + ";" )))
            if self.MedNameTextbox_5.text() != "":
                if self.MedDoseTextbox_5.text() != "":
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_5.text() + "-" + self.MedDoseTextbox_5.text() + ";" )))
                else:
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_5.text() + ";" ))) 
            if self.MedNameTextbox_6.text() != "":
                if self.MedDoseTextbox_6.text() != "":
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_6.text() + "-" + self.MedDoseTextbox_6.text() + ";" )))
                else:
                    self.tableWidget.setItem(j,1, QTableWidgetItem(str(self.tableWidget.item(j,1).text() + self.MedNameTextbox_6.text() + ";" ))) 
            if self.MedNameTextbox_1.text() == "" and self.MedNameTextbox_2.text() == "" and self.MedNameTextbox_3.text() == "" and self.MedNameTextbox_4.text() == "" and self.MedNameTextbox_5.text() == "" and self.MedNameTextbox_6.text() == "":
                    self.tableWidget.setItem(j,1, QTableWidgetItem("^"))     
            self.TempTextbox.setText(_translate("MainWindow",""))

    def Date_fixer(self):
        if self.StartingDateTextbox.text() != '' and self.DaysIntervalTextbox.text() != '' :              
            date = self.StartingDateTextbox.text()
            s = date
            date = datetime.strptime(s, "%d/%m/%Y")
            interval = self.DaysIntervalTextbox.text()
            modified_date = date + timedelta(days=int(interval))
            date = datetime.strftime(modified_date, "%d/%m/%Y")
            _translate = QtCore.QCoreApplication.translate
            self.StartingDateTextbox.setText(_translate("MainWindow",date)) 



    def Save_Button(self):
        col_0 = []
        col_1 = []
        col_2 = []
        for i in range(self.tableWidget.rowCount()):
            col_0.append(self.tableWidget.item(i, 0).text())
            col_1.append(self.tableWidget.item(i, 1).text())
            col_2.append(self.tableWidget.item(i, 2).text())
        df = pd.DataFrame(
            {'Temp': col_0,
            'Meds': col_1,
            'Date': col_2
            })
        patient_name = self.PatientNameTextbox.text()
        df.to_excel(os.getcwd()+ "/patients/" + patient_name + ".xlsx")

    def New_Patient_Button(self):
        _translate = QtCore.QCoreApplication.translate
        self.DayXLabel.setText(_translate("MainWindow", "Day " + "1"))
        self.tableWidget.setRowCount(0)
        self.MedNameTextbox_1.setText(_translate("MainWindow",""))
        self.MedNameTextbox_2.setText(_translate("MainWindow",""))
        self.MedNameTextbox_3.setText(_translate("MainWindow",""))
        self.MedNameTextbox_4.setText(_translate("MainWindow",""))
        self.MedNameTextbox_5.setText(_translate("MainWindow",""))
        self.MedNameTextbox_6.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_1.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_2.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_3.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_4.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_5.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_6.setText(_translate("MainWindow",""))
        self.TempTextbox.setText(_translate("MainWindow",""))
        self.DaysIntervalTextbox.setText(_translate("MainWindow","1"))
        self.PatientNameTextbox.setText(_translate("MainWindow",""))
        self.StartingDateTextbox.setText(_translate("MainWindow",datetime.today().strftime('%d/%m/%Y')))


    def End_Med_1(self):
        _translate = QtCore.QCoreApplication.translate
        self.MedNameTextbox_1.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_1.setText(_translate("MainWindow",""))
    def End_Med_2(self):
        _translate = QtCore.QCoreApplication.translate
        self.MedNameTextbox_2.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_2.setText(_translate("MainWindow",""))
    def End_Med_3(self):
        _translate = QtCore.QCoreApplication.translate
        self.MedNameTextbox_3.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_3.setText(_translate("MainWindow",""))
    def End_Med_4(self):
        _translate = QtCore.QCoreApplication.translate
        self.MedNameTextbox_4.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_4.setText(_translate("MainWindow",""))
    def End_Med_5(self):
        _translate = QtCore.QCoreApplication.translate
        self.MedNameTextbox_5.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_5.setText(_translate("MainWindow",""))
    def End_Med_6(self):
        _translate = QtCore.QCoreApplication.translate
        self.MedNameTextbox_6.setText(_translate("MainWindow",""))
        self.MedDoseTextbox_6.setText(_translate("MainWindow",""))


    def Export_Button(self):
        #create main plot section
        plt.figure(figsize=(11.69,8.27))
        col_0 = []
        col_1 = []
        col_2 = []
        rows = self.tableWidget.rowCount()
        for i in range(rows):
            col_0.append(self.tableWidget.item(i, 0).text())
            col_1.append(self.tableWidget.item(i, 1).text())
            col_2.append(self.tableWidget.item(i, 2).text())
            last_date = self.tableWidget.item(i, 2).text()
        plt.ylabel('Temparature in Celsius')
        plt.xlabel('Dates: ' + self.tableWidget.item(0, 2).text() + " - " + last_date)
        row = list(range(0, rows))
        col = [float(i) for i in col_0]
        plt.plot(row, col,'--go')
        plt.rc('font', size=15)
        for s, d in zip(col, row):
            plt.annotate(s, xy = (d,s ))
        #create meds subplots
        meds_all = []
        for item in col_1:
            meds_all.extend(item.split(";"))
        df = pd.DataFrame(
            {
            'Meds': meds_all,
            })
        meds_unique = df.Meds.unique()
        meds_unique_final = []
        for unique in meds_unique:
            if unique != "" and unique != "^":
                meds_unique_final.append(unique)
        med1 = [None]*rows
        med2 = [None]*rows
        med3 = [None]*rows
        med4 = [None]*rows
        med5 = [None]*rows
        med6 = [None]*rows
        k = 0
        j = len(meds_unique_final)
        while j < 6: 
            meds_unique_final.append("None")
            j += 1
        for item in col_1:
            if meds_unique_final[0] in item:
                med1[k] = 43
            if meds_unique_final[1] in item:
                med2[k] = 43.5
            if meds_unique_final[2] in item:
                med3[k] = 44    
            if meds_unique_final[3] in item:
                med4[k] = 44.5
            if meds_unique_final[4] in item:
                med5[k] = 45
            if meds_unique_final[5] in item:
                med6[k] = 45.5
            k += 1
        plt.plot(row, med1)
        x1 = self.indexer(med1)
        plt.text(x1,43, meds_unique_final[0])
        plt.plot(row, med2, "--")
        x2 = self.indexer(med2)
        plt.text(x2,43.5, meds_unique_final[1])
        plt.plot(row, med3, "-.")
        x3 = self.indexer(med3)
        plt.text(x3,44, meds_unique_final[2])
        plt.plot(row, med4, ":")
        x4 = self.indexer(med4)
        plt.text(x4,44.5, meds_unique_final[3])
        plt.plot(row, med5)
        x5 = self.indexer(med5)
        plt.text(x5,45, meds_unique_final[4])
        plt.plot(row, med6, "--")
        x6 = self.indexer(med6)
        plt.text(x6,45.5, meds_unique_final[5])
        adder = 0

        if med1 != [None]*rows:
            adder += 0.5
        
        if med2 != [None]*rows:
            adder += 0.5
        
        if med3 != [None]*rows:
            adder += 0.5
        
        if med4 != [None]*rows:
            adder += 0.5
        
        if med5 != [None]*rows:
            adder += 0.5

        if med6 != [None]*rows:
            adder += 0.5


        plt.ylim((34, 43 + adder)) 
        patient_name = self.PatientNameTextbox.text()
        plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = True, bottom=False, top = False, labeltop=True)
        plt.xticks(np.arange(0, rows, step=1))
        plt.grid(True)
        plt.savefig(os.getcwd()+ "/patients/" + patient_name + ".png")
        plt.show()  
        


    def indexer(self,listeru):
        i = 0
        for item in listeru:
            if item != None:
                return (i)
            i += 1
        return (9999)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
