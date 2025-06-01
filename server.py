from mcp.server.fastmcp import FastMCP
from mongo_client import users_collection
from bson.json_util import dumps
from pymongo.errors import PyMongoError

mcp = FastMCP("MongoDB App")


# ===== Resources =====
@mcp.resource("resource://all_users_data")
def all_users_data() -> str:
    """
    Returns all users in the MongoDB collection as a JSON string.
    This will be used by the LLM to answer user queries based on the data.
    """
    try:
        users = users_collection.find({}, {"_id": 0})  # exclude _id for readability
        return dumps(list(users))
    except PyMongoError as e:
        return f"Database error: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="sse")
