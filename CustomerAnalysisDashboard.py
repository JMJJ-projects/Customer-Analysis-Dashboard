import sys
import psycopg2
from PyQt5 import QtCore, QtWidgets, QtChart, QtGui
from PyQt5.QtCore import Qt

# Page 1: Login Page
class Ui_Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Login")
        self.setObjectName("Login")
        self.loginButton = QtWidgets.QPushButton(self)
        self.loginButton.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setText("Login")

        self.SignUpButton = QtWidgets.QPushButton(self)
        self.SignUpButton.setGeometry(QtCore.QRect(350, 130, 75, 23))
        self.SignUpButton.setObjectName("SignUpButton")
        self.SignUpButton.setText("Sign Up")

        self.loginText = QtWidgets.QTextEdit(self)
        self.loginText.setGeometry(QtCore.QRect(170, 30, 260, 20))
        self.loginText.setObjectName("loginEdit")

        self.passText = QtWidgets.QTextEdit(self)
        self.passText.setGeometry(QtCore.QRect(170, 70, 260, 20))
        self.passText.setObjectName("passEdit")

        self.labellogin = QtWidgets.QLabel(self)
        self.labellogin.setGeometry(QtCore.QRect(100, 30, 70, 16))
        self.labellogin.setObjectName("labellogin")
        self.labellogin.setText("Username:")

        self.labelpass = QtWidgets.QLabel(self)
        self.labelpass.setGeometry(QtCore.QRect(100, 70, 60, 16))
        self.labelpass.setObjectName("labelpass")
        self.labelpass.setText("Password:")

        self.loginauthenticate = QtWidgets.QLabel(self)
        self.loginauthenticate.setGeometry(QtCore.QRect(160, 100, 150, 25))
        self.loginauthenticate.setText("")
        self.loginauthenticate.setObjectName("loginauthenticate")

        self.labeltest = QtWidgets.QLabel(self)
        self.labeltest.setGeometry(QtCore.QRect(110, 190, 400, 25))
        self.labeltest.setObjectName("labeltest")
        self.labeltest.setText("(For testing purposes, you can log in without credentials)")


# Page 2: Menu Page
class Ui_Menu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()     
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Menu")
        self.setWindowTitle("Menu")

        self.logoutButton = QtWidgets.QPushButton(self)
        self.logoutButton.setGeometry(QtCore.QRect(10, 10, 75, 25))
        self.logoutButton.setObjectName("logButton")
        self.logoutButton.setText("Log out")
        
# Barre de recherche
        self.searchBar = QtWidgets.QLineEdit(self)
        self.searchBar.setGeometry(QtCore.QRect(130, 10, 595, 25))
        self.searchBar.setPlaceholderText("Search a client by ID, Income or any other criteria")
        self.searchBar.setObjectName("searchBar")
#Bouton de Recherche
        self.searchButton = QtWidgets.QPushButton(self)
        self.searchButton.setGeometry(QtCore.QRect(735, 10, 75, 25))
        self.searchButton.setObjectName("searchButton")
        self.searchButton.setText("Search")

#History
        self.labelhistory = QtWidgets.QLabel(self)
        self.labelhistory.setGeometry(QtCore.QRect(10, 50, 120, 25))
        self.labelhistory.setObjectName("labelhistory")
        self.labelhistory.setText("Command History:")
        self.historyBox = QtWidgets.QComboBox(self)
        self.historyBox.setGeometry(QtCore.QRect(130, 50, 595, 25))
        self.historyBox.setObjectName("historyBox")
        self.historyButton = QtWidgets.QPushButton(self)
        self.historyButton.setGeometry(QtCore.QRect(735, 50, 75, 25))
        self.historyButton.setObjectName("historyButton")
        self.historyButton.setText("Run")

