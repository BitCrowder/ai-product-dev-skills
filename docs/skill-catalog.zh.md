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
| `bug-debugging-playbook` | 系统化 Bug 调试手册 | 遇到崩溃、回归、失败测试或异常行为，需要证明根因。 | 症状、期望/实际行为、环境、日志、复现步骤、近期变更。 | 复现证据、假设、根因、最小修复、回归验证和风险。 | `issue-to-pr`、`codebase-onboarding` -> 本 Skill -> `test-generator`、`code-review-assistant`、`stakeholder-update-writer` |
| `test-generator` | 测试生成器 | 功能、修复或重构需要按行为和风险补足测试。 | 需求或代码路径、接口、风险、现有测试约定、复现条件。 | 分层测试用例、fixture/mocks、命令、预期结果和缺口。 | `spec-to-implementation-plan`、`issue-to-pr`、`bug-debugging-playbook` -> 本 Skill -> `code-review-assistant`、`refactor-with-safety`、`launch-readiness-checklist` |
| `code-review-assistant` | 代码审查助手 | 需要审查 PR、diff 或变更，优先找正确性和回归风险。 | 变更 diff、意图、验收标准、测试结果、相关代码。 | 按严重程度排序的发现、定位、修复建议和测试缺口。 | `issue-to-pr`、`test-generator`、`bug-debugging-playbook` -> 本 Skill -> `refactor-with-safety`、`launch-readiness-checklist`、`stakeholder-update-writer` |
| `refactor-with-safety` | 安全重构助手 | 想改善结构或减少重复，同时保持外部行为不变。 | 重构目标、边界、现有行为、测试、非目标、风险点。 | 行为保护计划、小步改动、验证证据和回滚策略。 | `codebase-onboarding`、`code-review-assistant`、`test-generator` -> 本 Skill -> `test-generator`、`code-review-assistant`、`launch-readiness-checklist` |

## AI 应用评测与质量

| Skill | 中文名 | 使用背景 | 典型输入 | 核心产出 | 推荐衔接 |
|---|---|---|---|---|---|
| `ai-app-eval-builder` | AI 应用评测设计器 | LLM、RAG、Agent 或 AI 功能需要可测量质量门槛。 | AI 系统说明、用户任务、样本/日志、失败成本、模型或提示基线。 | 测试集方案、rubric、评分策略、失败分类、阈值和回归门槛。 | `prd-builder`、`experiment-designer`、生产失败样本 -> 本 Skill -> `launch-readiness-checklist`、`stakeholder-update-writer`、`experiment-designer` |

## 发布、沟通与仓库治理

| Skill | 中文名 | 使用背景 | 典型输入 | 核心产出 | 推荐衔接 |
|---|---|---|---|---|---|
| `launch-readiness-checklist` | 上线就绪检查清单 | 版本、实验、迁移或重大变更准备发布，需要 go/no-go 判断。 | 发布范围、验收证据、监控、回滚、支持和合规约束。 | 责任清单、阻塞项、风险、上线/回滚计划和建议。 | `experiment-designer`、`ai-app-eval-builder`、`issue-to-pr` -> 本 Skill -> `stakeholder-update-writer`、`metric-diagnosis`、`skill-repo-release-verifier` |
| `stakeholder-update-writer` | 干系人汇报撰写器 | 需要把进展、指标、风险、阻塞和决策同步给相关方。 | 受众、时间范围、事实、指标、决策、风险、下一步和请求。 | 状态摘要、证据、风险升级、所需决策和负责人。 | `launch-readiness-checklist`、`experiment-designer`、`metric-diagnosis` -> 本 Skill -> `skill-repo-release-verifier` 或下一轮决策 |
| `skill-repo-release-verifier` | Skill 仓库发布验证器 | 修改多 Skill 仓库后，需要检查本地结构、提交、同步和远端可见性。 | 仓库路径、变更范围、分支、远端、中文覆盖要求。 | 本地验证证据、卫生检查、提交/同步状态和远端核验。 | 已完成的 Skill 改动、README、中文索引和验证记录 -> 本 Skill -> 仓库发布关卡 |
