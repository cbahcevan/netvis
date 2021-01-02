
import pandas as pd
from netvis.chart.bar import bar_template
import netvis.chart.main.chart as Chart
import webbrowser
from IPython.core.display import display, HTML
from IPython import get_ipython


class BarChart(Chart):
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

        self.data_of_chart = df.to_json(orient="records")

        self.max_y_value = str(df[yname].max())

        self.title = title
        self.xname = xname
        self.yname = yname
        self.xtitle = xtitle
        self.ytitle = ytitle
        self.backgroundcolor = backgroundcolor

        self.current_html = ""

        self.fontcolor = "#000"  # Default is black

        self.barcolor = "#416c9b"

        self.horizontal_grids = False
        self.vertical_grids = False

    def setFontColor(self, fontcolor):
        self.fontcolor = fontcolor

    def setBarColor(self, barcolor):
        self.barcolor = barcolor

    def setHorizontalLines(self, value):
        self.horizontal_grids = value

    def setVerticalLines(self, value):
        self.vertical_grids = value

    def constructDesignParts(self) -> str:
        self.current_html = ""

        self.current_html = bar_template.static_initial_part + bar_template.design_part

        self.current_html = self.current_html.replace(
            "|barcolor|", self.barcolor)
        self.current_html = self.current_html.replace(
            "|textcolor|", self.fontcolor)

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

        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|xtitle|", self.xtitle)
        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|ytitle|", self.ytitle)

        bar_chart_script_formatted = bar_chart_script_formatted.replace(
            "|backgroundcolor|", self.backgroundcolor)

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

        return self.current_html
