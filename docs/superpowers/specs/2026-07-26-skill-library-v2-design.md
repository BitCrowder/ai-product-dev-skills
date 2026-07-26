# AI Product Dev Skills V2 设计规范

## 1. 背景

当前仓库已经包含 20 个覆盖 AI 产品开发、工程协作、评测与发布的 Skill。现有版本具备基本目录、中文简介、模板、检查清单和示例，但整体仍存在以下问题：

- 多数 `SKILL.md` 以英文工作流为主，中文内容不足以帮助用户理解使用背景。
- Skill 之间的深度、判断规则和输出约束不完全一致。
- 部分参考文档更接近通用输出骨架，缺少可直接执行的中文说明。
- README 已有选型表和工作流，但分类边界、上下游关系、典型输入和核心产出仍不够清晰。
- 仓库要求“每次更新 Skill 同步维护 README”，但尚未成为明确的发布约束。

V2 的目标不是增加篇幅，而是把每个 Skill 升级为可发现、可执行、可验证、可维护的专业工作流。

## 2. 目标

V2 必须实现：

1. 全部 20 个 Skill 保留稳定的英文文件夹名和 Skill 名称。
2. YAML `description` 使用英文，以具体触发场景为核心，避免把完整流程塞进描述。
3. `SKILL.md` 正文以中文为主，必要的行业术语保留英文括注。
4. 每个 Skill 都明确使用背景、适用场景、不适用场景、输入要求、信息不足处理、执行流程、判断规则、输出契约、质量门槛和失败处理。
5. 每个 Skill 都提供中文使用说明、模板、检查清单和示例。
6. `agents/openai.yaml` 的展示名称、简短说明和默认调用提示与 V2 内容一致，并以中文表达。
7. README 按稳定的专业分类展示全部 Skill，说明每个 Skill 的用途、典型输入、核心产出和上下游关系。
8. 每完成一个 Skill，立即更新 README 与中文索引，并完成该 Skill 的结构校验和场景测试。
9. 全部升级完成后运行仓库级发布验证，确认本地文件、Git 状态与 GitHub 远端一致。

## 3. 非目标

- 不为了统一而重命名现有 Skill 文件夹。
- 不增加与 AI 产品开发无关的 Skill。
- 不在每个 Skill 内增加独立 `README.md`、安装指南或变更日志。
- 不把所有领域知识堆进 `SKILL.md`；详细模板、示例和检查项继续放在 `references/`。
- 不承诺每个 Skill 对任何输入都直接给出最终答案；输入不足时应输出缺口、假设和下一步。

## 4. 语言与命名约定

- 文件夹名和 frontmatter `name`：英文、小写、连字符。
- frontmatter `description`：英文，使用 `Use when...` 描述触发条件和问题症状。
- `SKILL.md` 正文：中文为主。
- `agents/openai.yaml`：中文展示文案，Skill 名称可保留英文或中英组合。
- `references/*.md`：中文为主，字段名在有工程交接价值时可保留英文括注。
- README 和中文索引：中文为主。

## 5. 单个 Skill 的 V2 结构

每个 Skill 的目录至少包含：

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

`microinteraction-motion-designer` 可以继续保留 `motion-patterns.md`；`skill-repo-release-verifier` 可以继续使用 `commands.md` 代替不适用的模板文件。

### 5.1 SKILL.md 内容契约

每个 `SKILL.md` 按以下顺序组织：

1. 中文简介
2. 使用背景
3. 核心原则
4. 适用场景
5. 不适用场景
6. 输入要求
7. 信息不足时的处理
8. 分阶段工作流
9. 领域判断规则
10. 输出契约
11. 质量门槛
12. 常见失败与修正
13. 参考资料路由

正文必须告诉另一个 Codex 实例如何做判断，而不只是列出产物名称。

### 5.2 usage-guide.zh.md 内容契约

每个中文使用说明至少包含：

- 这个 Skill 解决什么问题
- 为什么普通提示词容易失败
- 适合谁使用
- 使用前准备什么
- 推荐调用方式
- 输入不足时会发生什么
- 如何阅读输出
- 如何与其他 Skill 串联
- 一个完整但精简的实际使用场景

### 5.3 templates.md 内容契约

模板必须是可以直接填写或由 Codex 生成的输出结构，字段不可只写泛化占位语。模板应：

