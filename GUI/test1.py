import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()

        # Convert the dataframe to a QTableWidget
        table_widget = QTableWidget()
        table_widget.setRowCount(data.shape[0])
        table_widget.setColumnCount(data.shape[1])
        table_widget.setHorizontalHeaderLabels(
            [str(col) for col in data.columns])
        table_widget.setVerticalHeaderLabels([str(idx) for idx in data.index])

        # Set the values for each cell in the table widget
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                item = QTableWidgetItem(str(data.iloc[i, j]))
                table_widget.setItem(i, j, item)

        self.setCentralWidget(table_widget)
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Dataframe Table')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create a sample dataframe
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)

    # Display the dataframe in a table widget
    window = MainWindow(df)
    sys.exit(app.exec())
