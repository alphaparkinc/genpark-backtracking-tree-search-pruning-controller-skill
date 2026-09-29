import sys
import json
from client import TreeSearchController

tsc = TreeSearchController()

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-backtracking-tree-search-pruning-controller-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "register_reasoning_node",
                        "description": "Registers candidate reasoning thought with score and parent pointer",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "node_id": {"type": "string"},
                                "score": {"type": "number"},
                                "parent_id": {"type": "string"}
                            },
                            "required": ["node_id", "score"]
                        }
                    },
                    {
                        "name": "select_best_active_branch",
                        "description": "Returns best non-pruned leaf reasoning branch",
                        "inputSchema": {"type": "object", "properties": {}}
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        name = params.get("name")
        args = params.get("arguments", {})
        
        if name == "register_reasoning_node":
            tsc.register_node(args.get("node_id", ""), args.get("score", 0.0), args.get("parent_id"))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": "Registered"}]}}
        elif name == "select_best_active_branch":
            best = tsc.select_best_active_branch()
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": str(best)}]}}
            
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def run():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    run()
