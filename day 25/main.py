import pandas

df = pandas.read_csv("Squirrel_Data.csv")

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [0, 0, 0]
}
primary_fur_color = df["Primary Fur Color"]
fur_color = data_dict["Fur Color"]
squirrels_count = data_dict["Count"]

squirrels_count[0] = len(df[primary_fur_color == fur_color[0]])
squirrels_count[1] = len(df[primary_fur_color == fur_color[1]])
squirrels_count[2] = len(df[primary_fur_color == fur_color[2]])

print(squirrels_count)

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")