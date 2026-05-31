import asyncio
from dotenv import load_dotenv
load_dotenv()

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools

from langchain.agents import create_agent

llm = ChatOpenAI(temperature=0)

stdio_server_params = StdioServerParameters(
    command="python", 
    args=["/Users/s0v00ar/agentic/mycode/mcp-servers/mcp-crash-course/servers/math_server.py"]
)


async def main():
    async with stdio_client(stdio_server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            print("Session initialized")
            tools = await load_mcp_tools(session)
            # print(tools)

            agent = create_agent(
                llm,
                tools
            )
            result = await agent.ainvoke({"messages": [HumanMessage(content="What is result of (2 + 3) * 4 ?  use tools to get the answer")]})
            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
