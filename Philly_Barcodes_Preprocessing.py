import pandas as pd

data = pd.read_csv("philly_barcodes_test.csv")

col_unsplit = data['Description'].tolist()

Name = []
Desc = []

for row in col_unsplit:
	temp_name = row.split('-', 1)[0]
	temp_desc = row.split('-', 1)[1]
	Name.append(temp_name)
	Desc.append(temp_desc)

data['Name'] = Name
data['Description'] = Desc

print(data.head())

data.to_csv("philly_barcodes_test.csv")
