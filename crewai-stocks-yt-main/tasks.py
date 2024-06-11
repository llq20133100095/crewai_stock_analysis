from crewai import Task
from textwrap import dedent
from typing import List
from pydantic import BaseModel

class MarkdownReportCreationTasks:
    def __tip_section(self):
        return "If you do your BEST WORK and return exactly what I ask, I'll give you a $10,000 commission!"

    def parse_input(self, agent, data: str):
        return Task(
               description=dedent(f"""
            **Task**: Extract relevant data from string.
            **Description**: Take the input string and get the company
            symbol out of it and also any metrics that are available.

            **Parameters**: 
            - data: {data}

            **Notes**
            {self.__tip_section()}
            """
        ),
            agent=agent,
            expected_output="""A list of dictionaries containing the symbol and metric.
            Example output: `[{'symbol': 'MSTR', 'metric': 'cogs'}, {'symbol': 'MSTR', 'metric': 'fcf'}]`"""
        )

    def get_data_from_api(self, agent, context):
        return Task(
               description=dedent(f"""
            **Description**: For each metric, look up the metric for the symbol provided by using the tool.

            **Notes**
            You MUST use QuickFS to get data for EVERY metric that the client requests. You may have to complete this task multiple times.
            {self.__tip_section()}
            """
        ),
            agent=agent,
            context=context,
            expected_output="""A list of metrics and the data retrieved for each one. 
            Example output: [
                {metric:'fcf', data: [...data_points],
                {metric:'cogs', data: [...data_points],
                {...}
                ]"""
        )

    def create_charts(self, agent, context) -> Task:
        return Task(
            description=dedent(f"""
                Create graphics of the data representing financial metrics of a company.  DO NOT change the metric name when you create the title of the chart.

                {self.__tip_section()}
            """),
            agent=agent,
            context=context,
            expected_output="""
                A list of the file locations of the created charts.
                Example output: [fcf_chart.png, cogs_chart.png]
                """
        )


    def write_markdown(self, agent, context):
        return Task(
            description=dedent(f"""
                **Task**: Insert markdown syntax to md file
                **Description**: Take the input file location and insert it into a markdown file.
                For Example: writes ![](fcf_chart.png) to markdown file.

                YOU MUST USE MARKDOWN SYNTAX AT ALL TIMES.

                **Notes**
                {self.__tip_section()}
            """
        ),
            agent=agent,
            expected_output="""A report.md file formatted in markdown syntax. 
            Example output: 
                ![](./COGS_chart.png)\n
                ![](./FCF_chart.png)
                """,
            context = context,
        )
