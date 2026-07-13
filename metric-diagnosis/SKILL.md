---
name: metric-diagnosis
description: Diagnose product metrics, funnels, retention, activation, conversion, engagement, churn, revenue, cohorts, and anomalies. Use when the user asks why a metric changed, analyze a funnel drop, inspect activation or retention, explain conversion decline, create metric hypotheses, design a metric investigation, or turn product data into likely causes, validation queries, and next actions.
---

# Metric Diagnosis

## 中文简介

**产品指标诊断器**：用于分析转化率、留存、激活、漏斗、收入、异常波动等指标变化，拆解数据质量、分群、假设和验证路径。

## Overview

Use this skill to diagnose product metric movement with structured hypotheses, segmentation, and validation steps.

Do not jump from correlation to cause. Separate observed facts, plausible hypotheses, required data, and recommended actions.

## Workflow

1. Define the metric, formula, time window, baseline, target, and observed change.
2. Verify data quality: instrumentation, event definitions, bot/internal traffic, timezone, release changes, sampling, and missing data.
3. Segment the movement by user cohort, acquisition channel, platform, geography, plan, lifecycle stage, and version.
4. Map the metric to a funnel or retention model.
5. Generate hypotheses across product change, traffic mix, seasonality, pricing, onboarding, performance, bugs, messaging, and external factors.
6. Rank hypotheses by likelihood, impact, and ease of validation.
7. Propose validation queries, dashboards, experiments, or qualitative follow-up.
8. End with action recommendations and monitoring plan.

## Output Contract

Always include:

- metric definition
- observed movement
- data quality checks
- segmentation plan
- funnel/cohort view
- ranked hypotheses
- validation plan
- recommended actions
- residual uncertainty

Use `references/templates.md` for diagnosis tables and `references/checklists.md` before finalizing.
