# AI Product Dev Skills V2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将仓库中的 20 个 Skill 全量升级为中文为主、具备明确使用背景、专业判断规则、稳定输出契约和逐项验证证据的 V2 工作流库。

**Architecture:** 每个 Skill 独立完成“现状场景测试、正文与参考文档升级、展示元数据更新、README 与索引同步、结构和场景复测”的闭环。README 作为仓库级导航，按照六个稳定分类维护；`docs/validation/skill-v2-validation-report.md` 记录每个 Skill 的升级证据，最终由 `skill-repo-release-verifier` 执行仓库级发布验证。

**Tech Stack:** Markdown、YAML、Git、Codex Skill `quick_validate.py`、`rg`、GitHub CLI/API。

## Global Constraints

- 保留全部现有 Skill 文件夹名和 frontmatter `name`。
- frontmatter 只包含 `name` 和 `description`；`description` 使用英文并以 `Use when...` 开头，只描述触发条件。
- `SKILL.md`、`references/*.md`、README、中文索引和 `agents/openai.yaml` 展示文案以中文为主。
- 每个 Skill 新增 `references/usage-guide.zh.md`。
- `SKILL.md` 必须包含：中文简介、使用背景、核心原则、适用场景、不适用场景、输入要求、信息不足处理、分阶段工作流、专业判断规则、输出契约、质量门槛、常见失败与修正、参考资料路由。
- 每个 Skill 必须具备典型输入、信息不足、误用或边界三个场景的升级前后对照证据。
- 每升级一个 Skill，必须在同一任务内更新 `README.md` 和 `docs/skill-catalog.zh.md`。
- 每个 Skill 独立通过验证后才能进入下一个 Skill。
- 不创建 Skill 内部 `README.md`、安装指南或变更日志。
- 不使用虚构数据填补事实缺口；必须显式区分事实、假设、推断和待确认项。
- 不改动与本次 V2 升级无关的用户文件或提交。

---

## File Map

- Modify: `README.md` — 仓库定位、六类导航、选型矩阵、端到端工作流、使用方法、维护约束。
- Modify: `docs/skill-catalog.zh.md` — 20 个 Skill 的中文选型、使用背景、典型输入、核心产出和上下游关系。
- Create: `docs/validation/skill-v2-validation-report.md` — 记录每个 Skill 的升级前缺口、升级后验证和命令结果。
- Modify: `<skill>/SKILL.md` — V2 核心工作流。
- Modify: `<skill>/agents/openai.yaml` — 中文展示元数据和默认调用提示。
- Create: `<skill>/references/usage-guide.zh.md` — 面向使用者的中文说明和使用背景。
- Modify: `<skill>/references/templates.md` — 与输出契约一致的中文模板。
- Modify: `<skill>/references/checklists.md` — 中文质量门槛和判定。
- Modify: `<skill>/references/examples.md` — 典型、缺失信息、误用和合格输出骨架。
- Modify: `microinteraction-motion-designer/references/motion-patterns.md` — 中文动效模式与参数判断。
- Modify: `skill-repo-release-verifier/references/commands.md` — V2 仓库结构和 GitHub 验证命令。
- Create: `skill-repo-release-verifier/scripts/validate_skill_repo.py` — 确定性验证 Skill 数量、V2 必需文件、章节、分类覆盖和链接。

## Shared Verification Commands

单 Skill 结构校验：

```bash
PYTHONPATH=/tmp/codex-skill-validate-deps \
python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
<skill-directory>
```

单 Skill V2 覆盖检查：

```bash
test -f <skill-directory>/references/usage-guide.zh.md
rg -n '^## (中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料)$' \
  <skill-directory>/SKILL.md
rg -n '<skill-name>' README.md docs/skill-catalog.zh.md
```

单 Skill 卫生检查：

```bash
placeholder_pattern='待办''占位|未决''占位|补充''相关内容|在此''填写|示例''内容'
rg -n "$placeholder_pattern" <skill-directory> || true
git diff --check
```

场景验证记录必须写入 `docs/validation/skill-v2-validation-report.md`，包括：

- 三个场景的原始请求
- V1 的具体缺口
- V2 是否遵守输入边界
- V2 是否执行关键判断
- V2 输出是否符合契约
- 剩余风险

---

### Task 1: 建立 V2 仓库导航与验证记录

