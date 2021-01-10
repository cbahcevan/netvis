from netvis.chart.bar import bar
import pandas as pd

if __name__ == '__main__':

    
    my_df = pd.DataFrame(columns=["Sehir", "Nufus"])
    
    my_df["Sehir"] = ["Istanbul", "Ankara", "Bursa"]
    my_df["Nufus"] = [20000, 6000, 3000]
    my_df["Color"] = ["#5d2f8e", "#5d2f8e", "#5d2f8e"]
    
    """
    horizontal or vertical
    """
    my_bar_chart = bar.BarChart(
        my_df, "Deneme", xname="Nufus",yname="Sehir",orientation="v")
    
    #my_bar_chart.setHorizontalLines(True)
    #my_bar_chart.setVerticalLines(True)
    
    #my_bar_chart.setBarColor("#0074D9")
    #my_bar_chart.setFontColor("#85144b")
    
    my_bar_chart.setTitleColor("#000")
    
    my_bar_chart.showChart()