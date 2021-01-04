
import pandas as pd
from netvis.chart.scatter import scatter_template
from netvis.chart.main.chart import Chart
import webbrowser
from IPython.core.display import display, HTML
from IPython import get_ipython


class ScatterPlot(Chart):

    def __init__(self,
                 df,
                 title="",
                 xname,
                 yname,
                 xtitle="",
                 ytitle="",
                 backgroundcolor=""
                 ):
        if xtitle = "":
            xtitle = xname
        if ytitle = "":
			ytitle = yname

        self.data_of_chart = df.to_json(orient="records")

    	self.max_y_value = str(df[yname].max())

        self.title = title
        self.xname = xname
        self.yname = yname
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.backgroundcolor = backgroundcolor

        self.current_html = ""
		self.title_color = ""

        self.fontcolor = "#000"

        self.horizontal_grids = False
        self.vertical_grids = False

    def setFontColor(self, fontcolor):
        self.fontcolor = fontcolor

    def setHorizontalLines(self, value):
        self.horizontal_grids = value

    def setVerticalLines(self, value):
        self.vertical_grids = value

	def setTitleColor(self,title_color):
		self.title_color = title_color

    def constructorDesignPart(self) -> str:
        self.current_html = ""

        self.current_html = scatter_template.initial_html + scatter_template.css


    def constructChartHTML(self) -> str:

        self.constructorDesignPart()

        scatter_html_formatted = scatter_template.d3_js.replace(
            "|formatted_data|", self.data_of_chart)

		scatter_html_formatted = scatter_html_formatted.replace(
			"|xtitle|", self.xtitle)

		scatter_html_formatted = scatter_html_formatted.replace(
			"|ytitle|",self.ytitle)

		scatter_html_formatted = scatter_html_formatted.replace(
			"|title|",self.title)

		if self.title_color != "":
			bar_chart_script_formatted = bar_chart_script_formatted.replace("|titlecolor|", self.title_color)
        else:
            bar_chart_script_formatted = bar_chart_script_formatted.replace("|titlecolor|", self.fontcolor)




        self.current_html = self.current_html + scatter_html_formatted

        return self.current_html
