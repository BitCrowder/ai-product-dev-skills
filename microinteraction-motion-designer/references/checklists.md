# Motion Quality Checklist

## Product Fit

- Motion communicates a state change, feedback, hierarchy, progress, or continuity.
- Motion matches the product tone: utility tools stay restrained; playful apps can be more expressive.
- Motion does not distract from reading or completing the task.
- Motion frequency is appropriate for how often the interaction occurs.

## Spec Quality

- Trigger is explicit.
- Animated object is explicit.
- Starting and ending states are defined.
- Duration, easing, and delay/stagger are defined.
- Interruption behavior is defined.
- Reduced-motion fallback is defined.
- Acceptance criteria are observable.

## UX Quality

- User action receives immediate feedback.
- Navigation direction matches information hierarchy.
- Same-level changes feel continuous, not like a page jump.
- Drag surfaces have resistance, velocity, and snap points.
- Loading states avoid layout shift when real content appears.
- Data animations reveal change without misleading the scale.

## Engineering Quality

- Prefer transform and opacity for performance.
- Avoid animating layout-heavy properties unless necessary.
- Avoid long-running animations on large lists.
- Respect existing design system and framework patterns.
- Do not add a large animation dependency for one simple transition.
- Test mobile touch behavior when the motion is gesture-based.

## Accessibility

- Respect `prefers-reduced-motion` or platform equivalent.
- Do not rely on motion alone to communicate critical state.
- Avoid flashing, intense vibration, or rapid repeated motion.
- Keep focus states and keyboard navigation intact.

## Red Flags

- The spec only says "make it smooth" or "add premium feel".
- Multiple effects compete on the same object.
- Animation delays a common workflow.
- Motion continues after the user changes state.
- Text overlaps or layout shifts during animation.
- A page transition hides where the user came from.
