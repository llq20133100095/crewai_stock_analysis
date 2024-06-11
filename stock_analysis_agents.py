from crewai import Agent

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

class StockAnalysisAgents():
  def financial_analyst(self):
    return Agent(
      role='最佳财务分析师',
      goal="""用您的财务数据给所有客户留下深刻印象和市场趋势分析""",
      backstory="""经验最丰富的金融分析师，在股市分析和投资策略方面拥有丰富的专业知识，为一位超级重要的客户工作。""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        CalculatorTools.calculate,
        SECTools.search_10q,
        SECTools.search_10k
      ]
    )
    

  def research_analyst(self):
    return Agent(
      role='股票研究分析师',
      goal="""最擅长收集、解释数据并让客户惊叹""",
      backstory="""被称为最佳研究分析师，你擅长筛选新闻、公司公告，以及市场情绪。现在你正在为一位超级重要的客户工作""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        YahooFinanceNewsTool(),
        SECTools.search_10q,
        SECTools.search_10k
      ]
  )

  def investment_advisor(self):
    return Agent(
      role='私人投资顾问',
      goal="""通过对股票的全面分析和完整的投资建议给客户留下深刻印象""",
      backstory="""你是最有经验的投资顾问，你可以结合各种分析见解来制定战略投资建议。你现在为一个非常重要的客户工作，你需要给他留下深刻印象。""",
      verbose=True,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        CalculatorTools.calculate,
        YahooFinanceNewsTool()
      ]
    )