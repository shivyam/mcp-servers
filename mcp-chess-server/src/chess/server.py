from mcp.server.fastmcp import FastMCP
mcp = FastMCP('Chess')
from .chess_api import get_player_profile, get_player_stats

@mcp.tool()
def get_player_profile_tool(username: str):
    return get_player_profile(username)

@mcp.tool()
def get_player_stats_tool(username: str):
    return get_player_stats(username)


def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()