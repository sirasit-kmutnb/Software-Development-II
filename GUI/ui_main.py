# Form implementation generated from reading ui file 'ui_main.ui'
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
        MainWindow.setMaximumSize(QtCore.QSize(800, 16777215))
        MainWindow.setStyleSheet("background-color: rgb(17, 19, 22);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(parent=self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color:  rgb(35, 38, 53);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Top_Bar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top = QtWidgets.QFrame(parent=self.Top_Bar)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_top.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_top.setObjectName("frame_top")
        self.Title = QtWidgets.QLabel(parent=self.frame_top)
        self.Title.setGeometry(QtCore.QRect(370, 10, 90, 16))
        self.Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Title.setObjectName("Title")
        self.verticalLayout_2.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(parent=self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(parent=self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 38, 53)")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Home_Page = QtWidgets.QPushButton(parent=self.frame_left_menu)
        self.Home_Page.setMinimumSize(QtCore.QSize(0, 40))
        self.Home_Page.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 38, 53);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(49, 54, 80);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(49, 54, 80);\n"
"}")
        self.Home_Page.setCheckable(True)
        self.Home_Page.setChecked(True)
        self.Home_Page.setAutoExclusive(True)
        self.Home_Page.setObjectName("Home_Page")
        self.verticalLayout_3.addWidget(self.Home_Page)
        self.Search_Page = QtWidgets.QPushButton(parent=self.frame_left_menu)
        self.Search_Page.setMinimumSize(QtCore.QSize(0, 40))
        self.Search_Page.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  rgb(35, 38, 53);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(49, 54, 80);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(49, 54, 80);\n"
"}")
        self.Search_Page.setCheckable(True)
        self.Search_Page.setChecked(False)
        self.Search_Page.setAutoExclusive(True)
        self.Search_Page.setObjectName("Search_Page")
        self.verticalLayout_3.addWidget(self.Search_Page)
        self.Analyze_Page = QtWidgets.QPushButton(parent=self.frame_left_menu)
        self.Analyze_Page.setMinimumSize(QtCore.QSize(0, 40))
        self.Analyze_Page.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:  rgb(35, 38, 53);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(49, 54, 80);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(49, 54, 80);\n"
