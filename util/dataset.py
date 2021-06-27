
def get_dataset_head(df):
	return df.head(5)

def get_y_name(df) -> str:
	Y = df.iloc[:,-1]
	return Y.name