import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["reading time"].tolist()
fig = ff.create_distplot ([data],["reading time"],show_hist=False)
fig.show()
print("Population mean:-",statistics.mean(data))
std_deviation = statistics.stdev(data)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["reading time"],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    print("sampling mean:-",statistics.mean(mean_list))
setup()

## finding 1 standard deviation start and end values, and 2 standard deviation start and end values
first_std_deviation_start,first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*std_deviation), mean+(2*std_deviation)
#Plotting the chart;and lines for mean ,1 standard deviation and 2 stardard deviation and 3 standard deviation 
fig = ff.create_distplot([data],["reading time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0, 0.17],mode = "lines", name ="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0, 0.17], mode = "lines", name = "New mean sample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0, 0.17], mode = "lines", name = " New mean sample"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0, 0.17], mode = "lines", name = "New mean Sample"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0, 0.17], mode = "lines", name = " New mean sample"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0, 0.17], mode = "lines", name = "New mean sample"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0, 0.17], mode = "lines", name = " New mean sample"))
fig.show()
#Printing the findings
list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))
#finding the z score using the formula
z_score = (New_mean_sample-sampling_mean)/std_deviation
print("the z score is :" z_score)