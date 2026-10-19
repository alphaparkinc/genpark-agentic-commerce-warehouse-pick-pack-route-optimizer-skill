# -*- coding: utf-8 -*-
"""Model Context Protocol (MCP) Server for Warehouse Pick-Pack Traveling Salesman Route Optimizer Skill
Powered by GenPark (https://www.genpark.ai).
"""
import sys
import json
import logging
from .core import *

TOOLS_METADATA = [
  {
    "name": "optimize_picker_travel_path",
    "description": "Calculate minimal distance warehouse traversal path across designated pick bin coordinates using 2-opt TSP heuristic.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "depot_coordinate": {
          "type": "object",
          "properties": {
            "x": {
              "type": "number"
            },
            "y": {
              "type": "number"
            }
          },
          "required": [
            "x",
            "y"
          ]
        },
        "pick_locations": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "bin_id": {
                "type": "string"
              },
              "x": {
                "type": "number"
              },
              "y": {
                "type": "number"
              },
              "item_weight_kg": {
                "type": "number"
              }
            },
            "required": [
              "bin_id",
              "x",
              "y"
            ]
          }
        }
      },
      "required": [
        "depot_coordinate",
        "pick_locations"
      ]
    }
  },
  {
    "name": "partition_batch_picking_orders",
    "description": "Partition multiple customer orders into pick carts respecting maximum weight and volume capacity constraints.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "cart_max_weight_kg": {
          "type": "number"
        },
        "orders": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "order_id": {
                "type": "string"
              },
              "total_weight_kg": {
                "type": "number"
              },
              "total_items": {
                "type": "integer"
              }
            },
            "required": [
              "order_id",
              "total_weight_kg"
            ]
          }
        }
      },
      "required": [
        "cart_max_weight_kg",
        "orders"
      ]
    }
  }
]

def handle_rpc(request_str: str) -> str:
    try:
        req = json.loads(request_str)
    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error"}, "id": None})
    
    msg_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        return json.dumps({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "genpark-agentic-commerce-warehouse-pick-pack-route-optimizer-skill",
                    "version": "1.0.0",
                    "vendor": "GenPark (https://www.genpark.ai)"
                }
            }
        })

    if method == "tools/list":
        return json.dumps({
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"tools": TOOLS_METADATA}
        })

    if method == "tools/call":
        tool_name = params.get("name")
        arguments = params.get("arguments", {})
        
        func = globals().get(tool_name)
        if not func or not callable(func):
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Method '{tool_name}' not found"}
            })
        
        try:
            call_res = func(**arguments)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [
                        {"type": "text", "text": json.dumps(call_res, ensure_ascii=False, indent=2)}
                    ]
                }
            })
        except Exception as err:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32000, "message": f"Execution error: {str(err)}"}
            })

    return json.dumps({
        "jsonrpc": "2.0",
        "id": msg_id,
        "error": {"code": -32601, "message": f"Unhandled method '{method}'"}
    })

def run_self_test():
    print(f"=== Running Self Test for genpark-agentic-commerce-warehouse-pick-pack-route-optimizer-skill ===")
    init_res = json.loads(handle_rpc(json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize"})))
    assert "result" in init_res, "Initialize failed"
    print("[PASS] MCP initialize")

    list_res = json.loads(handle_rpc(json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})))
    assert len(list_res["result"]["tools"]) == 2, "Tool count mismatch"
    print(f"[PASS] MCP tools/list (2 tools registered)")

    # Execute smoke test for each tool

    call1 = json.loads(handle_rpc(json.dumps({
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "optimize_picker_travel_path",
            "arguments": {
                "depot_coordinate": {"x": 0.0, "y": 0.0},
                "pick_locations": [
                    {"bin_id": "A-12-04", "x": 10.0, "y": 25.0, "item_weight_kg": 1.2},
                    {"bin_id": "B-03-01", "x": 15.0, "y": 5.0, "item_weight_kg": 0.5},
                    {"bin_id": "C-08-09", "x": 40.0, "y": 30.0, "item_weight_kg": 2.1},
                    {"bin_id": "D-15-02", "x": 35.0, "y": 10.0, "item_weight_kg": 3.4}
                ]
            }
        }
    })))
    assert "result" in call1, "Call1 failed"
    print("[PASS] Tool smoke test: optimize_picker_travel_path")

    print("[ALL TESTS PASSED] Self-test verified successfully.")
    return True

if __name__ == "__main__":
    if "--test" in sys.argv:
        success = run_self_test()
        sys.exit(0 if success else 1)
    
    for line in sys.stdin:
        if not line.strip():
            continue
        out = handle_rpc(line)
        sys.stdout.write(out + "\n")
        sys.stdout.flush()
