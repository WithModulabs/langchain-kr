# DAY3
## 1. 랭체인에서 가장 많이 사용하는 Reranker 알고리즘

랭체인(LangChain)에서 Reranker는 검색 결과의 순위를 재조정하여 더 관련성 높은 결과를 상위에 노출시키는 역할을 합니다. 대표적으로 많이 사용되는 Reranker 알고리즘은 다음과 같습니다.

### 1) Cross-Encoder 기반 Reranker
가장 널리 사용되는 방식으로, 쿼리와 각 문서를 함께 입력하여 관련성을 직접 예측합니다. 대표적인 모델로는 **MS MARCO** 데이터셋으로 학습된 BERT, RoBERTa, DeBERTa 기반의 Cross-Encoder가 있습니다. HuggingFace의 `cross-encoder/ms-marco-MiniLM-L-6-v2` 모델이 많이 활용됩니다.

### 2) Cohere Rerank
Cohere에서 제공하는 상용 Reranker API로, 쿼리와 문서 쌍의 관련성을 점수로 반환합니다. 랭체인에서 손쉽게 사용할 수 있어 실무에서 많이 활용됩니다.

### 3) OpenAI Reranker
OpenAI의 GPT 모델을 활용한 Reranker도 최근 각광받고 있습니다. 쿼리와 문서를 입력해 relevance score를 반환하며, 랭체인에서 플러그인 형태로 지원됩니다.

### 4. 기타 알고리즘
- **MonoT5**: T5 기반의 단일 쿼리-문서 입력 방식 Reranker
- **RankGPT**: GPT 기반의 랭킹 모델


