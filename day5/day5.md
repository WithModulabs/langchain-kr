# Day 5: LangGraph 실습 및 그래프 기반 RAG


## 1. 주요 실습 내용

- **State 정의**: 그래프에서 공유되는 상태(`TypedDict` 기반) 정의  
- **노드 정의**: 각 단계별 함수(검색, 쿼리 재작성, LLM 실행, 관련성 평가 등) 정의  
- **그래프 정의 및 연결**:  
  - `StateGraph`를 사용해 노드와 엣지 연결, 조건부 분기 추가
- **그래프 컴파일 및 시각화**:  
  - `workflow.compile()`로 그래프 실행 객체 생성  
  - `visualize_graph(app)`으로 그래프 구조 시각화

- **조건부 엣지**: 관련성 평가 결과에 따라 재검색, 종료 등 분기 처리  
  예시:
  ```python
  workflow.add_conditional_edges(
      "결과 종합",
      decision,
      {
          "재검색": "retrieve",
          "종료": END,
      },
  )
  ```
- **멀티 LLM**: GPT, Claude 등 여러 LLM을 그래프 내에서 병렬 또는 조건부로 활용
- **쿼리 재작성**: 검색 결과가 부적합할 때 쿼리를 재작성하여 재검색



## 2. 주요 실습 내용
- **목적**: LangGraph를 활용한 가장 단순한 형태의 RAG(Retrieval-Augmented Generation) 워크플로우를 구현
- **문서 기반**: PDF 문서(`SPRI_AI_Brief_2023년12월호_F.pdf`)를 벡터화하여 검색 및 답변 생성에 활용


1. **PDF 기반 Retrieval Chain 생성**
   - PDF 문서를 로드하고, `pdf_retriever`와 `pdf_chain` 객체를 생성
   - `pdf_retriever`로 관련 문서 검색, `pdf_chain`으로 답변 생성

2. **State 정의**
   - `GraphState`(TypedDict)로 질문, 검색 결과(context), 답변, 메시지 리스트 등 상태값 정의

3. **노드(Node) 정의**
   - `retrieve_document`: 질문에 대해 PDF에서 관련 문서 검색
   - `llm_answer`: 검색 결과와 질문을 바탕으로 LLM이 답변 생성

4. **그래프 생성 및 연결**
   - `StateGraph`로 워크플로우 정의
   - `retrieve` → `llm_answer` → END 순서로 노드 연결

5. **그래프 실행**
   - 입력 질문을 받아 그래프 실행
   - 결과로 질문과 답변 출력


## 3. Groundedness(관련성) Check 추가 실습 요약

- **목적**: Naive RAG에 "검색 결과의 질문-문서 관련성(Groundedness)" 체크 단계를 추가하여, 검색 결과가 질문과 충분히 관련 있는지 자동 평가하고, 관련성이 없으면 재검색하도록 그래프를 확장

### 주요 절차

1. **State 확장**
   - 기존 State에 `relevance`(관련성 평가 결과) 필드를 추가

2. **노드(Node) 정의**
   - `retrieve_document`: 질문에 대해 PDF에서 관련 문서 검색
   - `relevance_check`: 검색 결과와 질문의 관련성을 LLM 기반 평가기로 판단(예: "yes"/"no")
   - `llm_answer`: 관련성이 충분할 때만 답변 생성

3. **조건부 그래프 흐름**
   - `retrieve` → `relevance_check` →  
     - 관련성 "yes" → `llm_answer` → END  
     - 관련성 "no" → `retrieve`(재검색, 재귀적 반복)

4. **재귀 방지**
   - 동일 쿼리 반복 시 무한루프 방지를 위해 `recursion_limit` 설정 및 `GraphRecursionError` 예외 처리

5. **실행 및 출력**
   - 질문 입력 시, 관련성 체크 결과에 따라 답변 생성 또는 재검색
   - 최종적으로 질문, 답변, 관련성 평가 결과를 출력


## 4. Query Rewrite(쿼리 재작성) 그래프 실습 요약

- **목적**: 검색 적합성을 높이기 위해 사용자의 원 질문을 LLM 기반 프롬프트로 재작성하여, 더 효과적인 벡터 검색 및 답변 생성을 유도

### 주요 절차
1. **State 확장**
   - `question` 필드를 리스트(List[str])로 확장하여, 원 질문과 재작성된 질문을 모두 저장

2. **Query Rewrite 노드 추가**
   - LLM 프롬프트(`PromptTemplate`)를 활용해 질문을 재작성하는 노드(`query_rewrite`) 구현
   - 재작성된 질문을 State에 추가

3. **그래프 구조**
   - `query_rewrite` → `retrieve` → `relevance_check` → (조건부 분기) → `llm_answer` 또는 `web_search` → END
   - 관련성 평가 결과에 따라 웹 검색 등 추가 분기 가능

4. **실행 및 출력**
   - 입력 질문, 재작성된 질문, 최종 답변을 모두 출력하여 비교 가능

