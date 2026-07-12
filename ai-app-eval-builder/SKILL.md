---
name: ai-app-eval-builder
description: Design evaluation systems for AI applications, LLM features, RAG pipelines, agents, chatbots, copilots, summarizers, classifiers, extraction tools, and prompt/model changes. Use when the user asks to evaluate AI quality, create evals, build test datasets, define rubrics, compare prompts or models, measure hallucination, test retrieval quality, assess agent tool use, or create regression gates for AI product releases.
---

# AI App Eval Builder

## Overview

Use this skill to turn vague AI quality goals into measurable eval plans with datasets, rubrics, graders, failure taxonomy, thresholds, and regression workflow.

The core rule: define what good means before judging outputs.

## Workflow

### 1. Define the AI System

Identify:

- AI feature type: chat, RAG, agent, extraction, classification, summarization, generation, coding, recommendation, or workflow automation
- user task
- expected output format
- allowed tools or data sources
- failure cost
- production constraints such as latency, cost, privacy, and safety
- current baseline prompt, model, or system

If the system is underspecified, ask focused questions or proceed with labeled assumptions.

### 2. Define Quality Dimensions

Choose dimensions relevant to the task:

- task success
- factuality or groundedness
- retrieval relevance
- citation accuracy
- instruction following
- completeness
- concision
- format validity
- safety or policy compliance
- tool-use correctness
- latency and cost
- user experience

Do not use a single "quality" score unless it decomposes into observable criteria.

### 3. Build the Dataset Plan

Create a dataset schema with:

- input
- context or retrieved documents
- expected behavior
- reference answer or rubric
- metadata
- difficulty
- risk category
- source

Include slices:

- happy path
- ambiguous inputs
- adversarial or prompt-injection cases
- missing information
- long context
- edge domains
- multilingual or locale-specific cases if relevant
- known production failures

Use `references/templates.md` for schemas.

### 4. Choose Grading Strategy

Select one or more:

- deterministic checks for JSON schema, regex, exact labels, citations, or tool calls
- human review for nuanced quality
- model-graded rubrics for scalable qualitative evaluation
- pairwise comparison for prompt/model variants
- retrieval metrics for RAG
- trace review for agents

Every grader must include criteria, pass/fail thresholds, and examples of passing and failing outputs.

### 5. Define Failure Taxonomy

Classify failures so teams can fix root causes:

- instruction miss
- hallucination or unsupported claim
- retrieval miss
- irrelevant retrieval
- citation mismatch
- tool selection error
- tool argument error
- unsafe response
- bad format
- incomplete answer
- excessive verbosity
- latency or cost regression

Tie each failure type to likely remediation.

### 6. Create Regression Workflow

Specify:

- baseline version
- candidate version
- dataset version
- pass thresholds
- review sampling
- release blocker criteria
- reporting format
- cadence

For high-risk AI features, require human review for at least a sampled set of failures.

### 7. Quality Gate

Read `references/checklists.md` before finalizing.

The eval plan is not ready if:

- success is not decomposed into criteria
- no dataset schema exists
- edge cases are missing
- grader thresholds are vague
- failure types do not map to fixes
- regression workflow is absent

## Output Rules

- Start with the eval objective and release decision it supports.
- Include a dataset schema and at least 10 example test case ideas unless the user asks for a shorter version.
- Include pass/fail thresholds.
- Mark which checks can be automated and which need human review.
- Do not claim an AI app is good without measurement.

## References

- Read `references/templates.md` for eval plan, dataset, rubric, and report structures.
- Read `references/checklists.md` before finalizing.
- Read `references/examples.md` for compact examples.
