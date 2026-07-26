# AI Product Dev Skills

一套面向 AI 产品开发与 AI 编程协作的 Codex Skills 工作流库。

我整理这个仓库的出发点很简单：团队并不缺零散的提示词，缺的是能重复使用、能说明判断依据、也能交接给下一步工作的流程。这里的每个 Skill 都把一个常见任务固定为可发现、可执行、可验证的工作流，帮助产品、设计和工程协作者把模糊想法推进成有证据的下一步。

## 仓库定位

这个仓库服务于从产品发现到发布与仓库治理的完整链路。它尤其适合使用 Codex、Cursor、Claude Code 或 ChatGPT 的 AI 产品经理、独立开发者、设计师和技术负责人。

与普通 Prompt 相比，Skill 不只描述“想要什么结果”，还约束“如何得到结果”：先澄清输入，区分事实与假设，使用固定输出契约，记录风险和验证证据，并把产物交给合适的上下游 Skill。

## 导航方式

以下六类是稳定的 V2 信息架构。每类先说明它解决的核心问题，再提供可直接选用的 Skill 表。表中“上游 / 下游”是推荐衔接，不是强制依赖；信息不足时应先补齐输入或显式记录假设。

完整中文索引见：[docs/skill-catalog.zh.md](docs/skill-catalog.zh.md)。逐项升级验证记录见：[docs/validation/skill-v2-validation-report.md](docs/validation/skill-v2-validation-report.md)。

### 产品发现与研究

解决“是否存在值得解决的问题、证据是什么、先验证什么”的问题。

| Skill | 中文用途 | 使用背景 | 典型输入 | 核心产出 | 上游 Skill | 下游 Skill |
|---|---|---|---|---|---|---|
| `competitive-research-brief` | 竞品调研简报 | 立项、市场分析、套餐或功能对比前，需要基于公开证据判断可比格局与差异。 | 决策问题、目标用户/工作流、地区与时间窗、竞品名单或发现范围、可用来源。 | 含来源层级、发布日期/采集日期、统一比较口径、置信度、未知项和验证建议的竞品矩阵。 | `feature-discovery-interviewer` 或待验证的产品假设。 | `prd-builder`、`roadmap-prioritizer`。 |
| `feature-discovery-interviewer` | 功能探索访谈设计器 | 在承诺方案前，需要以中立问题理解真实行为、痛点、替代方案和反例。 | 决策/研究目标、目标用户与工作流、问题假设、招募条件、访谈方式。 | 中立提纲、行为追问树、证据/证伪矩阵、记录与综合模板、伦理和偏差检查。 | 初步产品想法或 `metric-diagnosis` 的异常假设。 | `user-feedback-synthesizer`、`prd-builder`、`experiment-designer`。 |
| `user-feedback-synthesizer` | 用户反馈综合器 | 需要把访谈、工单、评论或问卷转成有证据边界的产品洞察，避免把重复、高频或稀疏反馈直接当路线图结论。 | 原始记录/可定位摘录、渠道与时间窗、反馈单位、去重线索、分群、样本范围和决策问题。 | 可追溯的去重主题、分群频率与严重性、反例/偏差、有限洞察、待验证机会与下一步。 | `feature-discovery-interviewer` 或已有反馈数据。 | `prd-builder`、`roadmap-prioritizer`、`experiment-designer`。 |
| `metric-diagnosis` | 产品指标诊断器 | 转化、留存、激活或收入异常，需要先确认口径、完整性和可比性，再建立可验证解释。 | 指标公式与分子/分母、时间窗/时区、数据新鲜度、分群、漏斗、发布记录、数据限制。 | 数据质量门、绝对/相对变化账本、分群/漏斗分解、竞争假设、验证查询和决策边界。 | 埋点数据、上线记录或 `launch-readiness-checklist` 的监控信号。 | `feature-discovery-interviewer`、`experiment-designer`、`roadmap-prioritizer`。 |

### 产品定义与决策

解决“要为谁做什么、范围如何取舍、如何用证据做决策”的问题。

