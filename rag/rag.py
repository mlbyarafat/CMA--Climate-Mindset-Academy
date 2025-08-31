import json
import math
from pathlib import Path
from typing import List, Dict

def _tokenize(text: str) -> List[str]:
    return [t.lower() for t in text.split()]

def _tf(doc_tokens: List[str]) -> Dict[str, float]:
    tf = {}
    for t in doc_tokens:
        tf[t] = tf.get(t, 0) + 1
    n = len(doc_tokens) or 1
    for k in tf:
        tf[k] /= n
    return tf

def _cosine(a: Dict[str, float], b: Dict[str, float]) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k,0.0)*b.get(k,0.0) for k in keys)
    na = math.sqrt(sum(v*v for v in a.values()))
    nb = math.sqrt(sum(v*v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot/(na*nb)

class TinyRAG:
    def __init__(self, docs_path: str):
        self.docs = json.loads(Path(docs_path).read_text(encoding="utf-8"))
        self.index = []
        for d in self.docs:
            tokens = _tokenize(d["title"] + " " + d["text"])
            self.index.append({"id": d["id"], "title": d["title"], "tf": _tf(tokens), "text": d["text"]})

    def search(self, query: str, k: int = 3):
        q_tf = _tf(_tokenize(query))
        scored = []
        for row in self.index:
            score = _cosine(q_tf, row["tf"])
            scored.append((score, row))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [{"title": r["title"], "text": r["text"], "score": float(s)} for s, r in scored[:k]]
