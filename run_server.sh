#!/bin/bash
# Script to run the MCP server using uv

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Run uv with the full path
/Users/samrasugu/.local/bin/uv --directory "$SCRIPT_DIR" run main.py 