#Sort
        self.labelsort = QtWidgets.QLabel(self)
        self.labelsort.setGeometry(QtCore.QRect(505, 90, 50, 25))
        self.labelsort.setObjectName("labelsort")
        self.labelsort.setText("Sort by:")
        self.sortBox = QtWidgets.QComboBox(self)
        self.sortBox.setGeometry(QtCore.QRect(555, 90, 170, 25))
        self.sortBox.setObjectName("sortBox")
        self.sortButton = QtWidgets.QPushButton(self)
        self.sortButton.setGeometry(QtCore.QRect(735, 90, 75, 25))
        self.sortButton.setObjectName("sortButton")
        self.sortButton.setText("Sort")

#Table Main
        self.tablemenu = QtWidgets.QTableWidget(self)
        self.tablemenu.setGeometry(QtCore.QRect(10, 130, 800, 710))
        self.tablemenu.setObjectName("tablemenu")

#Complaint
        self.labelcomplaint = QtWidgets.QLabel(self)
        self.labelcomplaint.setGeometry(QtCore.QRect(840, 5, 60, 20))
        self.labelcomplaint.setObjectName("labelcomplaint")
        self.labelcomplaint.setText("Complaint:")        
        self.complaintsBox = QtWidgets.QComboBox(self)
        self.complaintsBox.setGeometry(QtCore.QRect(840, 30, 750, 100))
        self.complaintsBox.setObjectName("complaintsBox")
        self.labelresponse = QtWidgets.QLabel(self)
        self.labelresponse.setGeometry(QtCore.QRect(840, 140, 70, 20))
        self.labelresponse.setObjectName("labelresponse")
        self.labelresponse.setText("Response:")
        self.Response = QtWidgets.QTextEdit(self)
        self.Response.setGeometry(QtCore.QRect(840, 165, 750, 100))
        self.Response.setObjectName("Response")
        self.respondButton = QtWidgets.QPushButton(self)
        self.respondButton.setGeometry(QtCore.QRect(1440, 275, 150, 60))
        self.respondButton.setObjectName("respondButton")
        self.respondButton.setText("Respond")        
        self.checkButton = QtWidgets.QCheckBox(self)
        self.checkButton.setGeometry(QtCore.QRect(1360, 275, 70, 30))
        self.checkButton.setObjectName("checkButton")
        self.checkButton.setText("Resolved")

#Loyalty
        self.labelloyalty = QtWidgets.QLabel(self)
        self.labelloyalty.setGeometry(QtCore.QRect(840, 340, 90, 20))
        self.labelloyalty.setObjectName("labelloyalty")
        self.labelloyalty.setText("Loyalty Rank:")
        self.tableloyalty = QtWidgets.QTableWidget(self)
        self.tableloyalty.setGeometry(QtCore.QRect(840, 370, 170, 470))
        self.tableloyalty.setObjectName("tableloyalty")

        self.chart = QtChart.QChart()
        self.chart_view = QtChart.QChartView(self.chart)
        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.addWidget(self.chart_view)

#THE MAIN!!!!!!!!!!!!!!!!!!!!!!!!!!
class MainApp(QtWidgets.QMainWindow):
#initiation
    def __init__(self):
        super().__init__()
        self.userID = 0  
        self.resize(580, 255)
        self.setWindowTitle("Customer Analysis Dashboard")
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.complaintsviewed = 0
        
        # Add pages
        self.login_page = Ui_Login()
        self.menu_page = Ui_Menu()
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.menu_page)
      
        # Connect buttons
        self.login_page.loginButton.clicked.connect(self.button_Login)
        self.login_page.SignUpButton.clicked.connect(self.button_Signup)
        self.menu_page.logoutButton.clicked.connect(self.button_Logout)
        self.menu_page.sortButton.clicked.connect(self.button_Sort)
        self.menu_page.searchButton.clicked.connect(self.search_Customers)
        self.menu_page.historyButton.clicked.connect(self.button_History)
        self.menu_page.complaintsBox.currentTextChanged.connect(self.complaint_Click)
        self.menu_page.respondButton.clicked.connect(self.button_Respond)
        self.setCentralWidget(self.stacked_widget)
        
        #Self explanatory       
        self.connect_DB()