| Skill | 中文用途 | 使用背景 | 典型输入 | 核心产出 | 上游 Skill | 下游 Skill |
|---|---|---|---|---|---|---|
| `prd-builder` | PRD 生成器 | 需要把想法、研究证据或会议纪要转为有边界、可测试且可交接的产品定义。 | 决策与目标、目标用户/JTBD、来源可定位的证据、候选范围、限制、指标和已有决策。 | 含证据/假设账本、MVP/后续候选/非目标、状态覆盖、验收、埋点、依赖、风险和决策日志的 PRD。 | `competitive-research-brief`、`user-feedback-synthesizer`、`feature-discovery-interviewer`、`metric-diagnosis`。 | `roadmap-prioritizer`、`prototype-brief-builder`、`spec-to-implementation-plan`、`experiment-designer`。 |
| `roadmap-prioritizer` | 路线图优先级排序器 | 候选项很多，需要在证据、战略约束、容量和依赖下透明决定先后与取舍。 | 候选项/问题、目标、周期、证据、RICE/成本估计、角色容量、依赖与强制项。 | 模型选择与评分依据、强制项/依赖/敏感性分析、阶段路线图，以及分开的评分、推荐和最终决定。 | `prd-builder`、`user-feedback-synthesizer`、`metric-diagnosis`。 | `prototype-brief-builder`、`experiment-designer`、`spec-to-implementation-plan`。 |
| `experiment-designer` | 实验设计器 | 需要用 A/B、holdout、灰度、准实验或低流量验证来判断产品改动是否值得扩大。 | 可证伪假设、干预/对照、人群、基线、指标、流量、随机化和风险约束。 | 含 MDE/样本/周期输入、主次指标与护栏、SRM/污染检查、预注册停止规则和替代验证边界的实验设计。 | `prd-builder`、`metric-diagnosis`、`user-feedback-synthesizer`。 | `launch-readiness-checklist`、`stakeholder-update-writer`、`ai-app-eval-builder`。 |

### 设计、原型与体验

解决“如何把产品意图转成可体验、可交接、可验证的界面和交互”的问题。

| Skill | 中文用途 | 使用背景 | 典型输入 | 核心产出 | 上游 Skill | 下游 Skill |
|---|---|---|---|---|---|---|
| `prototype-brief-builder` | 原型说明生成器 | 需要按验证目的把 PRD、用户流或早期想法交给设计师、Figma 或编程代理，避免用高保真和占位内容掩盖未决逻辑。 | 原型目的、目标用户/任务、平台、关键流程、内容/数据、品牌/技术约束和接收方。 | 保真度理由、关键任务流、页面/状态/组件/真实内容契约、跨端/无障碍/埋点与差异化交接包。 | `prd-builder`、`roadmap-prioritizer`。 | `microinteraction-motion-designer`、`spec-to-implementation-plan`、`test-generator`。 |
| `microinteraction-motion-designer` | 微动效设计器 | 主流程和状态已明确，需要将反馈、层级、加载或手势体验转成可打断、可降级的动效契约。 | 用户任务、组件/状态、触发、空间关系、平台/技术栈、性能预算、减少动态与设备约束。 | `M-*` 状态机、数值参数、完整/减少动态/低端三档、实现边界和可观察验收。 | `prototype-brief-builder`。 | `spec-to-implementation-plan`、`test-generator`、`code-review-assistant`。 |

### 工程实现与代码质量

解决“如何在理解现有系统的前提下，把规格安全地实现、验证、审查和演进”的问题。

