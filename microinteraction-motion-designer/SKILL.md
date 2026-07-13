---
name: microinteraction-motion-designer
description: Design and implement product-quality microinteractions for apps, websites, and AI-built interfaces. Use when the user asks to improve UI motion, add microinteractions, make an app feel premium or less stiff, design VibeCoding motion prompts, specify animation behavior for buttons, lists, tabs, loading states, page transitions, charts, drag panels, state changes, scroll-linked effects, or translate product UX intent into motion specs and frontend implementation guidance.
---

# Microinteraction Motion Designer

## 中文简介

**微动效设计器**：用于把“界面更丝滑、更高级”转成可实现的微动效规格，覆盖列表进入、按压反馈、骨架屏、Tab、页面切换、拖拽、图表和状态变化。

## Overview

Use this skill to turn vague requests like "make it smoother" or "add premium motion" into precise, implementation-ready microinteraction specifications.

Microinteractions must explain state, acknowledge user action, preserve spatial continuity, and reduce abruptness. Do not add motion as decoration when it does not help the user understand what changed.

## Core Principle

Good UI motion imitates physical rhythm and cause-effect:

- user action causes visible feedback
- entering content has order and timing
- leaving content exits gracefully
- page changes preserve direction and hierarchy
- draggable surfaces feel elastic and bounded
- data changes reveal scale and value changes over time

Use easing, stagger, spring behavior, opacity, transform, and continuity deliberately. Avoid hard jumps unless the product intentionally needs an instant state change.

## Workflow

### 1. Identify the Interaction Moment

First determine what the motion is supposed to communicate:

- feedback: "your action was recognized"
- continuity: "this is the same object moving"
- hierarchy: "you entered a deeper page"
- progress: "content is loading or arriving"
- state: "this item changed from one state to another"
- delight: "the interface feels alive without slowing the task"

Ask for the screen, component, trigger, platform, and existing motion style if missing. If the user wants speed, make assumptions and label them.

### 2. Choose the Motion Pattern

Select one or more patterns from `references/motion-patterns.md`.

Prefer common patterns:

- staggered list entrance
- press ripple
- skeleton shimmer
- sliding tabs
- crossfade or dissolve
- scroll-linked transformation
- spring drag
- chart growth
- push transition
- state morph

Do not stack many effects on the same element. One primary motion and one supporting motion is usually enough.

### 3. Write a Motion Spec

Use `references/templates.md`. A spec must include:

- trigger
- animated object
- starting state
- ending state
- duration or spring parameters
- easing
- delay or stagger
- interruption behavior
- reduced-motion fallback
- implementation notes
- acceptance criteria

Never stop at adjectives such as smooth, premium, bouncy, or silky. Translate them into timing, easing, transforms, opacity, and behavior.

### 4. Map Motion to Implementation

Adapt guidance to the target stack:

- CSS transitions/keyframes for simple opacity, transform, shimmer, and reduced-motion handling
- Framer Motion or Motion One for React layout transitions, enter/exit, and spring gestures
- React Native Reanimated for mobile gesture and spring motion
- native iOS/Android animation APIs when working in native apps
- chart libraries or requestAnimationFrame only when needed for data animation

Respect existing design systems and framework conventions. Do not introduce a heavy animation library for one simple transition.

### 5. Validate Quality

Read `references/checklists.md` before finalizing.

The motion is not ready if:

- it does not communicate a state or relationship
- it delays a frequent workflow
- it causes layout shift or text overlap
- it ignores reduced-motion preferences
- it animates expensive properties without need
- it feels disconnected from the user's action
- it makes navigation hierarchy unclear

## Output Modes

Choose the output that matches the user request:

- **Motion audit:** identify stiff moments and recommend patterns.
- **Motion spec:** produce implementation-ready specs.
- **VibeCoding prompt:** write precise prompts for Codex, Cursor, or other AI coding tools.
- **Implementation guidance:** provide stack-specific code direction and acceptance criteria.
- **QA review:** evaluate whether existing motion feels natural, performant, and accessible.

## References

- Read `references/motion-patterns.md` when choosing or explaining motion patterns.
- Read `references/templates.md` when writing specs or AI coding prompts.
- Read `references/checklists.md` before finalizing a motion plan.
- Read `references/examples.md` for ready-to-use prompts and compact examples.