**Files:**
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Create: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-07-26-skill-library-v2-design.md`
- Produces: 六类 README 信息架构、统一 Skill 表格字段、逐项验证记录格式。

- [ ] **Step 1: 重构 README 信息架构**

建立六个分类，并为每个 Skill 预留已存在的正式条目。每个条目统一包含：中文用途、使用背景、典型输入、核心产出、上游 Skill、下游 Skill。

- [ ] **Step 2: 扩展中文索引字段**

把中文索引从三列表扩展为：Skill、中文名、使用背景、典型输入、核心产出、推荐衔接。

- [ ] **Step 3: 创建验证报告**

按 20 个 Skill 创建章节。每章包含：场景、V1 缺口、V2 改进、结构验证、场景复测、剩余风险。

- [ ] **Step 4: 验证导航完整性**

Run:

```bash
for directory in */; do
  test -f "${directory}SKILL.md" || continue
  skill_name=${directory%/}
  rg -q "\`${skill_name}\`" README.md
  rg -q "\`${skill_name}\`" docs/skill-catalog.zh.md
done
git diff --check
```

Expected: 所有命令退出状态为 0。

- [ ] **Step 5: Commit**

```bash
git add README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Establish V2 skill documentation structure"
```

---

### Task 2: 升级 competitive-research-brief

**Files:**
- Modify: `competitive-research-brief/SKILL.md`
- Modify: `competitive-research-brief/agents/openai.yaml`
- Create: `competitive-research-brief/references/usage-guide.zh.md`
- Modify: `competitive-research-brief/references/templates.md`
- Modify: `competitive-research-brief/references/checklists.md`
- Modify: `competitive-research-brief/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 产品类别、研究目标、竞品名单或发现范围、地区、时间范围、可用证据。
- Produces: 证据分级的竞品矩阵、定位地图、差异化机会、风险和下一步验证。

- [ ] **Step 1: 运行三个升级前场景**

测试“已有竞品名单的功能与价格比较”“只给产品想法但没有竞品名单”“要求在没有来源时断言竞品优劣”，记录 V1 的来源纪律、事实时效、比较维度和结论置信度缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强研究问题定义、竞品纳入标准、第一方与第二方来源分级、事实日期、可比口径、缺失证据处理、机会判断和不确定性表达。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README“产品发现与研究”分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

执行 Shared Verification Commands。复测必须证明 V2 不会把营销文案当事实，不会在证据不足时伪造结论。

- [ ] **Step 5: Commit**

```bash
git add competitive-research-brief README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade competitive research skill to V2"
```

---

### Task 3: 升级 feature-discovery-interviewer

**Files:**
- Modify: `feature-discovery-interviewer/SKILL.md`
- Modify: `feature-discovery-interviewer/agents/openai.yaml`
- Create: `feature-discovery-interviewer/references/usage-guide.zh.md`
- Modify: `feature-discovery-interviewer/references/templates.md`
- Modify: `feature-discovery-interviewer/references/checklists.md`
- Modify: `feature-discovery-interviewer/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 研究目标、目标用户、待验证假设、招募条件、访谈方式。
- Produces: 中立访谈提纲、行为追问、假设证据矩阵、记录与总结模板。

- [ ] **Step 1: 运行三个升级前场景**

测试“验证用户是否需要 AI 总结”“只有功能想法没有研究假设”“要求用诱导性问题证明方案正确”，记录 V1 在问题中立性、历史行为追问和证伪路径上的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强 Mom Test 风格的历史行为提问、避免推销、追问树、证据强弱、访谈伦理、招募偏差和跨访谈综合规则。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 能拒绝诱导式设计，明确区分用户表达、实际行为与研究者推断。

- [ ] **Step 5: Commit**

```bash
git add feature-discovery-interviewer README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade feature discovery interview skill to V2"
```

---

### Task 4: 升级 user-feedback-synthesizer

**Files:**
- Modify: `user-feedback-synthesizer/SKILL.md`
- Modify: `user-feedback-synthesizer/agents/openai.yaml`
- Create: `user-feedback-synthesizer/references/usage-guide.zh.md`
- Modify: `user-feedback-synthesizer/references/templates.md`
- Modify: `user-feedback-synthesizer/references/checklists.md`
- Modify: `user-feedback-synthesizer/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 访谈、工单、评论、问卷或销售记录及其来源和样本范围。
- Produces: 去重后的主题、频率与严重性、用户分群、代表性证据、机会和验证建议。

