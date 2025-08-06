# DataBridge MCP - Data Processing Tools Server

A beginner-friendly Model Context Protocol (MCP) server that demonstrates how to create custom tools for AI assistants like Claude. This server provides tools to read and summarize CSV and Parquet files, serving as a foundation for building more advanced AI-powered workflows.

## What is MCP?

The Model Context Protocol (MCP) allows AI assistants to securely interact with external data and custom tools. Think of it as building your own mini API that exposes useful functions to an AI assistant running on your machine.

## Features

- **Two file reading tools**: CSV and Parquet file summarization
- **Clean, modular architecture**: Easy to extend with additional tools
- **Local execution**: Runs entirely on your machine
- **Claude Desktop integration**: Works seamlessly with Claude for Desktop
- **Type-safe**: Built with proper Python typing
- **Multiple run options**: Direct Python execution or uv-based workflow

## Project Structure

```
databridge_mcp/
│
├── data/                    # Sample data files
│   ├── sample.csv
│   └── sample.parquet
│
├── tools/                   # MCP tool definitions
│   ├── csv_tools.py
│   └── parquet_tools.py
│
├── utils/                   # Reusable utilities
│   └── file_reader.py
│
├── server.py               # MCP server instance
├── main.py                 # Entry point
├── generate_parquet.py     # Sample data generator
├── run_server.py          # Alternative Python runner
├── run_server.sh          # Shell script runner with full uv path
├── pyproject.toml         # Dependencies
└── uv.lock               # Locked dependencies
```

## Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)
- [Claude for Desktop](https://www.anthropic.com/claude) (for testing)

## Setup Instructions

### 1. Install uv (Recommended)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal after installation.

### 2. Clone and Setup Project

```bash
# Clone the repository
git clone https://github.com/samrasugu/databridge_mcp.git
cd databridge_mcp

# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Verify Sample Data

The project includes sample data files:
- `data/sample.csv` - Sample CSV data
- `data/sample.parquet` - Sample Parquet data

You can regenerate the Parquet file if needed:
```bash
uv run generate_parquet.py
```

## Running the Server

### Option 1: Using uv (Recommended)

```bash
uv run main.py
```

### Option 2: Direct Python Execution

```bash
python run_server.py
```

### Option 3: Shell Script (with full uv path)

```bash
./run_server.sh
```

The server will start and wait for connections from MCP clients.

## Configure Claude for Desktop

### Method 1: Using uv (may have PATH issues)

1. **Install Claude for Desktop** from [https://www.anthropic.com/claude](https://www.anthropic.com/claude)

2. **Edit the configuration file**:
   - **macOS/Linux**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

3. **Add your server configuration**:

```json
{
  "mcpServers": {
    "databridge_mcp": {
      "command": "uv", //or path to uv: "/Users/YOUR_USERNAME/.local/bin/uv"
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/databridge_mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

### Method 2: Using Full uv Path (Recommended)

If you encounter "spawn uv ENOENT" errors, use the full path to uv:

```json
{
  "mcpServers": {
    "databridge_mcp": {
      "command": "/Users/YOUR_USERNAME/.local/bin/uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/databridge_mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

### Method 3: Direct Python Execution

```json
{
  "mcpServers": {
    "databridge_mcp": {
      "command": "python3",
      "args": [
        "/ABSOLUTE/PATH/TO/databridge_mcp/run_server.py"
      ]
    }
  }
}
```

**Important**: Replace `/ABSOLUTE/PATH/TO/databridge_mcp` with the actual full path to your project folder.

4. **Restart Claude for Desktop**

## Usage

Once configured, you can interact with your tools through Claude:

```
"Summarize the CSV file named sample.csv"
"How many rows are in sample.parquet?"
"What's the structure of the data in sample.csv?"
"Read the first few rows of the sample data"
```

Claude will automatically detect and use the appropriate tools to answer your questions.

## Available Tools

- **`summarize_csv_file(filename)`**: Returns row and column count for CSV files
- **`summarize_parquet_file(filename)`**: Returns row and column count for Parquet files

## Troubleshooting

### Common Issues

**Server won't start:**
- Ensure all dependencies are installed: `uv sync`
- Check that you're in the correct directory
- Verify Python version compatibility (3.13+)

**Claude can't connect (spawn uv ENOENT):**
- Use Method 2 or 3 above with full paths
- Verify the absolute path in your config JSON is correct
- Ensure `uv` is in your system PATH or use full path
- Restart Claude for Desktop after config changes
- Check that data files exist in the `/data` directory

**Tools not appearing:**
- Confirm the server is running without errors
- Check the Claude UI for tool indicators (hammer icon)
- Verify tool registration in `main.py`
- Check server logs for any error messages

**Permission errors:**
- Make sure run scripts are executable: `chmod +x run_server.py run_server.sh`
- Check file read permissions for data files

## Development

### Adding New Tools

1. Create a new file in `tools/`
2. Import the server instance: `from server import mcp`
3. Define your tool with the `@mcp.tool()` decorator
4. Import your new tool module in `main.py`

Example:
```python
from server import mcp

@mcp.tool()
def my_new_tool(filename: str) -> str:
    """Description of what this tool does."""
    # Your tool implementation here
    return "Tool result"
```

### Extending Utilities

Add new functions to `utils/file_reader.py` or create new utility modules as needed.

### Project Structure Guidelines

- Keep tools in the `tools/` directory
- Place shared utilities in `utils/`
- Add sample data to `data/`
- Update `pyproject.toml` for new dependencies
- Run `uv sync` after dependency changes

## Dependencies

- **mcp[cli]** (>=1.12.2): Official MCP SDK and CLI tools
- **pandas** (>=2.3.1): Data manipulation and analysis
- **pyarrow** (>=21.0.0): Parquet file support

## License

MIT License - feel free to use this as a template for your own MCP servers.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and test thoroughly
4. Commit with descriptive messages: `git commit -m "feat: add new tool"`
5. Push to your fork: `git push origin feature/your-feature`
6. Create a pull request

## Changelog

### v0.1.0 (Current)
- Initial MCP server implementation
- CSV and Parquet file summarization tools
- Claude Desktop integration with multiple run options
- Sample data files and utilities
- Comprehensive troubleshooting guide