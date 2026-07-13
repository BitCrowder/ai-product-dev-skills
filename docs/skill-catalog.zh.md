# Skill 中文选型索引

这份索引用来快速判断遇到什么问题该使用哪个 Skill。每个 Skill 文件内也已补充 `中文简介`。

| Skill | 中文名 | 适合解决的问题 |
|---|---|---|
| `ai-app-eval-builder` | AI 应用评测设计器 | 为 LLM、RAG、Agent 或 AI 功能设计评测方案、测试集、评分标准、失败分类和回归门槛。适合在上线前判断 AI 效果是否可靠。 |
| `bug-debugging-playbook` | 系统化 Bug 调试手册 | 用于排查 Bug、崩溃、回归、失败测试或异常行为。它会先复现问题、建立假设、定位根因，再给出最小修复和回归验证。 |
| `code-review-assistant` | 代码审查助手 | 像资深工程师一样审查 PR、diff 或代码文件，优先发现 Bug、回归风险、边界问题和测试缺口，而不是泛泛总结代码。 |
| `codebase-onboarding` | 代码库入门导航 | 快速读懂陌生仓库：技术栈、目录结构、入口文件、运行命令、测试方式、核心模块、数据流和风险点。适合接手新项目或改代码前先建立全局认知。 |
| `competitive-research-brief` | 竞品调研简报 | 用于做有证据的竞品分析：定位、功能、价格、用户评价、差异化机会、可借鉴点和风险。适合产品立项、市场分析和功能对比。 |
| `experiment-designer` | 实验设计器 | 用于设计 A/B 测试、灰度发布、Beta、假门测试或产品验证实验，明确假设、样本、指标、风险、停止规则和成功标准。 |
| `feature-discovery-interviewer` | 功能探索访谈设计器 | 用于生成用户访谈提纲、追问问题、假设验证路径和访谈总结模板。适合在写 PRD 或做功能前验证真实用户需求。 |
| `issue-to-pr` | Issue 到 PR 执行器 | 把 GitHub Issue、Bug 报告或需求单转成实现计划、代码修改策略、测试方案、验证记录和 PR 描述。适合从任务到可审查 PR 的完整执行。 |
| `launch-readiness-checklist` | 上线就绪检查清单 | 用于发布前检查功能、文案、埋点、客服、FAQ、风控、监控、回滚和 go/no-go 决策。适合产品上线、灰度、Beta 或重大变更。 |
| `metric-diagnosis` | 产品指标诊断器 | 用于分析转化率、留存、激活、漏斗、收入、异常波动等指标变化，拆解数据质量、分群、假设和验证路径。 |
| `microinteraction-motion-designer` | 微动效设计器 | 用于把“界面更丝滑、更高级”转成可实现的微动效规格，覆盖列表进入、按压反馈、骨架屏、Tab、页面切换、拖拽、图表和状态变化。 |
| `prd-builder` | PRD 生成器 | 把模糊产品想法、用户问题或会议笔记整理成工程可用的 PRD，包括目标、用户、范围、需求、指标、风险、验收标准和待确认问题。 |
| `prototype-brief-builder` | 原型说明生成器 | 把产品想法或 PRD 转成可交给设计师、Figma、Codex 或 Cursor 的原型说明，包含页面流、组件状态、交互规则和交付要求。 |
| `refactor-with-safety` | 安全重构助手 | 用于在不改变用户可见行为的前提下重构代码。它会先锁定行为和测试，再小步调整结构、抽取模块、减少重复并验证。 |
| `roadmap-prioritizer` | 路线图优先级排序器 | 用 RICE、ICE、Kano、MoSCoW、影响/成本或自定义评分给需求、功能和机会排序，并解释取舍、依赖和推荐路线图。 |
| `spec-to-implementation-plan` | 规格转实施计划 | 把 PRD、设计说明、技术规格或模糊需求拆成工程实施计划，包括任务、文件、接口、测试、风险、上线和验证步骤。 |
| `stakeholder-update-writer` | 干系人汇报撰写器 | 把项目进展、周报、风险、阻塞、决策和下一步整理成清晰的老板/团队/跨部门汇报，适合周报、邮件、Slack 和项目同步。 |
| `test-generator` | 测试生成器 | 根据需求、Bug、代码路径或重构目标设计测试，覆盖单元、集成、组件、E2E、回归、边界、错误和空状态。 |
| `user-feedback-synthesizer` | 用户反馈综合器 | 把访谈、问卷、工单、评论、NPS、销售记录或社区反馈聚类成主题、痛点、机会、代表性引用、优先级和产品建议。 |

## 已覆盖的常见场景

- 想法到 PRD：`prd-builder`
- 用户反馈到机会点：`user-feedback-synthesizer`
- 竞品调研：`competitive-research-brief`
- 需求排序和路线图：`roadmap-prioritizer`
- 用户访谈和探索：`feature-discovery-interviewer`
- 指标异常分析：`metric-diagnosis`
- A/B 测试和灰度实验：`experiment-designer`
- 原型说明：`prototype-brief-builder`
- 微动效规格：`microinteraction-motion-designer`
- 上线检查：`launch-readiness-checklist`
- 代码库入门：`codebase-onboarding`
- 规格拆实施计划：`spec-to-implementation-plan`
- Issue 到 PR：`issue-to-pr`
- Bug 调试：`bug-debugging-playbook`
- 代码审查：`code-review-assistant`
- 测试生成：`test-generator`
- 安全重构：`refactor-with-safety`
- AI 应用评测：`ai-app-eval-builder`
- 干系人汇报：`stakeholder-update-writer`
