## DAY4

### 1. LangGraph에서 State의 개념

LangGraph에서 State는 그래프 기반 워크플로우의 각 단계(노드)에서 관리되는 데이터와 컨텍스트를 의미합니다. State는 다음과 같은 특징을 가집니다:

- **상태 저장**: 각 노드는 입력받은 State를 바탕으로 작업을 수행하고, 결과를 State에 저장하거나 갱신합니다.
- **데이터 전달**: State는 그래프의 노드 간에 데이터를 전달하는 역할을 하며, 워크플로우의 흐름을 제어합니다.
- **불변성/변경**: State는 불변(immutable) 객체로 설계되는 경우가 많으며, 노드 실행 시 새로운 State 객체를 반환하여 변경 사항을 반영합니다.
- **컨텍스트 관리**: LLM의 입력/출력, 중간 결과, 사용자 입력, 외부 API 응답 등 다양한 정보를 State에 저장할 수 있습니다.
- **분기와 조건**: State의 값에 따라 그래프의 분기(조건문)나 반복(루프) 구조를 구현할 수 있습니다.

#### 예시 코드 (Python)
```python
from langgraph.graph import StateGraph

# State는 dict 또는 커스텀 클래스로 정의할 수 있습니다.
class MyState:
    def __init__(self, value):
        self.value = value

graph = StateGraph(state_type=MyState)
```

> 요약: LangGraph의 State는 그래프 내 데이터 흐름과 컨텍스트를 관리하는 핵심 객체로, 각 노드의 입력/출력 및 전체 워크플로우의 상태를 추적하는 역할을 합니다.

### 2. LangChain/LangGraph에서 Node의 개념

Node(노드)는 LangChain 및 LangGraph에서 워크플로우의 한 단계를 구성하는 기본 단위입니다. 각 노드는 다음과 같은 특징을 가집니다:

- **작업 단위**: 노드는 일반적으로 하나의 함수, LLM 호출, 도구 실행 등 독립적인 작업을 수행합니다.
- **입력과 출력**: 노드는 State(상태) 또는 특정 입력값을 받아 처리하고, 결과를 반환합니다.
- **그래프 구성 요소**: 여러 노드를 연결하여 복잡한 데이터 흐름, 조건 분기, 반복 등 다양한 워크플로우를 설계할 수 있습니다.
- **재사용성**: 동일한 노드를 여러 그래프에서 재사용할 수 있습니다.
- **유연성**: 노드는 Python 함수, 체인, 에이전트, 외부 API 호출 등 다양한 형태로 정의할 수 있습니다.

#### 예시 코드 (Python)
```python
# 노드로 사용할 함수 정의
def my_node(state):
    # 입력값을 받아 처리
    result = ... # 작업 수행
    return {"result": result}

# 그래프에 노드 추가
from langgraph.graph import StateGraph

graph = StateGraph(state_type=dict)
graph.add_node("my_node", my_node)
```

> 요약: Node는 LangChain/LangGraph 워크플로우에서 데이터 처리, LLM 호출, 도구 실행 등 각 단계를 담당하는 핵심 구성 요소입니다. 노드를 조합하여 복잡한 AI 파이프라인을 설계할 수 있습니다.

### 3. LangChain/LangGraph에서 Graph와 Edge의 개념

#### Graph(그래프)
- **정의**: Graph는 여러 노드(Node)와 엣지(Edge)로 구성된 워크플로우의 전체 구조를 의미합니다.
- **역할**: 데이터와 작업의 흐름을 시각적으로 설계하고, 복잡한 파이프라인을 체계적으로 관리할 수 있게 해줍니다.
- **구성**: 노드(작업 단위)와 엣지(노드 간 연결)로 구성되며, 시작(START)과 종료(END) 지점을 명확히 지정할 수 있습니다.
- **유형**: StateGraph, MultiModalGraph 등 다양한 형태로 확장 가능합니다.

#### Edge(엣지)
- **정의**: Edge는 그래프 내에서 한 노드에서 다른 노드로의 데이터/제어 흐름을 연결하는 선입니다.
- **역할**: 워크플로우의 실행 순서, 분기, 반복 등 논리적 흐름을 결정합니다.
- **특징**: 조건부 분기, 루프, 동적 경로 등 다양한 제어 구조를 구현할 수 있습니다.

#### 예시 코드 (Python)
```python
from langgraph.graph import StateGraph, START, END

graph = StateGraph(state_type=dict)
graph.add_node("node1", node1_func)
graph.add_node("node2", node2_func)

# 엣지(Edge) 추가: node1 → node2
graph.add_edge("node1", "node2")
# 시작(START) → node1, node2 → 종료(END)
graph.add_edge(START, "node1")
graph.add_edge("node2", END)
```

> 요약: Graph는 전체 워크플로우의 구조와 실행 흐름을 정의하는 틀이며, Edge는 노드 간의 데이터/제어 흐름을 연결하는 역할을 합니다. 이 둘을 조합해 복잡한 AI 파이프라인을 설계할 수 있습니다.

---

### 4. Streamlit 설치 및 실행 방법

#### 1. 설치
Streamlit은 Python 기반의 웹 앱 프레임워크입니다. 아래 명령어로 설치할 수 있습니다.

```bash
pip install streamlit
```

#### 2. 실행 방법
Streamlit 앱 파일(예: `app.py`)이 있는 디렉터리에서 아래 명령어를 실행합니다.

```bash
streamlit run app.py
```

- 웹 브라우저가 자동으로 열리며, 기본적으로 `http://localhost:8501`에서 앱이 실행됩니다.
- 여러 앱 파일이 있을 경우, 원하는 파일명을 지정하여 실행하세요.

#### 3. 추가 팁
- Streamlit 앱을 종료하려면 터미널에서 `Ctrl+C`를 누르세요.
- Streamlit 공식 문서: https://docs.streamlit.io/

> 요약: `pip install streamlit`으로 설치 후, `streamlit run <파일명.py>`로 실행하면 웹 앱을 바로 확인할 수 있습니다.



