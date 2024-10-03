from __future__ import annotations

import logging

from gensec.naive_heuristics import NaiveHeuristics

if __name__ == "__main__":
    all_candidates = [
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

    selector = NaiveHeuristics(seed=42, level=logging.DEBUG)

    print(f"Longest candidate: {selector.naive_selection(all_candidates, 'longest')}")
    print(f"Shortest candidate: {selector.naive_selection(all_candidates, 'shortest')}")
    print(f"Most punctuation: {selector.naive_selection(all_candidates, 'most_punctuation')}")
    print(f"Least punctuation: {selector.naive_selection(all_candidates, 'least_punctuation')}")
    print(f"Random: {selector.naive_selection(all_candidates, 'random')}")
    print(f"Longest and most punctuation: {selector.naive_selection(all_candidates, 'longest_and_most_punctuation')}")
    print(
        f"Shortest candidate and least punctuation: {selector.naive_selection(all_candidates, 'shortest_and_least_punctuation')}"
    )
    print(
        f"Longest candidate and least punctuation: {selector.naive_selection(all_candidates, 'longest_and_least_punctuation')}"
    )
    print(
        f"Shortest candidate and most punctuation: {selector.naive_selection(all_candidates, 'shortest_and_most_punctuation')}"
    )
