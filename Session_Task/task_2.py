import pandas
import threading

def printit():
  threading.Timer(5.0, printit).start()
  print( "Top 5 Trending Songs!")
  csv =pandas.read_csv('/home/xs450-akatag/Desktop/Session_Task/Videos_Engagement_Metrics.csv')
  Total_Views = csv["Video_Name"].value_counts().head(5)
  print(Total_Views)


printit()
# print( "Top 5 Trending Songs!")
# csv =pandas.read_csv('/home/xs450-akatag/Desktop/Session_Task/Videos_Engagement_Metrics.csv')
# Total_Views = csv["Video_Name"].value_counts().head(5)
# Total_Likes = csv["Video_Name"].value_counts().head(5)
# print(Total_Views)
# print(Total_Likes)
