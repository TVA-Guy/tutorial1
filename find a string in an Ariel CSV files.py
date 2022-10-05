from dash import Dash, dash_table
import pandas as pd

app = Dash(__name__)

nstr: str

fteg = open("C:/Users/schneka00/OneDrive - INNIO/Documents/python stuff/temp files/LC8.csv")         # open CSV file
while True:
    nstr = fteg.readline()
    nstr.strip()
    print(nstr)
    if len(nstr) == 0:
        break
    result = nstr.find('Combined')
    if result != -1:
        print(nstr)


#root.mainloop()

if __name__ == '__main__':
    app.run_server(debug=True)