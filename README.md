# Structure-Aware Abstraction of Hierarchical Time Series

## Overview

This repository contains the artifact code for **Structure-Aware Abstraction of Hierarchical Time Series**. It implements V-Greedy, P-Greedy, and OSS for hierarchical time series abstraction on directed trees or directed acyclic hierarchy graphs.

The algorithms take a directed parent-to-child hierarchy and a time series attached to each node, then select representative subgraphs that balance temporal similarity and node values.

## Repository structure

```text
.
+-- V-Greedy.py              # Original V-Greedy implementation
+-- P-Greedy.py              # Original P-Greedy implementation
+-- oss.py                   # OSS implementation
+-- v_greedy.py              # Import-friendly wrapper for V-Greedy.py
+-- p_greedy.py              # Import-friendly wrapper for P-Greedy.py
+-- examples/
|   +-- minimal_demo.py      # Lightweight synthetic demo
+-- requirements.txt         # Python dependencies
+-- CITATION.cff             # GitHub/Zenodo citation metadata
+-- CITATION.bib             # BibTeX citation entries
+-- LICENSE                  # MIT license
+-- README.md
```

The original files with hyphenated names are kept for compatibility. The wrapper files make the V-Greedy and P-Greedy implementations easier to import from Python code.

## Installation

```bash
git clone https://github.com/caracallium/htsa.git
cd htsa
pip install -r requirements.txt
```

The code depends only on NumPy and NetworkX.

## Input format

The algorithms expect a `networkx.DiGraph` and a node metadata dictionary:

```python
node_dict[node_id] = (time_series, value, extra_info)
```

where:

- `node_id` is the node identifier used in the graph.
- `time_series` is a one-dimensional NumPy array.
- `value` is a numeric node weight or importance value.
- `extra_info` is an optional dictionary for labels or other metadata.

Edges in the graph should point from parent nodes to child nodes. The hierarchy should be a directed tree or DAG. P-Greedy is tree-oriented and uses root-to-node paths.

## Usage

Use the import-friendly wrappers for V-Greedy and P-Greedy:

```python
import networkx as nx
import numpy as np

from v_greedy import find_k_best_subgraphs as run_v_greedy
from p_greedy import find_k_best_subgraphs_lazy as run_p_greedy
from oss import expand_subgraph_hybrid_oss, find_k_best_subgraphs_lazy as run_oss

G = nx.DiGraph()
G.add_edges_from([("root", "a"), ("root", "b"), ("a", "a1")])

t = np.linspace(0.0, 1.0, 16)
node_dict = {
    "root": (np.sin(t), 5.0, {}),
    "a": (np.sin(t + 0.1), 3.0, {}),
    "a1": (np.sin(t + 0.2), 2.0, {}),
    "b": (np.cos(t), 1.0, {}),
}

v_subgraphs, v_total = run_v_greedy(G, node_dict, k=2)
p_subgraphs, p_total = run_p_greedy(G, node_dict, k=2)
oss_root_nodes, oss_root_score = expand_subgraph_hybrid_oss(G, node_dict, "root")
oss_subgraphs, oss_total = run_oss(G, node_dict, k=2)
```

You can still run or load the original scripts directly, but `V-Greedy.py` and `P-Greedy.py` are not valid module names for normal `import` statements because of the hyphen.

## Algorithms

**V-Greedy** greedily expands a candidate subgraph from a root by considering successor frontier nodes and accepting the node that improves the objective the most. The k-subgraph routine repeatedly selects disjoint subgraphs.

**P-Greedy** is a tree-oriented greedy method that expands along root-to-node paths. It uses cumulative path statistics and a lazy heap strategy for selecting multiple non-overlapping subgraphs.

**OSS** performs optimal-subtree-style enumeration with dominance filtering for a selected root. The repository also includes a lazy k-subgraph selection wrapper that calls the OSS root routine on candidate seeds.

All methods use frequency-domain similarity between node time series and evaluate subgraphs using the implemented score based on similarity, node value, and subgraph size.

## Minimal example

Run the synthetic example without any external datasets:

```bash
python examples/minimal_demo.py
```

The script constructs a tiny directed tree, creates synthetic NumPy time series, runs V-Greedy, P-Greedy, and OSS, and prints the selected nodes and scores.

## Citation

BibTeX citation entries are provided in `CITATION.bib`. Citation metadata for GitHub and Zenodo is also provided in `CITATION.cff`.

```bibtex
@inproceedings{wu2026structureaware,
  title = {Structure-Aware Abstraction of Hierarchical Time Series},
  author = {Wu, Yihan and Zhu, Xuliang and Li, Guozhong and Wang, Kai and Lin, Xuemin},
  booktitle = {Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining},
  year = {2026}
}

@misc{wu2026htsaartifact,
  title = {Structure-Aware Abstraction of Hierarchical Time Series},
  author = {Wu, Yihan and Zhu, Xuliang and Li, Guozhong and Wang, Kai and Lin, Xuemin},
  year = {2026},
  url = {https://github.com/caracallium/htsa},
  note = {KDD 2026 artifact repository}
}
```

No repository DOI is included yet. After Zenodo generates the repository DOI, add the real DOI to `CITATION.cff` and `CITATION.bib`.

## License

This repository is released under the MIT License. See `LICENSE`.

## Artifact note for KDD 2026

This repository is prepared for public artifact archiving for KDD 2026. It intentionally does not include large datasets, generated archives, release files, or a placeholder DOI. Create the GitHub Release first, connect it to Zenodo, and then update the citation metadata with the DOI generated by Zenodo.
