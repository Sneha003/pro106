import csv
import plotly.express as px
with open ('Size of TV,_Average time spent watching TV in a week (hours).csv') as f:
  data=csv.DictReader(f)
  newdata=list(data)
  print(newdata)

graph=px.scatter(newdata , x='Size of TV',y='\tAverage time spent watching TV in a week (hours)')
graph.show()