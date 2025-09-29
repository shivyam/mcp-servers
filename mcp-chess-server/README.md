Install this MCP server by adding the following to your JSON config:

```json
"chess": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/shivyam/mcp-servers.git#subdirectory=mcp-chess-server",
        "run",
        "chess"
      ]
    }
```
