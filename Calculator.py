# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(356, 433)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_one())
        self.pushButton_1.setGeometry(QtCore.QRect(70, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_two())
        self.pushButton_2.setGeometry(QtCore.QRect(130, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_three())
        self.pushButton_3.setGeometry(QtCore.QRect(190, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_four())
        self.pushButton_4.setGeometry(QtCore.QRect(70, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_five())
        self.pushButton_5.setGeometry(QtCore.QRect(130, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_eight())
        self.pushButton_8.setGeometry(QtCore.QRect(130, 260, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_six())
        self.pushButton_6.setGeometry(QtCore.QRect(190, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_nine())
        self.pushButton_9.setGeometry(QtCore.QRect(190, 260, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_sub = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_sub())
        self.pushButton_sub.setGeometry(QtCore.QRect(190, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_zero())
        self.pushButton_0.setGeometry(QtCore.QRect(130, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_add())
        self.pushButton_add.setGeometry(QtCore.QRect(70, 320, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_seven())
        self.pushButton_7.setGeometry(QtCore.QRect(70, 260, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.display = QtWidgets.QTextBrowser(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(50, 30, 261, 91))
        self.display.setFont(QtGui.QFont("Helvitica", 30))
        self.display.setObjectName("display")
        self.pushButton_mul = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_mul())
        self.pushButton_mul.setGeometry(QtCore.QRect(250, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setAutoFillBackground(False)
        self.pushButton_mul.setAutoDefault(False)
        self.pushButton_mul.setFlat(False)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_div())
        self.pushButton_div.setGeometry(QtCore.QRect(250, 200, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.cmd_equal())
        self.pushButton_equal.setGeometry(QtCore.QRect(250, 260, 41, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setObjectName("pushButton_equal")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 356, 21))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def cmd_zero(self):
    	self.display.setText(self.display.toPlainText() + "0")

    def cmd_one(self):
    	self.display.setText(self.display.toPlainText() + "1")

    def cmd_two(self):
    	self.display.setText(self.display.toPlainText() + "2")

    def cmd_three(self):
    	self.display.setText(self.display.toPlainText() + "3")

    def cmd_four(self):
    	self.display.setText(self.display.toPlainText() + "4")

    def cmd_five(self):
    	self.display.setText(self.display.toPlainText() + "5")

    def cmd_six(self):
    	self.display.setText(self.display.toPlainText() + "6")

    def cmd_seven(self):
    	self.display.setText(self.display.toPlainText() + "7")

    def cmd_eight(self):
    	self.display.setText(self.display.toPlainText() + "8")

    def cmd_nine(self):
    	self.display.setText(self.display.toPlainText() + "9")

    def cmd_add(self):
    	self.display.setText(self.display.toPlainText() + "+")

    def cmd_sub(self):
    	self.display.setText(self.display.toPlainText() + "-")

    def cmd_mul(self):
    	self.display.setText(self.display.toPlainText() + "*")

    def cmd_div(self):
    	self.display.setText(self.display.toPlainText() + "/")

    def cmd_equal(self):
    	self.display.setText(self.display.toPlainText() + "=")
    	self.calculate()

    def calculate(self):
    	s = self.display.toPlainText()

    	for i in s:
    		if (i in "*-/+"):
    			ch = i
    			break

    	a = float (s[ : s.index(ch)])
    	b = float (s[(s.index(ch) + 1) : len(s)-1])

    	switch = { "*" : self.multiply, "/" : self.divide, "-" : self.subtract,  "+" : self.add }
    	switch[ch](a, b)

    def add(self, a, b):
    	c = a + b
    	self.display.setText(str(c))


    def subtract(self, a, b):
    	c = a - b
    	self.display.setText(str(c))

    def multiply(self, a, b):
    	c = a * b
    	self.display.setText(str(c))

    def divide(self, a, b):
    	c = a / b
    	self.display.setText(str(c))



    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "MainWindow"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_sub.setText(_translate("Calculator", "-"))
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_add.setText(_translate("Calculator", "+"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_mul.setText(_translate("Calculator", "*"))
        self.pushButton_div.setText(_translate("Calculator", "/"))
        self.pushButton_equal.setText(_translate("Calculator", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
