import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import os

class Plotter:
    def __init__(self, json_url):
        # download the json file from the url
        response = requests.get(json_url)
        # convert the json to a pandas dataframe
        self.df = pd.read_json(response.content)
        # create a folder for plots if it does not exist
        self.plot_folder = "plots"
        if not os.path.exists(self.plot_folder):
            os.makedirs(self.plot_folder)
        # initialize a list for plot paths
        self.plot_paths = []

    def draw_plots(self):
        # draw a bar plot for the number of corners
        plt.figure(figsize=(10, 6))
        sns.barplot(x="room", y="gt_corners", data=self.df, hue="rb_corners")
        plt.title("Number of corners per room")
        plt.xlabel("Room")
        plt.ylabel("Number of corners")
        # save the plot and append the path to the list
        corner_plot = os.path.join(self.plot_folder, "corner_plot.png")
        plt.savefig(corner_plot)
        self.plot_paths.append(corner_plot)
        # draw a box plot for the deviation values
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.df[["mean", "max", "min", "std"]])
        plt.title("Deviation values per room")
        plt.xlabel("Deviation")
        plt.ylabel("Degrees")
        # save the plot and append the path to the list
        deviation_plot = os.path.join(self.plot_folder, "deviation_plot.png")
        plt.savefig(deviation_plot)
        self.plot_paths.append(deviation_plot)
        # return the list of plot paths
        return self.plot_paths