- [ ] **Step 1: 运行三个升级前场景**

测试“综合 100 条工单”“只有五条零散反馈”“要求把最高频需求直接列入路线图”，记录 V1 在样本偏差、重复反馈、引用追溯和频率不等于优先级方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强编码规则、去重、矛盾证据、分群、频率与严重性分离、证据追溯、偏差披露和从洞察到假设的边界。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 不会把少量反馈外推为总体事实，不会把用户提出的方案直接当作已验证需求。

- [ ] **Step 5: Commit**

```bash
git add user-feedback-synthesizer README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade feedback synthesis skill to V2"
```

---

### Task 5: 升级 metric-diagnosis

**Files:**
- Modify: `metric-diagnosis/SKILL.md`
- Modify: `metric-diagnosis/agents/openai.yaml`
- Create: `metric-diagnosis/references/usage-guide.zh.md`
- Modify: `metric-diagnosis/references/templates.md`
- Modify: `metric-diagnosis/references/checklists.md`
- Modify: `metric-diagnosis/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 指标定义、时间序列、分群、漏斗、发布记录、数据口径和基线。
- Produces: 数据质量检查、异常分解、假设优先级、验证查询和决策建议。

- [ ] **Step 1: 运行三个升级前场景**

测试“注册转化下降 15%”“只有一张截图没有口径”“要求看到相关性后直接归因”，记录 V1 在数据质量、季节性、分母变化、分群和因果边界上的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强口径校验、完整性与延迟检查、绝对值和相对值、分群与漏斗分解、变点、发布关联、假设优先级和验证查询。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 先验证数据再解释业务，并明确相关性不能直接证明因果。

- [ ] **Step 5: Commit**

```bash
git add metric-diagnosis README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade metric diagnosis skill to V2"
```

---

### Task 6: 升级 prd-builder

**Files:**
- Modify: `prd-builder/SKILL.md`
- Modify: `prd-builder/agents/openai.yaml`
- Create: `prd-builder/references/usage-guide.zh.md`
- Modify: `prd-builder/references/templates.md`
- Modify: `prd-builder/references/checklists.md`
- Modify: `prd-builder/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 产品想法、用户问题、证据、业务目标、限制和已有决策。
- Produces: 可实施 PRD、范围边界、需求与验收标准、指标、风险、依赖和开放问题。

- [ ] **Step 1: 运行三个升级前场景**

测试“一句话 AI 产品想法”“会议纪要转 PRD”“要求把所有想法都写进 MVP”，记录 V1 在问题证据、范围控制、需求可测性和非目标方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强问题定义、目标用户与 JTBD、证据分级、MVP 切分、功能与非功能需求、状态覆盖、埋点、验收、依赖和决策日志。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README“产品定义与决策”分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 不会把假设写成事实，能够拒绝无边界的 MVP，并给出可测试验收标准。

- [ ] **Step 5: Commit**

```bash
git add prd-builder README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade PRD builder skill to V2"
```

---

### Task 7: 升级 roadmap-prioritizer

**Files:**
- Modify: `roadmap-prioritizer/SKILL.md`
- Modify: `roadmap-prioritizer/agents/openai.yaml`
- Create: `roadmap-prioritizer/references/usage-guide.zh.md`
- Modify: `roadmap-prioritizer/references/templates.md`
- Modify: `roadmap-prioritizer/references/checklists.md`
- Modify: `roadmap-prioritizer/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 候选项、目标、规划周期、容量、证据、依赖和评分参数。
- Produces: 模型选择、透明评分、敏感性分析、排序、取舍和阶段路线图。

- [ ] **Step 1: 运行三个升级前场景**

测试“完整 RICE 数据”“只有主观需求列表”“管理层指定最高优先级但要求客观评分”，记录 V1 在模型选择、伪精确、战略约束和敏感性分析上的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强 RICE、ICE、Kano、MoSCoW 和自定义模型选择规则，增加评分口径、证据置信度、依赖、容量、强制项和情景敏感性分析。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 会展示公式与假设，不以虚构数字制造客观感，并区分评分结果与最终决策。

- [ ] **Step 5: Commit**

```bash
git add roadmap-prioritizer README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade roadmap prioritization skill to V2"
```

---

### Task 8: 升级 experiment-designer

**Files:**
- Modify: `experiment-designer/SKILL.md`
- Modify: `experiment-designer/agents/openai.yaml`
- Create: `experiment-designer/references/usage-guide.zh.md`
- Modify: `experiment-designer/references/templates.md`
- Modify: `experiment-designer/references/checklists.md`
- Modify: `experiment-designer/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 产品假设、干预、目标人群、基线、指标、流量、风险和实验约束。
- Produces: 实验设计、样本与周期假设、指标体系、分流、护栏、停止规则和决策框架。

