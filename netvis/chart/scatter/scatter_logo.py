import pandas as pd
from netvis.chart.scatter import scatter_template_logo
from netvis.chart.main.chart import Chart
import webbrowser
from IPython.core.display import display, HTML
from IPython import get_ipython


class ScatterPlot(Chart):

    def __init__(self,
                 df,
                 title="",
                 xtitle="",
                 ytitle="",
                 backgroundcolor=""
                 ):


        self.data_of_chart = df.to_json(orient="records")

        self.title = title
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.backgroundcolor = backgroundcolor

        self.current_html = ""
        self.title_color = ""

        self.fontcolor = "#000"

        self.horizontal_grids = False
        self.vertical_grids = False

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

        self.current_html = scatter_template_logo.initial_html + scatter_template_logo.css


    def constructChartHTML(self) -> str:

        self.constructorDesignPart()

        scatter_html_formatted = scatter_template_logo.d3_js.replace(
            "|jsondata|", self.data_of_chart)

        scatter_html_formatted = scatter_html_formatted.replace(
			"|xtitle|", self.xtitle)

        scatter_html_formatted = scatter_html_formatted.replace(
			"|ytitle|",self.ytitle)

        scatter_html_formatted = scatter_html_formatted.replace(
			"|title|",self.title)


        self.current_html = self.current_html + scatter_html_formatted

        return self.current_html
