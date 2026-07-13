# Code Review Example

```text
Use $code-review-assistant to review this PR diff.
```

```markdown
### High: Empty results crash search page
File/line: `src/search.tsx:48`
Issue: code reads `results[0].title` before checking length.
Impact: users with no matches see a runtime crash.
Suggested fix: render empty state before accessing first result.
```
