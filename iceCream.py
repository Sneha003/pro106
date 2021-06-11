import csv
import plotly.express as px
with open ('Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv') as f:
  data=csv.DictReader(f)
  newdata=list(data)
  print(newdata)

graph=px.scatter(newdata , x='Temperature',y='Ice-cream Sales( ₹ )')
graph.show()