# Reasoning Techniques Pattern

## When to Use

- **Complex problem-solving**: Multi-step logical challenges
- **Mathematical reasoning**: Problems requiring systematic thinking
- **Strategic planning**: Evaluating multiple approaches
- **Critical analysis**: Deep examination of options
- **Decision making**: Weighing alternatives systematically
- **Creative exploration**: Generating diverse solutions

## Where It Fits

- **Research analysis**: Breaking down complex research questions
- **Code debugging**: Systematic problem identification
- **Business strategy**: Evaluating strategic options
- **Medical diagnosis**: Differential diagnosis reasoning
- **Legal analysis**: Building logical arguments

## Pros

- **Improved accuracy**: Systematic thinking reduces errors
- **Transparency**: Clear reasoning traces
- **Exploration**: Considers multiple solution paths
- **Robustness**: Multiple methods provide validation
- **Learning**: Reasoning traces help improvement
- **Flexibility**: Different techniques for different problems
- **Quality**: Higher quality solutions through deliberation

## Cons

- **Increased latency**: Multiple reasoning steps take time
- **Token consumption**: Verbose reasoning uses more tokens
- **Complexity**: Managing reasoning flows is challenging
- **Overthinking**: Can make simple problems complex
- **Context limits**: Long reasoning may exceed windows
- **Cost multiplication**: Multiple paths increase costs
- **Diminishing returns**: Extra reasoning may not help

## Real-World Examples

1. **Mathematical Problem Solver**:
   - Chain-of-Thought for step-by-step solutions
   - Self-consistency checking multiple approaches
   - Tree-of-Thoughts exploring solution branches
   - Validation through different methods
   - Clear explanation generation

2. **Strategic Business Advisor**:
   - Tree-of-Thoughts for strategy exploration
   - Debate between growth vs efficiency
   - Self-consistency across market analyses
   - ReAct pattern with data retrieval
   - Synthesis of best strategies

3. **Code Architecture Designer**:
   - Chain-of-Thought for design decisions
   - Tree exploration of architectures
   - Debate between design patterns
   - ReAct with code analysis tools
   - Reasoning persistence for documentation

4. **Medical Diagnostic System**:
   - Differential diagnosis reasoning tree
   - Self-consistency across symptoms
   - Chain-of-Thought for treatment plans
   - Debate between treatment options
   - Evidence-based reasoning traces

5. **Legal Case Analyzer**:
   - Chain-of-Thought for legal arguments
   - Tree exploration of precedents
   - Debate between interpretations
   - Self-consistency across statutes
   - Structured legal reasoning

6. **Investment Analysis Platform**:
    - Tree-of-Thoughts for scenario analysis
    - Self-consistency across valuations
    - Debate bull vs bear cases
    - Chain reasoning for DCF models
    - ReAct with market data retrieval

## Mermaid Diagram

```mermaid
graph TD
    Start[Hard Problem to Solve] --> Choose{Pick Best Way to Think}
    
    Choose -->|Step by Step| StepByStep[Think Through Each Step]
    Choose -->|Explore Options| Tree[Explore Different Paths]
    Choose -->|Double Check| Multiple[Try Multiple Ways]
    Choose -->|Debate It| Debate[Argue Both Sides]
    Choose -->|Think and Do| ThinkDo[Think Then Act, Repeat]
    
    StepByStep --> Steps[Break Into Steps]
    Steps --> Think1[Step 1: First Thought]
    Think1 --> Think2[Step 2: Next Thought]
    Think2 --> Think3[Step 3: Final Thought]
    
    Tree --> Branch[Create Different Ideas]
    Branch --> Explore[Explore Each Path]
    Explore --> Compare[Compare Options]
    Compare --> Remove[Remove Bad Paths]
    
    Multiple --> Make[Make Several Solutions]
    Make --> Path1[Solution Method 1]
    Make --> Path2[Solution Method 2]
    Make --> Path3[Solution Method 3]
    
    Debate --> For[Arguments For]
    Debate --> Against[Arguments Against]
    For --> Discuss[Compare Arguments]
    Against --> Discuss
    
    ThinkDo --> Think[Think About It]
    Think --> Act[Take Action]
    Act --> See[See What Happens]
    See --> Think
    
    Think3 --> Grade[Grade Solutions]
    Remove --> Grade
    Path1 --> Grade
    Path2 --> Grade
    Path3 --> Grade
    Discuss --> Grade
    
    Grade --> Test{Test Against Standards}
    
    Test --> Check[Check Logic]
    Check --> Verify[Verify It Works]
    Verify --> Rank[Rank Best to Worst]
    
    Rank --> Pick{Pick Winner}
    
    Pick -->|One Best| UseBest[Use Best Solution]
    Pick -->|Several Good| Combine[Combine Good Parts]
    
    UseBest --> Limit{Too Many Steps?}
    Combine --> Limit
    
    Limit -->|OK| Continue[Keep Going]
    Limit -->|Too Many| Trim[Remove Extra Steps]
    
    Continue --> Save[Save the Work]
    Trim --> Save
    
    Save --> Keep[Keep for Later Use]
    Keep --> CanReuse[Can Use Again]
    
    CanReuse --> Answer[Final Solution]
    Answer --> End[Problem Solved]
    
    style Start fill:#e1f5fe
    style Choose fill:#fff59d
    style Test fill:#fff9c4
    style Pick fill:#f3e5f5
    style End fill:#c8e6c9
```

[Mermaid Diagram Source](../mermaid-diagrams/reasoning-techniques.mmd)