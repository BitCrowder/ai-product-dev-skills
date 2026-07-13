# Debugging Example

```text
Use $bug-debugging-playbook to investigate why checkout shows a blank page after coupon apply.
```

```markdown
Root cause: coupon API returns `discount: null`; UI assumes a number and crashes during formatting.
Regression: add null discount test.
```