"}")
        self.Analyze_Page.setCheckable(True)
        self.Analyze_Page.setAutoExclusive(True)
        self.Analyze_Page.setObjectName("Analyze_Page")
        self.verticalLayout_3.addWidget(self.Analyze_Page)
        self.frame_top_menus = QtWidgets.QFrame(parent=self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(parent=self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_3 = QtWidgets.QFrame(parent=self.page_1)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_12 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_12)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setStyleSheet("color: #FFF;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_22.addWidget(self.label_2)
        self.verticalLayout_21.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Keyword_Pull_Field = QtWidgets.QLineEdit(parent=self.frame_11)
        self.Keyword_Pull_Field.setMinimumSize(QtCore.QSize(200, 30))
        self.Keyword_Pull_Field.setMaximumSize(QtCore.QSize(240, 30))
        self.Keyword_Pull_Field.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Keyword_Pull_Field.setObjectName("Keyword_Pull_Field")
        self.horizontalLayout_6.addWidget(self.Keyword_Pull_Field)
        self.Keyword_Pull_Field_2 = QtWidgets.QLineEdit(parent=self.frame_11)
        self.Keyword_Pull_Field_2.setMinimumSize(QtCore.QSize(80, 30))
        self.Keyword_Pull_Field_2.setMaximumSize(QtCore.QSize(200, 30))
        self.Keyword_Pull_Field_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Keyword_Pull_Field_2.setObjectName("Keyword_Pull_Field_2")
        self.horizontalLayout_6.addWidget(self.Keyword_Pull_Field_2)
        self.PullTweet_Field = QtWidgets.QPushButton(parent=self.frame_11)
        self.PullTweet_Field.setMinimumSize(QtCore.QSize(100, 30))
        self.PullTweet_Field.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 38, 53);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(49, 54, 80);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(49, 54, 80);\n"
"}")
        self.PullTweet_Field.setObjectName("PullTweet_Field")
        self.horizontalLayout_6.addWidget(self.PullTweet_Field)
        self.progressBar = QtWidgets.QProgressBar(parent=self.frame_11)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setVisible(False)
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.verticalLayout_21.addWidget(self.frame_11)
        self.verticalLayout_19.addWidget(self.frame_5)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_3)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #FFF;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_20.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#FFF;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_20.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#FFF;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_20.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#FFF;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_20.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=self.frame_10)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#FFF;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_20.addWidget(self.label_7)
        self.verticalLayout_19.addWidget(self.frame_10)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(parent=self.page_2)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.Search_Frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.Search_Frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Search_Frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Search_Frame_2.setObjectName("Search_Frame_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.Search_Frame_2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.Search_Analyze_Field_2 = QtWidgets.QFrame(parent=self.Search_Frame_2)
        self.Search_Analyze_Field_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Search_Analyze_Field_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Search_Analyze_Field_2.setObjectName("Search_Analyze_Field_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Search_Analyze_Field_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_4 = QtWidgets.QFrame(parent=self.Search_Analyze_Field_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.Hashtag_Search = QtWidgets.QLineEdit(parent=self.frame_4)
        self.Hashtag_Search.setMinimumSize(QtCore.QSize(240, 30))
        self.Hashtag_Search.setMaximumSize(QtCore.QSize(240, 30))
        self.Hashtag_Search.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Hashtag_Search.setObjectName("Hashtag_Search")
        self.verticalLayout_15.addWidget(self.Hashtag_Search)
        self.Location_Search = QtWidgets.QLineEdit(parent=self.frame_4)
        self.Location_Search.setMinimumSize(QtCore.QSize(240, 30))
        self.Location_Search.setMaximumSize(QtCore.QSize(240, 30))
        self.Location_Search.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Location_Search.setObjectName("Location_Search")
        self.verticalLayout_15.addWidget(self.Location_Search)
        self.StartTime_Search = QtWidgets.QLineEdit(parent=self.frame_4)
        self.StartTime_Search.setMinimumSize(QtCore.QSize(240, 30))
        self.StartTime_Search.setMaximumSize(QtCore.QSize(240, 30))
        self.StartTime_Search.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.StartTime_Search.setObjectName("StartTime_Search")
        self.verticalLayout_15.addWidget(self.StartTime_Search)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.frame_9 = QtWidgets.QFrame(parent=self.Search_Analyze_Field_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.Author_Search = QtWidgets.QLineEdit(parent=self.frame_9)
        self.Author_Search.setMinimumSize(QtCore.QSize(240, 30))
        self.Author_Search.setMaximumSize(QtCore.QSize(240, 30))
        self.Author_Search.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Author_Search.setObjectName("Author_Search")
        self.verticalLayout_16.addWidget(self.Author_Search)
        self.Text_Search = QtWidgets.QLineEdit(parent=self.frame_9)
        self.Text_Search.setMinimumSize(QtCore.QSize(240, 30))
        self.Text_Search.setMaximumSize(QtCore.QSize(240, 30))
        self.Text_Search.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Text_Search.setObjectName("Text_Search")
        self.verticalLayout_16.addWidget(self.Text_Search)
        self.EndTime_Search = QtWidgets.QLineEdit(parent=self.frame_9)
        self.EndTime_Search.setMinimumSize(QtCore.QSize(240, 30))
        self.EndTime_Search.setMaximumSize(QtCore.QSize(240, 30))
        self.EndTime_Search.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.EndTime_Search.setObjectName("EndTime_Search")
        self.verticalLayout_16.addWidget(self.EndTime_Search)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.verticalLayout_14.addWidget(self.Search_Analyze_Field_2)
        self.Search_Button = QtWidgets.QFrame(parent=self.Search_Frame_2)
        self.Search_Button.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Search_Button.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Search_Button.setObjectName("Search_Button")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Search_Button)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Search = QtWidgets.QPushButton(parent=self.Search_Button)
        self.Search.setMinimumSize(QtCore.QSize(0, 30))
        self.Search.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 38, 53);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(49, 54, 80);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(49, 54, 80);\n"
"}")
        self.Search.setObjectName("Search")
        self.horizontalLayout_5.addWidget(self.Search)
        self.Remove = QtWidgets.QPushButton(parent=self.Search_Button)
        self.Remove.setMinimumSize(QtCore.QSize(0, 30))
        self.Remove.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 38, 53);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(49, 54, 80);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(49, 54, 80);\n"