- 包含必填字段
- 标明可选字段
- 明确证据、假设、事实和待确认项
- 与 `SKILL.md` 的输出契约一致
- 避免多个模板重复表达同一结构

### 5.4 checklists.md 内容契约

检查清单必须覆盖：

- 输入完整性
- 推理与证据质量
- 输出结构完整性
- 风险、边界和异常状态
- 可执行性
- 交接质量
- 最终“通过 / 有条件通过 / 不通过”判定

### 5.5 examples.md 内容契约

每个 Skill 至少提供：

- 一个典型中文调用示例
- 一个信息不足的调用示例
- 一个容易误用的反例
- 一份压缩后的合格输出骨架

示例不能包含无意义占位文本，不能假装掌握用户未提供的事实。

## 6. README 信息架构

README 采用六个稳定分类：

### 6.1 产品发现与研究

- `competitive-research-brief`
- `feature-discovery-interviewer`
- `user-feedback-synthesizer`
- `metric-diagnosis`

### 6.2 产品定义与决策

- `prd-builder`
- `roadmap-prioritizer`
- `experiment-designer`

### 6.3 设计、原型与体验

- `prototype-brief-builder`
- `microinteraction-motion-designer`

### 6.4 工程实现与代码质量

- `codebase-onboarding`
- `spec-to-implementation-plan`
- `issue-to-pr`
- `bug-debugging-playbook`
- `test-generator`
- `code-review-assistant`
- `refactor-with-safety`

### 6.5 AI 应用评测与质量

- `ai-app-eval-builder`

### 6.6 发布、沟通与仓库治理

- `launch-readiness-checklist`
- `stakeholder-update-writer`
- `skill-repo-release-verifier`

每个分类在 README 中必须包含：

- 该阶段解决的核心问题
- Skill 选型表
- 每个 Skill 的中文用途
- 典型输入
- 核心产出
- 推荐上游和下游 Skill

README 还必须包含：

- 仓库定位和作者视角
- 与普通 Prompt 的差异
- 三到五条端到端推荐工作流
- 安装与调用方式
- 单个 Skill 的目录说明
- 质量标准和贡献约束
- “更新 Skill 时同步 README 和中文索引”的维护规则

## 7. 逐个升级顺序

为保证依赖关系清楚，按以下顺序升级：

1. 产品发现与研究
2. 产品定义与决策
3. 设计、原型与体验
4. 工程实现与代码质量
5. AI 应用评测与质量
6. 发布、沟通与仓库治理

同一分类内优先升级上游 Skill，再升级依赖其产出的下游 Skill。

## 8. 单个 Skill 的升级循环

每个 Skill 必须独立完成以下循环后才能进入下一个：

1. 建立至少三个真实调用场景：典型、缺失信息、误用或边界。
2. 记录现有 Skill 在场景中的结构缺口或判断缺口。
3. 重写 `SKILL.md` 和必要的参考文件。
4. 更新 `agents/openai.yaml`。
5. 更新 README 对应分类与选型信息。
6. 更新 `docs/skill-catalog.zh.md`。
7. 运行 `quick_validate.py`。
8. 检查中文文档覆盖、模板残留和文件链接。
9. 用场景重新检查输出契约是否可执行。
10. 记录通过结果，再进入下一个 Skill。

## 9. 验证策略

### 9.1 单 Skill 验证

- frontmatter 合法且名称与目录一致
- `description` 能匹配真实触发场景
- `SKILL.md` 包含 V2 必需章节
- `usage-guide.zh.md` 存在并覆盖使用背景
- 展示文案为中文且与正文一致
- 模板、清单和示例与输出契约一致
- README 和中文索引已包含该 Skill
- 无待办占位、未决占位或模板指令残留

### 9.2 仓库级验证

- 20 个 Skill 全部通过 `quick_validate.py`
- Skill 数量、README 数量和中文索引数量一致
- 六个分类没有遗漏或重复
- README 中的相对链接全部存在
- 每个 Skill 都有中文使用背景和使用说明
- Git 工作区只包含本次升级内容
- 提交后确认远端默认分支、可见性和文件树

## 10. 完成标准

V2 只有在以下条件全部满足时才算完成：

- 20 个 Skill 均达到统一结构和专业深度。
- 20 个 Skill 均有中文说明文档与使用背景。
- README 正确分类并完整覆盖所有 Skill。
- 中文索引与 README、目录实际内容一致。
- 所有本地校验通过。
- GitHub 远端同步并完成文件树核验。
