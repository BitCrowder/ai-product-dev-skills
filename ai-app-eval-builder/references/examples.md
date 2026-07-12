# AI Eval Examples

## Invocation

```text
Use $ai-app-eval-builder to design evals for a RAG chatbot that answers customer support policy questions with citations.
```

## Output Skeleton

```markdown
# Eval Plan: Support Policy RAG Chatbot

## Objective
Decide whether the new retrieval prompt can ship without increasing unsupported policy claims.

## Quality Dimensions
| Dimension | Definition | Threshold |
|---|---|---|
| Groundedness | Answer only uses retrieved policy text | >= 95% pass |
| Citation accuracy | Cited source supports the claim | >= 95% pass |
| Refusal behavior | Says it cannot answer when context is missing | >= 90% pass |

## Failure Taxonomy
| Failure | Likely fix |
|---|---|
| Unsupported claim | Prompt constraint or retrieval filtering |
| Wrong citation | Citation selection logic |
| Missing context | Chunking or retrieval query rewrite |
```