# Connect to the database
    def connect_DB(self):       
        self.conn = psycopg2.connect(
            database="Enterprise Data", user="Guest", host="ep-lively-mode-a2bxegau.eu-central-1.aws.neon.tech", password="FE5UMNCte9nT"
        )
        self.cursor = self.conn.cursor()
        
        # Load data for menu page
        self.cursor.execute("SELECT * FROM customers ORDER BY ID")
        self.conn.commit()
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            self.menu_page.tablemenu.setRowCount(0)
            self.menu_page.tablemenu.setColumnCount(0)
            return
        self.menu_page.tablemenu.setRowCount(len(rows))
        self.menu_page.tablemenu.setColumnCount(len(self.cursor.description))
        headers = [desc[0] for desc in self.cursor.description]
        self.menu_page.tablemenu.setHorizontalHeaderLabels(headers)
        
        #Add elements to table
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                self.menu_page.tablemenu.setItem(i, j, QtWidgets.QTableWidgetItem(str(col)))
        header = self.menu_page.tablemenu.horizontalHeader()
        for j in range(len(self.cursor.description)):
            header.setSectionResizeMode(j, QtWidgets.QHeaderView.ResizeToContents)
        
        # Add headers to sort combo box
        self.menu_page.sortBox.clear()
        self.menu_page.sortBox.addItems(headers)   

        #Load data for complaints
        self.cursor.execute("SELECT * FROM complaints ORDER BY complaint_id")
        self.conn.commit()        
        rows = self.cursor.fetchall()
        for row in rows : 
            self.menu_page.complaintsBox.addItem(str(row[1]))
        
        #Load data loyalty table
        self.cursor.execute("WITH CustomerScores AS (SELECT ID, CASE WHEN NumWebVisitsMonth > 0 THEN (MntFishProducts + MntFruits + MntGoldProds + MntMeatProducts + MntSweetProducts + MntWines) * NumCatalogPurchases / (NumWebVisitsMonth * 10000) ELSE 0 END AS Score FROM customers) SELECT c.ID, c.Score, (SELECT COUNT(*) FROM CustomerScores c2 WHERE c2.Score > c.Score) + 1 AS Rank FROM CustomerScores c ORDER BY Rank ASC;")
        self.conn.commit()        
        rows = self.cursor.fetchall()
        headers = [desc[0] for desc in self.cursor.description]
        if len(rows) == 0:
            self.menu_page.tableloyalty.setRowCount(0)
            self.menu_page.tableloyalty.setColumnCount(0)
            return
        self.menu_page.tableloyalty.setRowCount(len(rows))
        self.menu_page.tableloyalty.setColumnCount(len(self.cursor.description))
        headers = [desc[0] for desc in self.cursor.description]
        self.menu_page.tableloyalty.setHorizontalHeaderLabels(headers)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                self.menu_page.tableloyalty.setItem(i, j, QtWidgets.QTableWidgetItem(str(col)))
        header = self.menu_page.tableloyalty.horizontalHeader()
        for j in range(len(self.cursor.description)):
            header.setSectionResizeMode(j, QtWidgets.QHeaderView.ResizeToContents)
            
        #loyalty pie chart
        self.cursor.execute("WITH CategorizedCustomers AS (SELECT  ID, CASE WHEN NumWebVisitsMonth > 0 AND ((MntFishProducts + MntFruits + MntGoldProds + MntMeatProducts + MntSweetProducts + MntWines) * NumCatalogPurchases) / NULLIF(NumWebVisitsMonth, 0) > 25000.00 THEN 'Loyal Customer' WHEN NumDealsPurchases > 0 AND (NumCatalogPurchases + NumStorePurchases + NumWebPurchases) / NULLIF(NumDealsPurchases, 0) > 8.00 THEN 'Discount Buyer' WHEN (NumCatalogPurchases + NumStorePurchases + NumWebPurchases) > 0 AND (MntFishProducts + MntFruits + MntGoldProds + MntMeatProducts + MntSweetProducts + MntWines) / NULLIF((NumCatalogPurchases + NumStorePurchases + NumWebPurchases), 0) > 10000 THEN 'Luxury Buyer' WHEN NumWebVisitsMonth > 0 AND NumWebPurchases / NULLIF(NumWebVisitsMonth, 0) < 0.75 THEN 'Window Shopper' WHEN NumWebVisitsMonth > 0 AND NumWebPurchases / NULLIF(NumWebVisitsMonth, 0) >= 1.5 THEN 'Impulse Buyer' ELSE 'Uncategorized' END AS Category FROM customers ), CategoryCounts AS (SELECT Category, COUNT(*) AS CustomerCount FROM CategorizedCustomers GROUP BY Category ) SELECT Category, CustomerCount FROM CategoryCounts ORDER BY CustomerCount DESC;")
        self.conn.commit()        
        category = self.cursor.fetchall()   
        LoyalC = category[0][1]
        LuxuryB = category[1][1]
        WindowS = category[2][1]
        DiscountB = category[3][1]
        ImpulsiveB = category[4][1]
        self.slice1 = QtChart.QPieSlice('Discount Buyer ' + str(DiscountB), DiscountB)
        self.slice1.setLabelPosition(0)    
        self.slice1.setLabelVisible(True)
        self.slice2 = QtChart.QPieSlice('Luxury Buyer '+str(LuxuryB), LuxuryB)        
        self.slice2.setLabelColor(QtGui.QColor('white'))        
        self.slice2.setLabelPosition(1)        
        self.slice2.setLabelVisible(True)
        self.slice3 = QtChart.QPieSlice('Impulsive Buyer '+str(ImpulsiveB), ImpulsiveB)        
        self.slice3.setLabelColor(QtGui.QColor('white'))                
        self.slice3.setLabelPosition(1)    
        self.slice3.setLabelVisible(True)
        self.slice4 = QtChart.QPieSlice('Window Shopper '+str(WindowS), WindowS)        
        self.slice4.setLabelColor(QtGui.QColor('white'))                
        self.slice4.setLabelPosition(1)    
        self.slice4.setLabelVisible(True)
        self.slice5 = QtChart.QPieSlice('Loyal Customer '+ str(LoyalC), LoyalC)
        self.slice5.setLabelColor(QtGui.QColor('white'))
        self.slice5.setLabelPosition(1)    
        self.slice5.setLabelVisible(True)
        self.series = QtChart.QPieSeries()
        self.series.append(self.slice1)
        self.series.append(self.slice2)
        self.series.append(self.slice3)
        self.series.append(self.slice4)
        self.series.append(self.slice5)        
        self.menu_page.chart.addSeries(self.series)
            
            
