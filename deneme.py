from netvis.chart.pie import pie
from netvis.chart.bar import bar
import pandas as pd

if __name__ == '__main__':
    my_df = pd.DataFrame(columns=["Sehir", "Nufus"])

    my_df["Sehir"] = ["Istanbul", "Ankara", "Bursa"]
    my_df["Nufus"] = [15000, 4000, 3000]
    my_df["Color"] = ["#5d2f8e", "#5d2f8e", "#5d2f8e"]

    # my_pie_chart = pie.PieChart(my_df, "Deneme", "Sehir", "Nufus")
    # my_pie_chart.showChart()

    my_bar_chart = bar.BarChart(
        my_df, "Deneme", "Sehir", "Nufus", "Sehir", "Nufus", "#5d2f8e")
    # my_bar_chart.setHorizontalLines(True)
    # my_bar_chart.setVerticalLines(True)
    my_bar_chart.setFontColor("gray")
    my_bar_chart.showChart()
