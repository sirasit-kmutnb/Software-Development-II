# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(17, 19, 22);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Side_Menu = QtWidgets.QFrame(parent=self.centralwidget)
        self.Side_Menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Side_Menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Side_Menu.setLineWidth(0)
        self.Side_Menu.setObjectName("Side_Menu")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Side_Menu)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.List_Menu = QtWidgets.QListWidget(parent=self.Side_Menu)
        self.List_Menu.setLayoutDirection(
            QtCore.Qt.LayoutDirection.LeftToRight)
        self.List_Menu.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color:rgb(35, 38, 53);\n"
                                     "padding: 10px;\n"
                                     "")
        self.List_Menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.List_Menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.List_Menu.setLineWidth(0)
        self.List_Menu.setObjectName("List_Menu")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.List_Menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.List_Menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.List_Menu.addItem(item)
        self.gridLayout_2.addWidget(self.List_Menu, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.Side_Menu)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Top_Bar = QtWidgets.QFrame(parent=self.frame_2)
        self.Top_Bar.setEnabled(True)
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 38, 53);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Top_Bar.setLineWidth(0)
        self.Top_Bar.setObjectName("Top_Bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Top_Bar)
        self.verticalLayout_2.setContentsMargins(12, -1, 12, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.Top_Bar)
        self.label.setStyleSheet("color:rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(parent=self.frame_2)
        self.Content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Content.setObjectName("Content")
        self.verticalLayout_3.addWidget(self.Content)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.List_Menu.isSortingEnabled()
        self.List_Menu.setSortingEnabled(False)
        item = self.List_Menu.item(0)
        item.setText(_translate("MainWindow", "Home"))
        item = self.List_Menu.item(1)
        item.setText(_translate("MainWindow", "Search"))
        item = self.List_Menu.item(2)
        item.setText(_translate("MainWindow", "Analyze"))
        self.List_Menu.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Twitter Keeper"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
