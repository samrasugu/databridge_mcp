#!/usr/bin/env python3
"""
Simple script to run the MCP server directly.
This can be used as an alternative to uv run main.py
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the MCP server
from main import mcp

if __name__ == "__main__":
    mcp.run()
