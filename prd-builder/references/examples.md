# PRD Builder Examples

## Invocation

```text
Use $prd-builder to create a PRD for an AI meeting-notes feature that turns Zoom transcripts into action items for startup teams.
```

## Lightweight Output Skeleton

```markdown
# PRD: AI Meeting Action Items

## Executive Summary
Startup teams lose follow-through after meetings because decisions and owners are buried in transcripts. Build a v1 that extracts action items, owners, and due dates from uploaded transcripts, then lets users confirm before saving.

## Known Facts
- Users have meeting transcripts.
- Desired outcome is clearer follow-through.

## Assumptions
- Users trust AI only after review.
- Transcript quality varies by meeting tool.

## Core Requirements
| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| FR-1 | The user can upload a transcript file. | Must | Given a `.txt` transcript, when uploaded, then the system parses it and shows extraction status. |
| FR-2 | The system suggests action items with owner and due date. | Must | Given a parsed transcript, when extraction completes, then each suggestion includes task text and confidence. |
```
