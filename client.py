from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    async with sse_client(url="http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:

            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print("Available tools:", tools)

            # Ask user for input
            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b: "))

            # Call add tool
            result = await session.call_tool("add", arguments={"a": a, "b": b})
            print("Addition Result:", result.content[0].text)

            # Call subtract tool
            result = await session.call_tool("subtract", arguments={"a": a, "b": b})
            print("Subtraction Result:", result.content[0].text)

            # List resources
            resources = await session.list_resources()
            print("Available resources:", resources)

            # Read static resource
            content = await session.read_resource("resource://some_static_resource")
            print("Static Resource:", content.contents[0].text)

            # Read dynamic greeting resource
            name = input("Enter your name for greeting: ")
            content = await session.read_resource(f"greeting://{name}")
            print("Greeting Resource:", content.contents[0].text)

            # List prompts
            prompts = await session.list_prompts()
            print("Available prompts:", prompts)

            # Use code review prompt
            code = input("Enter some code to review: ")
            prompt = await session.get_prompt("review_code", arguments={"code": code})
            print("Code Review Prompt:", prompt)

            # Use debug error prompt
            error = input("Enter an error message to debug: ")
            prompt = await session.get_prompt("debug_error", arguments={"error": error})
            print("Debug Prompt:", prompt)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
