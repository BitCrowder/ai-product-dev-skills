# Skill 中文选型索引

这份索引用于按使用背景选择 Skill，并在任务交接时明确输入、预期产出和推荐衔接。六类导航与仓库 README 保持一致；“推荐衔接”表示常见上游与下游，不限制独立调用。

## 产品发现与研究

| Skill | 中文名 | 使用背景 | 典型输入 | 核心产出 | 推荐衔接 |
|---|---|---|---|---|---|
| `competitive-research-brief` | 竞品调研简报 | 立项、市场分析、套餐或功能对比前，需要根据公开证据在统一口径下判断竞品格局。 | 决策问题、目标用户/工作流、地区与时间窗、竞品名单或发现范围、可用来源。 | 含来源层级、发布日期/采集日期、可比口径、置信度、未知项、机会和验证建议的竞品矩阵。 | `feature-discovery-interviewer` -> 本 Skill -> `prd-builder`、`roadmap-prioritizer` |
| `feature-discovery-interviewer` | 功能探索访谈设计器 | 承诺方案前，需要以中立问题理解真实行为、痛点、替代方案和反例。 | 决策/研究目标、用户分群与工作流、问题假设、招募条件、访谈方式。 | 中立提纲、行为追问树、证据/证伪矩阵、记录与综合模板、伦理和偏差检查。 | 产品假设或 `metric-diagnosis` -> 本 Skill -> `user-feedback-synthesizer`、`prd-builder`、`experiment-designer` |
| `user-feedback-synthesizer` | 用户反馈综合器 | 需要把访谈、工单、评论或问卷转成有证据边界的产品洞察，避免把重复、高频或稀疏反馈直接当路线图结论。 | 原始记录/可定位摘录、渠道与时间窗、反馈单位、去重线索、分群、样本范围和决策问题。 | 可追溯的去重主题、分群频率与严重性、反例/偏差、有限洞察、待验证机会与下一步。 | `feature-discovery-interviewer` -> 本 Skill -> `prd-builder`、`roadmap-prioritizer`、`experiment-designer` |
| `metric-diagnosis` | 产品指标诊断器 | 转化、留存、激活或收入异常，需要先核验口径、数据完整性、延迟和可比性，再建立可验证解释。 | 公式与分子/分母、时间窗/时区、数据截至时间、分群、漏斗、发布/实验记录、数据限制。 | 数据质量门、绝对/相对变化账本、分群/漏斗/变点分解、竞争假设、查询规格和因果边界。 | 数据/监控信号 -> 本 Skill -> `feature-discovery-interviewer`、`experiment-designer`、`roadmap-prioritizer` |

## 产品定义与决策

| Skill | 中文名 | 使用背景 | 典型输入 | 核心产出 | 推荐衔接 |
|---|---|---|---|---|---|
| `prd-builder` | PRD 生成器 | 需要把想法、研究证据或会议纪要整理为有事实边界、范围取舍和可测试交接物的产品定义。 | 决策/目标、目标用户与 JTBD、可定位证据、候选范围、限制、指标、依赖和已有决策。 | 证据/假设账本、MVP/后续候选/非目标、功能/非功能/状态需求、埋点、验收、依赖、风险和决策日志。 | `competitive-research-brief`、`feature-discovery-interviewer`、`user-feedback-synthesizer`、`metric-diagnosis` -> 本 Skill -> `roadmap-prioritizer`、`prototype-brief-builder`、`spec-to-implementation-plan`、`experiment-designer` |
| `roadmap-prioritizer` | 路线图优先级排序器 | 候选项很多，需要在证据、战略约束、容量和依赖下透明决定先后与取舍。 | 候选项/问题、目标、周期、证据、RICE/成本估计、角色容量、依赖与强制项。 | 模型选择与评分依据、强制项/依赖/敏感性分析、阶段路线图，以及分开的评分、推荐和最终决定。 | `prd-builder`、`user-feedback-synthesizer`、`metric-diagnosis` -> 本 Skill -> `prototype-brief-builder`、`experiment-designer`、`spec-to-implementation-plan` |
| `experiment-designer` | 实验设计器 | 需要用 A/B、holdout、灰度、准实验或低流量验证判断产品改动是否值得扩大。 | 可证伪假设、干预/对照、人群、基线、指标、流量、随机化与风险。 | 实验设计、MDE/样本/周期输入、主次指标/护栏、SRM/污染检查、预注册停止规则和替代验证边界。 | `prd-builder`、`metric-diagnosis`、`user-feedback-synthesizer` -> 本 Skill -> `launch-readiness-checklist`、`stakeholder-update-writer`、`ai-app-eval-builder` |

## 设计、原型与体验

