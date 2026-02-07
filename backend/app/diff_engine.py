import numpy as np

THRESHOLD = 0.82

def semantic_diff(old_chunks, new_chunks, old_vecs, new_vecs):
    diffs = []

    for i, new_vec in enumerate(new_vecs):
        sims = old_vecs @ new_vec
        best_idx = int(np.argmax(sims))
        best_sim = float(sims[best_idx])

        if best_sim < THRESHOLD:
            diffs.append({
                "type": "added",
                "new": new_chunks[i]
            })
        else:
            diffs.append({
                "type": "modified",
                "old": old_chunks[best_idx],
                "new": new_chunks[i],
                "similarity": round(best_sim, 3)
            })

    return diffs
