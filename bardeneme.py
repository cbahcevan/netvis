from netvis.chart.bar import bar
import pandas as pd

if __name__ == '__main__':

    
    my_df = pd.DataFrame(columns=["Sehir", "Nufus"])
    
    my_df["Sehir"] = ["IstanbulIstanbul", "Ankara", "Bursa","Berlin","HamburgHamburgHamburgHamburg","ParisParis","Zyxel","Huawei"]
    my_df["Nufus"] = [20000, 6000, 3000,4000,5000,6000,9000,10000]
    
    """
    horizontal or vertical
    """
    my_bar_chart = bar.BarChart(
        my_df, "2021 Şehirlerin nüfusları", yname="Nufus",xname="Sehir")
    
    my_bar_chart.setHorizontalLines(True)
    my_bar_chart.setVerticalLines(True)
    
    #my_bar_chart.setBarColor("#0074D9")
    #my_bar_chart.setFontColor("#85144b")
    
    my_bar_chart.setTitleColor("#000")
    
    my_bar_chart.showChart()