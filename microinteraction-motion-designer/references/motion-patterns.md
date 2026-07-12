# Motion Patterns

Use these patterns to turn product intent into concrete UI motion. Prefer the smallest pattern that communicates the state change.

## 1. Staggered List Entrance

**Use when:** a list, feed, card group, menu, search results, or onboarding steps appear.

**Behavior:** items enter one by one with a short delay, usually from slight vertical offset and low opacity to final position and full opacity.

**Why it works:** creates rhythm and order, guiding the user's eye naturally downward.

**Typical spec:** 180-280ms per item, 30-70ms stagger, `ease-out`, `opacity: 0 -> 1`, `translateY(8-16px) -> 0`.

**Avoid:** long delays on large lists; animate only first visible items or use virtualization-safe entrance.

## 2. Press Ripple

**Use when:** buttons, list rows, cards, tabs, or touch targets need immediate feedback.

**Behavior:** a subtle circular wave expands from the press point or element center while fading out.

**Why it works:** tells the user the tap/click was recognized.

**Typical spec:** 250-450ms, `ease-out`, scale `0 -> 1`, opacity `0.18 -> 0`.

**Avoid:** high-contrast ripples on premium minimalist UIs; prefer a quieter pressed-state scale or background tint.

## 3. Skeleton Shimmer

**Use when:** content takes time to load and the final layout is predictable.

**Behavior:** show gray placeholders with a soft highlight moving across them.

**Why it works:** reduces waiting anxiety and indicates content is coming.

**Typical spec:** 1000-1600ms loop, low-contrast gradient, no layout shift when real content arrives.

**Avoid:** using shimmer for very fast loads, unpredictable layouts, or long-running background tasks where progress is more useful.

## 4. Sliding Tabs

**Use when:** tab selection changes within the same level of navigation.

**Behavior:** the active indicator slides with the finger or click transition; content can crossfade or slide slightly in the same direction.

**Why it works:** preserves continuity and clearly shows the current category.

**Typical spec:** indicator 180-260ms, content 160-220ms, `ease-out` or spring with low bounce.

**Avoid:** making content move in the opposite direction from the tab or animating every internal element.

## 5. Crossfade or Dissolve

**Use when:** two pieces of content occupy the same position and one replaces the other.

**Behavior:** outgoing content fades out while incoming content fades in, sometimes with tiny scale or blur change.

**Why it works:** avoids abrupt visual jumps.

**Typical spec:** 150-240ms, overlap 40-80ms, opacity crossfade, optional scale `0.98 -> 1`.

**Avoid:** crossfading unrelated navigation levels where a push transition better communicates hierarchy.

## 6. Scroll-Linked Transformation

**Use when:** scrolling should reveal more content or compress persistent UI.

**Behavior:** headers shrink, titles collapse, background blur appears, or supporting elements fade as the page scrolls.

**Why it works:** gives content more room while preserving orientation.

**Typical spec:** map scroll range to transform/opacity; clamp values; keep motion tied to scroll position.

**Avoid:** scroll effects that fight user control, hide navigation too early, or cause jank.

## 7. Spring Drag

**Use when:** bottom sheets, drawers, cards, sliders, or draggable panels move with direct manipulation.

**Behavior:** the surface follows the gesture, resists bounds, then springs to the nearest snap point.

**Why it works:** creates a physical, high-quality feeling and clarifies the allowed range.

**Typical spec:** snap points, rubber-band resistance outside bounds, spring stiffness/damping, velocity-aware release.

**Avoid:** panels that stop rigidly, overshoot too far, or lack clear snap positions.

## 8. Chart Growth

**Use when:** bars, progress, metrics, or dashboards enter or update.

**Behavior:** values animate from baseline or previous value to target; labels count up in sync.

**Why it works:** makes data change more intuitive and alive.

**Typical spec:** 500-900ms, stagger bars 40-80ms, `ease-out`; count numbers over the same duration.

**Avoid:** replaying data animation every time the user returns to the page; animate on first reveal or meaningful update.

## 9. Push Transition

**Use when:** navigating into a detail page or deeper hierarchy.

**Behavior:** new page slides in from the side while previous page moves out or recedes in the opposite direction.

**Why it works:** communicates page hierarchy and direction.

**Typical spec:** 220-350ms, direction matches navigation model; support back gesture.

**Avoid:** using push for same-level tab switches or modal overlays.

## 10. State Morph

**Use when:** the same component changes state, such as save to saved, follow to following, collapsed to expanded, or pending to complete.

**Behavior:** color, icon, shape, label, and size transition continuously instead of swapping abruptly.

**Why it works:** lets the user perceive the state change as one continuous object.

**Typical spec:** 160-280ms, icon morph or crossfade, background/color transition, optional subtle scale.

**Avoid:** morphing unrelated icons that become confusing; use a short crossfade when shapes are too different.

## Easing Guidance

- Use `ease-out` for entrances and feedback.
- Use `ease-in` for exits.
- Use `ease-in-out` for same-level transitions.
- Use spring motion for direct manipulation and snap-back.
- Add "弹簧阻尼感" by increasing damping enough to avoid cartoon bounce.
- Add "先快后慢" with strong ease-out: fast start, gentle settle.
- Add "微震颤" only for validation errors or playful confirmations, never for core reading.