- [ ] **Step 1: 运行三个升级前场景**

测试“标准 A/B 测试”“低流量产品验证”“要求实验跑到显著为止”，记录 V1 在统计功效、窥探、样本污染、护栏指标和替代实验设计上的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强可证伪假设、随机化单位、样本估算输入、MDE、实验周期、SRM、污染、护栏、停止规则，以及低流量时的灰度或准实验替代方案。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 不会建议反复窥探显著性，能在缺少基线时列出估算缺口并提供替代验证方式。

- [ ] **Step 5: Commit**

```bash
git add experiment-designer README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade experiment design skill to V2"
```

---

### Task 9: 升级 prototype-brief-builder

**Files:**
- Modify: `prototype-brief-builder/SKILL.md`
- Modify: `prototype-brief-builder/agents/openai.yaml`
- Create: `prototype-brief-builder/references/usage-guide.zh.md`
- Modify: `prototype-brief-builder/references/templates.md`
- Modify: `prototype-brief-builder/references/checklists.md`
- Modify: `prototype-brief-builder/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: PRD 或想法、原型目的、目标用户、平台、关键流程、品牌与技术约束。
- Produces: 原型范围、页面与状态清单、流程、组件、内容、交互和交付提示。

- [ ] **Step 1: 运行三个升级前场景**

测试“交给设计师的可用性原型”“交给 Codex 的高保真实现说明”“只有一句产品想法”，记录 V1 在保真度选择、状态覆盖、内容真实性和工具交接差异上的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强原型目标到保真度的映射、页面存在理由、关键任务流、完整状态、真实内容策略、响应式、无障碍、埋点和设计/编程工具差异化交付。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README“设计、原型与体验”分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 能控制原型范围，不以占位内容掩盖产品逻辑，并能针对接收方生成不同的交接细节。

- [ ] **Step 5: Commit**

```bash
git add prototype-brief-builder README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade prototype brief skill to V2"
```

---

### Task 10: 升级 microinteraction-motion-designer

**Files:**
- Modify: `microinteraction-motion-designer/SKILL.md`
- Modify: `microinteraction-motion-designer/agents/openai.yaml`
- Create: `microinteraction-motion-designer/references/usage-guide.zh.md`
- Modify: `microinteraction-motion-designer/references/templates.md`
- Modify: `microinteraction-motion-designer/references/checklists.md`
- Modify: `microinteraction-motion-designer/references/examples.md`
- Modify: `microinteraction-motion-designer/references/motion-patterns.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 产品界面、交互目标、平台、组件状态、设计系统、性能和无障碍约束。
- Produces: 动效意图、触发、属性、时长、缓动、降级、实现建议和验收标准。

- [ ] **Step 1: 运行三个升级前场景**

测试“优化移动端列表进入”“给所有页面增加高级动效”“低端设备和减少动态效果模式”，记录 V1 在动效目的、性能、可访问性和过度动画控制上的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强动效与反馈目的、空间层级、时长与距离关系、弹簧参数、打断、手势连续性、Reduced Motion、低性能降级和可测验收。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 能拒绝无目的动画，能输出可实现参数，并覆盖降级与中断状态。

- [ ] **Step 5: Commit**

```bash
git add microinteraction-motion-designer README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade microinteraction motion skill to V2"
```

---

### Task 11: 升级 codebase-onboarding