| Skill | 中文名 | 使用背景 | 典型输入 | 核心产出 | 推荐衔接 |
|---|---|---|---|---|---|
| `prototype-brief-builder` | 原型说明生成器 | 需要按验证目的把 PRD、用户流或早期想法交给设计师、Figma 或编程代理，避免用高保真和占位内容掩盖未决逻辑。 | 原型目的、目标用户/任务、平台、关键流程、内容/数据、品牌/技术约束和接收方。 | 保真度理由、关键任务流、页面/状态/组件/真实内容契约、跨端/无障碍/埋点与差异化交接包。 | `prd-builder`、`roadmap-prioritizer` -> 本 Skill -> `microinteraction-motion-designer`、`spec-to-implementation-plan`、`test-generator` |
| `microinteraction-motion-designer` | 微动效设计器 | 主流程和状态已明确，需要将反馈、层级、加载或手势体验转成可打断、可降级的动效契约。 | 用户任务、组件/状态、触发、空间关系、平台/技术栈、性能预算、减少动态与设备约束。 | `M-*` 状态机、数值参数、完整/减少动态/低端三档、实现边界和可观察验收。 | `prototype-brief-builder` -> 本 Skill -> `spec-to-implementation-plan`、`test-generator`、`code-review-assistant` |

## 工程实现与代码质量

| Skill | 中文名 | 使用背景 | 典型输入 | 核心产出 | 推荐衔接 |
|---|---|---|---|---|---|
| `codebase-onboarding` | 代码库入门导航 | 接手陌生仓库、无文档启动诊断或局部改动前，需要按任务而非全仓库遍历建立入口、数据流和测试证据。 | 仓库路径、目标决定、入口线索、时间/命令权限、可见文档、清单和配置结构。 | 阅读预算、已知/推测/未知账本、目录/入口/数据流、三态命令证据、秘密边界、测试拓扑、风险热区和下一步阅读顺序。 | 待处理 Issue、PRD 或 `spec-to-implementation-plan` -> 本 Skill -> `issue-to-pr`、`bug-debugging-playbook`、`test-generator`、`refactor-with-safety` |
| `spec-to-implementation-plan` | 规格转实施计划 | 编码、估算或交接前，需要把规格转成有证据边界的工程计划，尤其涉及跨团队接口、迁移或发布。 | PRD、技术规格、设计说明、仓库证据、验收标准、数据/发布约束和非目标。 | 可实施性门槛、文件职责、`consumes/produces` 接口、独立任务/依赖、分层测试、迁移、flag/回滚/监控和可验证命令。 | `prd-builder`、`prototype-brief-builder`、`codebase-onboarding` -> 本 Skill -> `issue-to-pr`、`test-generator`、`launch-readiness-checklist` |
| `issue-to-pr` | Issue 到 PR 安全交付 | 需要把 Issue、Bug 或需求单推进为范围受控、可复现、可审查的改动，避免不可复现时伪修复、覆盖工作区改动或借机重构。 | Issue 原文、验收/非目标、复现/日志、仓库路径与工作区状态、现有测试、发布约束。 | 可执行性卡、工作区保护、复现/TDD 账本、验收证据矩阵、独立提交及含风险/回滚的 PR。 | `spec-to-implementation-plan`、`codebase-onboarding`、`bug-debugging-playbook` -> 本 Skill -> `test-generator`、`code-review-assistant`、`launch-readiness-checklist` |
| `bug-debugging-playbook` | Bug 调试证据链手册 | 遇到接口错误、崩溃、卡死、回归或间歇故障时，需要先用复现或观测、环境差异和单变量实验确认机制，防止猜测性修复。 | 症状/影响、期望与实际、复现/成功对照、日志/trace、时间线、环境/数据、近期变更和代码库。 | `E-*` 证据链、最小复现或观测增强、差异矩阵、`H-*`/`X-*`、根因/缓解决策、最小修复与回归门禁。 | `codebase-onboarding`、`issue-to-pr` -> 本 Skill -> `issue-to-pr`、`test-generator`、`code-review-assistant`、`stakeholder-update-writer` |
| `test-generator` | 风险驱动测试生成器 | 新功能、接口、Bug 修复或重构需要按可观察行为和失效风险选择层级，避免覆盖率、快照或浅层 mock 掩盖关键缺口。 | 验收/行为、风险、代码与契约、现有测试约定、Bug 复现或修复前版本、执行限制。 | `B-*`/`R-*` 风险矩阵、fixture/mock 边界、`RED-*`/`ALT-*`/`GREEN-*`/`T-*` 命令证据和剩余缺口。 | `codebase-onboarding`、`spec-to-implementation-plan`、`issue-to-pr`、`bug-debugging-playbook` -> 本 Skill -> `code-review-assistant`、`refactor-with-safety`、`launch-readiness-checklist` |
| `code-review-assistant` | 证据驱动代码审查 | 需要审查 PR、完整 diff 或变更，并以需求/契约、相邻上下文和可复现风险判断是否可合并。 | base/head diff、需求/验收、代码与消费者、测试/CI、数据/权限/并发/兼容约束。 | `F-*` 严重度/置信度/路径行号/触发条件/影响/证据/最小修复，`RC-*` 对照、`GAP-*`、测试缺口与结论。 | `issue-to-pr`、`test-generator`、`bug-debugging-playbook` -> 本 Skill -> `refactor-with-safety`、`launch-readiness-checklist`、`stakeholder-update-writer` |
| `refactor-with-safety` | 安全重构助手 | 拆大文件、抽取边界、去重或公共改名时，需要保持外部行为、公共 API/数据/副作用、兼容和性能，并阻止功能夹带。 | 重构目标/非目标、`B-*` 行为、调用方/测试、`C-*` 契约/依赖、兼容窗口、性能基线、工作区和回滚限制。 | `B-*`/`C-*`/`P-*` 基线、机械/语义/功能分轨、可逆 `S-*`、真实 `E-*`、`GAP-*`、停止与回滚策略。 | `codebase-onboarding`、`code-review-assistant`、`test-generator`、`bug-debugging-playbook` -> 本 Skill -> `test-generator`、`code-review-assistant`、`issue-to-pr`、`launch-readiness-checklist` |

