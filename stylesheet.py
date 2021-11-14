import os
from pathlib import Path

dir_path = os.fspath(Path(__file__).resolve().parent).replace("\\", "/")
DROPDOW_IMG = dir_path + "/images/dropdown.png"
DROPDOW_ON_IMG = dir_path + "/images/dropdown_on.png"

styleMainWindow = ("""QWidget{
    background-color: #1E1D25;
}
QLabel{
    color:  #fff;
}
QPushButton{
    color: #fff;
    outline: none;
    text-align: center;
}
QLineEdit{
    padding-left: 5px;
    border-radius: 8px;
    background-color: #fff;
    border: 2px solid #1F90D6;
}
QTextBrowser{
    background-color: #fff;
    border-radius: 8px;
    margin: 0px 50px 50px 50px;
    border: 2px solid #1F90D6;
    padding-left: 5px;
}""")

styleSearchButton = ("""QPushButton{
    border-radius: 8px;
    border: 2px solid #1F90D6;
    letter-spacing: 1px;
}
QPushButton:hover{
    border: 2px solid #fff;
    background-color: #1F90D6;
}""")

styleInfoButton = ("""QPushButton{
    border-radius: 26px;
    border: 2px solid #1F90D6;
}
QPushButton:hover{
    border: 2px solid #fff;
    background-color: #1F90D6;
}""")

labelsFields = ("""QLabel{
    padding-right: 10px;
}""")

paragraphIcon = ("""QLabel{
    margin-left: -40px;
}""")

dropdownsStyle  = ("""QComboBox{
    padding-left: 5px;
    background-color: #fff;
    border: 2px solid #1F90D6;
    color: black;
    border-radius: 8px;
    selection-background-color: #fff;
}
QComboBox:editable {
    background: #1E1D25;
    border-radius: 8px;
}
QComboBox:!editable, QComboBox::drop-down:editablec{
    background: #fff;
}
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: #fff;
}
QComboBox::drop-down {
    color: black;
    background-color: #fff;
    border-radius: 8px;
    border: 0px;
}
QComboBox::down-arrow {"""
+   "image: url(" +  DROPDOW_IMG + ");" + """
   width: 14px;
   height: 14px;
   padding-right: 10px;
   border: 0;
}
QComboBox::down-arrow:on { /* shift the arrow when popup is open */ """
+    "image: url(" + DROPDOW_ON_IMG + ");" + """
}
QListView{
    color: #fff;
    border: 2px solid #1F90D6;
    border-radius: 8px;
    selection-color: #fff;
    selection-background-color: #1E1D25;
    background-color: #1E1D25;
    outline: none;
}
""")

completerStyle = ("""QListView {
    color: #fff;
    border: 2px solid #1F90D6;
    border-radius: 8px;
    background-color: #1E1D25;
    selection-background-color: #1E1D25;
}""")

scrollBarStyle = ("""QScrollBar:vertical {
    border-left: 2px solid  #1F90D6;
    background: #1F90D6;
}
QScrollBar::handle:vertical {
    background: #1E1D25;
    border: 1px solid  #1F90D6;
    border-radius: 4px;
}
QScrollBar::add-line:vertical {
    background: none;
    height: 0px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
    background: none;
    height: 0px;
    subcontrol-position: top left;
    subcontrol-origin: margin;
    position: absolute;
}
QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {
    height: 0px;
    background: #fff;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}""")

inputFieldsStyle = ("""QLineEdit{
    color: #000000;
    padding-left: 5px;
    border-radius: 8px;
    background-color: #fff;
    border: 2px solid #1F90D6;
}""")

inputFieldsStyleWarning = ("""QLineEdit{
    color: #FF0000;
    padding-left: 5px;
    border-radius: 8px;
    background-color: #fff;
    border: 2px solid #1F90D6;
}""")

styleInfoWindow = ("""QWidget{
   background-color: #1E1D25;
   color: #fff;
}
QPushButton{
    width: 80px;
    height: 40px;
    border-radius: 8px;
    border: 2px solid #1F90D6;
    letter-spacing: 1px;
}
QPushButton:hover{
    border: 2px solid #fff;
    background-color: #1F90D6;
}""")