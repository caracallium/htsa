"""Import-friendly wrapper for the legacy V-Greedy.py script."""

import importlib.util
from pathlib import Path


_LEGACY_PATH = Path(__file__).with_name("V-Greedy.py")
_SPEC = importlib.util.spec_from_file_location("_htsa_v_greedy_legacy", _LEGACY_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"Cannot load legacy module from {_LEGACY_PATH}")

_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

NodeDict = _MODULE.NodeDict
NONLINEAR = _MODULE.NONLINEAR
_sim_fds = _MODULE._sim_fds
expand_subgraph_greedy = _MODULE.expand_subgraph_greedy
find_k_best_subgraphs = _MODULE.find_k_best_subgraphs

__all__ = [
    "NodeDict",
    "NONLINEAR",
    "_sim_fds",
    "expand_subgraph_greedy",
    "find_k_best_subgraphs",
]
