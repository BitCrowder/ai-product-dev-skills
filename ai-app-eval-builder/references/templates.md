# AI App Eval Templates

## Eval Plan

```markdown
# Eval Plan: [AI Feature]

## Objective
- AI task:
- Release decision supported:
- Baseline:
- Candidate:
- Users affected:
- Failure cost:

## Quality Dimensions
| Dimension | Definition | Grader | Threshold |
|---|---|---|---|

## Dataset Schema
| Field | Type | Required | Description |
|---|---|---|---|
| id | string | yes | Stable case ID |
| input | string/object | yes | User request or task input |
| context | string/list | no | Source docs, retrieved chunks, or tool state |
| expected_behavior | string | yes | What a good output must do |
| reference_answer | string | no | Gold answer when appropriate |
| rubric | string | yes | Case-specific grading criteria |
| metadata | object | yes | Slice, difficulty, source, risk |

## Dataset Slices
| Slice | Purpose | Minimum cases |
|---|---|---:|
| Happy path | Normal use | 10 |
| Edge case | Boundary behavior | 10 |
| Adversarial | Robustness | 5 |
| Production failure | Regression | 5 |

## Rubric
| Score | Meaning | Criteria |
|---|---|---|
| 0 | Fail | Unsafe, unsupported, wrong, or unusable |
| 1 | Partial | Some correct elements but misses key requirement |
| 2 | Pass | Correct, grounded, complete enough |
| 3 | Excellent | Correct and especially useful |

## Automated Checks
| Check | Method | Pass condition |
|---|---|---|

## Human Review
| Sample | Reviewer task | Escalation |
|---|---|---|

## Failure Taxonomy
| Failure type | Definition | Likely fix |
|---|---|---|

## Regression Workflow
1. Freeze dataset version.
2. Run baseline.
3. Run candidate.
4. Compare by slice and failure type.
5. Block release if thresholds fail.
6. Review sampled failures.
7. Record decision and follow-ups.
```

## Example Test Case JSON

```json
{
  "id": "rag-citation-001",
  "input": "What is our refund window for annual plans?",
  "context": ["Refunds are available within 14 days for annual plans."],
  "expected_behavior": "Answer with the 14-day window and cite the provided policy.",
  "reference_answer": "Annual plans can be refunded within 14 days.",
  "rubric": "Pass only if the answer states 14 days and does not invent exceptions.",
  "metadata": {
    "slice": "happy_path",
    "difficulty": "easy",
    "risk": "policy_accuracy",
    "source": "support_policy"
  }
}
```