**Files:**
- Modify: `codebase-onboarding/SKILL.md`
- Modify: `codebase-onboarding/agents/openai.yaml`
- Create: `codebase-onboarding/references/usage-guide.zh.md`
- Modify: `codebase-onboarding/references/templates.md`
- Modify: `codebase-onboarding/references/checklists.md`
- Modify: `codebase-onboarding/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 本地仓库、目标任务、可执行权限、已有文档和时间预算。
- Produces: 有证据的仓库地图、启动和测试命令、关键路径、风险和下一步阅读顺序。

- [ ] **Step 1: 运行三个升级前场景**

测试“接手完整 Web 仓库”“缺少文档且无法启动”“只要求修改一个局部功能”，记录 V1 在证据引用、范围控制、命令验证和推测架构方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强由任务驱动的阅读策略、入口与数据流追踪、配置和秘密边界、运行命令证据、测试拓扑、风险热区和已知/推测分离。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README“工程实现与代码质量”分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 不会声称未运行的命令成功，不会无目的遍历整个仓库，并能输出文件级证据。

- [ ] **Step 5: Commit**

```bash
git add codebase-onboarding README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade codebase onboarding skill to V2"
```

---

### Task 12: 升级 spec-to-implementation-plan

**Files:**
- Modify: `spec-to-implementation-plan/SKILL.md`
- Modify: `spec-to-implementation-plan/agents/openai.yaml`
- Create: `spec-to-implementation-plan/references/usage-guide.zh.md`
- Modify: `spec-to-implementation-plan/references/templates.md`
- Modify: `spec-to-implementation-plan/references/checklists.md`
- Modify: `spec-to-implementation-plan/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: PRD、技术规格、设计说明、仓库上下文和验收标准。
- Produces: 文件级实施计划、接口契约、任务依赖、测试、迁移、发布和验证步骤。

- [ ] **Step 1: 运行三个升级前场景**

测试“完整 PRD 转计划”“模糊需求转计划”“没有读代码库就要求给出精确文件”，记录 V1 在前置探索、任务边界、接口一致性和伪造文件路径上的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强需求可实施性门槛、代码库证据、文件职责、接口消费与产出、依赖图、测试层级、数据迁移、回滚和可验证步骤。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 在缺少仓库证据时不会编造路径，并能把任务拆成独立可审查的交付物。

- [ ] **Step 5: Commit**

```bash
git add spec-to-implementation-plan README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade implementation planning skill to V2"
```

---

### Task 13: 升级 issue-to-pr

**Files:**
- Modify: `issue-to-pr/SKILL.md`
- Modify: `issue-to-pr/agents/openai.yaml`
- Create: `issue-to-pr/references/usage-guide.zh.md`
- Modify: `issue-to-pr/references/templates.md`
- Modify: `issue-to-pr/references/checklists.md`
- Modify: `issue-to-pr/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: Issue、Bug 或需求、代码库、分支状态、验收标准和发布约束。
- Produces: 可追溯的实现、测试证据、提交和 PR 描述。

- [ ] **Step 1: 运行三个升级前场景**

测试“清晰 GitHub Issue”“无法复现的 Bug”“包含额外重构诱惑的需求”，记录 V1 在需求确认、最小修改、测试先行、工作区保护和 PR 证据上的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强 Issue 可执行性检查、仓库状态保护、复现与失败测试、范围控制、实现循环、验证、提交粒度、PR 风险和回滚说明。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 不会修改无关文件，不会在无法复现时假装修复，并会报告真实测试输出。

- [ ] **Step 5: Commit**

```bash
git add issue-to-pr README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade issue to PR skill to V2"
```

---

### Task 14: 升级 bug-debugging-playbook

**Files:**
- Modify: `bug-debugging-playbook/SKILL.md`
- Modify: `bug-debugging-playbook/agents/openai.yaml`
- Create: `bug-debugging-playbook/references/usage-guide.zh.md`
- Modify: `bug-debugging-playbook/references/templates.md`
- Modify: `bug-debugging-playbook/references/checklists.md`
- Modify: `bug-debugging-playbook/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 症状、复现步骤、日志、环境、最近变化和代码库。
- Produces: 可复现案例、假设日志、根因证据、最小修复和回归验证。

- [ ] **Step 1: 运行三个升级前场景**

测试“稳定复现的接口错误”“偶发前端卡死”“用户要求先改最可能的代码”，记录 V1 在证据链、单变量验证、环境差异和停止猜测方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强症状与根因分离、最小复现、变更二分、数据和时间线、假设优先级、单变量实验、根因确认、回归测试和无法复现时的观测增强。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 在修改代码前建立证据，不会同时尝试多个猜测，并能明确根因与缓解措施的差别。

