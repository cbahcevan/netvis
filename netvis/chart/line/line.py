import pandas as pd
import numpy as np
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
                 fontcolor="black",
                 backgroundcolor="",
                 theme="dark"
                 ):

        if len(df.columns) == 2:
            #single line
            df.insert(2, 'type', 'one')

        df.columns = ['data_x','data_y','type']

        self.data_of_chart = df.to_json(orient="records")

        self.title = title
        self.xtitle = xtitle
        self.ytitle = ytitle

        self.backgroundcolor = backgroundcolor
        self.fontcolor = fontcolor
        self.theme = theme

        self.y_isdate = np.issubdtype(df['data_y'].dtype, np.datetime64)
        self.x_isdate = np.issubdtype(df['data_x'].dtype, np.datetime64)

        self.current_html = ""




    def constructorDesignPart(self) -> str:
        self.current_html = ""
        self.current_html = line_template.initial_html + line_template.css.replace('|text-color|',
            self.fontcolor)

        if self.theme == "light":

            self.current_html += line_template.d3_light
            self.current_html = self.current_html.replace('|grid-line|','black')

        elif self.theme == "blue":
            self.current_html += line_template.d3_blue
            self.current_html = self.current_html.replace('|grid-line|','white')

        elif self.theme == 'dark':
            self.current_html += line_template.d3_dark
            self.current_html = self.current_html.replace('|grid-line|','white')

        elif self.theme == 'paper':
            self.current_html += line_template.d3_paper
            self.current_html = self.current_html.replace('|grid-line|','black')

        else:
            print('Invalid Theme/Color')

    def constructChartHTML(self) -> str:

        self.constructorDesignPart()

        line_html_formatted = line_template.d3_js.replace(
            "|jsondata|", self.data_of_chart)

        #date time checker
        if self.x_isdate:
            line_html_formatted = line_html_formatted.replace('var x = d3.scaleLinear()','var x = d3.scaleTime()')

        if self.y_isdate:
            line_html_formatted = line_html_formatted.replace('var x = d3.scaleLinear()','var x = d3.scaleTime()')

        line_html_formatted = line_html_formatted.replace(
			"|xtitle|", self.xtitle)

        line_html_formatted = line_html_formatted.replace(
			"|ytitle|",self.ytitle)

        line_html_formatted = line_html_formatted.replace(
			"|title|",self.title)


        self.current_html = self.current_html + line_html_formatted

        return self.current_html