"}")
        self.Remove.setObjectName("Remove")
        self.horizontalLayout_5.addWidget(self.Remove)
        self.verticalLayout_14.addWidget(self.Search_Button)
        self.verticalLayout_18.addWidget(self.Search_Frame_2)
        self.Search_List = QtWidgets.QFrame(parent=self.frame)
        self.Search_List.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Search_List.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Search_List.setLineWidth(1)
        self.Search_List.setObjectName("Search_List")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.Search_List)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.Search_List)
        self.listWidget_2.setStyleSheet("color: #FFF;")
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_17.addWidget(self.listWidget_2)
        self.verticalLayout_18.addWidget(self.Search_List)
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.page_3)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 672, 1724))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Search_Frame = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.Search_Frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Search_Frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Search_Frame.setObjectName("Search_Frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.Search_Frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Search_Analyze_Field = QtWidgets.QFrame(parent=self.Search_Frame)
        self.Search_Analyze_Field.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Search_Analyze_Field.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Search_Analyze_Field.setObjectName("Search_Analyze_Field")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Search_Analyze_Field)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.Search_Analyze_Field)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Hashtag_Search_2 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.Hashtag_Search_2.setMinimumSize(QtCore.QSize(240, 30))
        self.Hashtag_Search_2.setMaximumSize(QtCore.QSize(240, 30))
        self.Hashtag_Search_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Hashtag_Search_2.setObjectName("Hashtag_Search_2")
        self.verticalLayout_10.addWidget(self.Hashtag_Search_2)
        self.Location_Search_2 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.Location_Search_2.setMinimumSize(QtCore.QSize(240, 30))
        self.Location_Search_2.setMaximumSize(QtCore.QSize(240, 30))
        self.Location_Search_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Location_Search_2.setObjectName("Location_Search_2")
        self.verticalLayout_10.addWidget(self.Location_Search_2)
        self.StartTime_Search_2 = QtWidgets.QLineEdit(parent=self.frame_2)
        self.StartTime_Search_2.setMinimumSize(QtCore.QSize(240, 30))
        self.StartTime_Search_2.setMaximumSize(QtCore.QSize(240, 30))
        self.StartTime_Search_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.StartTime_Search_2.setObjectName("StartTime_Search_2")
        self.verticalLayout_10.addWidget(self.StartTime_Search_2)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_7 = QtWidgets.QFrame(parent=self.Search_Analyze_Field)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Author_Search_2 = QtWidgets.QLineEdit(parent=self.frame_7)
        self.Author_Search_2.setMinimumSize(QtCore.QSize(240, 30))
        self.Author_Search_2.setMaximumSize(QtCore.QSize(240, 30))
        self.Author_Search_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Author_Search_2.setObjectName("Author_Search_2")
        self.verticalLayout_11.addWidget(self.Author_Search_2)
        self.Text_Search_2 = QtWidgets.QLineEdit(parent=self.frame_7)
        self.Text_Search_2.setMinimumSize(QtCore.QSize(240, 30))
        self.Text_Search_2.setMaximumSize(QtCore.QSize(240, 30))
        self.Text_Search_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.Text_Search_2.setObjectName("Text_Search_2")
        self.verticalLayout_11.addWidget(self.Text_Search_2)
        self.EndTime_Search_2 = QtWidgets.QLineEdit(parent=self.frame_7)
        self.EndTime_Search_2.setMinimumSize(QtCore.QSize(240, 30))
        self.EndTime_Search_2.setMaximumSize(QtCore.QSize(240, 30))
        self.EndTime_Search_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37,39,48);\n"
