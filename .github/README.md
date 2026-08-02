# Agentic Design Patterns Documentation

A comprehensive visual and textual documentation of 21 essential agentic design patterns for building intelligent AI systems with its code examples using langchain and opensource models.

##  What's Included

This repository contains four main types of documentation for each pattern:

###  Mermaid Diagrams (`/mermaid-diagrams`)
Visual flowcharts in plain English showing how each pattern works, designed to be easily understood without technical jargon.

###  Pattern Discussions (`/pattern-discussion`)
Detailed explanations covering:
- When to use each pattern
- Where it fits in your architecture
- Concise pattern definitions
- Pros and cons
- Implementation considerations
- Embedded Mermaid diagrams

###  ASCII Art Diagrams (`/ascii-art`)
Text-based diagrams perfect for copying into Miro boards, documentation, or anywhere that doesn't support rich graphics.

###  Code (`/code`)
Runnable examples implementing each pattern with [LangChain](https://python.langchain.com) and NVIDIA NIM endpoints. See [Running the Code](#-running-the-code) to get started.

Available so far: [Prompt Chaining](../code/prompt-chaining.py) - more examples in progress.

##  The 21 Patterns

### Core Patterns
1. **Prompt Chaining** - Breaking complex tasks into sequential steps
- [Ascii Art](../ascii-art/prompt-chaining.txt)
- [Mermaid Diagram](../mermaid-diagrams/prompt-chaining.mmd)
- [Discussion](../pattern-discussion/prompt-chaining.md)

2. **Routing** - Directing requests to the right handler
- [Ascii Art](../ascii-art/routing.txt)
- [Mermaid Diagram](../mermaid-diagrams/routing.mmd)
- [Discussion](../pattern-discussion/routing.md)

3. **Parallelization** - Running multiple tasks simultaneously
- [Ascii Art](../ascii-art/parallelization.txt)
- [Mermaid Diagram](../mermaid-diagrams/parallelization.mmd)
- [Discussion](../pattern-discussion/parallelization.md)

4. **Reflection** - Self-evaluation and improvement
- [Ascii Art](../ascii-art/reflection.txt)
- [Mermaid Diagram](../mermaid-diagrams/reflection.mmd)
- [Discussion](../pattern-discussion/reflection.md)

5. **Tool Use** - Integrating external capabilities
- [Ascii Art](../ascii-art/tool-use.txt)
- [Mermaid Diagram](../mermaid-diagrams/tool-use.mmd)
- [Discussion](../pattern-discussion/tool-use.md)

### Advanced Patterns
6. **Planning** - Strategic task decomposition
- [Ascii Art](../ascii-art/planning.txt)
- [Mermaid Diagram](../mermaid-diagrams/planning.mmd)
- [Discussion](../pattern-discussion/planning.md)

7. **Multi-Agent Collaboration** - Coordinating multiple agents
- [Ascii Art](../ascii-art/multi-agent-collaboration.txt)
- [Mermaid Diagram](../mermaid-diagrams/multi-agent-collaboration.mmd)
- [Discussion](../pattern-discussion/multi-agent-collaboration.md)

8. **Memory Management** - Storing and retrieving context
- [Ascii Art](../ascii-art/memory-management.txt)
- [Mermaid Diagram](../mermaid-diagrams/memory-management.mmd)
- [Discussion](../pattern-discussion/memory-management.md)

9. **Learning and Adaptation** - Improving over time
- [Ascii Art](../ascii-art/learning-and-adaptation.txt)
- [Mermaid Diagram](../mermaid-diagrams/learning-and-adaptation.mmd)
- [Discussion](../pattern-discussion/learning-and-adaptation.md)

10. **Model Context Protocol** - Standardized agent communication
- [Ascii Art](../ascii-art/model-context-protocol.txt)
- [Mermaid Diagram](../mermaid-diagrams/model-context-protocol.mmd)
- [Discussion](../pattern-discussion/model-context-protocol.md)

### System Patterns
11. **Goal Setting and Monitoring** - Tracking objectives
- [Ascii Art](../ascii-art/goal-setting-and-monitoring.txt)
- [Mermaid Diagram](../mermaid-diagrams/goal-setting-and-monitoring.mmd)
- [Discussion](../pattern-discussion/goal-setting-and-monitoring.md)

12. **Exception Handling and Recovery** - Graceful error management
- [Ascii Art](../ascii-art/exception-handling-and-recovery.txt)
- [Mermaid Diagram](../mermaid-diagrams/exception-handling-and-recovery.mmd)
- [Discussion](../pattern-discussion/exception-handling-and-recovery.md)

13. **Human-in-the-Loop** - Incorporating human feedback
- [Ascii Art](../ascii-art/human-in-the-loop.txt)
- [Mermaid Diagram](../mermaid-diagrams/human-in-the-loop.mmd)
- [Discussion](../pattern-discussion/human-in-the-loop.md)

14. **Knowledge Retrieval (RAG)** - Accessing external knowledge
- [Ascii Art](../ascii-art/knowledge-retrieval-rag.txt)
- [Mermaid Diagram](../mermaid-diagrams/knowledge-retrieval-rag.mmd)
- [Discussion](../pattern-discussion/knowledge-retrieval-rag.md)

15. **Inter-Agent Communication** - Agent-to-agent messaging
- [Ascii Art](../ascii-art/inter-agent-communication-a2a.txt)
- [Mermaid Diagram](../mermaid-diagrams/inter-agent-communication-a2a.mmd)
- [Discussion](../pattern-discussion/inter-agent-communication-a2a.md)

### Optimization Patterns
16. **Resource-Aware Optimization** - Efficient resource usage
- [Ascii Art](../ascii-art/resource-aware-optimization.txt)
- [Mermaid Diagram](../mermaid-diagrams/resource-aware-optimization.mmd)
- [Discussion](../pattern-discussion/resource-aware-optimization.md)

17. **Reasoning Techniques** - Structured thinking approaches
- [Ascii Art](../ascii-art/reasoning-techniques.txt)
- [Mermaid Diagram](../mermaid-diagrams/reasoning-techniques.mmd)
- [Discussion](../pattern-discussion/reasoning-techniques.md)

18. **Guardrails/Safety Patterns** - Ensuring safe operations
- [Ascii Art](../ascii-art/guardrails-safety-patterns.txt)
- [Mermaid Diagram](../mermaid-diagrams/guardrails-safety-patterns.mmd)
- [Discussion](../pattern-discussion/guardrails-safety-patterns.md)

19. **Evaluation and Monitoring** - Performance tracking
- [Ascii Art](../ascii-art/evaluation-and-monitoring.txt)
- [Mermaid Diagram](../mermaid-diagrams/evaluation-and-monitoring.mmd)
- [Discussion](../pattern-discussion/evaluation-and-monitoring.md)

### Strategic Patterns
20. **Prioritization** - Managing task importance
- [Ascii Art](../ascii-art/prioritization.txt)
- [Mermaid Diagram](../mermaid-diagrams/prioritization.mmd)
- [Discussion](../pattern-discussion/prioritization.md)

21. **Exploration and Discovery** - Finding new solutions
- [Ascii Art](../ascii-art/exploration-and-discovery.txt)
- [Mermaid Diagram](../mermaid-diagrams/exploration-and-discovery.mmd)
- [Discussion](../pattern-discussion/exploration-and-discovery.md)

##  Quick Start

Each pattern includes:
- A visual diagram showing the flow (Mermaid + ASCII)
- Embedded diagrams directly in pattern discussions
- Plain English explanations
- Concise pattern definitions
- Real-world use cases
- Implementation tips

Navigate to any folder to explore the patterns in your preferred format.

##  Running the Code

Examples live in [`/code`](../code) and use [LangChain](https://python.langchain.com) with NVIDIA NIM endpoints.

```bash
cd code
python -m venv .venv
.venv\Scripts\activate          # Windows (use: source .venv/bin/activate on macOS/Linux)
pip install langchain-nvidia-ai-endpoints python-dotenv colorama rich
```

Add your NVIDIA API key to `code/resources/.env`:

```env
API_KEY=your_nvidia_api_key
```

Then run an example:

```bash
python prompt-chaining.py
```

##  Source

These patterns are distilled from extensive research on agentic AI systems, made accessible through simple visual representations and clear explanations.
- [Agentic Design Patterns Book](../books/Agentic_Design_Patterns_Complete.pdf)

##  Contributing

Feel free to suggest improvements or additional patterns through issues or pull requests.

##  License

[MIT License](../LICENSE) - Use these patterns freely in your projects!