import sys
from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QVBoxLayout, QLabel


class CustomQListWidgetItem(QListWidgetItem):
    def __init__(self, title, detail):
        super().__init__()

        # Create a label to display the title and detail
        label = QLabel()
        label.setText(f"<b>{title}</b><br/>{detail}")

        # Set the label as the widget for the item
        self.setSizeHint(label.sizeHint())
        self.setText("")
        self.setToolTip(title)
        self.listwidget_item = label
        self.setSizeHint(label.sizeHint())
        self.setText("")

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.listwidget_item = label

        self.setSizeHint(label.sizeHint())
        self.setToolTip(title)
        self.listwidget_item = label

        self.listwidget_item = label


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Create a QListWidget to display the lists
        self.listwidget = QListWidget(self)

        # Create a list of tuples containing the title and details
        list_a = [("Title A", "Details A"), ("Title B",
                                             "Details B"), ("Title C", "Details C")]

        # Loop through the list and add each item to the QListWidget
        for item in list_a:
            title = item[0]
            details = item[1]
            listwidget_item = CustomQListWidgetItem(title, details)
            self.listwidget.addItem(listwidget_item)
            self.listwidget.setItemWidget(
                listwidget_item, listwidget_item.listwidget_item)

        # Create a QVBoxLayout and add the QListWidget to it
        vbox = QVBoxLayout()
        vbox.addWidget(self.listwidget)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('List A in List B')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
