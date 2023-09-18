"""
The purpose of this module is to read in data from the Nobel Prize public API (note, no authentication is required -
see: https://www.nobelprize.org/about/developer-zone-2/ ) and provide a simple summary of the average prize awarded across
the years. Please note that you can use any dependencies that you may require, and create any methods you think would
create a logical interface.

Once the task has been finished to your satisfaction, think about how this could be integrated into a wider system: what
are some ways these results could be served to end users (and how could this be done, without going into very specific
details)? What are some trade-offs if you can think of a few different approaches?
"""
import pandas as pd

from api_connection import NobelApiConnection
from nobel_data_plot import NobelPrizePlot

#function expecting input of a dataframe, also expected to return a dataframe
def aggregate_nobel_data(data: pd.DataFrame) -> pd.DataFrame:
    # group data by year, taking mean average of the GBP prize amount
    agg_data = data.groupby(['awardYear'])['prizeAmountAdjusted'].agg(['mean']).reset_index()
    # rename columns
    agg_data.columns = ['Year', 'Prize Amount']
    # return aggregated dataframe
    return agg_data

# if script is being run directly..
if __name__ == '__main__':
    # Connect to API and read in dataset
    api_conn = NobelApiConnection("https://api.nobelprize.org/2.1/nobelPrizes")
    nobel_data = api_conn.read_data()
    # Aggregate data to obtain average prize awarded per year
    aggregated_data = aggregate_nobel_data(nobel_data)
    # create plot of aggregated data
    prize_plot = NobelPrizePlot(aggregated_data)
    prize_plot.create_plot()
    # save plot to a file
    prize_plot.save_plot()