"    border-radius: 50px;\n"
"    color: #FFF;\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}")
        self.EndTime_Search_2.setObjectName("EndTime_Search_2")
        self.verticalLayout_11.addWidget(self.EndTime_Search_2)
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.verticalLayout_9.addWidget(self.Search_Analyze_Field)
        self.Analyze_Button = QtWidgets.QFrame(parent=self.Search_Frame)
        self.Analyze_Button.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Analyze_Button.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Analyze_Button.setObjectName("Analyze_Button")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Analyze_Button)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Search_Trend = QtWidgets.QPushButton(parent=self.Analyze_Button)
        self.Search_Trend.setMinimumSize(QtCore.QSize(0, 30))
        self.Search_Trend.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 38, 53);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(49, 54, 80);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(49, 54, 80);\n"
"}")
        self.Search_Trend.setObjectName("Search_Trend")
        self.horizontalLayout.addWidget(self.Search_Trend)
        self.PullTweet_Field_3 = QtWidgets.QPushButton(parent=self.Analyze_Button)
        self.PullTweet_Field_3.setMinimumSize(QtCore.QSize(0, 30))
        self.PullTweet_Field_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 38, 53);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(49, 54, 80);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(49, 54, 80);\n"
"}")
        self.PullTweet_Field_3.setObjectName("PullTweet_Field_3")
        self.horizontalLayout.addWidget(self.PullTweet_Field_3)
        self.Analyze_Selected_List = QtWidgets.QPushButton(parent=self.Analyze_Button)
        self.Analyze_Selected_List.setMinimumSize(QtCore.QSize(0, 30))
        self.Analyze_Selected_List.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 38, 53);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(49, 54, 80);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(49, 54, 80);\n"
