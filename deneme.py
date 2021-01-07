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


    my_df = pd.DataFrame(columns=["Sehir", "Nufus"])

    my_df["Sehir"] = ["Istanbul", "Ankara", "Bursa"]
    my_df["Nufus"] = [15000, 4000, 3000]
    my_df["Color"] = ["#5d2f8e", "#5d2f8e", "#5d2f8e"]

    my_pie_chart = pie.PieChart(my_df, "Deneme", "Sehir", "Nufus")
    my_pie_chart.showChart()


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


    # line_json = [{"data_x":1,"data_y":0.03},{"data_x":2,"data_y":0.04},
    # {"data_x":3,"data_y":0.06},
    # {"data_x":4,"data_y":0.09},{"data_x":5,"data_y":0.13},{"data_x":6,"data_y":0.18},
    # {"data_x":7,"data_y":0.25},{"data_x":8,"data_y":0.33},{"data_x":9,"data_y":0.45},
    # {"data_x":10,"data_y":0.59},{"data_x":11,"data_y":0.76},{"data_x":12,"data_y":0.97},
    # {"data_x":13,"data_y":1.22},{"data_x":14,"data_y":1.52},{"data_x":15,"data_y":1.85},
    # {"data_x":16,"data_y":2.24},{"data_x":17,"data_y":2.66},{"data_x":18,"data_y":3.13},
    # {"data_x":19,"data_y":3.63},{"data_x":20,"data_y":4.16},{"data_x":21,"data_y":4.71},
    # {"data_x":22,"data_y":5.27},{"data_x":23,"data_y":5.83},{"data_x":24,"data_y":6.38},
    # {"data_x":25,"data_y":6.91},{"data_x":26,"data_y":7.4},{"data_x":27,"data_y":7.85},
    # {"data_x":28,"data_y":8.25},{"data_x":29,"data_y":8.59},{"data_x":30,"data_y":8.86},
    # {"data_x":31,"data_y":9.06},{"data_x":32,"data_y":9.18},{"data_x":33,"data_y":9.24},
    # {"data_x":34,"data_y":9.22},{"data_x":35,"data_y":9.15},{"data_x":36,"data_y":9.01},
    # {"data_x":37,"data_y":8.83},{"data_x":38,"data_y":8.6},{"data_x":39,"data_y":8.34},
    # {"data_x":40,"data_y":8.05},{"data_x":41,"data_y":7.74},{"data_x":42,"data_y":7.41},
    # {"data_x":43,"data_y":7.08},{"data_x":44,"data_y":6.76},{"data_x":45,"data_y":6.43},
    # {"data_x":46,"data_y":6.11},{"data_x":47,"data_y":5.81},{"data_x":48,"data_y":5.51},
    # {"data_x":49,"data_y":5.24},{"data_x":50,"data_y":4.98},{"data_x":51,"data_y":4.74},
    # {"data_x":52,"data_y":4.52},{"data_x":53,"data_y":4.32},{"data_x":54,"data_y":4.15},
    # {"data_x":55,"data_y":3.99},{"data_x":56,"data_y":3.84},{"data_x":57,"data_y":3.71},
    # {"data_x":58,"data_y":3.59},{"data_x":59,"data_y":3.49},{"data_x":60,"data_y":3.39},
    # {"data_x":61,"data_y":3.31},{"data_x":62,"data_y":3.23},{"data_x":63,"data_y":3.15},
    # {"data_x":64,"data_y":3.09},{"data_x":65,"data_y":3.02},{"data_x":66,"data_y":2.97},
    # {"data_x":67,"data_y":2.91},{"data_x":68,"data_y":2.86},{"data_x":69,"data_y":2.81},
    # {"data_x":70,"data_y":2.77},{"data_x":71,"data_y":2.73},{"data_x":72,"data_y":2.68},
    # {"data_x":73,"data_y":2.64},{"data_x":74,"data_y":2.6},{"data_x":75,"data_y":2.56},
    # {"data_x":76,"data_y":2.52},{"data_x":77,"data_y":2.47},{"data_x":78,"data_y":2.43},
    # {"data_x":79,"data_y":2.39},{"data_x":80,"data_y":2.34},{"data_x":81,"data_y":2.29},
    # {"data_x":82,"data_y":2.24},{"data_x":83,"data_y":2.19},{"data_x":84,"data_y":2.13},
    # {"data_x":85,"data_y":2.08},{"data_x":86,"data_y":2.02},{"data_x":87,"data_y":1.96},
    # {"data_x":88,"data_y":1.89},{"data_x":89,"data_y":1.83},{"data_x":90,"data_y":1.76},
    # {"data_x":91,"data_y":1.69},{"data_x":92,"data_y":1.62},{"data_x":93,"data_y":1.54},
    # {"data_x":94,"data_y":1.47},{"data_x":95,"data_y":1.39},{"data_x":96,"data_y":1.32},
    # {"data_x":97,"data_y":1.24},{"data_x":98,"data_y":1.17},{"data_x":99,"data_y":1.09},
    # {"data_x":100,"data_y":1.02}]

    # my_df = pd.DataFrame(line_json)
    # my_line_chart = line.LineChart(my_df,'Test Title','Title X', 'Title Y','red')
    # my_line_chart.showChart()