| Skill | 中文用途 | 使用背景 | 典型输入 | 核心产出 | 上游 Skill | 下游 Skill |
|---|---|---|---|---|---|---|
| `codebase-onboarding` | 代码库入门导航 | 接手陌生仓库、诊断无法启动，或在局部改动前需要按任务建立有证据的入口、数据流和测试地图。 | 仓库路径、目标决定、入口线索、时间/命令权限、README/清单/配置和可用证据。 | 含阅读预算、已知/推测/未知、目录/入口/数据流、命令状态、秘密边界、测试拓扑、风险热区和下一步的入门简报。 | 待处理的 Issue、PRD 或 `spec-to-implementation-plan`。 | `issue-to-pr`、`bug-debugging-playbook`、`test-generator`、`refactor-with-safety`。 |
| `spec-to-implementation-plan` | 规格转实施计划 | 在编码、估算或交接前，需要把规格转成有证据边界的实施计划，尤其面对迁移、发布或跨团队接口。 | PRD、技术规格、设计说明、仓库证据、验收标准、数据/发布约束和非目标。 | 13 项计划：可实施性门槛、文件职责、consumes/produces 接口、独立任务/依赖、分层测试、迁移、flag/回滚/监控与验证。 | `prd-builder`、`prototype-brief-builder`、`codebase-onboarding`。 | `issue-to-pr`、`test-generator`、`launch-readiness-checklist`。 |
| `issue-to-pr` | Issue 到 PR 安全交付 | 需要把 Issue、Bug 或需求单推进为范围受控、可复现、可审查的改动，尤其要防止不可复现时伪修复或顺手重构。 | Issue 原文、验收与非目标、复现/日志、仓库与工作区状态、现有测试、发布约束。 | 可执行性卡、工作区保护记录、复现/TDD 账本、验收证据矩阵、独立提交与含风险/回滚的 PR。 | `spec-to-implementation-plan`、`codebase-onboarding`、`bug-debugging-playbook`。 | `test-generator`、`code-review-assistant`、`launch-readiness-checklist`。 |
| `bug-debugging-playbook` | 系统化 Bug 调试手册 | 遇到崩溃、回归、失败测试或异常行为，需要先证明根因再修复。 | 症状、期望/实际行为、环境、日志、复现步骤、近期变更。 | 复现证据、假设、根因、最小修复、回归验证与剩余风险。 | `issue-to-pr`、`codebase-onboarding`。 | `test-generator`、`code-review-assistant`、`stakeholder-update-writer`。 |
| `test-generator` | 测试生成器 | 功能、修复或重构需要以行为和风险为中心补足覆盖。 | 需求或代码路径、接口、风险、现有测试约定、复现条件。 | 分层测试用例、fixture/mocks、命令、预期结果与测试缺口。 | `spec-to-implementation-plan`、`issue-to-pr`、`bug-debugging-playbook`。 | `code-review-assistant`、`refactor-with-safety`、`launch-readiness-checklist`。 |
| `code-review-assistant` | 代码审查助手 | 需要审查 PR、diff 或变更文件，优先发现正确性和回归风险。 | 变更 diff、意图、验收标准、测试结果、相关代码。 | 按严重程度排序的发现、文件/行定位、修复建议与测试缺口。 | `issue-to-pr`、`test-generator`、`bug-debugging-playbook`。 | `refactor-with-safety`、`launch-readiness-checklist`、`stakeholder-update-writer`。 |
| `refactor-with-safety` | 安全重构助手 | 想改善结构或减少重复，同时保持用户可见行为不变。 | 重构目标、边界、现有行为、测试、非目标、风险点。 | 行为保护计划、小步改动序列、验证证据、回滚策略。 | `codebase-onboarding`、`code-review-assistant`、`test-generator`。 | `test-generator`、`code-review-assistant`、`launch-readiness-checklist`。 |

### AI 应用评测与质量

解决“如何定义 AI 功能的好坏、发现失败类型，并让上线质量可以回归验证”的问题。

| Skill | 中文用途 | 使用背景 | 典型输入 | 核心产出 | 上游 Skill | 下游 Skill |
|---|---|---|---|---|---|---|
| `ai-app-eval-builder` | AI 应用评测设计器 | LLM、RAG、Agent 或 AI 功能需要有可测量的质量门槛，而非只凭主观感受。 | AI 系统说明、用户任务、样本/日志、失败成本、模型或提示基线。 | 测试集方案、rubric、评分策略、失败分类、阈值和回归门槛。 | `prd-builder`、`experiment-designer`、生产失败样本。 | `launch-readiness-checklist`、`stakeholder-update-writer`、`experiment-designer`。 |

### 发布、沟通与仓库治理

