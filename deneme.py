from netvis.chart.pie import pie
from netvis.chart.bar import bar
from netvis.chart.scatter import scatter
from netvis.chart.line import line
import pandas as pd
import numpy as np

if __name__ == '__main__':

#--------------------- bar chart test -----------------------------------------------
    #
    # my_df = pd.DataFrame(columns=["Sehir", "Nufus"])
    #
    # my_df["Sehir"] = ["Istanbul", "Ankara", "Bursa"]
    # my_df["Nufus"] = [15000, 4000, 3000]
    # my_df["Color"] = ["#5d2f8e", "#5d2f8e", "#5d2f8e"]
    #
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


#---------------------------pie chart test ----------------------------------

    #
    # my_df = pd.DataFrame(columns=["Sehir", "Nufus"])
    #
    # my_df["Sehir"] = ["Istanbul", "Ankara", "Bursa"]
    # my_df["Nufus"] = [15000, 4000, 3000]
    # my_df["Color"] = ["#5d2f8e", "#5d2f8e", "#5d2f8e"]
    #
    # my_pie_chart = pie.PieChart(my_df, "Deneme", "Sehir", "Nufus")
    # my_pie_chart.showChart()


#-------------------------- scatterplot test -----------------------------------


	# xx = np.array([0, 199])
	# yy = np.array([0.33, 180])
	# means = [xx.mean(), yy.mean()]
	# stds = [xx.std() / 3, yy.std() / 3]
	# corr = 0.8
	# covs = [[stds[0]**2, stds[0]*stds[1]*corr], [stds[0]*stds[1]*corr,stds[1]**2]]
	# m = np.random.multivariate_normal(means, covs, 1000).T
	# scatter_df = pd.DataFrame({'data_x':m[0],'data_y':m[1]})
    #
	# my_scatterplot = scatter.ScatterPlot(scatter_df,"Positive Correlation Scatter Plot"," Scatter X","Y Scatter")
	# my_scatterplot.showChart()



#--------------------------------line test -------------------------------------
    import datetime as datetime
    #x = np.random.randint(low=0, high=100, size=10)
    base = datetime.datetime.today()
    x = [(base - datetime.timedelta(weeks=x)) for x in range(10)]
    y = np.random.randint(low=0, high=100, size=10)

    #x.sort()
    y.sort()
    my_df = pd.DataFrame({'data_x':x,'data_y':y})
    my_line_chart = line.LineChart(my_df,'Test Title','Title X', 'Title Y','red')
    my_line_chart.showChart()
