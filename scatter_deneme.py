from netvis.chart.pie import pie
from netvis.chart.bar import bar
from netvis.chart.scatter import scatter_logo
import pandas as pd

if __name__ == '__main__':
    # my_df = pd.DataFrame(columns=["Sehir", "Nufus"])
    #
    # my_df["Sehir"] = ["Istanbul", "Ankara", "Bursa"]
    # my_df["Nufus"] = [15000, 4000, 3000]
    # my_df["Color"] = ["#5d2f8e", "#5d2f8e", "#5d2f8e"]

    # my_pie_chart = pie.PieChart(my_df, "Deneme", "Sehir", "Nufus")
    # my_pie_chart.showChart()

    # my_bar_chart = bar.BarChart(
    #     my_df, "Deneme", "Sehir", "Nufus", "Sehir", "Nufus", "#5d2f8e")
    # my_bar_chart.setHorizontalLines(True)
    # my_bar_chart.setVerticalLines(True)
    #
    # my_bar_chart.setBarColor("#0074D9")
    # my_bar_chart.setFontColor("#85144b")
    #
    # my_bar_chart.setTitleColor("#000")
    #
    # my_bar_chart.showChart()

	testDF = pd.DataFrame(columns = ['name','type','data_x','data_y'])
	import names
	import random

	name = []
	types = []
	x = []
	y = []
	for i in range(500):
		name.append(names.get_first_name())
		types.append(random.randint(1,1))
		x.append(random.randint(0,200))
		y.append(random.randint(0,200))

	testDF['name'] = name
	testDF['type'] = types
	testDF['data_x'] = x
	testDF['data_y'] = y

	my_chart = scatter_logo.ScatterPlot(testDF,"Names and Numbers","X","Y")
	my_chart.showChart()
