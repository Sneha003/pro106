import csv
import plotly.express as px
with open ('cups of coffee vs hours of sleep.csv') as f:
  data=csv.DictReader(f)
  newdata=list(data)
  print(newdata)

graph=px.scatter(newdata , x='Coffee in ml',y='sleep in hours')
graph.show()