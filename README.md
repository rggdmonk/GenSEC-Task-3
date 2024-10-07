# Context and System Fusion in Post-ASR Emotion Recognition with Large Language Models

<p align="left">
<a href="https://arxiv.org/abs/2410.03312" alt="arXiv">
        <img src="https://img.shields.io/badge/arXiv-2410.03312-b31b1b.svg?style=flat" /></a>
</p>


The official repository which contains the code for our paper [Context and System Fusion in Post-ASR Emotion Recognition with Large Language Models](https://arxiv.org/abs/2410.03312).

## Installation
```bash
pip install -r requirements.txt
```

## Examples
```bash
python -m examples.use_metrics
python -m examples.use_naive_heuristics
python -m examples.use_rerank_metrics
```

## Run tests
```bash
pytest
```

## Citation
For attribution in academic contexts, please cite this work as:

```bib
@article{stepachev-2024-contextfusion,
      title={Context and System Fusion in Post-ASR Emotion Recognition with Large Language Models}, 
      author={Pavel Stepachev and Pinzhen Chen and Barry Haddow},
      year={2024},
      eprint={2410.03312},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.03312}, 
}
```