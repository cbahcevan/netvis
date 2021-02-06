import pandas as pd
from netvis.chart.pie import pie_template
import webbrowser
import numpy as np
from netvis.chart.main.chart import Chart
from IPython.core.display import display, HTML


def color_generator(no_colors):
    colors = []
    while len(colors) < no_colors:
        random_number = np.random.randint(0, 16777215)
        hex_number = format(random_number, 'x')
        if len(hex_number) == 6:
            hex_number = '#' + hex_number
            colors.append(hex_number)
    return colors


class PieChart(Chart):
    def __init__(self,
                 df,
                 title,
                 subtoptitle,
                 subbottomtitle,
                 xname,
                 yname
                 ):

        self.df = df
        self.title = title
        self.subtoptitle = subtoptitle
        self.subbottomtitle = subbottomtitle
        self.title = title
        self.xname = xname
        self.yname = yname

        self.current_html = ""

    def constructDesignParts(self) -> str:
        self.current_html = ""
        self.current_html = pie_template.static_initial_part + pie_template.design_part

    def constructChartHTML(self) -> str:

        self.constructDesignParts()

        jsonValuesData = str(self.df.to_json(
            orient="records")).replace('"', "'")

        # print(jsonValuesData)

        pie_chart_html_formatted = pie_template.script_part.replace(
            "|jsonValuesData|", (jsonValuesData).strip('\"'))

        pie_chart_html_formatted = pie_chart_html_formatted.replace(
            "|Title|", self.title)
        pie_chart_html_formatted = pie_chart_html_formatted.replace(
            "|SubTopTitle|", self.subtoptitle)
        pie_chart_html_formatted = pie_chart_html_formatted.replace(
            "|SubBottomTitle|", self.subbottomtitle)

        self.current_html = self.current_html + pie_chart_html_formatted

        return self.current_html
