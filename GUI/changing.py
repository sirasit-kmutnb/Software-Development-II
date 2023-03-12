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
