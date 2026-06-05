"""Import-friendly wrapper for the legacy P-Greedy.py script."""

import importlib.util
from pathlib import Path


_LEGACY_PATH = Path(__file__).with_name("P-Greedy.py")
_SPEC = importlib.util.spec_from_file_location("_htsa_p_greedy_legacy", _LEGACY_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"Cannot load legacy module from {_LEGACY_PATH}")

_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

NodeDict = _MODULE.NodeDict
NONLINEAR = _MODULE.NONLINEAR
EPS = _MODULE.EPS
sim_fds = _MODULE.sim_fds
expand_subgraph_pgreedy_tree = _MODULE.expand_subgraph_pgreedy_tree
find_k_best_subgraphs_lazy = _MODULE.find_k_best_subgraphs_lazy

__all__ = [
    "NodeDict",
    "NONLINEAR",
    "EPS",
    "sim_fds",
    "expand_subgraph_pgreedy_tree",
    "find_k_best_subgraphs_lazy",
]
