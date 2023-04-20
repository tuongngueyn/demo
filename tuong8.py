from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QVBoxLayout, QTableWidgetItem
import sys

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QTableWidget
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['Column 1', 'Column 2'])

        # Populate the table with some data
        for row in range(1):
            for col in range(1):
                item = QTableWidgetItem(f"({row}, {col})")
                self.tableWidget.setItem(row, col, item)

        # Create a QPushButton to delete the selected row
        self.deleteButton = QPushButton('Delete Selected Row')
        self.deleteButton.clicked.connect(self.deleteRow)

        # Add the table and button to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.deleteButton)
        self.setLayout(layout)

    def deleteRow(self):
        # Get the currently selected row
        selected_row = self.tableWidget.currentRow()

        # If a row is selected, remove it from the table
        if selected_row >= 0:
            self.tableWidget.removeRow(selected_row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
