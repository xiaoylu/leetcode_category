Machine learning system design
===
Note: the focus is the system design part, not ML.

Ranking
---
* Both youtube and google search rank items (i.e. video or urls), but they work on different modes.
* Youtube: can rank items offline, then push the result to a user's queue, display after the user clicks youtube.com
  * recommendation quality suffers
  * too many users
* Search:
  * instantly ranking, requires a small candidate set

Online vs Offline
---
* Training:
  * offline: not fresh, but more space to prepare high-quality traning set
  * online: fresh, but need to filter out biased data (ML fairness)
* Inference
  * offline: fast, can push data to a lookup table, can't handle out-of-scope input
  * online: slower, QA before each new model releasing

Freshness
---
* data seasonality/skew

Safety
---
* filtering out sensitive input, output
* fairness, bias
* sometimes, false negative or positive can risk lives (driving, health care)
