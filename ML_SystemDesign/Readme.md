Machine learning system design
===

# Formulate loss functions

| **Problem Type**                    | **Activation + Loss Function Combo**                           | **Math (in LaTeX)**                                                                                  |
|--------------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| **Binary Classification**            | Sigmoid + Binary Cross-Entropy                                | $L = - y log(p) + (1 - y) log(1 - p)$                                                                |
| **Imbalanced Binary Classification** | Sigmoid + Weighted Binary Cross-Entropy                       | $L = - [ w_1 y log(p) + w_2 (1 - y) log(1 - p) ]$                                                    |
| **Multi-Class Classification**       | Softmax + Categorical Cross-Entropy                           | $L = - \sum_{i} y_i log(p_i)$, allow multiple classes, but $y_i$s should sum to 1                    |
| **Multi-Class Classification**       | Log-Softmax + Negative Log-Likelihood (NLL)                   | $L = - \log(p_i)$ where $y_i = 1$ only for the "true" class $i$                                      |
| **Multi-Label Classification**       | Sigmoid (per class) + Binary Cross-Entropy (per class)        | $L = - [ y log(p) + (1 - y) log(1 - p) ]$, there is one loss per output activation                   |
| **Regression**                       | None (Linear) + Mean Squared Error (MSE)                      | $L = 1/N \sum_{i} (y_i - hat{y}_i)^2$, L2 penalize outliers                                        |
| **Regression**                       | None (Linear) + Mean Absolute  error (MAE)                    | $L = 1/N \sum_{i} \|y_i - hat{y}_i\|$, L1 encourage sparsity                                         |
| **Autogression/Next-token prediction** | Softmax + Categorical Cross-Entropy                         | $L = - \sum_{i} y_i log(p_i)$                                                                        |
| **Ranking/Pairwise Learning**        | None (Linear/ Sigmoid) + Contrastive Loss / Triplet Loss      | $y_i > y_j$ or $\|y_i - y_j\| > \|y_k - y_j\|$                                                           |

# Feature

- feature engineering:
  - domain-specific, use human common sense 
- unsupervised feature representation learning (cold start, new/fresh item recommendations):
  - word2vec style -- similar embeddings for similar items, learn from item-to-item interactions.
  - autoencoder (VAE) 

# Explotaion and Exploration
  - fairness, diversity
  - use temperature in softmax to smooth the output
  - add a probablistic layer in the neural net
  - Multi-arm Bandit
    - episoly greedy: randomly select someone by small prob.
    
