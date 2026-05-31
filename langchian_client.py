import asyncio

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiMCPClient
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

load_dotenv()

llm = ChatOpenAI(temperature=0)


async def main():
    print("Hello from langchian_client!")

if __name__ == "__main__":
    asyncio.run(main())