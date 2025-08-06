
## DAY6

### 1. Plan-and-Execute 에이전트 개념

- 복잡한 문제를 해결할 때, 먼저 전체 계획을 세우고 각 단계를 실행하며 필요시 계획을 재수정하는 방식입니다.
- 대표 논문: [Plan-and-Solve](https://arxiv.org/abs/2305.04091)
- Baby-AGI, ReAct 등 다양한 프로젝트에서 영감을 받음

#### 주요 구현 단계
1. **도구 정의**: Tavily 검색 등
2. **실행 에이전트 정의**: LLM과 도구 결합
3. **상태(State) 정의**: input, plan, past_steps, response
4. **계획(Plan) 단계**: LLM으로 단계별 계획 수립
5. **재계획(Re-Plan) 단계**: 실행 결과에 따라 계획 수정
6. **그래프 생성 및 실행**: LangGraph 워크플로우, 조건부 엣지, MemorySaver


#### 참고 자료
- [LangGraph 공식 문서](https://langchain-ai.github.io/langgraph/)
- [Plan-and-Solve 논문](https://arxiv.org/abs/2305.04091)
- [Baby-AGI 프로젝트](https://github.com/yoheinakajima/babyagi)
- [ReAct 논문](https://arxiv.org/abs/2210.03629)

---

### 2. Multi-Agent Supervisor 개념

- 여러 전문 에이전트(Researcher, Coder 등)를 팀으로 구성하고, Supervisor가 전체 작업 흐름을 관리하는 방식입니다.
- Supervisor는 각 에이전트의 결과를 바탕으로 다음 작업자를 선택하거나, 작업을 종료하는 역할을 수행합니다.
- LangGraph의 조건부 엣지와 상태(State) 관리 기능을 활용해 복잡한 팀 협업을 구현할 수 있습니다.

#### 주요 구현 단계
1. **상태(State) 정의**: messages, next
2. **도구 및 에이전트 생성**: TavilySearch, PythonREPLTool 등
3. **Supervisor 에이전트 생성**: RouteResponse 반환, 다음 작업자 선택
4. **그래프 구성 및 실행**: 각 에이전트 노드와 Supervisor 노드 추가, 조건부 엣지로 흐름 제어


#### 참고 자료
- [LangGraph 공식 문서](https://langchain-ai.github.io/langgraph/)
- [멀티 에이전트 Supervisor 개념](https://langchain-ai.github.io/langgraph/concepts/multi_agent/#supervisor)
- [create_react_agent 함수 문서화](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)