- [ ] **Step 5: Commit**

```bash
git add bug-debugging-playbook README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade debugging playbook skill to V2"
```

---

### Task 15: 升级 test-generator

**Files:**
- Modify: `test-generator/SKILL.md`
- Modify: `test-generator/agents/openai.yaml`
- Create: `test-generator/references/usage-guide.zh.md`
- Modify: `test-generator/references/templates.md`
- Modify: `test-generator/references/checklists.md`
- Modify: `test-generator/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 行为、风险、代码、现有测试约定、Bug 或验收标准。
- Produces: 风险驱动的测试矩阵、可运行测试、命令、结果和剩余缺口。

- [ ] **Step 1: 运行三个升级前场景**

测试“为新 API 补测试”“为已修复 Bug 加回归测试”“只追求覆盖率百分比”，记录 V1 在测试层级选择、先失败证明、行为导向和脆弱断言方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强风险到测试层级映射、测试先失败、边界与错误状态、契约和并发、fixture 与 mock 边界、可维护断言、覆盖缺口和测试输出证据。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 不会用快照或浅层测试制造虚假覆盖率，Bug 回归测试必须先证明能捕获问题。

- [ ] **Step 5: Commit**

```bash
git add test-generator README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade test generation skill to V2"
```

---

### Task 16: 升级 code-review-assistant

**Files:**
- Modify: `code-review-assistant/SKILL.md`
- Modify: `code-review-assistant/agents/openai.yaml`
- Create: `code-review-assistant/references/usage-guide.zh.md`
- Modify: `code-review-assistant/references/templates.md`
- Modify: `code-review-assistant/references/checklists.md`
- Modify: `code-review-assistant/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: diff、PR、需求、代码上下文、测试结果和部署风险。
- Produces: 按严重度排序、可定位、可执行且有证据的审查发现。

- [ ] **Step 1: 运行三个升级前场景**

测试“完整 PR diff”“只有单个文件没有需求”“用户要求只总结不找问题”，记录 V1 在需求对照、行号证据、严重度、误报控制和测试缺口方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强正确性优先、行为回归、数据与安全边界、并发和状态、兼容性、测试质量、发现格式、置信度和无发现时的残余风险。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 的发现包含具体路径、触发条件和影响，不用风格偏好冒充 Bug。

- [ ] **Step 5: Commit**

```bash
git add code-review-assistant README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade code review skill to V2"
```

---

### Task 17: 升级 refactor-with-safety

**Files:**
- Modify: `refactor-with-safety/SKILL.md`
- Modify: `refactor-with-safety/agents/openai.yaml`
- Create: `refactor-with-safety/references/usage-guide.zh.md`
- Modify: `refactor-with-safety/references/templates.md`
- Modify: `refactor-with-safety/references/checklists.md`
- Modify: `refactor-with-safety/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 重构目标、行为边界、测试、代码热点、兼容性和性能约束。
- Produces: 行为基线、小步重构序列、验证证据、回滚方式和残余风险。

- [ ] **Step 1: 运行三个升级前场景**

测试“拆分大文件”“重命名公共 API”“重构同时增加功能”，记录 V1 在行为锁定、公共契约、提交可逆性和范围混合方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强重构与功能变更分离、characterization test、公共契约、依赖缝隙、机械变更、每步验证、性能基线、回滚和停止条件。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 会阻止未锁定行为的宽泛重构，并明确每一步是否保持行为。

- [ ] **Step 5: Commit**

```bash
git add refactor-with-safety README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade safe refactoring skill to V2"
```

---

### Task 18: 升级 ai-app-eval-builder

**Files:**
- Modify: `ai-app-eval-builder/SKILL.md`
- Modify: `ai-app-eval-builder/agents/openai.yaml`
- Create: `ai-app-eval-builder/references/usage-guide.zh.md`
- Modify: `ai-app-eval-builder/references/templates.md`
- Modify: `ai-app-eval-builder/references/checklists.md`
- Modify: `ai-app-eval-builder/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: AI 功能目标、用户任务、架构、风险、生产失败、模型和成本约束。
- Produces: eval 目标、数据集、评分规则、评审方式、失败分类、回归门槛和运行计划。

