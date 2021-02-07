
import pandas as pd
from netvis.chart.bar import bar_template
from netvis.chart.bar import verticalbar_template
from netvis.chart.bar import grouppedbarchart_template
from netvis.chart.main.chart import Chart
import webbrowser
from IPython.core.display import display, HTML
from IPython import get_ipython



def BarChart(df,title,xname,yname,group="",xtitle="",ytitle="",backgroundcolor="",orientation="h"):

    if group != "":
        return GrouppedBarChart(df,title,xname,yname,group=group)

    if orientation == "h":
        return HorizontalBarChart(df,title,xname,yname, xtitle,ytitle, backgroundcolor)
    else:
        return VerticalBarChart(df,title,xname,yname, xtitle,ytitle, backgroundcolor)


class BarChartSchema(Chart):
    def __init__(self,
                 df,
                 title,
                 xname,
                 yname,
                 xtitle="",
                 ytitle="",
                 backgroundcolor="#fff"
                 ):

        if xtitle == "":
            xtitle = xname

        if ytitle == "":
            ytitle = yname
        
        self.df = df

        self.data_of_chart = df.to_json(orient="records")

        self.max_y_value = str(df[yname].max())
        self.max_x_value = str(df[xname].max())

        self.title = title
        self.xname = xname
        self.yname = yname
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.backgroundcolor = backgroundcolor

        self.current_html = ""
        self.title_color = ""

        self.fontcolor = "#000"  # Default is black

        self.barcolor = "#416c9b"

        self.horizontal_grids = False
        self.vertical_grids = False

    def setFontColor(self, fontcolor):
        self.fontcolor = fontcolor

    def setBackgroundColor(self, backgroundcolor):
        self.backgroundcolor = backgroundcolor

    def setBarColor(self, barcolor):
        self.barcolor = barcolor

    def setHorizontalLines(self, value):
        self.horizontal_grids = value

    def setVerticalLines(self, value):
        self.vertical_grids = value

    
    def setTitleColor(self,title_color):
        self.title_color = title_color

    def constructDesignParts(self) -> str:
        self.current_html = ""

        self.current_html = bar_template.static_initial_part + bar_template.design_part

        self.current_html = self.current_html.replace(
            "|barcolor|", self.barcolor)

        self.current_html = self.current_html.replace(
            "|textcolor|", self.fontcolor)

        if self.title_color != "":
            self.current_html = self.current_html.replace("|titlecolor|", self.title_color)
        else:
            self.current_html = self.current_html.replace("|titlecolor|", self.fontcolor)
        
        





class VerticalBarChart(BarChartSchema):
    
    def __init__(self,
                 df,
                 title,
                 xname,
                 yname,
                 xtitle="",
                 ytitle="",
                 backgroundcolor=""
                 ):


            super(VerticalBarChart, self).__init__(df,
                 title,
                 xname,
                 yname,
                 xtitle,
                 ytitle,
                 backgroundcolor)

    def constructChartHTML(self) -> str:

        self.constructDesignParts()





        bar_chart_script_formatted = verticalbar_template.script_part.replace(
            "|jsondata|", self.data_of_chart)

        


        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|maxy|", self.max_y_value)
        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|xname|", self.xname)
        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|yname|", self.yname)

        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|title|", self.title)

        """[summary]
        Check if title font color is  specified
        """


        

        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|xtitle|", self.xtitle)
        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|ytitle|", self.ytitle)



        if self.horizontal_grids is False:
            bar_chart_script_formatted = bar_chart_script_formatted.replace(
                "|horizontallinepart|", "")
        else:
            bar_chart_script_formatted = bar_chart_script_formatted.replace(
                "|horizontallinepart|", bar_template.horizontal_lines_part)

        if self.vertical_grids is False:
            bar_chart_script_formatted = bar_chart_script_formatted.replace(
                "|verticallinepart|", "")
        else:
            bar_chart_script_formatted = bar_chart_script_formatted.replace(
                "|verticallinepart|", bar_template.vertical_lines_part)
        
        if self.backgroundcolor != "":
            self.current_html = self.current_html.replace(
                "|backgroundcolor|", self.backgroundcolor)

        else:
                self.current_html = self.current_html.replace(
                "|backgroundcolor|", "#fff")
        

        self.current_html = self.current_html + bar_chart_script_formatted

        return self.current_html


class HorizontalBarChart(BarChartSchema):
    def __init__(self,
                 df,
                 title,
                 xname,
                 yname,
                 xtitle="",
                 ytitle="",
                 backgroundcolor=""
                 ):


            super(HorizontalBarChart, self).__init__(df,
                 title,
                 xname,
                 yname,
                 xtitle,
                 ytitle,
                 backgroundcolor)

            
     


    def constructChartHTML(self) -> str:
        self.constructDesignParts()

        bar_chart_script_formatted = bar_template.script_part.replace(
            "|jsondata|", self.data_of_chart)
        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|maxy|", self.max_y_value)
        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|xname|", self.xname)
        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|yname|", self.yname)

        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|title|", self.title)

        # X axis labels length rotation

        lettersoflabels = "".join(self.df[self.xname].values.tolist())
        
        lengthoflabels = len(lettersoflabels)

        
        if lengthoflabels > 65:
            bar_chart_script_formatted = bar_chart_script_formatted.replace("|rotationtext|",bar_template.text_rotation)
        else:
            bar_chart_script_formatted = bar_chart_script_formatted.replace("|rotationtext|","")

        



        

        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|xtitle|", self.xtitle)
        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|ytitle|", self.ytitle)



        if self.horizontal_grids is False:
            bar_chart_script_formatted = bar_chart_script_formatted.replace(
                "|horizontallinepart|", "")
        else:
            bar_chart_script_formatted = bar_chart_script_formatted.replace(
                "|horizontallinepart|", bar_template.horizontal_lines_part)

        if self.vertical_grids is False:
            bar_chart_script_formatted = bar_chart_script_formatted.replace(
                "|verticallinepart|", "")
        else:
            bar_chart_script_formatted = bar_chart_script_formatted.replace(
                "|verticallinepart|", bar_template.vertical_lines_part)

        self.current_html = self.current_html + bar_chart_script_formatted


        if self.backgroundcolor != "":
            self.current_html = self.current_html.replace(
                "|backgroundcolor|", self.backgroundcolor)

        else:
                self.current_html = self.current_html.replace(
                "|backgroundcolor|", "#fff")
        

        return self.current_html



class GrouppedBarChart(BarChartSchema):

    def __init__(self, df, title, xname, yname,group, xtitle='', ytitle='',grouptitle="",backgroundcolor=''):

        super(GrouppedBarChart, self).__init__(df, title, xname, yname, xtitle=xtitle, ytitle=ytitle, backgroundcolor=backgroundcolor)
        self.grouplabel = group

        self.colorRange = '[' + "','".join(["'#e41a1c",'#377eb8',"#4daf4a'"]) + ']'
    
    def constructChartHTML(self) -> str:

        self.constructDesignParts()

        bar_chart_script_formatted = grouppedbarchart_template.groupped_template.replace(
            "|jsondata|", self.data_of_chart)

        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|title|", self.title)

        
        bar_chart_script_formatted = bar_chart_script_formatted.replace("|groups|", str(self.df.columns.tolist()[1:]))

        bar_chart_script_formatted = bar_chart_script_formatted.replace("|group|",self.grouplabel)

        bar_chart_script_formatted = bar_chart_script_formatted.replace("|colorgroup|",self.colorRange)

        self.current_html = self.current_html + bar_chart_script_formatted

        return self.current_html


