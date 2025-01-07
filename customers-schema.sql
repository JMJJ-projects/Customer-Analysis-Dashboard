CREATE TABLE customers (
    ID INT PRIMARY KEY,
    Year_Birth INT,
    Education VARCHAR(50),
    Marital_Status VARCHAR(50),
    Income FLOAT,
    Kidhome INT,
    Teenhome INT,
    Dt_Customer DATE,
    Recency INT,
    Complain INT,
    MntWines INT,
    MntFruits INT,
    MntMeatProducts INT,
    MntFishProducts INT,
    MntSweetProducts INT,
    MntGoldProds INT,
    NumDealsPurchases INT,
    AcceptedCmp1 INT,
    AcceptedCmp2 INT,
    AcceptedCmp3 INT,
    AcceptedCmp4 INT,
    AcceptedCmp5 INT,
    Response INT,
    NumWebPurchases INT,
    NumCatalogPurchases INT,
    NumStorePurchases INT,
    NumWebVisitsMonth INT
);
CREATE TABLE users(
    ID INT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
);
CREATE TABLE history(
    History_ID INT,
    request VARCHAR(400),
    FOREIGN KEY (History_ID) REFERENCES client(ID)
);
CREATE TABLE complaints(
    Complaint_ID INT,
    complaint VARCHAR(400),
    comment VARCHAR(400),
    resolved BOOLEAN DEFAULT 'f',
    resolvedby INT,
    FOREIGN KEY (Complaint_ID) REFERENCES customers(ID)
    FOREIGN KEY (resolvedby) REFERENCES users(ID)
);
