from __future__ import annotations

import logging

from gensec.rerank_metrics import Reranker

if __name__ == "__main__":
    candidates = [
        ["Do I come off?", "Do I come off???", "Do 1 come off?", "Do I come off?!", "Do I come off?!?!"],
        [
            "i don't want to argue with him it's just for god's sake its time yo realize it no one believes with him any more",
            "him i don't want to argue with him is just for god'sake a time he realize it no one believes with him any more",
            "i don't want to argue with him as just for god's sake its time you realize that no one believes with him any more",
            "i don't want to argue with him it's just for god's sake is time he realized that no one believes with him any more",
            "i don't want to argue with him it's just for god's sake its time ye realizes that no one believes with him any more",
            "ei dont want to argue with him is just for godsake a sim he realize it no one believes with him any more",
            "I don't want to argue with him. It's just... For God's sake",
            "I don't want to argue with him",
            "I don't want to argue with hi3",
            "I don't want to argue wit? him",
            "I don't want to argue with him. It's just For God's sake it's time. He realized that no one believes with him anymore1",
            "I don't want to argue with him. It's just For God's sake it's time. He realized that no one believes with him anymore!",
            "I don't want to argue with him. It's just... For God's sake",
            "I don't want to argue with him. It's just... For God's sake",
        ],
        ["", "hello my name is human", "", "hello my name is human", "hello"],
    ]

    reranker = Reranker(level=logging.DEBUG)

    print(f"chrF: {reranker.rerank(candidates, 'chrf')}")
    print(f"chrF++: {reranker.rerank(candidates, 'chrf++')}")
    print(f"WIP: {reranker.rerank(candidates, 'wip')}")

    print(f"TER: {reranker.rerank(candidates, 'ter')}")
    print(f"WER: {reranker.rerank(candidates, 'wer')}")
    print(f"MER: {reranker.rerank(candidates, 'mer')}")
    print(f"WIL: {reranker.rerank(candidates, 'wil')}")
