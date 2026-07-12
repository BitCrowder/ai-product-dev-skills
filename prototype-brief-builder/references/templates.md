# Prototype Brief Templates

## Full Prototype Brief

```markdown
# Prototype Brief: [Feature/Product]

## Prototype Purpose
- Purpose:
- Fidelity:
- Audience:
- Primary question to answer:
- Not in scope:

## User and Scenario
- User:
- Situation:
- Goal:
- Entry point:
- Successful exit:

## Primary Flow
1. User starts at [screen].
2. User [action].
3. System [response].
4. User reaches [success state].

## Screen Inventory
| Screen | Purpose | User action | System response | Data/content needed | States |
|---|---|---|---|---|---|

## Component Inventory
| Component | Used on screens | Variants | States | Notes |
|---|---|---|---|---|

## State Requirements
| Screen/Component | Default | Empty | Loading | Error | Success | Edge cases |
|---|---|---|---|---|---|---|

## Content Requirements
| Surface | Copy needed | Source | Placeholder allowed? |
|---|---|---|---|

## Interaction Rules
| Trigger | Behavior | Validation | Error handling |
|---|---|---|---|

## Responsive Behavior
| Viewport | Layout behavior | Navigation behavior | Content priority |
|---|---|---|---|

## Analytics and Instrumentation
| Event | Trigger | Properties |
|---|---|---|

## Handoff Notes
- Design system:
- Visual references:
- Accessibility:
- Engineering notes:
- Open questions:
```

## Coding-Agent Prompt Pattern

```text
Build a prototype for [feature] using the brief below. Preserve the described user flow, screen states, and responsive behavior. Do not add new product logic unless marked as an assumption. Use placeholders only where the brief allows them.
```
