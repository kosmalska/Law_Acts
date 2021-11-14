import requests, enum

class LinksEnum(enum.Enum):
    MAIN_LINK = "https://isap.sejm.gov.pl/api/isap/"
    TYPES_LINK = "https://isap.sejm.gov.pl/api/isap/types"
    KEYWORDS_LINK = "https://isap.sejm.gov.pl/api/isap/keywords"
    PDF_LINK = "https://isap.sejm.gov.pl/api/isap/deeds/{}/{}/{}/text.pdf"
    SEARCH_LINK = "https://isap.sejm.gov.pl/api/isap/acts/search?&limit=5000&"

class Act:
    url = "" # np. http://isap.sejm.gov.pl/api/isap/deeds/WDU/2017/2/text.pdf
    publisher = "" # WDU/WMP
    year = "" # np. 1999
    pos = 0 # 1992
    displayAddress = "" # np. Dz.U. 2021 poz. 1892
    status = "" # np. "obowiązujacy"
    actType = "" # np. "Obwieszczenie"

    def __init__(self, publisher, year, pos, displayAddress, status, actType):
        self.publisher = publisher
        self.year = year
        self.pos = pos 
        self.displayAddress = displayAddress
        self.status = status
        self.actType = actType
        self.url = LinksEnum.PDF_LINK.value.format(publisher, year, pos)

    def getUrl(self):
        return self.url
    
    def setUrl(self, url):
        self.url = url
    
    def getPublisher(self):
        return self.publisher
    
    def setPublisher(self, publisher):
        self.publisher = publisher
    
    def getYear(self):
        return self.year
    
    def setYear(self, year):
        self.year = year
    
    def getPos(self):
        return self.pos
    
    def setPos(self, pos):
        self.pos = pos
    
    def getDisplayAddress(self):
        return self.displayAddress
    
    def setDisplayAddress(self, displayAddress):
        self.displayAddress = displayAddress
    
    def getstatus(self):
        return self.status
    
    def setStatus(self, status):
        self.status = status
    
    def getType(self):
        return self.actType
    
    def setType(self, actType):
        self.actType = actType

class ActsUtils:
    keywordsList = []
    typeList = []
    searchResultList = []

    def __init__(self):
        self.fillKeywords()
        self.fillTypes()

    def fillKeywords(self):
        response = requests.get(LinksEnum.KEYWORDS_LINK.value)
        
        if response.status_code == 200:
            self.keywordsList = list(response.json())

    def fillTypes(self):
        response = requests.get(LinksEnum.TYPES_LINK.value)
        
        if response.status_code == 200:
            self.typeList = list(response.json())
    
    def getKeywordList(self):
        return self.keywordsList
    
    def getTypeList(self):
        return self.typeList
    
    def getSearchResutList(self):
        return self.searchResultList
    
    # https://isap.sejm.gov.pl/api/isap/acts/search?pubDateFrom=1999-01-01&pubDateTo=2000-01-01&limit=50&offset=100
    def search(self, argsDict):
        requestLink = LinksEnum.SEARCH_LINK.value

        for k, v in argsDict.items():
            requestLink += k + "=" + v + "&"
        
        requestLink = requestLink[:-1]

        response = requests.get(requestLink)
        if response.status_code == 200:
            self.objectMapper(response.json())
        else:
            self.objectMapper({})

    def objectMapper(self, contentJson):
        self.searchResultList.clear()
        itemsArr = contentJson['items']
        for json in itemsArr:
            self.searchResultList.append(Act(
                json['publisher'],
                json['year'],
                json['pos'],
                json['displayAddress'],
                json['status'],
                json['type']
            ))