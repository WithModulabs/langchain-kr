# DAY3
## 1. 랭체인에서 가장 많이 사용하는 Reranker 알고리즘

랭체인(LangChain)에서 Reranker는 검색 결과의 순위를 재조정하여 더 관련성 높은 결과를 상위에 노출시키는 역할을 합니다. 대표적으로 많이 사용되는 Reranker 알고리즘은 다음과 같습니다.

### 1) Cross-Encoder 기반 Reranker
가장 널리 사용되는 방식으로, 쿼리와 각 문서를 함께 입력하여 관련성을 직접 예측합니다. 대표적인 모델로는 **MS MARCO** 데이터셋으로 학습된 BERT, RoBERTa, DeBERTa 기반의 Cross-Encoder가 있습니다. HuggingFace의 `cross-encoder/ms-marco-MiniLM-L-6-v2` 모델이 많이 활용됩니다.

### 2) Cohere Rerank
Cohere에서 제공하는 상용 Reranker API로, 쿼리와 문서 쌍의 관련성을 점수로 반환합니다. 랭체인에서 손쉽게 사용할 수 있어 실무에서 많이 활용됩니다.

### 3) OpenAI Reranker
OpenAI의 GPT 모델을 활용한 Reranker도 최근 각광받고 있습니다. 쿼리와 문서를 입력해 relevance score를 반환하며, 랭체인에서 플러그인 형태로 지원됩니다.

### 4) 기타 알고리즘
- **MonoT5**: T5 기반의 단일 쿼리-문서 입력 방식 Reranker
- **RankGPT**: GPT 기반의 랭킹 모델

---

## 2. 랭체인에서 Evaluation(평가) 방법

랭체인(LangChain)에서는 검색 및 생성 결과의 품질을 평가하기 위한 다양한 Evaluation(평가) 도구와 방법을 제공합니다.   
대표적인 평가 방식은 다음과 같습니다.

### 1) 기준 기반 평가 (Reference-based Evaluation)
- 정답(Reference)과 모델의 출력 결과를 비교하여 정확도, 정밀도, 재현율 등 다양한 지표로 평가합니다.
- 예시: 정답 문서와 검색 결과의 일치 여부, 생성된 텍스트와 기준 답변의 유사도 등

### 2) 기준 없는 평가 (Reference-free Evaluation)
- 기준 답변 없이 모델의 출력 품질을 평가합니다.
- 예시: 모델의 응답이 논리적으로 타당한지, 문법적으로 올바른지, 정보가 충분한지 등

### 3) 자동화 평가 (Automated Evaluation)
- BLEU, ROUGE, METEOR 등 전통적인 자연어 처리 평가 지표를 활용
- 임베딩 기반 유사도(Embedding Similarity), 랭킹 기반 평가 등

### 4) LLM 기반 평가 (LLM-as-a-Judge)
- 대형 언어모델(LLM)을 활용해 생성 결과의 품질을 평가
- 예시: OpenAI GPT, Cohere 등으로 평가 프롬프트를 작성해 자동화된 품질 판정

### 5) 사용자/휴먼 평가 (Human Evaluation)
- 실제 사용자 또는 전문가가 직접 결과를 평가
- 예시: 설문, 직접 점수 매기기, 피드백 수집 등



## 3. 랭체인과 Ragas

### 1) RAGAS (RAG Assessment)
RAGAS는 RAG(검색 증강 생성) 시스템의 품질을 자동으로 평가하는 오픈소스 라이브러리입니다. 랭체인과 쉽게 연동되며, 검색/생성 결과에 대해 다양한 품질 지표를 제공합니다.

- 주요 평가 지표:
    - **Faithfulness**: 생성 결과가 실제 검색된 문서와 얼마나 일치하는지
    - **Answer Relevancy**: 답변이 질문에 얼마나 적합한지
    - **Context Precision/Recall**: 검색된 문서가 실제로 답변에 얼마나 기여했는지
    - **Context Recall**: 정답이 포함된 문서가 검색 결과에 포함되었는지

- 자동화된 평가 파이프라인 제공
- LLM 기반 평가와 임베딩 기반 평가 모두 지원