- [ ] **Step 1: 运行三个升级前场景**

测试“RAG 问答评测”“Agent 工具调用评测”“只要求用准确率评价聊天助手”，记录 V1 在任务分解、数据集代表性、LLM-as-judge 偏差、切片和线上线下联动方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强能力与风险拆解、黄金集与生产样本、困难和对抗样本、确定性检查、rubric、人工校准、judge 偏差、分片指标、成本延迟、回归门槛和版本追踪。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README“AI 应用评测与质量”分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 不会用单一平均分掩盖高风险失败，能定义可复现的评分和发布门槛。

- [ ] **Step 5: Commit**

```bash
git add ai-app-eval-builder README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade AI application eval skill to V2"
```

---

### Task 19: 升级 launch-readiness-checklist

**Files:**
- Modify: `launch-readiness-checklist/SKILL.md`
- Modify: `launch-readiness-checklist/agents/openai.yaml`
- Create: `launch-readiness-checklist/references/usage-guide.zh.md`
- Modify: `launch-readiness-checklist/references/templates.md`
- Modify: `launch-readiness-checklist/references/checklists.md`
- Modify: `launch-readiness-checklist/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 发布范围、平台、用户、依赖、风险、监控、支持和回滚信息。
- Produces: 带证据和负责人的上线清单、阻断项、go/no-go 决策和发布后观察计划。

- [ ] **Step 1: 运行三个升级前场景**

测试“普通 Web 功能上线”“高风险 AI 功能灰度”“截止时间已到但回滚方案缺失”，记录 V1 在证据要求、负责人、阻断项、回滚演练和 AI 风险方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强按风险裁剪、功能和数据迁移、文案、埋点、监控、支持、隐私安全、AI 内容风险、feature flag、回滚触发器、go/no-go 权限和发布后观察。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README“发布、沟通与仓库治理”分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 不会把“有人看过”当作证据，关键阻断项未关闭时必须给出 no-go 或有条件 go。

- [ ] **Step 5: Commit**

```bash
git add launch-readiness-checklist README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade launch readiness skill to V2"
```

---

### Task 20: 升级 stakeholder-update-writer

**Files:**
- Modify: `stakeholder-update-writer/SKILL.md`
- Modify: `stakeholder-update-writer/agents/openai.yaml`
- Create: `stakeholder-update-writer/references/usage-guide.zh.md`
- Modify: `stakeholder-update-writer/references/templates.md`
- Modify: `stakeholder-update-writer/references/checklists.md`
- Modify: `stakeholder-update-writer/references/examples.md`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 原始进展、受众、周期、状态、指标、风险、决策和行动项。
- Produces: 面向不同受众的状态更新、风险升级、决策记录和明确请求。

- [ ] **Step 1: 运行三个升级前场景**

测试“给老板的周报”“跨团队风险升级”“输入只有零散笔记且要求包装成进展顺利”，记录 V1 在受众适配、事实与判断、坏消息透明度和明确请求方面的缺口。

- [ ] **Step 2: 重写 Skill 与中文参考文档**

补强受众与决策目的、RAG 状态判定、事实/解释/预测分离、业务影响、风险升级、决策日志、负责人和日期、敏感信息控制。

- [ ] **Step 3: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 4: 运行结构校验与相同场景复测**

确认 V2 不会粉饰风险，能让忙碌读者快速看见状态、影响、需要的决策和下一步。

- [ ] **Step 5: Commit**

```bash
git add stakeholder-update-writer README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade stakeholder update skill to V2"
```

---

### Task 21: 升级 skill-repo-release-verifier 并加入确定性验证脚本

**Files:**
- Modify: `skill-repo-release-verifier/SKILL.md`
- Modify: `skill-repo-release-verifier/agents/openai.yaml`
- Create: `skill-repo-release-verifier/references/usage-guide.zh.md`
- Modify: `skill-repo-release-verifier/references/commands.md`
- Modify: `skill-repo-release-verifier/references/checklists.md`
- Modify: `skill-repo-release-verifier/references/examples.md`
- Create: `skill-repo-release-verifier/scripts/validate_skill_repo.py`
- Create: `skill-repo-release-verifier/scripts/test_validate_skill_repo.py`
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 本地 Skill 仓库、远端仓库、默认分支和发布要求。
- Produces: 机器可读验证结果、提交证据、同步结果和远端完整性报告。

- [ ] **Step 1: 写脚本失败测试**

创建临时 fixture，覆盖：缺失 `usage-guide.zh.md`、README 遗漏 Skill、分类重复、缺失 V2 章节、合法仓库。先运行测试并确认当前不存在验证脚本。

- [ ] **Step 2: 实现确定性仓库验证脚本**

脚本必须检查：

- Skill 目录与 frontmatter 名称一致
- V2 必需文件存在
- V2 必需章节存在
- `agents/openai.yaml` 存在
- README 和中文索引覆盖全部 Skill
- 六类清单没有遗漏和重复
- Markdown 相对链接指向存在文件
- 没有模板残留

- [ ] **Step 3: 升级 Skill 与中文参考文档**

补强预检、逐 Skill 校验、Git 状态、提交范围、普通 push、Contents API 回退、远端 SHA 比对、默认分支和文件树核验，以及网络失败时的准确报告。

- [ ] **Step 4: 同步展示和仓库导航**

更新中文 `openai.yaml`、README 分类、中文索引和验证报告。

- [ ] **Step 5: 运行脚本测试与 Skill 校验**

Run:

```bash
python3 skill-repo-release-verifier/scripts/test_validate_skill_repo.py -v
python3 skill-repo-release-verifier/scripts/validate_skill_repo.py .
PYTHONPATH=/tmp/codex-skill-validate-deps \
python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
skill-repo-release-verifier
```

Expected: 全部测试通过，仓库验证结果为通过。

- [ ] **Step 6: Commit**

```bash
git add skill-repo-release-verifier README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Upgrade skill repository verifier to V2"
```

---

### Task 22: 全仓库验证、README 终审与 GitHub 同步

**Files:**
- Modify: `README.md`
- Modify: `docs/skill-catalog.zh.md`
- Modify: `docs/validation/skill-v2-validation-report.md`

**Interfaces:**
- Consumes: 20 个已独立验证的 V2 Skill。
- Produces: 本地通过证据、最终提交、GitHub 远端同步和文件树核验。

- [ ] **Step 1: 运行全部 quick_validate**

```bash
set -e
for skill_file in */SKILL.md; do
  skill_directory=${skill_file%/SKILL.md}
  PYTHONPATH=/tmp/codex-skill-validate-deps \
  python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
    "$skill_directory"
