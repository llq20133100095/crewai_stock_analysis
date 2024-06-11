# from dotenv import load_dotenv
# dotenv_path = '.env.example'
# load_dotenv(dotenv_path)

# from langchain.agents import AgentType, initialize_agent
# from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
# from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(temperature=0.0)
# tools = [YahooFinanceNewsTool()]
# agent_chain = initialize_agent(
#     tools,
#     llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     verbose=True,
# )

# res = agent_chain.run(
#     "What happens today with Microsoft stocks?",
# )
# print(res)


import yfinance as yf

ticker = "MSFT"
company = yf.Ticker(ticker)

try:
    isin = company.isin
    print(isin)
except Exception as e:
    print(f"An error occurred: {e}")
