# Planning Pattern

The Planning pattern decomposes a goal into milestones, builds a dependency graph, and allocates resources under constraints like time and budget. Execution proceeds step by step with checkpoints that monitor progress. When a step is blocked or new information arises, the agent replans dynamically rather than failing. This pattern trades upfront planning overhead for strategic, adaptive execution that handles complex, long-running, multi-step projects.

## When to Use

- **Complex multi-step projects**: When tasks have multiple dependencies and phases
- **Goal-oriented workflows**: When working toward specific, measurable objectives
- **Resource-constrained operations**: When managing budgets, time, or computational limits
- **Uncertain environments**: When adaptability to changing conditions is needed
- **Collaborative tasks**: When coordinating multiple agents or tools
- **Long-running processes**: When tasks span extended timeframes

## Where It Fits

- **Project management automation**: Breaking down projects into executable tasks
- **Software development**: Planning features from requirements to deployment
- **Research projects**: Organizing literature review, experimentation, and analysis
- **Content production**: Planning multi-part content series or campaigns
- **Business process automation**: Orchestrating complex business workflows

## Pros

- **Strategic execution**: Transforms reactive agents into proactive planners
- **Dependency management**: Handles complex task interdependencies
- **Resource optimization**: Allocates resources efficiently across steps
- **Adaptability**: Can adjust plans based on new information
- **Progress visibility**: Clear tracking of milestone completion
- **Risk mitigation**: Early identification of blockers and issues
- **Reusability**: Plans can be templated and reused

## Cons

- **Upfront overhead**: Planning phase adds initial latency
- **Rigidity risk**: Over-planning can reduce flexibility
- **Complexity**: Managing plan state and dependencies is challenging
- **Prediction errors**: Initial plans may be based on incorrect assumptions
- **Replanning costs**: Adjusting plans mid-execution can be expensive
- **Context limitations**: Long plans may exceed context windows
- **Coordination overhead**: Managing multiple agents increases complexity

## Real-World Examples

1. **Software Feature Development**:
   - Requirements analysis and design
   - Development task breakdown
   - Testing strategy planning
   - Deployment scheduling
   - Documentation preparation
   - Rollback planning

2. **Marketing Campaign Execution**:
   - Market research and analysis
   - Content creation schedule
   - Channel selection and timing
   - Budget allocation
   - Performance monitoring setup
   - A/B testing plans

3. **Academic Research Project**:
   - Literature review planning
   - Hypothesis formulation
   - Experiment design
   - Data collection schedule
   - Analysis methodology
   - Publication timeline

4. **Data Migration Project**:
   - Data audit and mapping
   - Schema design
   - Migration script development
   - Testing phases
   - Rollout schedule
   - Validation checkpoints

5. **Product Launch Planning**:
   - Development milestones
   - Marketing preparation
   - Sales enablement
   - Support documentation
   - Launch event coordination
   - Post-launch monitoring

6. **Compliance Audit Preparation**:
    - Requirement identification
    - Document gathering
    - Gap analysis
    - Remediation planning
    - Review scheduling
    - Report generation

## Mermaid Diagram

```mermaid
graph TD
    Start[Goal Input] --> Decompose[Decompose into Milestones]
    Decompose --> Map[Create Dependency Graph]
    
    Map --> Constraints{Check Constraints}
    Constraints --> Data[Data Availability]
    Constraints --> Auth[Authorization Check]
    Constraints --> Budget[Budget Limits]
    Constraints --> Time[Deadlines/SLAs]
    
    Data --> Plan[Generate Step-by-Step Plan]
    Auth --> Plan
    Budget --> Plan
    Time --> Plan
    
    Plan --> Assign[Assign Agent/Tool per Step]
    Assign --> Step1[Execute Step 1]
    
    Step1 --> Check1{Checkpoint}
    Check1 -->|Success| Step2[Execute Step 2]
    Check1 -->|Blocked| Analyze[Analyze Blocker]
    
    Step2 --> Check2{Checkpoint}
    Check2 -->|Success| Step3[Execute Step 3]
    Check2 -->|Issue| Analyze
    
    Step3 --> Check3{Checkpoint}
    Check3 -->|Success| StepN[Execute Step N]
    Check3 -->|Problem| Analyze
    
    Analyze --> NewInfo{New Information?}
    NewInfo -->|Yes| Replan[Adjust Plan]
    NewInfo -->|No| Escalate[Escalate Issue]
    
    Replan --> Assign
    Escalate --> Handle[Handle Exception]
    
    StepN --> Progress[Track Progress]
    Progress --> Complete{Goals Met?}
    
    Complete -->|Yes| Accept[Acceptance Criteria Check]
    Complete -->|No| Analyze
    
    Accept --> PostMortem[Generate Post-Mortem]
    Handle --> PostMortem
    PostMortem --> End[Close Task]
    
    style Start fill:#e1f5fe
    style Constraints fill:#fff9c4
    style NewInfo fill:#fff59d
    style Complete fill:#f3e5f5
    style End fill:#c8e6c9
```

[Mermaid Diagram Source](../mermaid-diagrams/planning.mmd)