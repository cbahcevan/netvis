import pandas as pd
from netvis.chart.pie import pie_template
import webbrowser
import numpy as np
import netvis.chart.main.chart as Chart
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


class PieChart:
    def __init__(self,
                 df,
                 title,
                 xname,
                 yname
                 ):

        self.df = df
        self.title = title
        self.xname = xname
        self.yname = yname

        self.current_html = ""

    def constructDesignParts(self) -> str:
        self.current_html = ""
        self.current_html = pie_template.static_initial_part + pie_template.design_part

    def constructChartHTML(self) -> str:

        self.constructDesignParts()

        jsonLabelsData = list(self.df[self.xname])
        jsonValuesData = list(self.df[self.yname])
        colors = color_generator(len(jsonLabelsData))

        pie_chart_html_formatted = pie_template.script_part.replace(
            "|jsonValuesData|", str(jsonValuesData))
        pie_chart_html_formatted = pie_chart_html_formatted.replace(
            "|jsonLabelsData|", str(jsonLabelsData))
        pie_chart_html_formatted = pie_chart_html_formatted.replace(
            "|jsonColorsData|", str(colors))
        pie_chart_html_formatted = pie_chart_html_formatted.replace(
            "|Title|", self.title)

        self.current_html = self.current_html + pie_chart_html_formatted

        return self.current_html

    def showChart(self):
        self.constructChartHTML()
        self.saveChart('deneme.html')
        display(HTML(
            "<iframe width='800' height='400' frameBorder='0' src='deneme.html'></iframe>"))

        # webbrowser.open('deneme.html')

    def saveChart(self, filename=""):
        current_file = open(filename, mode="w", encoding="utf-8")
        current_file.write(self.current_html)
        current_file.close()
