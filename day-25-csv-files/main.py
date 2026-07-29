import pandas as pd


# Read the CSV file
data = pd.read_csv("central_park_squirrel_data.csv")

# Filter out and count the squirrel's color by group color
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

# Create a dictionary to convey the Dataframe formatting
data_dic = {
    "Fur color": ["Grey", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

# Export to a new csv file using the formatted dictionary
dataframe = pd.DataFrame(data_dic)
dataframe.to_csv("squirrel_count.csv")

