Install this MCP server by adding the following to your JSON config:

```json
"chess": {
      "command": "uvx",
      "args": [
        "--from",
        "git+",
        "run",
        "chess"
      ]
    }
```

Then run `mcpctl install mcp-chess-server` to install the server.
