# MCP Chess Server

## Installation

Install this MCP server by adding the following to your Claude Desktop config:

### For Windows:

```json
"chess": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/shivyam/mcp-servers.git#subdirectory=mcp-chess-server",
        "chess"
      ]
    }
```

### For macOS:

You need to specify the full path to your uvx installation:

```json
"chess": {
      "command": "/Users/example-user/.local/bin/uvx",
      "args": [
        "--from",
        "git+https://github.com/shivyam/mcp-servers.git#subdirectory=mcp-chess-server",
        "chess"
      ]
    }
```

**Note:** Replace `/Users/example-user/.local/bin/uvx` with your actual uvx path. You can find it by running `which uvx` in your terminal.
