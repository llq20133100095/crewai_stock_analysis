from crewai import Agent, Task, Crew, Process

from textwrap import dedent
from agents import FinancialResearchAgents
from tasks import MarkdownReportCreationTasks

class FinancialCrew:
    def __init__(self, data):
        self.data = data

    def run(self):
        agents = FinancialResearchAgents()
        tasks = MarkdownReportCreationTasks()

        # AGENTS
        report_creator = agents.markdown_report_creator()
        chart_creator = agents.chart_creator()
        markdown_writer = agents.markdown_writer()

        # TASKS
        parse_inputs_task = tasks.parse_input(report_creator, self.data)
        retrieve_metrics_data_task = tasks.get_data_from_api(report_creator, [parse_inputs_task])
        create_chart_task = tasks.create_charts(chart_creator, [retrieve_metrics_data_task])
        create_markdown_file_task = tasks.write_markdown(markdown_writer, [create_chart_task])

        # Define your custom crew here
        crew = Crew(
            agents=[
                report_creator, 
                chart_creator,
                markdown_writer
                ],
            tasks=[
                parse_inputs_task,
                retrieve_metrics_data_task,
                create_chart_task,
                create_markdown_file_task
                ],
            verbose=True,
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Welcome to Report Creator Crew")
    print("-------------------------------")
    data = input(dedent("""Enter company symbol followed by the metrics you want to add to the markdown file report:\n>> """))

    mycrew = FinancialCrew(data)
    result = mycrew.run()
    print("\n\n########################")
    print("## Here is your result:")
    print("########################\n")
    print(result)