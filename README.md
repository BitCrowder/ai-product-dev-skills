# AI Product Dev Skills

<p align="center">
  <strong>A reusable skill library for AI product work — from discovery to launch.</strong><br/>
  Built for Codex · Cursor · Claude Code · ChatGPT agents who need process, not just prompts.
</p>

<p align="center">
  <img src="docs/assets/hero.svg" alt="AI Product Dev Skills workflow map" width="100%" />
</p>

<p align="center">
  <a href="#中文"><img src="https://img.shields.io/badge/中文-说明-red" alt="中文" /></a>
  <img src="https://img.shields.io/badge/skills-20%2B-blue" alt="skills" />
  <img src="https://img.shields.io/badge/workflow-evidence--first-success" alt="evidence" />
  <a href="https://github.com/BitCrowder/ai-product-dev-skills"><img src="https://img.shields.io/github/stars/BitCrowder/ai-product-dev-skills?style=social" alt="stars" /></a>
</p>

---

## The problem

Teams don’t lack prompts. They lack **repeatable workflows** that:

1. clarify inputs
2. separate facts from assumptions
3. produce handoff-ready artifacts
4. leave verification evidence for the next step

This repo packages those workflows as installable skills spanning product discovery, definition, design, engineering, and release.

## Skill map (V2)

| Category | Skills | Solves |
| --- | --- | --- |
| **Discover** | `competitive-research-brief`, `feature-discovery-interviewer`, `user-feedback-synthesizer`, `metric-diagnosis` | Is this problem real? What’s the evidence? |
| **Decide** | `prd-builder`, `roadmap-prioritizer`, `experiment-designer` | What should we build next, and why? |
| **Design** | `prototype-brief-builder`, `microinteraction-motion-designer` | How should it feel and behave? |
| **Build** | `spec-to-implementation-plan`, `codebase-onboarding`, `test-generator`, `code-review-assistant`, `bug-debugging-playbook`, `refactor-with-safety`, `issue-to-pr` | Ship safely with AI coding agents |
| **Launch** | `launch-readiness-checklist`, `stakeholder-update-writer`, `ai-app-eval-builder`, `skill-repo-release-verifier` | Release with confidence |

Full Chinese catalog: [`docs/skill-catalog.zh.md`](docs/skill-catalog.zh.md)

## Quick start

```bash
git clone https://github.com/BitCrowder/ai-product-dev-skills.git
# Point your agent / Codex skills root at this directory
# or copy individual skill folders into ~/.codex/skills/
```

Then invoke by name, for example:

```text
Use $prd-builder. Inputs: research notes + target user + constraints.
Output a testable PRD with evidence/assumption ledger.
```

```text
Use $roadmap-prioritizer on these candidates with capacity and dependencies.
Show scoring separately from the final decision.
```

## What makes a “skill” here

Unlike a one-off prompt, each skill defines:

- required inputs
- fact vs assumption handling
- a fixed output contract
- upstream / downstream handoffs
- risks and verification notes

## Example chain

```text
feature-discovery-interviewer
        ↓
user-feedback-synthesizer
        ↓
prd-builder → roadmap-prioritizer
        ↓
spec-to-implementation-plan → test-generator
        ↓
launch-readiness-checklist → stakeholder-update-writer
```

## Who should star this

- AI PMs building with coding agents
- Indie hackers who want product rigor without process theater
- Eng leads standardizing how AI work is handed off

## Validation

V2 upgrade verification notes: [`docs/validation/skill-v2-validation-report.md`](docs/validation/skill-v2-validation-report.md)

## Related

- [website-builder-skill](https://github.com/BitCrowder/website-builder-skill)
- [anti-slop-ui-redesigner](https://github.com/BitCrowder/anti-slop-ui-redesigner)
- [design-dna-compiler](https://github.com/BitCrowder/design-dna-compiler)

---

## 中文

**一句话：** 面向 AI 产品开发的可复用 Skill 库——从发现、决策、设计、实现到发布，每一步都有输入契约与证据边界。

团队缺的不是零散提示词，而是能重复使用、能说明判断依据、也能交接给下一步的流程。打开 [`docs/skill-catalog.zh.md`](docs/skill-catalog.zh.md) 按场景选用即可。

觉得有用的话，欢迎 ⭐ Star，方便更多做 AI 产品的人发现这套工作流。
