from server import mcp

# import tools to register them with the MCP server
import tools.csv_tools
import tools.parquet_tools

if __name__ == "__main__":
    mcp.run()