#Login button on login screen
    def button_Login(self):
        _username = self.login_page.loginText.toPlainText()
        _password = self.login_page.passText.toPlainText()
        self.cursor.execute("SELECT count(*) FROM users WHERE username = '"+str(_username)+"' AND password = '"+str(_password)+"'")
        self.conn.commit()
        authenticate = self.cursor.fetchall()
        if(authenticate[0][0] > 0):
            self.cursor.execute("SELECT ID FROM users WHERE username = '"+str(_username)+"' AND password = '"+str(_password)+"'")
            self.conn.commit()
            identity = self.cursor.fetchall()
            self.userID = identity[0][0]
            
            #Load History
            self.cursor.execute("SELECT distinct * FROM history WHERE History_ID = "+str(self.userID))
            self.conn.commit()
            rows = self.cursor.fetchall()
            for row in rows : 
                self.menu_page.historyBox.addItem(str(row[1]))
        else:
            self.login_page.loginauthenticate.setText("Authentication failed")
        self.menu_page.vertical_layout.setContentsMargins(1020,340,0,0)
        self.resize(1600,850)
        self.stacked_widget.setCurrentIndex(1)
     
     
#Sign Up button on login screen
    def button_Signup(self):
        self.cursor.execute("SELECT count(*) FROM users")
        self.conn.commit()
        count = self.cursor.fetchall()
        _username = self.login_page.loginText.toPlainText()
        _password = self.login_page.passText.toPlainText()
        _id = count[0][0] + 1
        self.cursor.execute(""f"INSERT INTO users(id, username, password) VALUES ({_id},'{_username}', '{_password}')""")
        self.login_page.loginauthenticate.setText("Sign Up Successful!");
        
        
    def button_Logout(self):
        self.userID = 0        
        self.resize(580,225)
        self.menu_page.vertical_layout.setContentsMargins(0,0,0,0)
        self.login_page.loginauthenticate.setText("")
        self.stacked_widget.setCurrentIndex(0)
        self.menu_page.historyBox.clear()
        complaintsviewed = 0
        
        
