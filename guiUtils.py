import actsUtils, re, string
from stylesheet import *
from PyQt6 import QtWidgets, QtGui, QtCore

aUtils = actsUtils.ActsUtils()

# Fills main window with data about law acts
def fillLinkList(self):
    self.linkList.clear()
    for act in aUtils.getSearchResutList():
        self.linkList.append(('<a href={} style="color:#1F90D6; text-decoration: none;">{}{}</a>').format(
            act.url,
            act.displayAddress,
            prepareSpan(self,
                act.actType,
                act.status
                )))
    if len(aUtils.getSearchResutList()) == 0:
        self.linkList.append('<span style="color:#000; text-decoration: none;">Brak wyników wyszukiwania</span>')

def prepareSpan(self, actType, status):
    return ('<span style="color:#000; text-decoration: none;"> - <b>rodzaj:</b> {} - <b>status:</b> {}</span>').format(actType, status)

# Perform action on search button click
def onSearchClick(self):
    self.linkList.clear()
    tmpMap = mapInputs(self)

    if len(tmpMap) == 0:
        self.linkList.append('<span style="color:#000; text-decoration: none;">Brak wyników wyszukiwania</span>')
    elif len(tmpMap) == 1 and "publisher" in tmpMap:
        self.linkList.append('<span style="color:#000; text-decoration: none;">Brak wyników wyszukiwania</span>')
    else:
        aUtils.search(tmpMap)
        fillLinkList(self)


# Method to get content of inputs and map them into dict
def mapInputs(self):
    typeInputText = self.typeInput.text()
    positionInputText = self.positionInput.text()
    publicationPlaceText = self.publicationPlaceDropDown.currentText()
    keywordsText = self.keywordsInput.text()
    dateFromInputText = self.dateFromInput.text()
    dateToInputText = self.dateToInput.text()
    yearInputText = self.yearInput.text()

    typeBool = typeInputValidation(self, typeInputText)
    positionBool = positionInputValidation(self, positionInputText)
    publicationPlaceBool = publicationPlaceValidation(self, publicationPlaceText)
    keywordsBool = keywordsInputValidation(self, keywordsText)
    dateFromBool = dateFromInputValidation(self, dateFromInputText)
    dateToBool = dateToInputValidation(self, dateToInputText)
    yearBool = yearInputValidation(self, yearInputText)

    inputMap = {}

    if publicationPlaceBool != False and publicationPlaceText != "": inputMap["publisher"] = resolvePublisher(publicationPlaceText)   
    if typeBool != False and typeInputText != "": inputMap["type"] = typeInputText
    if positionBool != False and positionInputText != "": inputMap["position"] = positionInputText
    if keywordsBool != False and keywordsText != "": inputMap["keywordName"] = resolveKeywords(keywordsText)
    if dateFromBool != False and dateFromInputText != "": inputMap["pubDateFrom"] = dateFromInputText
    if dateToBool != False and dateToInputText != "": inputMap["pubDateTo"] = dateToInputText
    if yearBool != False and yearInputText != "": inputMap["year"] = yearInputText
        
    return inputMap
  
# Method to resolve publisher shortuct
def resolvePublisher(publisher):
    if publisher == "Dziennik Ustaw":
        return "WDU"
    elif publisher == "Monitor Polski":
        return "WMP"
    else:
        return ""

# Method to replace " " with "%20"
def resolveKeywords(keywords):
    return keywords.replace(" ", "%20")

# Method to get list of act types
def getTypeList(self):
    typeList = aUtils.getTypeList()
    return typeList

# Method to get list of keywords
def getKeywordsList(self):
    keywordsList = aUtils.getKeywordList()
    return keywordsList

# Method to validate type input
def typeInputValidation(self, typeInputText):
    lowerList = [s.lower() for s in self.typeList]
    
    if typeInputText.lower() in lowerList or typeInputText == "":
        return True
    else:
        self.typeInput.setText("Wybierz poprawny rodzaj aktu!".upper())
        return False

# Method to validate position input
def positionInputValidation(self, positionInputText):
    if positionInputText.isdigit() and int(positionInputText) > 0 or positionInputText == "":
        return True
    else:
        self.positionInput.setText("Wpisz poprany numer pozycji!".upper())
        return False

# Method to validate publication place input
def publicationPlaceValidation(self, publicationPlaceText):
    if publicationPlaceText != "":
        return True
    else:
        self.publicationPlaceDropDown.setCurrentText("Wybierz poprawne miejsce publikacji!".upper())
        return False

# Method to validate keywords input
def keywordsInputValidation(self, keywordsInputText):
    lowerList = [s.lower() for s in self.keywordsList]
    
    if keywordsInputText.lower() in lowerList or keywordsInputText == "":
        return True
    else:
        self.keywordsInput.setText("Wpisz poprawne słowa kluczowe!".upper())
        return False

# Method to validate year input
def yearInputValidation(self, yearInputText):
    if yearInputText.isdigit() and int(yearInputText) > 0 or yearInputText == "":
        return True
    else:
        self.yearInput.setText("Wpisz poprawną datę!".upper())
        return False

# Method to validate date from input
def dateFromInputValidation(self, dateFromInputText):
    result = re.match('^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$', dateFromInputText)

    if result != None or dateFromInputText == "":
        return True
    else:
        self.dateFromInput.setText("Wpisz poprawną datę!".upper())
        return False

# Method to validate date to input
def dateToInputValidation(self, dateToInputText):
    result = re.match("^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$", dateToInputText)

    if result != None or dateToInputText == "":
        return True
    else:
        self.dateToInput.setText("Wpisz poprawną datę!".upper())
        return False

# Method to show info screen
def showMessageBox(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msgBox.setText("""<p>Program przygotowany na potrzeby reazlizacji pracy masgisterskiej przeznaczony do wyszukiwania aktów prawnych.</p>
        <p>Zewnętrzne API dostarczone przez ISAP: <a href="http://isap.sejm.gov.pl/api/isap/" style="color:#1F90D6; text-decoration: none;">http://isap.sejm.gov.pl/api/isap/</a></p>
        <p>Autor: Joanna Kosmalska</p>
        <p>Wersja: 1.0</p>
        """)
        msgBox.setWindowTitle("Info")
        msgBox.setStyleSheet(styleInfoWindow)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msgBox.buttons()[0].setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        msgBox.exec()