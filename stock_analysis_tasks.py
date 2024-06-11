from crewai import Task
from textwrap import dedent

class StockAnalysisTasks():
  def research(self, agent, company):
    return Task(description=dedent(f"""

        收集和总结最近的新闻文章，出版
        发布，以及与股票相关的市场分析
        其行业。
        特别关注任何重大事件、市场
        情绪和分析师的意见。还包括即将推出的
        收入等事件。
          
        您的最终答案必须是一份包含
        最新消息的综合摘要，任何值得注意的
        市场情绪的转变，以及对
        股票。
        还要确保归还股票行情。
                
        {self.__tip_section()}
          
        请确保尽可能使用最新的数据。
          
        客户选择的公司：{company}
      """),
      agent=agent,
      expected_output="Detailed financial analysis and strategic recommendations",
    )
    
  def financial_analysis(self, agent): 
    return Task(description=dedent(f"""

        对股票的财务状况进行彻底分析
        健康和市场表现。
        这包括检查关键的财务指标，如
        市盈率、每股收益增长、收入趋势，以及
        债务股本比率。
        此外，比较分析股票的表现
        其行业同行和整体市场趋势。

        您的最终报告必须在提供的摘要基础上进行扩展
        但现在包括对股票的明确评估
        财务状况及其优势和劣势，
        以及在当前与竞争对手的竞争中
        市场情景。{self.__tip_section()}

        请确保尽可能使用最新的数据。
      """),
      agent=agent,
      expected_output="Detailed financial analysis and strategic recommendations",
    )

  def filings_analysis(self, agent):
    return Task(description=dedent(f"""
        分析EDGAR针对有问题股票提交的最新10-Q和10-K文件。
        重点关注管理层的讨论和分析、财务报表、内幕交易活动和任何披露的风险等关键部分。
        提取可能影响股票未来表现的相关数据和见解。

        您的最终答案必须是一份扩展报告，该报告现在还强调了这些文件的重要发现，包括您的客户的任何危险信号或积极指标。
        {self.__tip_section()} 
      """),
      agent=agent,
      expected_output="Detailed financial analysis and strategic recommendations",
    )

  def recommend(self, agent):
    return Task(description=dedent(f"""
        审查并综合由提供的分析
      财务分析师和研究分析师。
      将这些见解结合起来，形成一个全面的
      投资建议。
              
      你必须考虑所有方面，包括财务
      健康、市场情绪和定性数据
      EDGAR文件。

      确保包括一个显示内部人士的部分
      交易活动以及收益等即将发生的事件。

      您的最终答案必须是针对您的
      顾客它应该是一份完整的超级详细的报告，提供
      明确的投资立场和战略以及支持性证据。
      为您的客户制作美观且格式良好的表格。
        {self.__tip_section()}
      """),
      agent=agent,
      expected_output="Detailed financial analysis and strategic recommendations",
    )

  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commission!"
