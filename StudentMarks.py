import csv
import plotly.express as px
with open ('Student Marks vs Days Present.csv') as f:
  data=csv.DictReader(f)
  newdata=list(data)
  print(newdata)

graph=px.scatter(newdata , x='Marks In Percentage',y='Days Present')
graph.show()