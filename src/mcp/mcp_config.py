from dotenv import load_dotenv
load_dotenv()
import os

def mcp_client_config():
    """
    Local MCP service based on Python：
    {
        “(Your MCP service name)”:{
            {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": ["/path/to/math_server.py"],
            "transport": "stdio",
        },
    }

    SSE MCP service：
        {
        “(Your MCP service name)”:{
            # Ensure that the service website is correct
            "url": "http://localhost:8000/sse",
            "transport": "sse",
        }
    }
    """
    _mcp_client_config = {
        "gaode": {
            "url": f"https://mcp.amap.com/sse?key={os.getenv('GAODE_KEY')}",
            "transport": "sse",
        },
    }

    return _mcp_client_config