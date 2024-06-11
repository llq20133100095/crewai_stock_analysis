import os
import json
from dotenv import load_dotenv
from quickfs import QuickFS
from langchain.tools import tool
from pydantic.v1 import BaseModel, validator, Field
from typing import List
import random
import matplotlib.pyplot as plt
load_dotenv()

class ExtractionTools():
    @tool("Extract symbol and metrics")
    def parse_string(data:str):
        """
        Useful to extract the relevant information from the input string. Parses string and extracts the symbol and all of the relevant metrics requested.
        """
        words = data.split()
        symbol = words[0]
        result_list = [{"symbol":symbol, "metric":metric} for metric in words[1:]]

        return result_list 

class DataFetchingTools():
    @tool("Retrieve metric data from QuickFS API.")
    def get_metric_data_from_quickfs(symbol, metric: str):
        """
        Useful to retrieve data from the QuickFS API based on the given symbol and metric.

        :param symbol: str, only one symbol
        :param metric: str, only one metric
        :return value: list, A list containing the data points retrieved
        Return value example: [...data_points]
        """
        api_key = os.environ.get("QUICKFS_API_KEY")
        client = QuickFS(api_key)
      
        res = client.get_data_range(symbol=f'{symbol}:US', metric=metric, period='FY-9:FY')

        return res

class CreateChartInput(BaseModel):
    metric: str
    data: List[float]

class CreateChartOutput(BaseModel):
    file_path: str

class ChartingTools():
    @tool("Create a chart of the data")
    def create_chart(metric_name:str, data:List) -> CreateChartOutput:
        """
        Creates a bar chart graphic based on the provided metric and data.

        Parameters:
        - metric_name (str): The name of the metric to be visualized on the chart.
        - data (List[float]): A list of numerical data points representing the metric over time.

        Returns:
        - file_path (str): The file path to the saved chart image.
        
        Example:
        - create_chart(metric='revenue', data=[100, 150, 120, 200, 180]))
        - Returns: CreateChartOutput(file_path='./{{metric_name}}.png')
        """
        years = list(range(len(data)))

        # Generate a random color for all bars
        bar_color = f'#{random.randint(0, 0xFFFFFF):06x}'

        fig, ax = plt.subplots()
        ax.bar(years, data, color=bar_color)
        ax.set_xlabel('Years')
        ax.set_title(metric_name)

        # Save the figure to the current directory
        file_path = f"./{metric_name.replace(' ', '_')}_chart.png"
        fig.savefig(file_path, format='png')
        plt.close(fig)  # Close the Matplotlib figure to free resources

        return CreateChartOutput(file_path=file_path)


class MarkdownTools():
    @tool("Write text to markdown file")
    def write_text_to_markdown_file(text: str) -> str:
        """Useful to write markdown text in a *.md file.
           The input to this tool should be a string representing what should used to create markdown syntax. Takes the location of the file as a string and creates the correct syntax thats compatible with an .md file eg report.md

            **Example** Writes `![](fcf_chart.png)` to report.md file.
           
           :param text: str, the string to write to the file
           """
        try:
            markdown_file_path = r'report.md'
            
            with open(markdown_file_path, 'w') as file:
                file.write(text)
            
            return f"File written to {markdown_file_path}."
        except Exception:
            return "Something has gone wrong writing images to markdown file."