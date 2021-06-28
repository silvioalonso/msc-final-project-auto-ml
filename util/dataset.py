# function to extract first 5 lines of a dataset
# Return:
# 	5 line dataset
def get_dataset_head(df):
	return df.head(5)

# function to get the name of the last column of a dataset
# Return:
# 	string
def get_y_name(df) -> str:
	Y = df.iloc[:,-1]
	return Y.name