#Sort button in Menu
    def button_Sort(self):
        #Preliminary step to avoid bugs when table or headers are empty
        self.menu_page.tablemenu.clearContents()
        self.menu_page.tablemenu.setRowCount(0)
        self.cursor.execute(""f"SELECT * FROM customers ORDER BY id""")
        self.conn.commit()
        headers = [desc[0] for desc in self.cursor.description]
        _sortby = str(self.menu_page.sortBox.currentText())
        if _sortby not in headers:
            return
            
        #Actual sort function
        self.cursor.execute(""f"SELECT * FROM customers ORDER BY {_sortby}""")
        self.conn.commit()
        rows2 = self.cursor.fetchall()
        self.menu_page.tablemenu.setRowCount(len(rows2))
        for i, row in enumerate(rows2):
            for j, col in enumerate(row):
                self.menu_page.tablemenu.setItem(i, j, QtWidgets.QTableWidgetItem(str(col)))
                
        #Insert into history
        self.cursor.execute("INSERT INTO History(history_id, request) VALUES ("+str(self.userID)+",'Ordered by: "+str(_sortby)+"')")
        self.conn.commit()
        self.update()


#When clicking in complaint text box
    def complaint_Click(self, complaintsviewed):
        #Loads the complain and corresponding response by a user (not unique so that complaints aren't answered twice)
        self.menu_page.Response.clear()
        _complaints = str(self.menu_page.complaintsBox.currentText())
        self.cursor.execute(""f"SELECT * FROM complaints WHERE complaint = $${_complaints}$$""")
        self.conn.commit()
        rows3 = self.cursor.fetchall()
        self.menu_page.Response.setText(str(rows3[0][2]))
        if(str(rows3[0][3]) == 'True'):
            self.menu_page.checkButton.setChecked(1)
        else:
            self.menu_page.checkButton.setChecked(0)
        
        #Insert into history
        if self.complaintsviewed != 0:
            self.cursor.execute("INSERT INTO History(history_id, request) VALUES ("+str(self.userID)+",'Checked complaint: "+str(_complaints)+"')")
        self.conn.commit()
        self.complaintsviewed = self.complaintsviewed + 1


#Allows user to add a comment to a complaint and even mark it as resolved    
    def button_Respond(self):
        _text = self.menu_page.Response.toPlainText()
        _complaints = str(self.menu_page.complaintsBox.currentText())
        if(self.menu_page.checkButton.isChecked):
            _resolved = 'true'
        else:
            _resolved = 'false'
        self.cursor.execute(""f"UPDATE complaints SET comment = '{_text}', resolved = {_resolved}, resolvedby = {self.userID} WHERE complaint = $${_complaints}$$;""")
        self.conn.commit()