done
```

Expected: 20 个 Skill 全部输出有效。

- [ ] **Step 2: 运行 V2 仓库验证器**

```bash
python3 skill-repo-release-verifier/scripts/validate_skill_repo.py .
```

Expected: Skill 数量 20，缺失文件 0，缺失章节 0，README 遗漏 0，中文索引遗漏 0，分类重复 0，无效链接 0。

- [ ] **Step 3: 人工终审 README**

检查作者视角、分类边界、典型输入、核心产出、上下游关系、端到端工作流、安装方法和维护规则。确认没有重复条目、分类错误或与实际文件不一致的描述。

- [ ] **Step 4: 完成验证报告**

写入全部命令、结果、20 个 Skill 的通过状态、仍存在的限制和远端同步方式。

- [ ] **Step 5: 检查工作区并提交终审修正**

```bash
git diff --check
git status --short
git add README.md docs/skill-catalog.zh.md docs/validation/skill-v2-validation-report.md
git commit -m "Finalize V2 skill library documentation"
```

Expected: 只包含 V2 终审修正；若没有修正，不创建空提交。

- [ ] **Step 6: 同步 GitHub**

优先执行：

```bash
git push origin master:main
```

若 Git transport 因网络或协议失败，按 `skill-repo-release-verifier/references/commands.md` 使用 GitHub Contents API 同步本次提交涉及的文件。

- [ ] **Step 7: 核验远端**

```bash
gh repo view BitCrowder/ai-product-dev-skills \
  --json nameWithOwner,visibility,url,defaultBranchRef
gh api 'repos/BitCrowder/ai-product-dev-skills/git/trees/main?recursive=1' \
  --jq '[.tree[] | select(.type=="blob") | .path]'
```

Expected:

- 仓库为 `PUBLIC`
- 默认分支为 `main`
- README、中文索引、验证报告和 20 个 Skill 的 V2 文件全部存在
- 远端文件内容与本地提交一致
