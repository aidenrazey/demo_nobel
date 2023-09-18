import pandas as pd
import matplotlib.pyplot as plt

class NobelPrizePlot:

    def __init__(self, nobel_data: pd.DataFrame):
        self.nobel_data = nobel_data

    def create_plot(self):
        plt.figure(figsize=(14,8))
        plt.scatter(self.nobel_data['Year'], self.nobel_data['Prize Amount']/1000000, color='blue')
        plt.xticks(ticks=range(1900,2025,5), rotation=90)
        plt.xlabel('Award Year')
        plt.ylabel('Prize Award Amount, SEK millions (inflation adj.)')
        plt.title('Average Nobel Prize Award Money by Year')
        plt.show()

    def save_plot(self, plot_filename: str = "nobel_prizes") -> None:
        self.create_plot()
        filename_with_ext = f"{plot_filename}.png"
        plt.savefig(filename_with_ext)
        print(f"File has been saved as {filename_with_ext}.")