解决“如何决定是否发布、如何同步决策和风险、如何保证 Skill 仓库可发布”的问题。

| Skill | 中文用途 | 使用背景 | 典型输入 | 核心产出 | 上游 Skill | 下游 Skill |
|---|---|---|---|---|---|---|
| `launch-readiness-checklist` | 上线就绪检查清单 | 版本、实验、迁移或重大变更准备发布，需要跨职能 go/no-go 判断。 | 发布范围、验收证据、监控、回滚、支持和合规约束。 | 责任清单、阻塞项、风险、上线/回滚计划和 go/no-go 建议。 | `experiment-designer`、`ai-app-eval-builder`、`issue-to-pr`。 | `stakeholder-update-writer`、`metric-diagnosis`、`skill-repo-release-verifier`。 |
| `stakeholder-update-writer` | 干系人汇报撰写器 | 需要把进展、指标、风险、阻塞和决策同步给管理者或跨职能团队。 | 受众、时间范围、事实、指标、决策、风险、下一步和请求。 | 状态摘要、证据、风险升级、所需决策和带负责人的下一步。 | `launch-readiness-checklist`、`experiment-designer`、`metric-diagnosis`。 | `skill-repo-release-verifier` 或下一轮产品/工程决策。 |
| `skill-repo-release-verifier` | Skill 仓库发布验证器 | 修改多 Skill 仓库后，需要统一检查本地结构、提交、同步和远端可见性。 | 仓库路径、变更范围、分支、远端、中文覆盖要求。 | 本地验证证据、卫生检查、提交/同步状态和远端文件树核验。 | 已完成的 Skill 改动、README、中文索引和验证记录。 | 无；作为仓库发布关卡。 |

## 端到端推荐工作流

### 从问题发现到产品方案

```text
feature-discovery-interviewer
-> user-feedback-synthesizer
-> competitive-research-brief
-> prd-builder
-> roadmap-prioritizer
```

### 从 PRD 到工程交付

```text
prd-builder
-> prototype-brief-builder
-> codebase-onboarding
-> spec-to-implementation-plan
-> issue-to-pr
-> test-generator
-> code-review-assistant
```

### 从指标异常到验证决策

```text
metric-diagnosis
-> feature-discovery-interviewer
-> experiment-designer
-> stakeholder-update-writer
```

### 从 AI 功能到可控上线

```text
prd-builder
-> ai-app-eval-builder
-> experiment-designer
-> launch-readiness-checklist
-> stakeholder-update-writer
```

### 从仓库改动到发布确认

```text
issue-to-pr
-> test-generator
-> code-review-assistant
-> skill-repo-release-verifier
```

## 安装与调用

每个 Skill 都是独立目录。将所需目录放入你的 Codex Skills 目录，或在本仓库直接阅读其 `SKILL.md` 与 `references/`；调用时提供该 Skill 所需的背景、输入材料和目标决策。信息不足时，优先补充关键事实，或要求 Skill 将假设、缺口和下一步明确写出。

单个 V2 Skill 的目录结构如下：

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── usage-guide.zh.md
    ├── templates.md
    ├── checklists.md
    └── examples.md
```

- `SKILL.md`：触发场景、判断规则、工作流、输出契约和质量门槛。
- `agents/openai.yaml`：中文展示名称、简短说明和默认调用提示。
- `references/usage-guide.zh.md`：中文使用背景与串联建议。
- `references/templates.md`、`checklists.md`、`examples.md`：可直接使用的模板、验收清单和调用示例。

## 质量与贡献

V2 的质量标准要求每个 Skill 明确使用背景、适用与不适用场景、输入要求、信息不足处理、工作流、判断规则、输出契约、质量门槛和失败修正；配套中文使用说明、模板、清单和示例必须与正文一致。

修改任何 Skill 时，必须在同一变更中同步更新 README 对应条目和 [中文索引](docs/skill-catalog.zh.md)，并在 [逐项验证记录](docs/validation/skill-v2-validation-report.md) 中补齐结构校验与场景复测证据。发布前使用 `skill-repo-release-verifier` 复核本地文件、Git 状态与远端文件树。
