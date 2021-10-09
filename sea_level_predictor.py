import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    x = data['Year']
    y = data['CSIRO Adjusted Sea Level']




    # Create scatter plot
    plt.scatter(x,y)
    
    




    # Create first line of best fit
    res=linregress(x,y)
    x_pre= pd.Series([i for i in range(1880,2051)])
    y_pre= res.slope*x_pre + res.intercept
    plt.plot(x_pre,y_pre,'r')



    # Create second line of best fit
    new_data= data.loc[data['Year']>=2000]
    new_x= new_data['Year']
    new_y= new_data['CSIRO Adjusted Sea Level']
    new_res=linregress(new_x,new_y)
    new_x_pred= pd.Series([i for i in range(2000,2051)])
    new_y_pred= new_res.slope*new_x_pred + new_res.intercept
    plt.plot(new_x_pred, new_y_pred,'blue')


    # Add labels and title
  
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    