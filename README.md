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
| `bug-debugging-playbook` | Bug 调试证据链手册 | 遇到接口错误、崩溃、卡死、回归或间歇故障，需要在改代码前用复现或观测、环境差异和单变量实验确认机制。 | 症状/影响、期望与实际、复现/成功对照、日志/trace、时间线、环境/数据、近期变更和代码库。 | `E-*` 证据链、最小复现或观测增强、环境差异矩阵、`H-*`/`X-*`、根因与缓解决策、最小修复及回归门禁。 | `codebase-onboarding`、`issue-to-pr`。 | `issue-to-pr`、`test-generator`、`code-review-assistant`、`stakeholder-update-writer`。 |
| `test-generator` | 风险驱动测试生成器 | 新功能、接口、Bug 修复或重构需要用可观察行为和失效风险选择测试层级，防止覆盖率、快照或浅层 mock 掩盖关键缺口。 | 验收/行为、风险、代码与契约、现有测试约定、Bug 复现或修复前版本、执行限制。 | `B-*`/`R-*` 风险矩阵、层级选择、fixture/mock 边界、`RED-*`/`ALT-*`/`GREEN-*`/`T-*` 证据账本和缺口结论。 | `codebase-onboarding`、`spec-to-implementation-plan`、`issue-to-pr`、`bug-debugging-playbook`。 | `code-review-assistant`、`refactor-with-safety`、`launch-readiness-checklist`。 |
| `code-review-assistant` | 证据驱动代码审查 | 需要审查 PR、完整 diff 或变更，且要以需求/契约、相邻上下文和可复现风险决定是否可合并。 | base/head diff、需求/验收、代码与消费者、测试/CI、数据/权限/并发/兼容约束。 | `F-*` 严重度/置信度/路径行号/触发条件/影响/证据/最小修复，`RC-*` 对照、`GAP-*`、测试缺口与合并结论。 | `issue-to-pr`、`test-generator`、`bug-debugging-playbook`。 | `refactor-with-safety`、`launch-readiness-checklist`、`stakeholder-update-writer`。 |
| `refactor-with-safety` | 安全重构助手 | 拆大文件、抽取边界、去重或改名时，必须保持用户行为、公共 API/数据/副作用、兼容性和性能可控，并防止新功能混入重构。 | 重构目标/非目标、`B-*` 行为、调用方与测试、`C-*` 契约/依赖、兼容窗口、性能基线、工作区和回滚限制。 | `B-*`/`C-*`/`P-*` 基线、机械/语义/功能分轨、可逆 `S-*`、真实 `E-*` 证据、`GAP-*`、停止与回滚策略。 | `codebase-onboarding`、`code-review-assistant`、`test-generator`、`bug-debugging-playbook`。 | `test-generator`、`code-review-assistant`、`issue-to-pr`、`launch-readiness-checklist`。 |

### AI 应用评测与质量

解决“如何定义 AI 功能的好坏、发现失败类型，并让上线质量可以回归验证”的问题。

| Skill | 中文用途 | 使用背景 | 典型输入 | 核心产出 | 上游 Skill | 下游 Skill |
|---|---|---|---|---|---|---|
| `ai-app-eval-builder` | AI 应用评测设计器 | LLM、RAG、Agent 或 AI 功能需要以离线数据集和线上失败回流建立可测量的质量门槛，而非只凭平均分或主观感受。 | 用户任务/风险、系统与版本、黄金集和脱敏生产失败、成本延迟预算、人工与线上观测约束。 | 版本化数据集、确定性/人工/LLM grader、RAG/Agent 分层评测、切片门禁、发布决定和线上回流计划。 | `prd-builder`、`experiment-designer`、`bug-debugging-playbook`、生产失败样本。 | `launch-readiness-checklist`、`stakeholder-update-writer`、`experiment-designer`。 |

### 发布、沟通与仓库治理

解决“如何决定是否发布、如何同步决策和风险、如何保证 Skill 仓库可发布”的问题。

| Skill | 中文用途 | 使用背景 | 典型输入 | 核心产出 | 上游 Skill | 下游 Skill |
|---|---|---|---|---|---|---|
| `launch-readiness-checklist` | 上线就绪与发布决策 | Web、实验、迁移、AI 或公开发布需要以可复核证据而非口头确认做跨职能 go/no-go，尤其涉及灰度、不可逆数据或高危权限。 | 发布类型/范围、风险、真实测试与监控证据、owner/截止、依赖、flag、迁移/回滚、支持、安全，以及 AI eval/注入/越权/人工兜底。 | 按风险裁剪的 `R-*` 就绪账本、Blocker/例外、flag 灰度、前向兼容回滚、具名 go/no-go 与发布后观察/退出门禁。 | `experiment-designer`、`ai-app-eval-builder`、`issue-to-pr`、`spec-to-implementation-plan`。 | `stakeholder-update-writer`、`metric-diagnosis`、`bug-debugging-playbook`、`skill-repo-release-verifier`。 |
| `stakeholder-update-writer` | 干系人状态与风险汇报 | 需要把进展、指标、风险、阻塞和决策同步给管理者或跨职能团队，且不能以乐观措辞掩盖不确定性或坏消息。 | 受众/渠道/权限、周期、决策目的、带来源与置信度的事实、里程碑、指标、风险、决策和行动项。 | 规则化 RAG/待确认状态、事实/解释/预测/请求账本、业务/用户影响、风险升级、决策日志和单一 owner/截止行动项。 | `launch-readiness-checklist`、`experiment-designer`、`metric-diagnosis`。 | `skill-repo-release-verifier` 或下一轮产品/工程决策。 |
| `skill-repo-release-verifier` | Skill 仓库发布验证器 | 多 Skill 仓库发布前，需要用确定性本地检查和实际远端证据阻止目录遗漏、分类重复、范围漂移与“未核验即成功”。 | 仓库路径、base/候选提交、批准文件、`OWNER/REPO`、预期默认分支、中文覆盖要求和权限/网络状态。 | `{path, code, message}` 本地问题、逐 Skill 证据、范围/提交 SHA、push 或 API 结果，以及默认分支/SHA/文件树核验状态。 | 已完成的 Skill 改动、README、中文索引和验证记录。 | 无；作为仓库发布关卡，远端未核验时只报告受阻或未验证。 |

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
