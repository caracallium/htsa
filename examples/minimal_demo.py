"""Minimal synthetic demo for hierarchical time series abstraction."""

import sys
from pathlib import Path

import networkx as nx
import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from oss import expand_subgraph_hybrid_oss
from p_greedy import find_k_best_subgraphs_lazy as run_p_greedy
from v_greedy import find_k_best_subgraphs as run_v_greedy


def make_demo_graph():
    t = np.linspace(0.0, 2.0 * np.pi, 32)

    graph = nx.DiGraph()
    graph.add_edges_from(
        [
            ("root", "seasonal"),
            ("root", "trend"),
            ("seasonal", "seasonal_child"),
            ("trend", "noise"),
        ]
    )

    node_dict = {
        "root": (np.sin(t), 5.0, {"label": "root"}),
        "seasonal": (np.sin(t + 0.1), 4.0, {"label": "similar seasonal"}),
        "seasonal_child": (np.sin(t + 0.2), 3.0, {"label": "seasonal child"}),
        "trend": (np.linspace(0.0, 1.0, len(t)), 2.0, {"label": "trend"}),
        "noise": (np.cos(3.0 * t), 1.0, {"label": "different pattern"}),
    }
    return graph, node_dict


def print_results(name, results, total):
    print(f"{name}: total score = {total:.4f}")
    for index, (nodes, score) in enumerate(results, start=1):
        selected = ", ".join(sorted(nodes))
        print(f"  {index}. score = {score:.4f}; nodes = {{{selected}}}")


def main():
    graph, node_dict = make_demo_graph()

    v_results, v_total = run_v_greedy(graph, node_dict, k=2)
    print_results("V-Greedy", v_results, v_total)

    p_results, p_total = run_p_greedy(graph, node_dict, k=2)
    print_results("P-Greedy", p_results, p_total)

    oss_nodes, oss_score = expand_subgraph_hybrid_oss(graph, node_dict, "root")
    selected = ", ".join(sorted(oss_nodes))
    print(f"OSS root subgraph: score = {oss_score:.4f}; nodes = {{{selected}}}")


if __name__ == "__main__":
    main()
