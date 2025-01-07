from datetime import datetime
f = open("marketing_campaign.csv", 'r')
header = next(f).strip().split('\t')

for line in f:
    items = line.strip().split('\t')
    row = dict(zip(header, items))
    
    education = row['Education'].replace("'", "''") 
    marital_status = row['Marital_Status'].replace("'", "''")
    dt_customer = datetime.strptime(row['Dt_Customer'], '%d-%m-%Y').date()
    
    customers_insert = (
        f"INSERT INTO customers (ID, Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome, Dt_Customer, Recency, Complain, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, AcceptedCmp1, AcceptedCmp2, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, Response, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth) "
        f"VALUES ("
        f"{row['ID']}, "
        f"{row['Year_Birth']}, "
        f"'{education}', "
        f"'{marital_status}', "
        f"{row['Income'] if row['Income'] else 'NULL'}, "
        f"{row['Kidhome']}, {row['Teenhome']}, "
        f"'{dt_customer}', "
        f"{row['Recency']}, {row['Complain']}"
        f"{row['ID']}, {row['MntWines']}, {row['MntFruits']}, "
        f"{row['MntMeatProducts']}, {row['MntFishProducts']}, "
        f"{row['MntSweetProducts']}, {row['MntGoldProds']}"
        f"{row['ID']}, {row['NumDealsPurchases']}, "
        f"{row['AcceptedCmp1']}, {row['AcceptedCmp2']}, {row['AcceptedCmp3']}, "
        f"{row['AcceptedCmp4']}, {row['AcceptedCmp5']}, {row['Response']}"
        f"{row['ID']}, {row['NumWebPurchases']}, "
        f"{row['NumCatalogPurchases']}, {row['NumStorePurchases']}, "
        f"{row['NumWebVisitsMonth']}"
        f");"
    )
    print(customers_insert)  