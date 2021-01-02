import pandas as pd
import scatter_template
import webbrowser


class ScatterPlot:


	def __init__(self,
				df,
				title,
				xname,
				yname,
				xtitle,
				ytitle,
				backgroundcolor =""
		):

		self.data_of_chart = df.to_json(orient="records")
	

	#	self.max_y_value = str(df[yname].max())

		self.title = title
		self.xname = xname
		self.yname = yname
		self.xtitle = xtitle
		self.ytitle = ytitle
		self.backgroundcolor = backgroundcolor
	
		self.current_html = ""
		self.fontcolor = "#000"

		self.horizontal_grids = False
		self.vertical_grids = False


	def setFontColor (self, fontcolor):
		self.fontcolor = fontcolor



	def setFontColor(self, fontcolor):
		self.fontcolor = fontcolor

	def setBarColor(self,barcolor):
    		self.barcolor = barcolor

	def setHorizontalLines(self,value):
    		self.horizontal_grids = value
    
	def setVerticalLines(self,value):
    		self.vertical_grids = value


	def constructorDesignPart(self) -> str:
		self.current_html = ""

		self.current_html = scatter_template.initial_html + scatter_template.css

	#--------------------------------------------------------------

	def constructChartHTML(self) -> str:

		self.constructorDesignPart()


		scatter_html_formatted = scatter_template.d3_js.replace("|formatted_data|", self.data_of_chart)

		self.current_html = self.current_html + scatter_html_formatted

		return self.current_html



	def showChart(self):
		my_chart.constructChartHTML()
		self.saveChart('deneme.html')

		webbrowser.open('deneme.html')

	def saveChart(self,filename =""):

		current_file = open(filename, mode = "w", encoding = "utf-8")
		current_file.write(self.current_html)
		current_file.close()




class ScatterPlotChart:
	pass

if __name__ == '__main__':

	testDF = pd.DataFrame(columns = ['name','type','data_x','data_y'])
	import names
	import random 

	name = []
	types = []
	x = []
	y = []
	for i in range(16):
		name.append(names.get_first_name())
		types.append(random.randint(1,5))
		x.append(random.randint(0,90))
		y.append(random.randint(0,5))
		
	testDF['name'] = name
	testDF['type'] = types
	testDF['data_x'] = x
	testDF['data_y'] = y

	my_chart = ScatterPlot(testDF,"cathy","cathy","cathy","cathy","cathy")
	my_chart.showChart()
