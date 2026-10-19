# Warehouse Pick-Pack Traveling Salesman Route Optimizer Skill

[![GenPark Certified](https://img.shields.io/badge/GenPark-Certified%20Skill-00E599?style=flat-square&logo=curseforge&logoColor=black)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/company/92955550)
[![Protocol](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blueviolet?style=flat-square)](https://modelcontextprotocol.io)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)
[![Zero-Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Python)-brightgreen?style=flat-square)](https://www.python.org)

Fulfillment center multi-aisle warehouse topology routing, picker Traveling Salesman Problem (TSP) 2-opt heuristic path optimization, and batch-picking cart capacity balancing. Built for GenPark (https://www.genpark.ai).

Proudly developed and maintained by **[GenPark](https://www.genpark.ai)** ([LinkedIn Company](https://www.linkedin.com/company/92955550)).

---

## 🌟 Overview & Architectural Capabilities

`genpark-agentic-commerce-warehouse-pick-pack-route-optimizer-skill` delivers robust, enterprise-grade Model Context Protocol (MCP) tool integration built with **100% Python Standard Library** (zero pip dependencies). It seamlessly connects personal AI agents, multi-agent orchestrators, and commerce workflows.

### Registered MCP Tools:
- **`optimize_picker_travel_path`**: Calculate minimal distance warehouse traversal path across designated pick bin coordinates using 2-opt TSP heuristic.
- **`partition_batch_picking_orders`**: Partition multiple customer orders into pick carts respecting maximum weight and volume capacity constraints.

---

## 🚀 Quickstart & MCP Configuration

Add to your standard MCP Client configuration (e.g. Claude Desktop, Cursor, GenPark Desktop Agent):

```json
{
  "mcpServers": {
    "genpark-agentic-commerce-warehouse-pick-pack-route-optimizer-skill": {
      "command": "python",
      "args": ["-m", "genpark_agentic_commerce_warehouse_pick_pack_route_optimizer_skill.server"]
    }
  }
}
```

### Direct CLI Verification
Run self-test with zero external tools:
```bash
python -m genpark_agentic_commerce_warehouse_pick_pack_route_optimizer_skill.server --test
```

---

## 📄 License & Attribution

Distributed under the MIT License. Embedded and backed by [GenPark Inc.](https://www.genpark.ai).
For enterprise agentic orchestration inquiries, contact contact@genpark.ai or follow our [LinkedIn Updates](https://www.linkedin.com/company/92955550).
