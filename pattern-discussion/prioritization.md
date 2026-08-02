# Prioritization Pattern

Prioritization scores queued tasks by value, effort, urgency, and risk, then ranks them using a formula (Priority = Value/Effort x Urgency). Tasks are executed from the top of the ranked queue. When a higher-priority item arrives, the current task can be preempted and state saved. Aging and quotas prevent low-priority starvation. The pattern trades scoring overhead and context-switching cost for optimal resource utilization and responsive, fair task scheduling.

## When to Use

- **Resource constraints**: Limited processing capacity
- **Multiple objectives**: Competing goals and tasks
- **Dynamic environments**: Constantly changing priorities
- **Complex dependencies**: Tasks with interdependencies
- **Time-sensitive operations**: Deadline-driven work
- **Fair scheduling**: Preventing task starvation

## Where It Fits

- **Task management systems**: Workflow orchestration
- **Customer service**: Ticket prioritization
- **Manufacturing**: Production scheduling
- **Healthcare**: Patient triage systems
- **DevOps**: Deployment and maintenance prioritization

## Pros

- **Efficiency**: Optimal use of resources
- **Responsiveness**: High-priority items handled first
- **Fairness**: Prevents indefinite delays
- **Adaptability**: Adjusts to changing conditions
- **Transparency**: Clear prioritization logic
- **Goal alignment**: Tasks ranked by business value
- **Scalability**: Handles growing task queues

## Cons

- **Complexity**: Priority calculation can be complex
- **Overhead**: Continuous reordering costs resources
- **Starvation risk**: Low-priority tasks may wait forever
- **Context switching**: Preemption adds overhead
- **Subjective scoring**: Priority factors may be disputed
- **Dependencies**: Complex dependency management
- **Prediction errors**: Effort estimates may be wrong

## Real-World Examples

1. **Customer Support System**:
   - Premium customers get priority
   - Urgent issues ranked higher
   - Age-based escalation
   - Skill-based routing
   - SLA compliance tracking
   - Load balancing across agents

2. **Software Development Pipeline**:
   - Critical bugs prioritized
   - Feature value scoring
   - Technical debt scheduling
   - Dependency resolution
   - Sprint capacity planning
   - Resource allocation

3. **Healthcare Triage**:
   - Emergency severity scoring
   - Wait time consideration
   - Resource availability
   - Specialist routing
   - Test result prioritization
   - Appointment scheduling

4. **Manufacturing Scheduler**:
   - Order value prioritization
   - Deadline management
   - Resource optimization
   - Setup time minimization
   - Quality requirements
   - Maintenance windows

5. **Content Publishing**:
   - Trending topic priority
   - Editorial calendar
   - Author availability
   - SEO value scoring
   - Social media timing
   - Cross-platform coordination

6. **Network Traffic Management**:
    - QoS packet prioritization
    - Bandwidth allocation
    - Latency-sensitive routing
    - Fair queuing
    - Emergency traffic priority
    - Load balancing

## Mermaid Diagram

```mermaid
graph TD
    Start[Task Queue] --> Build[Build Dependency Graph]
    
    Build --> Map[Map Dependencies]
    Map --> Tasks[Task List]
    Tasks --> T1[Task 1]
    Tasks --> T2[Task 2]
    Tasks --> T3[Task 3]
    Tasks --> TN[Task N]
    
    T1 --> Score[Score Each Task]
    T2 --> Score
    T3 --> Score
    TN --> Score
    
    Score --> Value{Scoring Factors}
    
    Value --> Business[Business Value]
    Value --> Risk[Risk Level]
    Value --> Effort[Effort Required]
    Value --> Urgency[Time Sensitivity]
    Value --> Dependencies[Dependency Count]
    
    Business --> Calculate[Calculate Priority Score]
    Risk --> Calculate
    Effort --> Calculate
    Urgency --> Calculate
    Dependencies --> Calculate
    
    Calculate --> Formula[Priority = Value/Effort × Urgency × Risk]
    
    Formula --> Rank[Rank Tasks]
    Rank --> Order[Initial Order]
    
    Order --> Schedule{Scheduling Strategy}
    
    Schedule --> Quota[Apply Quotas]
    Schedule --> Aging[Task Aging]
    Schedule --> Balance[Load Balance]
    
    Quota --> Prevent[Prevent Starvation]
    Aging --> Boost[Boost Old Tasks]
    Balance --> Distribute[Distribute Work]
    
    Prevent --> Queue2[Priority Queue]
    Boost --> Queue2
    Distribute --> Queue2
    
    Queue2 --> Execute[Execute Top Task]
    
    Execute --> Monitor{New High Priority?}
    
    Monitor -->|Yes| Preempt[Preempt Current]
    Monitor -->|No| Continue[Continue Current]
    
    Preempt --> Save[Save State]
    Save --> Switch[Switch to High Priority]
    
    Continue --> Complete{Task Complete?}
    Switch --> Complete
    
    Complete -->|Yes| Remove[Remove from Queue]
    Complete -->|No| Execute
    
    Remove --> Events{New Events?}
    
    Events -->|Yes| Reorder[Re-calculate Priorities]
    Events -->|No| Next[Get Next Task]
    
    Reorder --> Rank
    Next --> Execute
    
    Next --> End[Optimized Execution]
    
    style Start fill:#e1f5fe
    style Value fill:#fff59d
    style Schedule fill:#fff9c4
    style Monitor fill:#f3e5f5
    style End fill:#c8e6c9
```

[Mermaid Diagram Source](../mermaid-diagrams/prioritization.mmd)