import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QSplitter, QListWidget, QTextEdit, QWidget, QVBoxLayout, QStackedWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a splitter widget to divide the window into two areas
        splitter = QSplitter(self)
        self.setCentralWidget(splitter)

        # Create a QListWidget for the side menu
        menu = QListWidget(self)
        menu.addItems(['Home', 'Search', 'Analyze'])
        menu.currentItemChanged.connect(self.change_page)

        # Create a QStackedWidget to hold the pages that will be displayed on the right
        pages_widget = QStackedWidget(self)

        # Create the pages and add them to the pages widget
        home_page = QTextEdit('This is the home page')
        home_page.setWindowTitle('Home')
        pages_widget.addWidget(home_page)

        search_page = QTextEdit('This is the search page')
        search_page.setWindowTitle('Search')
        pages_widget.addWidget(search_page)

        analyze_page = QTextEdit('This is the analyze page')
        analyze_page.setWindowTitle('Analyze')
        pages_widget.addWidget(analyze_page)

        # Add the menu and pages widget to the splitter
        splitter.addWidget(menu)
        splitter.addWidget(pages_widget)

    def change_page(self, current, previous):
        # Get the text of the current menu item
        page_name = current.text()

        # Find the index of the current menu item
        page_index = self.find_page_index(page_name)

        # Get the pages widget
        pages_widget = self.centralWidget().widget(1)

        # Set the current page to the page at the selected index
        pages_widget.setCurrentIndex(page_index)

    def find_page_index(self, page_name):
        # Find the index of the page with the given name
        pages_widget = self.centralWidget().widget(1)
        for i in range(pages_widget.count()):
            page = pages_widget.widget(i)
            if page.windowTitle() == page_name:
                return i
        return -1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
