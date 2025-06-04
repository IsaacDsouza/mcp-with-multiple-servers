from mcp.server.fastmcp import FastMCP
from gcalendar_helper import list_events, add_event

mcp = FastMCP("Google Calendar Agent")

@mcp.tool(name="list_calendar_events", description="List upcoming Google Calendar events")
def list_calendar_events_tool() -> list:
    """Returns a list of upcoming events."""
    return list_events()

@mcp.tool(name="add_calendar_event", description="Add a new event to Google Calendar")
def add_calendar_event_tool(summary: str, start_time: str, end_time: str) -> str:
    """Adds a new calendar event"""
    return add_event(summary, start_time, end_time)

if __name__ == "__main__":
    mcp.run(transport="sse")
