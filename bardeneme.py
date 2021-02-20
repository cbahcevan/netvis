from netvis.chart.bar import bar
import pandas as pd

if __name__ == '__main__':


    my_df = pd.DataFrame(columns=["Sehir", "Nufus"])

    my_df["Sehir"] = ["IstanbulIstanbul", "Ankara", "Bursa","Berlin","HamburgHamburgHamburgHamburg","ParisParis","Zyxel","Huawei"]
    my_df["Nufus"] = [20000, 6000, 3000,4000,5000,6000,9000,10000]



    """

    my_bar_chart = bar.BarChart(
        my_df, "2021 Şehirlerin nüfusları", yname="Sehir",xname="Nufus", orientation="v")

    my_bar_chart.setHorizontalLines(True)
    my_bar_chart.setVerticalLines(True)




    my_bar_chart.setBarColor("#0074D9")


    my_bar_chart.setTitleColor("#39CCCC")
    my_bar_chart.showChart()


    """

    new_df = {"sehir":["istanbul","ankara","izmir","berlin","bursa"],"nufus":[15,3,4,8,6],"kirlilik":[20,10,2,1,2]}
    new_df = pd.DataFrame.from_dict(new_df)

    my_bar_chart = bar.BarChart(new_df,"Sehirler arası dagilim","kirlilik","nufus","sehir",theme="blue")
    my_bar_chart.showChart()