## AI 应用评测与质量

| Skill | 中文名 | 使用背景 | 典型输入 | 核心产出 | 推荐衔接 |
|---|---|---|---|---|---|
| `ai-app-eval-builder` | AI 应用评测设计器 | LLM、RAG、Agent 或 AI 功能需要由离线数据集和线上失败回流共同支撑的质量门槛，不能由平均分代替。 | 用户任务/风险、系统与版本、黄金集和脱敏生产失败、成本延迟预算、人工与线上观测约束。 | 版本化数据集、确定性/人工/LLM grader、RAG/Agent 分层评测、切片门禁、发布决定和线上回流计划。 | `prd-builder`、`experiment-designer`、`bug-debugging-playbook`、生产失败样本 -> 本 Skill -> `launch-readiness-checklist`、`stakeholder-update-writer`、`experiment-designer` |

## 发布、沟通与仓库治理

| Skill | 中文名 | 使用背景 | 典型输入 | 核心产出 | 推荐衔接 |
|---|---|---|---|---|---|
| `launch-readiness-checklist` | 上线就绪与发布决策 | Web、实验、迁移、AI 或公开发布需要按影响和风险，以可复核证据而非口头确认做跨职能 go/no-go。 | 发布类型/范围、风险、测试/监控证据、owner/截止、依赖、flag、迁移/回滚、支持/安全，以及 AI eval/注入/越权/人工兜底。 | 风险裁剪的 `R-*` 就绪账本、Blocker/例外、灰度、前向兼容回滚、具名 go/no-go 与发布后观察/退出门禁。 | `experiment-designer`、`ai-app-eval-builder`、`issue-to-pr`、`spec-to-implementation-plan` -> 本 Skill -> `stakeholder-update-writer`、`metric-diagnosis`、`bug-debugging-playbook`、`skill-repo-release-verifier` |
| `stakeholder-update-writer` | 干系人状态与风险汇报 | 需要面向管理者或跨职能团队同步进展、风险、阻塞和决定，且要以规则化状态和事实边界阻止粉饰坏消息。 | 受众/渠道/权限、周期、决策目的、来源/日期/置信度明确的事实、里程碑、指标、风险、决策和行动项。 | RAG/待确认判定、`F-*`/`I-*`/`P-*`/`A-*`/`GAP-*` 账本、业务/用户影响、风险升级、决策日志和带单一 owner/截止的行动项。 | `launch-readiness-checklist`、`experiment-designer`、`metric-diagnosis` -> 本 Skill -> `skill-repo-release-verifier` 或下一轮决策 |
| `skill-repo-release-verifier` | Skill 仓库发布验证器 | 多 Skill 仓库发布前，需要以确定性结构检查、范围审计和实际远端证据阻止遗漏、重复或未核验即成功。 | 仓库路径、base/候选提交、批准文件、`OWNER/REPO`、默认分支、中文覆盖要求和权限/网络状态。 | `{path, code, message}` 本地问题、逐 Skill 校验、提交范围/SHA、同步方法、默认分支/SHA/文件树核验与准确状态。 | 已完成的 Skill 改动、README、中文索引和验证记录 -> 本 Skill -> 已验证同步，或明确受阻/未验证 |
