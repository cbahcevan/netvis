
import pandas as pd
import webbrowser
from IPython.core.display import display, HTML
from IPython import get_ipython

def isEnviromentIPython() -> bool:
    try:
        shell_name = get_ipython().__class__.__name__
        return shell_name in ['ZMQInteractiveShell','TerminalInteractiveShell']
    
    except:
        return False

class Chart:

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


if __name__ ==  '__main__':
    print('Main chart class is imported.')