"}")
        self.Analyze_Selected_List.setObjectName("Analyze_Selected_List")
        self.horizontalLayout.addWidget(self.Analyze_Selected_List)
        self.verticalLayout_9.addWidget(self.Analyze_Button)
        self.verticalLayout_8.addWidget(self.Search_Frame)
        self.List = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.List.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.List.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.List.setLineWidth(1)
        self.List.setObjectName("List")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.List)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.listWidget = QtWidgets.QListWidget(parent=self.List)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.listWidget.setStyleSheet("color: #FFF;")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_12.addWidget(self.listWidget)
        self.verticalLayout_8.addWidget(self.List)
        self.Sentiment = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.Sentiment.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Sentiment.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Sentiment.setObjectName("Sentiment")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.Sentiment)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.Sentiment_Label = QtWidgets.QLabel(parent=self.Sentiment)
        self.Sentiment_Label.setStyleSheet("color:#FFF;")
        self.Sentiment_Label.setObjectName("Sentiment_Label")
        self.verticalLayout_13.addWidget(self.Sentiment_Label)
        self.frame_8 = QtWidgets.QFrame(parent=self.Sentiment)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_13.addWidget(self.frame_8)
        self.verticalLayout_8.addWidget(self.Sentiment)
        self.WordCloud = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.WordCloud.setMinimumSize(QtCore.QSize(0, 0))
        self.WordCloud.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.WordCloud.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.WordCloud.setObjectName("WordCloud")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.WordCloud)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.WordCloud_Label = QtWidgets.QLabel(parent=self.WordCloud)
        self.WordCloud_Label.setStyleSheet("color: #FFF;")
        self.WordCloud_Label.setObjectName("WordCloud_Label")
        self.verticalLayout_23.addWidget(self.WordCloud_Label)
        self.frame_13 = QtWidgets.QFrame(parent=self.WordCloud)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_23.addWidget(self.frame_13)
        self.verticalLayout_8.addWidget(self.WordCloud)
        self.frame_6 = QtWidgets.QFrame(parent=self.scrollAreaWidgetContents)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label = QtWidgets.QLabel(parent=self.frame_6)
        self.label.setStyleSheet("color:#FFF;")
        self.label.setObjectName("label")
        self.verticalLayout_25.addWidget(self.label)
        self.frame_15 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_25.addWidget(self.frame_15)
        self.verticalLayout_8.addWidget(self.frame_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "Twitter Keeper"))
        self.Home_Page.setText(_translate("MainWindow", "Home"))
        self.Search_Page.setText(_translate("MainWindow", "Search"))
        self.Analyze_Page.setText(_translate("MainWindow", "Analyze"))
        self.label_2.setText(_translate("MainWindow", "Pull Tweets"))
        self.Keyword_Pull_Field.setPlaceholderText(_translate("MainWindow", "Keyword"))
        self.Keyword_Pull_Field_2.setPlaceholderText(_translate("MainWindow", "Amount"))
        self.PullTweet_Field.setText(_translate("MainWindow", "Pull Tweets"))
        self.label_3.setText(_translate("MainWindow", "How to use ?"))
        self.label_4.setText(_translate("MainWindow", "Keyword : Text, Amount : Number"))
        self.label_5.setText(_translate("MainWindow", "Hashtag : #Text, Author, Location, Text : Text"))
        self.label_6.setText(_translate("MainWindow", "Start Time, End Time : year.month.day.hour.minute.second"))
        self.label_7.setText(_translate("MainWindow", "Push Button you want to do !"))
        self.Hashtag_Search.setPlaceholderText(_translate("MainWindow", "Hashtag"))
        self.Location_Search.setPlaceholderText(_translate("MainWindow", "Location"))
        self.StartTime_Search.setPlaceholderText(_translate("MainWindow", "Start Time"))
        self.Author_Search.setPlaceholderText(_translate("MainWindow", "Author"))
        self.Text_Search.setPlaceholderText(_translate("MainWindow", "Text"))
        self.EndTime_Search.setPlaceholderText(_translate("MainWindow", "End Time"))
        self.Search.setText(_translate("MainWindow", "Search"))
        self.Remove.setText(_translate("MainWindow", "Remove"))
        self.Hashtag_Search_2.setPlaceholderText(_translate("MainWindow", "Hashtag"))
        self.Location_Search_2.setPlaceholderText(_translate("MainWindow", "Location"))
        self.StartTime_Search_2.setPlaceholderText(_translate("MainWindow", "Start Time"))
        self.Author_Search_2.setPlaceholderText(_translate("MainWindow", "Author"))
        self.Text_Search_2.setPlaceholderText(_translate("MainWindow", "Text"))
        self.EndTime_Search_2.setPlaceholderText(_translate("MainWindow", "End Time"))
        self.Search_Trend.setText(_translate("MainWindow", "Search for Analyze"))
        self.PullTweet_Field_3.setText(_translate("MainWindow", "Search Trend (Without Query)"))
        self.Analyze_Selected_List.setText(_translate("MainWindow", "Analyze from list"))
        self.Sentiment_Label.setText(_translate("MainWindow", "Sentiment"))
        self.WordCloud_Label.setText(_translate("MainWindow", "Word Cloud"))
        self.label.setText(_translate("MainWindow", "Spatial"))
   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # PAGE 1
    ui.Home_Page.clicked.connect(
        lambda: ui.stackedWidget.setCurrentWidget(ui.page_1))

    # PAGE 2
    ui.Search_Page.clicked.connect(
        lambda: ui.stackedWidget.setCurrentWidget(ui.page_2))

    # PAGE 3
    ui.Analyze_Page.clicked.connect(
        lambda: ui.stackedWidget.setCurrentWidget(ui.page_3))
    MainWindow.show()
    sys.exit(app.exec())
