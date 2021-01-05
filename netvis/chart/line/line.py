import pandas as pd
from netvis.chart.line import line_template
from netvis.chart.main.chart import Chart
import webbrowser
from IPython.core.display import display, HTML
from IPython import get_ipython


class LineChart(Chart):

    def __init__(self,
                 df,
                 title="",
                 xtitle="",
                 ytitle="",
                 color="black",
                 backgroundcolor=""
                 ):


        self.data_of_chart = df.to_json(orient="records")

        self.title = title
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.color = color
        self.backgroundcolor = backgroundcolor

        self.current_html = ""
        self.title_color = ""

        self.fontcolor = "#000"



#------------ needs to be adjusted properly ------------------#
    def setFontColor(self, fontcolor):
        self.fontcolor = fontcolor

    def setHorizontalLines(self, value):
        self.horizontal_grids = value

    def setVerticalLines(self, value):
        self.vertical_grids = value

    def setTitleColor(self,title_color):
        self.title_color = title_color

#------------ needs to be adjusted properly ------------------#


    def constructorDesignPart(self) -> str:
        self.current_html = ""

        formatted_line_css = line_template.css.replace('|line-color|',
        self.color)

        self.current_html = line_template.initial_html + formatted_line_css


    def constructChartHTML(self) -> str:

        self.constructorDesignPart()

        line_html_formatted = line_template.d3_js.replace(
            "|jsondata|", self.data_of_chart)

        line_html_formatted = line_html_formatted.replace(
			"|xtitle|", self.xtitle)

        line_html_formatted = line_html_formatted.replace(
			"|ytitle|",self.ytitle)

        line_html_formatted = line_html_formatted.replace(
			"|title|",self.title)



        self.current_html = self.current_html + line_html_formatted

        return self.current_html
