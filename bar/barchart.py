
import pandas as pd
import barcharttemplates
import webbrowser
from IPython.core.display import display, HTML
from IPython import get_ipython


def isEnviromentIPython() -> bool:
    try:
        shell_name = get_ipython().__class__.__name__

        return shell_name in ['ZMQInteractiveShell','TerminalInteractiveShell']
    
    except:

        return False


class BarChart:

    def __init__(self):
        pass


    def saveChart(self,filename=""):



        current_file = open(filename, mode = "w", encoding="utf-8")
        current_file.write(self.current_html)
        current_file.close()


    def showChart(self):

        self.constructChartHTML()
        self.saveChart('deneme.html')

        if isEnviromentIPython():

            display(HTML("<iframe width='1000' height='700' frameBorder='0' src='deneme.html'></iframe>"))
        
        else:
            webbrowser.open('deneme.html')

class BasicBarChart(BarChart):



    def __init__(self,
                df,
                title,
                xname,
                yname,
                xtitle="",
                ytitle="",
                backgroundcolor=""
                ):

        
        if xtitle == "":
            xtitle = xname
        
        if ytitle == "":
            ytitle = yname
        


        self.data_of_chart =  df.to_json(orient="records") 

        self.max_y_value = str(df[yname].max())

        self.title  = title
        self.xname = xname
        self.yname = yname
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.backgroundcolor = backgroundcolor

        self.current_html = ""

        self.fontcolor = "#000" # Default is black

        self.barcolor = "#416c9b"

        self.horizontal_grids = False
        self.vertical_grids = False


    def setFontColor(self, fontcolor):
        self.fontcolor = fontcolor

    def setBarColor(self,barcolor):
        self.barcolor = barcolor

    def setHorizontalLines(self,value):
        self.horizontal_grids = value
    
    def setVerticalLines(self,value):
        self.vertical_grids = value

    
    def constructDesignParts(self) -> str:
        self.current_html = ""


        self.current_html = barcharttemplates.static_initial_part + barcharttemplates.design_part

        self.current_html = self.current_html.replace("|barcolor|",self.barcolor)
        self.current_html = self.current_html.replace("|textcolor|", self.fontcolor)

    def constructChartHTML(self) -> str:


        self.constructDesignParts()




        bar_chart_script_formatted = barcharttemplates.script_part.replace("|jsondata|", self.data_of_chart)
        bar_chart_script_formatted = bar_chart_script_formatted.replace("|maxy|",self.max_y_value)
        bar_chart_script_formatted = bar_chart_script_formatted.replace("|xname|", self.xname)
        bar_chart_script_formatted = bar_chart_script_formatted.replace("|yname|", self.yname)

        bar_chart_script_formatted = bar_chart_script_formatted.replace("|title|", self.title)

        bar_chart_script_formatted = bar_chart_script_formatted.replace("|xtitle|", self.xtitle)
        bar_chart_script_formatted = bar_chart_script_formatted.replace("|ytitle|", self.ytitle)

        bar_chart_script_formatted = bar_chart_script_formatted.replace("|backgroundcolor|", self.backgroundcolor)


        if self.horizontal_grids is False:
            bar_chart_script_formatted = bar_chart_script_formatted.replace("|horizontallinepart|","")
        else:
            bar_chart_script_formatted  = bar_chart_script_formatted.replace("|horizontallinepart|",barcharttemplates.horizontal_lines_part)



        if self.vertical_grids is False:
            bar_chart_script_formatted = bar_chart_script_formatted.replace("|verticallinepart|","")
        else:
            bar_chart_script_formatted  = bar_chart_script_formatted.replace("|verticallinepart|",barcharttemplates.vertical_lines_part)



        self.current_html = self.current_html + bar_chart_script_formatted

        return self.current_html



class Horizontal(BarChart):
    pass




class StackedBarChart:
    pass


if __name__ ==  '__main__':
    my_df = pd.DataFrame(columns=["Sehir","Nufus"])

    my_df["Sehir"] = ["Istanbul","Ankara","Bursa"]
    my_df["Nufus"] = [15000,4000,3000]
    my_df["Color"] = ["#5d2f8e","#5d2f8e","#5d2f8e"]


    my_chart = BasicBarChart(my_df,"Deneme","Sehir","Nufus","Sehir","Nufus")
    #my_chart.setHorizontalLines(True)
    #my_chart.setVerticalLines(True)
    my_chart.setFontColor("gray")

    my_chart.showChart()



