# DataBridge MCP - Data Tools Server

A local Model Context Protocol (MCP) server that provides data file reading capabilities through natural language interfaces. This server enables seamless interaction with CSV and Parquet files via Claude for Desktop.

## Overview

DataBridge MCP is designed as a modular MCP server that exposes data file reading tools to AI assistants like Claude. It provides a clean, extensible architecture for adding new data processing capabilities over time.

## Features

### Current Tools
- **CSV Reader**: Read and analyze CSV files with automatic data type inference
- **Parquet Reader**: Read and process Parquet files with schema inspection
- **Data Preview**: Quick data sampling and structure overview
- **Error Handling**: Robust file validation and error reporting

### Planned Features
- JSON file reader
- Excel file reader  
- Data transformation tools
- Statistical analysis tools
- Data visualization utilities

## Project Structure

```
databridge-mcp/
├── main.py              # MCP server entry point
├── pyproject.toml        # Project dependencies and configuration
├── README.md            # This file
├── data/                # Sample data files for testing
├── tools/               # MCP tool implementations
│   ├── __init__.py      # Tools package initialization
│   ├── csv_reader.py    # CSV file reading tool
│   └── parquet_reader.py # Parquet file reading tool
└── utils/               # Shared utilities and helpers
    ├── __init__.py      # Utils package initialization
    ├── file_validators.py # File validation utilities
    └── data_helpers.py   # Common data processing functions
```

## Dependencies

- **mcp[cli]** (>=1.12.2): Model Context Protocol implementation
- **pandas** (>=2.3.1): Data manipulation and analysis
- **pyarrow** (>=21.0.0): Parquet file support and columnar data processing

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/samrasugu/databridge-mcp.git
   cd databridge-mcp
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

3. **Activate the virtual environment**:
   ```bash
   source .venv/bin/activate
   ```

## Usage

### Running the MCP Server

Start the server locally:
```bash
python main.py
```

The server will start and listen for MCP protocol connections from compatible clients.

### Connecting to Claude for Desktop

1. **Configure Claude for Desktop** to connect to your local MCP server
2. **Add server configuration** in Claude's settings:
   ```json
   {
     "name": "databridge_mcp",
     "command": "python",
     "args": ["/path/to/databridge-mcp/main.py"],
     "env": {}
   }
   ```

3. **Restart Claude for Desktop** to load the new server configuration

### Available Tools

Once connected, you can interact with your data files through natural language:

#### CSV File Reading
- "Read the CSV file at /path/to/data.csv"
- "Show me the first 10 rows of the sales data"
- "What are the column names and data types in this CSV?"

#### Parquet File Reading  
- "Load the Parquet file and show its schema"
- "Read the analytics data and give me a summary"
- "What's the size and structure of this Parquet file?"

## Development

### Adding New Tools

1. **Create a new tool file** in the `tools/` directory
2. **Implement the MCP tool interface** with proper error handling
3. **Add utility functions** to the `utils/` directory if needed
4. **Register the tool** in the main server configuration
5. **Update this README** with the new tool documentation

### Tool Development Guidelines

- Follow the MCP protocol specifications
- Include comprehensive error handling
- Provide clear, descriptive tool names and descriptions
- Add input validation for file paths and parameters
- Include helpful error messages for common issues

## Testing

### Sample Data
Place test data files in the `data/` directory:
- `sample.csv` - Example CSV file for testing
- `sample.parquet` - Example Parquet file for testing

### Manual Testing
1. Start the MCP server
2. Connect through Claude for Desktop
3. Test each tool with sample data files
4. Verify error handling with invalid inputs

## Troubleshooting

### Common Issues

- **File not found**: Ensure file paths are absolute and accessible
- **Permission errors**: Check file read permissions
- **Data format errors**: Verify file format matches the tool used
- **Connection issues**: Confirm MCP server is running and accessible

### Debug Mode
Run the server with debug logging:
```bash
python main.py --debug
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your changes with tests
4. Update documentation as needed
5. Submit a pull request

## License

[Add your license information here]

## Changelog

### v0.1.0 (Current)
- Initial MCP server setup
- Basic project structure
- CSV and Parquet reading tools (planned)
- Claude for Desktop integration support