#Allows a user to rerun previous commands if applicable (is unique to each user)
    def button_History(self):
        _run = str(self.menu_page.historyBox.currentText())
        _understand = _run.split()
        #Sorts
        if _understand[0] == "Ordered":
            self.menu_page.tablemenu.clearContents()
            self.menu_page.tablemenu.setRowCount(0)
            self.cursor.execute(""f"SELECT * FROM customers ORDER BY id""")
            self.conn.commit()
            headers = [desc[0] for desc in self.cursor.description]
            _sortby = _understand[2]
            if _sortby not in headers:
                return
            self.cursor.execute("SELECT * FROM customers ORDER BY " +str(_sortby))
            self.conn.commit()
            rows2 = self.cursor.fetchall()            
            self.menu_page.tablemenu.setRowCount(len(rows2))
            for i, row in enumerate(rows2):
                for j, col in enumerate(row):
                    self.menu_page.tablemenu.setItem(i, j, QtWidgets.QTableWidgetItem(str(col)))
            self.update()
        #Complaints         
        if _understand[0] == "Checked":
            _complainttext  = _run.split(": ")
            self.menu_page.complaintsBox.setCurrentText(str(_complainttext[1]))
            self.complaint_Click(0)
        #Searches   
        if _understand[0] == "Search:":
            search_query = _understand[1]      
            # Vérifier si une recherche est effectuée
            if not search_query:
                self.load_Customers()
                return
            # Construire et exécuter la requête SQL
            self.cursor.execute(f"""
                 SELECT * FROM customers 
                 WHERE CAST(id AS TEXT) LIKE '%{search_query}%' 
                   OR LOWER(education) LIKE LOWER('%{search_query}%') 
                   OR LOWER(marital_status) LIKE LOWER('%{search_query}%') 
                   OR CAST(kidhome AS TEXT) LIKE '%{search_query}%'
                 """) 
            self.conn.commit()
            results = self.cursor.fetchall()
            # Mettre à jour la table avec les résultats
            self.menu_page.tablemenu.clearContents()
            self.menu_page.tablemenu.setRowCount(len(results))
            for i, row in enumerate(results):
                for j, col in enumerate(row):
                    self.menu_page.tablemenu.setItem(i, j, QtWidgets.QTableWidgetItem(str(col)))
    

#Bouton de Recherche
    def search_Customers(self):
        # Récupérer le texte de la barre de recherche
        search_query = self.menu_page.searchBar.text().strip()
        
        # Vérifier si une recherche est effectuée
        if not search_query:
            self.load_Customers()
            return
        # Construire et exécuter la requête SQL
        self.cursor.execute(f"""
             SELECT * FROM customers 
             WHERE CAST(id AS TEXT) LIKE '%{search_query}%' 
               OR LOWER(education) LIKE LOWER('%{search_query}%') 
               OR LOWER(marital_status) LIKE LOWER('%{search_query}%') 
               OR CAST(kidhome AS TEXT) LIKE '%{search_query}%'
             """) 
        self.conn.commit()
        results = self.cursor.fetchall()

        # Mettre à jour la table avec les résultats
        self.menu_page.tablemenu.clearContents()
        self.menu_page.tablemenu.setRowCount(len(results))

        for i, row in enumerate(results):
            for j, col in enumerate(row):
                self.menu_page.tablemenu.setItem(i, j, QtWidgets.QTableWidgetItem(str(col)))

        #Enregistrement de la requête dans l'historique
        self.cursor.execute("INSERT INTO History(history_id, request) VALUES ("+str(self.userID)+",'Search: "+str(search_query)+"')")
        self.conn.commit()
    
    
#Basic function that loads the table for when bugs arise
    def load_Customers(self):         
        self.cursor.execute("SELECT * FROM customers ORDER BY id")
        self.conn.commit()
        rows = self.cursor.fetchall()
        self.menu_page.tablemenu.clearContents()
        self.menu_page.tablemenu.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                self.menu_page.tablemenu.setItem(i, j, QtWidgets.QTableWidgetItem(str(col)))
        self.update()

# Run the Application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
