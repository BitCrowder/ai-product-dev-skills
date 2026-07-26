# Skill V2 验证记录

本文件是 20 个 Skill 的逐项升级记录。每次完成一个 Skill 的 V2 更新，应在对应章节中补充命令、输出摘要、场景证据和剩余风险；未实际运行的检查必须明确写为未执行，不能以计划替代结果。

## 记录规则

- 每个 Skill 至少复测三个场景：典型调用、信息不足调用、误用或边界调用。
- “V1 缺口”记录更新前实际观察到的结构或判断问题；“V2 改进”记录已落地的修正。
- “结构验证”至少覆盖 frontmatter、V2 必需章节、中文使用说明、展示文案、参考资料、README/中文索引链接和 `quick_validate.py`。
- “场景复测”记录输入摘要、预期行为、实际结果和证据位置；缺失输入时，合格行为是提出关键问题或带标签的假设，而不是编造事实。
- 每个章节完成后记录结论：通过、有条件通过或不通过，并说明剩余风险和后续动作。

## 结构验证命令基线

```bash
python3 skill-repo-release-verifier/references/quick_validate.py <skill-name>
rg -q "\`<skill-name>\`" README.md
rg -q "\`<skill-name>\`" docs/skill-catalog.zh.md
```

## 产品发现与研究

### `competitive-research-brief`

- 场景：典型：比较三个同类产品的定位、价格与体验；信息不足：仅给出产品类别；边界：要求把未经证实的社交媒体传闻写成结论。
- V1 三场景审查（更新前）：
  - 典型请求：`比较 Notion、Coda、ClickUp 在中国大陆团队知识库场景的功能、价格和体验；给出最适合小团队的结论。` V1 要求“同维度比较”和记录 `Date checked`，但价格表没有计划档位、计费周期、币种、税费、地区或发布日期字段，也没有把功能定义为同一可观察能力；因此“价格最低”或“功能更全”可在不同套餐、不同地区或不同时点之间失去可比性。来源表只记录采集日期，不能区分页面发布日期、更新日期和实际观察日期。
  - 信息不足请求：`我想做面向自由职业者的 AI 合同工具，帮我找竞品并找差异化机会。` V1 允许在未给竞品时“identify candidate competitors and label why each belongs”，却没有规定发现范围、纳入/排除标准、地区、目标工作流、替代方案边界或候选来源证据。它也没有要求先追问或把这些缺口登记为假设/未知项，易把搜索到的相邻产品混入直接竞品，并以不完整样本推导机会。
  - 边界请求：`没有链接或资料，直接断言 A 比 B 更受用户欢迎且更值得做，并把社交媒体传闻写成结论。` V1 虽要求重要主张有来源并提醒不要把营销文案当作客户价值，但没有“无证据即未知、不得排名/下结论”的停止规则，也没有传闻来源的降级或交叉验证门槛。其模板预设“Best-positioned competitor”和“Recommended direction”，可能诱导在证据不足时仍产出确定性排序。
- V1 缺口归纳：来源纪律缺少来源层级、主张与原文证据绑定和传闻处理；时效缺少发布日期/更新日期与采集日期的分离及按事实类型的有效期；可比口径缺少地区、套餐、计费周期、功能定义和“未知不等于缺失”；结论置信度缺少可执行分级、降级条件和无证据时的拒答/验证路径。
- V2 改进：正文改为中文主工作流，并新增来源层级（A 第一方、B 独立可核验第二方、C 线索）、事实/假设/推断/未知标签、发布日期/更新时间与采集日期分离、按事实类型的时效窗口、价格/功能/体验的统一比较口径、无证据停止规则和机会三条件门槛。新增中文使用说明；模板、清单和示例均要求来源台账、陈述台账、未知项、置信度和下一步验证。`openai.yaml`、README 和中文索引已同步这一输入与产出契约。
- 结构验证：2026-07-26 在仓库根目录执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py competitive-research-brief`，原始结果为 `Skill is valid!`。执行 V2 章节正则检查，13 个必需章节全部命中；`references/usage-guide.zh.md` 与三份参考文件均存在。`rg -n '\`competitive-research-brief\`' README.md docs/skill-catalog.zh.md` 命中 README 第 25 行和中文索引第 9 行的正式条目。以 `待办占位|未决占位|补充相关内容|在此填写|示例内容` 扫描该 Skill 无输出；本轮 `git diff --check` 退出状态为 0。
- 场景复测（文档级；输入未提供附件、链接或实时浏览结果）：
  - 典型请求：`比较 Notion、Coda、ClickUp 在中国大陆团队知识库场景的功能、价格和体验；给出最适合小团队的结论。` 实际规则结果：先要求或登记中国大陆可购套餐、币种/税费、席位和付款周期，并把功能写成可观察能力；没有合格来源时价格、体验与最终推荐均为 `[未知]`，不输出“最适合”。这由 `SKILL.md` 的“信息不足时的处理”“时效规则”“可比口径规则”和 `examples.md` 场景一共同约束，符合来源纪律和输出契约。
  - 信息不足请求：`我想做面向自由职业者的 AI 合同工具，帮我找竞品并找差异化机会。` 实际规则结果：先确认地区/法律体系、合同类型、目标工作流和候选纳入标准；当前只产出 `[假设]` 的研究范围与 `[未知]` 的结论边界，不把相邻产品列成直接竞品，也不声称已有差异化机会。证据支持的机会必须同时具备用户问题、竞品覆盖和可测试价值主张；见 `SKILL.md` 的“信息不足时的处理”“机会与结论规则”及 `examples.md` 场景二。
  - 边界请求：`没有链接或资料，直接断言 A 比 B 更受用户欢迎且更值得做，并把社交媒体传闻写成结论。` 实际规则结果：拒绝优劣和受欢迎程度断言，将传闻限定为 C 类待核验线索，并输出 `[未知]` 与可验证指标/来源清单。不会用“低置信度”替代未知；见 `SKILL.md` 的“来源纪律与证据置信度”“机会与结论规则”及 `examples.md` 场景三。
- 结论：通过。V2 在三个场景中均保留输入边界、执行来源/时效/口径判断，并在证据不足时输出未知项和验证路径，而非伪造排名或机会结论。
- 剩余风险：公开信息时效、地区差异、动态定价和来源质量仍可能影响结论；Skill 将要求在输出中披露而不消除这些限制。

### `feature-discovery-interviewer`

- 场景：典型：为目标用户设计问题探索访谈；信息不足：没有目标用户或学习目标；边界：要求用诱导问题证明既定功能。
- V1 三场景审查（更新前）：典型的“验证用户是否需要 AI 总结”会把方案词直接带入访谈主题，虽有“最近一次”追问却没有可执行的中立改写、行为/表达/推断分层或证伪条件；只有功能想法时没有最小追问、显式假设或招募/伦理停止规则，易编造对象和结论；要求以诱导问题证明方案正确时只笼统提醒避免诱导，没有拒绝路径、中立替代脚本或跨访谈反例规则。完整基线记录见 `.superpowers/sdd/task-3-report.md`。
- V2 改进：正文改为中文主工作流，新增中立历史行为问题、追问树、表达/实际行为/研究者推断/未知分层、假设的支持与削弱预测、替代解释、招募偏差、知情同意、数据最小化和跨访谈综合规则。新增中文使用说明；模板、清单和示例均要求反例、证伪路径、伦理记录和证据边界。`openai.yaml`、README 和中文索引已同步输入与产出契约。
- 结构验证：2026-07-26 在仓库根目录执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py feature-discovery-interviewer`，原始结果为 `Skill is valid!`。执行 V2 章节正则检查，13 个必需章节全部命中；`references/usage-guide.zh.md` 与三份参考文件均存在。`rg -q '\`feature-discovery-interviewer\`' README.md` 和中文索引均通过。以 `待办占位|未决占位|补充相关内容|在此填写|示例内容` 扫描该 Skill 无输出；本轮 `git diff --check` 退出状态为 0。
- 场景复测（文档级；尚无真实受访者或原始访谈资料）：典型请求“为每周参加多场项目会议的项目经理设计访谈，验证他们是否需要 AI 会议总结”会先改写为会后交接行为假设，从最近事件、过程、决策、替代方案和反例追问，不直接断言需要 AI；信息不足请求“我想做自动总结会议的功能，帮我准备访谈”会先确认决策、分群、工作流、招募和隐私条件，或仅输出 `[假设]` 与 `[未知]`，不编造用户或机会；边界请求“让用户承认 AI 总结能节省大量时间并证明我们应该开发”会被拒绝预设证明，改为中立的最近行为问题、削弱信号和下一步判别动作。对应规则见 `SKILL.md` 的“信息不足时的处理”“中立问题与历史行为”“证据强弱与证伪路径”，以及 `examples.md` 的三个场景。
- 结论：通过。V2 在三种场景中均保留输入边界，区分用户表达、实际行为、研究者推断与未知项，并以反例、替代解释、招募偏差和伦理条件约束结论。
- 剩余风险：样本偏差、受访者记忆偏差和访谈者引导仍需在结果中披露；少量访谈不能单独估计总体比例、市场大小或因果关系，也不能替代原型/实验验证。

### `user-feedback-synthesizer`

- 场景：典型：综合访谈、工单和评论中的重复痛点；信息不足：只提供少量无来源评论；边界：将高声量个案直接视为最高优先级。
- V1 三场景审查（更新前）：典型请求“综合 100 条与新手引导有关的工单，找出最重要的问题”只有清理/分组和主题频率的概览，没有反馈事件定义、去重键、合并理由、编码本、分母或主题到原始记录的追溯，故同一账户追问、批量事故、转发和独立经历都可能被错误计数。信息不足请求“根据这五条零散评论告诉我用户最需要什么”虽可填写来源/样本量，却没有暂停规则、渠道/作者/时间/分群缺口或“方案请求不等于需求”的边界，容易把五条材料外推为总体。边界请求“把出现次数最多的需求直接排进下一季度路线图”虽有“不把高声量当优先级”的提醒，但没有拒绝转换路径、候选机会门槛、冲突/未覆盖分群保留或战略/成本/风险的缺口，模板中的产品建议和优先级仍会诱导直接排期。
- V1 缺口归纳：缺少原始记录、去重反馈事件与独立用户的分层计数；缺少编码定义、版本和方案请求的底层问题追问；缺少矛盾证据、分群/渠道偏差与可定位引文；频率和严重性未被严格分离；洞察、假设、候选方案和路线图决定之间没有停止规则。
- V2 改进：正文改为中文主工作流，新增综合卡、反馈单位与分母、来源/去重台账、编码本、分类证据、矛盾拆分、分群主题、频率与严重性分离、渠道/样本偏差和洞察到可证伪假设的边界。新增中文使用说明；模板、清单和示例均要求事件编号、去重理由、反例、未知项、验证/停止条件与路线图移交条件。`openai.yaml`、README 和中文索引已同步这一输入与产出契约。
- 结构验证：2026-07-26 在仓库根目录执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py user-feedback-synthesizer`，原始结果为 `Skill is valid!`。执行 V2 章节正则检查，13 个必需章节全部命中；`references/usage-guide.zh.md` 与三份参考文件均存在。`rg -n '\`user-feedback-synthesizer\`' README.md docs/skill-catalog.zh.md` 命中 README 第 27 行和中文索引第 11 行的正式条目。以 `待办占位|未决占位|补充相关内容|在此填写|示例内容` 扫描该 Skill 无输出；本轮 `git diff --check` 退出状态为 0。
- 场景复测（文档级；输入未提供可计数的真实附件或记录）：典型请求“综合 100 条与新手引导有关的工单，找出最重要的问题”会先区分原始工单、去重事件和独立账户；按账户/关联工单/事件/时间窗去重并保留理由，将相同事故的不同账户保留为独立反馈，再按分群、版本和渠道报告 `分子/分母` 的频率、独立的严重性证据与反例。信息不足请求“根据这五条零散评论告诉我用户最需要什么”会将渠道、时间、作者、分群和重复状态标为 `[未知]`，只给候选代码与补样动作，不输出总体需求、比例、严重性或优先级。边界请求“把出现次数最多的需求直接排进下一季度路线图”会拒绝直接排期，将高频方案词转为待验证问题假设，列出替代解释、影响证据、通过/停止条件及战略、成本、可行性、风险和依赖等移交缺口。对应规则见 `SKILL.md` 的“信息不足时的处理”“编码与去重规则”“频率、严重性与分群规则”“从洞察到假设的边界”，以及 `examples.md` 的三个场景。
- 结论：通过。V2 在三个场景中均保留原始证据和样本边界，防止重复计数、将少量材料外推为总体，以及让最高频方案绕过验证成为路线图承诺。
- 剩余风险：反馈渠道仍会过度代表遇到问题、愿意发声或商业价值较高的群体；去重键缺失、匿名用户、产品版本变化和自述偏差仍会限制结论，须在交付中持续披露，并以补样、行为数据、原型或实验进一步验证。

### `metric-diagnosis`

- 场景：典型：注册转化下降 15%；信息不足：只有一张截图、没有口径；边界：看到相关性后要求直接归因给新功能。
- V1 三场景审查（更新前）：典型请求“注册转化率本周下降 15%，帮我找原因”虽会要求定义指标、看数据质量、分群和季节性，但没有分子/分母、绝对量、百分点/相对变化、数据成熟度、完整性/延迟/回填、可比日历、分群贡献、变点或发布暴露的暂停/交付规则，容易在不可比数据上排序业务假设。截图请求虽能触发指标定义，却没有把截图读数和未知口径分开，也未要求停止归因并索取原始导出、窗口、时区、样本、筛选和新鲜度。直接归因请求虽有“不要从相关跳到原因”的提醒，但没有拒绝路径、竞争解释、对照/反事实、干预前趋势、混杂检查或可推翻条件，发布邻近仍可能被写成根因。
- V1 缺口归纳：指标口径和数据质量缺少可执行的通过/暂停门；比率没有与分子、分母、绝对量和构成变化绑定；季节性、分群/漏斗、变点和发布关联没有共同的证据边界；假设优先级、查询规格和因果验证条件不完整。
- V2 改进：正文改为中文主工作流，新增诊断卡、数据质量门、变化账本和暂停条件；要求同时报告绝对量、百分点、相对变化和分母/流量构成；补齐可比日历、完整性/延迟/回填、分群/漏斗分解、变点与实际发布暴露对齐、竞争假设及查询规格。新增中文使用说明；模板、清单和示例均保留截图未知项、支持/削弱信号、混杂因素、停止条件和“相关不等于因果”的边界。`openai.yaml`、README 和中文索引已同步输入与产出契约。
- 结构验证：2026-07-26 在仓库根目录执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py metric-diagnosis`，原始结果为 `Skill is valid!`。再以同一依赖路径运行 `generate_openai_yaml.py` 重建 `agents/openai.yaml`，结果为 `[OK] Created agents/openai.yaml`。13 个必需章节、`references/usage-guide.zh.md` 与三份参考文件、以及 README/中文索引中的 `metric-diagnosis` 导航均通过脚本断言；以 `TODO|TBD|placeholder|fill in|[your|your .*here|待办占位|未决占位|补充相关内容|在此填写|示例内容` 扫描 `metric-diagnosis/` 无输出。`find . -type d -name '* 2'`、`git ls-files .superpowers/sdd` 均无输出，`git diff --check` 退出状态为 0。
- 场景复测（文档级；未提供真实指标数据、截图或仓库 schema）：典型请求“注册转化率本周下降 15%，帮我找原因”会先厘清百分点或相对变化，再要求两期分子/分母、口径、成熟度和可比日历；在完整性、延迟、回填和版本检查通过后，才按渠道/平台/版本/生命周期与漏斗分解，并将发布仅列为待验证关联。截图请求“只有这张截图，注册转化从 42% 变成 33%，告诉我发生了什么”会把可见读数标为 `[截图读数]`，把口径、样本、窗口、时区、筛选、新鲜度和分群标为 `[未知]`，只请求原始导出与元数据，不输出原因。边界请求“新功能上线后转化下降，而且相关性很强，直接归因给这个功能”会拒绝直接归因，要求实际暴露、对照/反事实、干预前趋势、竞争变化和混杂检查；缺少这些条件时只报告关联并给出实验或准实验路径。对应规则见 `SKILL.md` 的“信息不足时的处理”“指标口径、绝对量与分母”“完整性、延迟与可比性”“分群、漏斗、变点与发布关联”“假设、查询与因果边界”，以及 `examples.md` 的三个场景。
- 结论：通过。V2 在三种场景中均先验证数据再解释业务，显式保留口径、数据成熟度、分母、季节性、分群、变点和因果边界，且为每个候选解释提供可削弱的查询或设计。
- 剩余风险：真实数据仍可能受埋点定义、延迟、漏斗资格、季节/活动、样本量、未观测混杂和发布并行变化限制；无对照或实验时只能交付关联和下一步验证，不可作因果归因。

## 产品定义与决策

### `prd-builder`

- 场景：一句话 AI 产品想法；将会议纪要转 PRD；要求把所有想法都写进 MVP。
- V1 缺口：
  - 一句话想法：能要求补充上下文，却没有“条件草案/问题假设卡”的稳定降级产物，容易让执行者补写用户、痛点、基线和收益。
  - 会议纪要：虽要求区分事实和假设，但没有逐项来源、日期、发言类型、冲突和决策日志规则，会议偏好容易升级为硬性需求。
  - 无边界 MVP：仅建议使用优先级框架，未要求保留候选池并输出 MVP、后续候选、非目标、重审条件和具名决策路径。
  - 需求交接：验收只笼统列出边界状态，未把状态、埋点事件/属性、非功能约束、依赖、风险和开放决策统一绑定到需求。
- V2 改进：正文按 13 个 V2 章节重写，增加问题/JTBD、五类证据标签与强弱规则、纪要处理、MVP 切分、状态覆盖、可测功能/非功能需求、埋点规格、依赖/风险/决策日志；新增中文使用说明，并同步模板、清单、示例、展示元数据和导航条目。修复后，核心功能需求以 `FR-* → ST-* → EV-* → AC-*` 双向引用，非功能需求只引用已定义的验收 ID。
- 结构验证：`PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py prd-builder` 返回 `Skill is valid!`；`generate_openai_yaml.py` 重建展示元数据返回 `[OK] Created agents/openai.yaml`。13 个必需章节、`references/usage-guide.zh.md`、README/中文索引导航均存在。模板残留模式无匹配，`git diff --check` 通过。聚焦 ID 引用检查输出 `ID traceability check passed`：CRM 工程评估为 `[待确认]`，模板包含需求到状态/埋点/验收的引用，`AC-2` 定义并关联 `NFR-1`，示例的 `FR-1`、`ST-1`、`EV-1` 和 `AC-1` 构成闭环。
- 场景复测：
  - 一句话 AI 产品想法：V2 输出 `[假设]` 用户/情境/JTBD、`[待确认]` 证据和问题假设卡，限定为导入、候选结果、人工确认、保存与事件记录的最小路径；没有编造画像、频率、基线或收益。
  - 会议纪要转 PRD：V2 为每条纪要保留标签、来源、限制和下一步，将销售发言保留为 `[推断]`，将负责人决定与工程依赖分开处理；CSV 试用范围有后续候选和非目标，而非把所有发言升级为需求。
  - 所有想法塞进 MVP：V2 明确拒绝无边界 MVP，保留候选清单并按核心结果、阻断性、依赖和可延后性划分 MVP、后续候选与非目标，要求具名决策人确认取舍。
  - 可测试交接：核心需求模板强制绑定状态覆盖、验收 ID、Given/When/Then 与事件规格；示例包含格式错误重试、权限限制、保存结果和 `follow_up_saved` 事件。
- 剩余风险：PRD 不能替代真实用户研究、工程估算、合规评审或数据口径确认；这些输入缺失时只能交付条件草案和验证路径。

### `roadmap-prioritizer`

- 场景：完整 RICE 数据；只有主观需求列表；管理层指定最高优先级但要求“客观评分”。
- V1 三场景审查（更新前）：完整 RICE 请求虽然可套用公式，但 V1 没有规定 Reach 的时间窗/计量单位、Impact 尺度、Confidence 证据或跨职能 Effort 口径，也没有把容量和依赖带进可交付顺序；数字因此不可审计且带来伪精确。主观清单请求没有缺失数据停止规则、离散分级或补数路径，容易把任意小数当成 RICE 输入。管理层指定 SSO 的请求没有强制项台账、指定人/依据、容量占用、机会成本或“评分与最终决定”的分界，既可能用低分误导强制项，也可能把高层偏好伪装成模型结论。完整基线记录见 `.superpowers/sdd/task-7-report.md`。
- V2 改进：正文按 13 个 V2 章节改写为中文主工作流，新增 RICE/ICE/Kano/MoSCoW/自定义模型选择门、公式和尺度锚点、证据置信度、未知项与反伪精确规则、战略/合规/合同/安全强制项账本、角色容量与关键路径、敏感性分析以及评分/推荐/最终决定三层边界。新增中文使用说明；模板、清单和示例形成完整 RICE、主观清单和管理层指定优先级的闭环。`openai.yaml`、README 和中文索引同步输入与产出契约。
- 结构验证：2026-07-26 在仓库根目录执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py roadmap-prioritizer`，原始结果为 `Skill is valid!`；同一环境运行 `generate_openai_yaml.py` 重建展示元数据，结果为 `[OK] Created agents/openai.yaml`。13 个必需章节全部命中；`references/usage-guide.zh.md` 与三份参考文件均存在。`rg -n '\`roadmap-prioritizer\`' README.md docs/skill-catalog.zh.md` 命中 README 第 37 行和中文索引第 19 行的正式条目。以 `TODO|TBD|placeholder|fill in|[your|your .*here|待办占位|未决占位|补充相关内容|在此填写|示例内容` 扫描该 Skill 无输出；`find . -type d -name '* 2'` 与 `git ls-files .superpowers/sdd` 均无输出，`git diff --check` 退出状态为 0。
- 场景复测（文档级；未提供真实路线图数据、工程排期或合同材料）：
  - 完整 RICE 请求：V2 固定 Reach 为同周期的合格工作区、Impact 为已声明的离散尺度、Confidence 为证据强度、Effort 为跨职能人周，并显示 `RICE = (Reach × Impact × Confidence) / Effort`。日历同步与会议模板同为 240，故不以伪精确打破平局；OAuth 安全评审与 12 人周容量使日历同步成为条件项。Confidence 下调和 Effort 上调的敏感性结果均被保留；见 `SKILL.md` 的“尺度、口径与置信度”“强制项、容量、依赖与敏感性”及 `examples.md` 场景一。
  - 主观清单请求：V2 不填 RICE，将 SSO、导出和仪表盘改为问题假设，保留来源日期及目标分群、影响、Effort、容量和依赖的 `[未知]`。它只允许带明确约束的临时 MoSCoW 分层，并输出合同/安全核验、工单分群和工程粗估等补数动作，不承诺季度排期；见“信息不足时的处理”和 `examples.md` 场景二。
  - 管理层指定请求：V2 只在指定人、依据、截止时间、最小范围和失败后果可核验时将 SSO 登记为战略/合同强制项；容量、安全/身份依赖、延后项目与机会成本均单列。它拒绝隐藏取舍，并把评分结果、推荐组合和 CEO 最终决定分别记录；见“评分与最终决策的边界”和 `examples.md` 场景三。
- 结论：通过。V2 在三种场景中均选择与输入相称的模型，保留未知项与证据边界，将战略强制项、可行性和敏感性引入路线图，并防止评分取代具名决策。
- Important 修复复测：ICE 现使用独立的 `1-5` Impact/Confidence/Ease 锚点，不再复用 RICE 的 `0.25/0.5/1/2/3` 或 `50/80/100%`；模板、清单、使用说明和主观清单示例均要求无锚点依据时保留 `[未知]`。完整 RICE 示例补入已扣除维护/承诺的 12 人周角色容量、两个产品工作流上限及四项具名依赖，但因依赖结论未提供，仅输出候选序列，不承诺 Now。日历同步和会议模板对 Confidence、Effort、Reach、Impact 与依赖延期逐项复测；每项均改变平局、相对 Slack 的位置或可交付序列，因此准确标为“敏感”，没有虚构“稳健”结论。
- Important 验证：`quick_validate.py roadmap-prioritizer` 返回 `Skill is valid!`。聚焦断言确认 ICE 公式、三套独立 `1-5` 锚点、模板/清单/主观清单的未知项门槛均存在，且 ICE 模板段不含 RICE 的 `0.25/0.5/1/2/3` 或 `50/80/100%`。RICE 算术复核覆盖基准 `240/240/125/50`、Confidence 低值 `150/150`、Effort 上调 `192/192`、Reach 低值 `180/160` 与 Impact 低值 `120/120`；两个 Top 候选的 10 个敏感性行均命中。13 个必需章节仍全部存在，`git diff --check` 退出状态为 0。
- 剩余风险：Reach、Impact、Effort 和依赖仍是估计；敏感性分析只能暴露脆弱假设，不能替代工程评估、合规判断、战略授权或真实用户验证。

### `experiment-designer`

- 场景：标准 A/B 测试新引导页；低流量产品验证；要求“跑到显著为止”。完整升级前基线记录见未跟踪的 `.superpowers/sdd/task-8-report.md`。
- V1 三场景审查（更新前）：标准 A/B 请求只有通用“样本考虑”，没有基线、MDE、显著性、功效、随机化/分析单位、资格、预计流量、完整周期或 SRM 的强制输入，容易生成不可审计的样本/结束日；低流量请求虽能列出 Beta 或假门，却没有比较所需与可达样本的门槛，也没有说明灰度、switchback、准实验和定性方案各自的识别前提与结论边界；“每日看 p 值、显著即停”请求只会得到笼统停止规则，未禁止固定样本检验的连续窥探，也未区分统计停止与安全/护栏暂停。
- V1 缺口归纳：可证伪性缺少 MDE、反向预测和明确决策边界；识别设计缺少随机化单位、资格、曝光、分析单位、污染、网络效应与 SRM；统计设计缺少基线/方差、显著性、功效、分流、流量、周期、归因窗和不确定区间；治理缺少预注册、固定/序贯设计区别、窥探约束、护栏动作和低流量替代的因果边界。
- V2 改进：正文按 13 个 V2 章节重写为中文主工作流，新增可证伪假设、MDE、随机化与分析单位、资格/曝光/持久分组、主次指标/护栏分层、样本和周期输入、SRM、污染、预注册与固定/序贯停止规则。新增中文使用说明；模板、清单和示例形成标准 A/B、低流量与窥探误用的闭环，并规定缺少基线时只交付补数路径或情景范围。`openai.yaml`、README 和中文索引同步输入与产出契约。
- 结构验证：2026-07-26 在仓库根目录执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py experiment-designer`，原始结果为 `Skill is valid!`。13 个必需章节全部命中；`references/usage-guide.zh.md` 与三份参考文件均存在。`rg -n '\`experiment-designer\`' README.md docs/skill-catalog.zh.md` 命中 README 第 38 行和中文索引第 20 行的正式条目。以 `TODO|TBD|placeholder|fill in|[your|your .*here|待办占位|未决占位|补充相关内容|在此填写|示例内容` 扫描该 Skill 无输出；`find . -type d -name '* 2'` 与 `git ls-files .superpowers/sdd` 均无输出，`git diff --check` 退出状态为 0。
- 场景复测（文档级；未提供真实基线、流量或实验日志）：
  - 标准 A/B：`为新团队的三步引导页设计 A/B 测试，判断是否提升 7 日激活。` V2 将假设固定为工作区级的首次管理员曝光、唯一主指标、7 日归因窗和 3 个百分点 MDE；工作区同时是随机化与分析单位，避免把共享引导状态当独立用户。基线、方差、显著性、功效、资格率、团簇相关性和流量未提供时，只要求补数，不虚构样本或结束日；并在上线前要求 A/A、SRM、污染、护栏和预注册检查。见 `SKILL.md` 的“可证伪假设与决策边界”“随机化、资格与污染”“指标、样本与周期”，以及 `examples.md` 场景一。
  - 低流量：`每月约 300 个合格新用户，想验证付费页改版是否值得做。` V2 先比较所需和可达样本，明确拒绝以两周低功效 A/B 的无显著推导“没有价值”。它把初始灰度限定为链路/伤害验证，列出 switchback 的时间平衡与残留条件、准实验的可信对照/趋势前提，并用原型、假门、concierge 或可用性测试验证机制与兴趣而不宣称总体转化提升。见“低流量与替代验证”和 `examples.md` 场景二。
  - 窥探误用：`每天看一次结果；不显著就继续，显著立刻停。` V2 明确拒绝固定样本检验的连续窥探，要求在曝光前二选一：固定样本的最大样本/最短周期/唯一最终检查，或具明确最大样本、检查节点和效应/无效/伤害边界的序贯设计。安全、合规和护栏暂停与统计停止分开；到达边界仍不确定时报告区间而非选择性延长。见“预注册、窥探与停止规则”和 `examples.md` 场景三。
- 结论：通过。V2 在三种场景中均把统计和因果前提写成输入与质量门，不以缺失数据制造精确计划，不把低流量无显著写成无价值，也不允许以反复窥探 p 值制造显著性。
- 复审修复（2026-07-26）：上一版“13 个必需章节全部命中”的结论不准确，`SKILL.md` 末尾仍残留英文 `Workflow` 和 `Output Contract`，实际有 15 个一级章节；标准 A/B 示例也将无来源的 3 个百分点写成 MDE 与 ship 阈值，并不当地要求工作区级一次二元结果提供团簇相关性。现已删除两节英文遗留；MDE 改为由业务 owner 以价值、成本和风险确认的 `[待确认]` 输入，数值仅可标为 `[演示假设]`；工作区随机且工作区级一次二元主指标以基线率推伯努利方差，只有单位不一致、重复观测或额外相关结构时才要求 ICC/design effect。修复后的验证结果追加于本条目。
- 复审验证（2026-07-26）：`quick_validate.py experiment-designer` 返回 `Skill is valid!`。精确一级章节检查返回 13 个，且顺序为中文 V2 的 13 节；`Workflow`、`Output Contract` 均不存在。MDE/ICC 聚焦检查确认：标准 A/B 示例含 `[待确认 MDE]`、不含固定的 3 个百分点、要求业务 owner 依据价值/成本/风险确认；模板、清单、使用说明均同步；工作区随机且工作区级一次二元主指标不要求 ICC/design effect，单位不一致、重复观测或额外相关结构才要求。`git diff --check` 退出状态为 0。故修复后结论为通过；上一版的章节计数结论已由本条取代。
- 剩余风险：样本估算依赖真实基线、方差、资格率和流量；随机化仍可能受身份合并、污染、季节性、并行发布和未观测混杂影响。低流量替代方案只能在明确前提下提供有限证据，不能替代合格随机实验。

## 设计、原型与体验

### `prototype-brief-builder`

- 场景：设计师可用性原型；Codex 高保真实现说明；只有一句产品想法。
- V1 三场景审查（更新前）：设计师场景只得到笼统的“Medium”保真度和页面列表，没有将可用性问题、主持任务、可点击路径、观测点与 Figma 分层对应；Codex 场景虽提到状态和响应式，却没有要求可执行的真实内容来源、确定数据、组件契约、键盘/语义规则或实现验收，容易由代理补造产品逻辑；一句话想法场景会直接要求屏幕和组件清单，没有把未知的用户、平台、任务、成功条件与内容来源显式保留，容易伪造高保真范围。
- V1 缺口归纳：缺少“原型目的 -> 保真度 -> 必要页面/状态”的选择规则；页面存在理由和关键任务流不构成范围门；状态、真实内容、响应式、无障碍与埋点没有统一的输出契约；设计师/Figma 与编程代理收到相同粒度的交接，无法避免视觉稿、可用性原型和可运行实现之间的错配。
- V2 改进：正文按 13 个中文章节重写，先建立原型决策卡，再映射目的到低/中/高保真，并以页面存在理由和关键任务流控制范围。新增屏幕/组件状态、真实/脱敏/受控合成内容、响应式、无障碍与事件契约；新增中文使用说明，并让模板、清单和三场景示例区分设计师/Figma、编程代理和一句话想法探索卡。`openai.yaml`、README 和中文索引同步输入、产出和接收方差异。
- 结构验证：2026-07-26 在仓库根目录执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py prototype-brief-builder`，结果为 `Skill is valid!`。精确一级章节检查返回 13 个，顺序为统一中文 V2 章节；`references/usage-guide.zh.md`、模板、清单和示例均存在。`rg -n '\`prototype-brief-builder\`' README.md docs/skill-catalog.zh.md` 命中两处正式条目；以 `TODO|TBD|placeholder|fill in|[your|your .*here|待办占位|未决占位|补充相关内容|在此填写|示例内容` 扫描该 Skill 无输出；`find . -type d -name '* 2'`、`git ls-files .superpowers/sdd` 均无输出，`git diff --check` 退出状态为 0。
- 场景复测（文档级；未提供真实设计系统、接口或用户研究材料）：
  - 设计师可用性原型：日程助手连接日历场景被定为中保真，不制作生产 OAuth 或完整设置页；输出受试任务、关键可点击路径、权限拒绝恢复、`CalendarPermission` 状态、Figma 页面树/连接、脱敏内容、键盘焦点与研究事件。页面都对应理解、连接或恢复问题，见 `SKILL.md` 的“原型目的与保真度”“页面、任务流与完整状态”及 `examples.md` 场景一。
  - Codex 高保真实现说明：订阅取消场景被限制为详情、原因、条件性保留优惠和确认；只有接口提供 `retentionOffer` 才显示优惠，金额和日期来自指定字段。输出组件状态转换、错误恢复、320px 到桌面的重排、键盘/读屏规则和最小事件属性，明确不生成退款或客服逻辑，见“内容、响应式、无障碍与埋点”“接收方差异化交付”及 `examples.md` 场景二。
  - 一句话想法：自由职业者发票网站只生成低保真探索卡，保留用户、地区、税务、平台、内容来源和成功条件的 `[待确认]`，提出访谈与边界核对动作；没有发明支付、税务或完整仪表盘，见“信息不足时的处理”及 `examples.md` 场景三。
- 结论：通过。V2 让保真度服从原型目的，让页面、状态和内容可追溯到关键任务，并对设计师/Figma 与编程代理给出不同的可执行交接；输入不足时明确降级为探索，而非伪造生产范围。
- P1/P2 修复复测：编程代理模板新增 `P-*`、`C-*`、`B-*` 追溯与完整行为契约。每个 `B-*` 强制记录当前状态、事件、守卫、下一状态、明确路由目标、副作用、请求、成功/失败响应和失败恢复；模板和清单把设计师的研究任务/观察记录，与 Figma 的页面树/组件变量/原型连接拆开。三个示例改为精简完整实例并附清单结果：日程助手研究原型填入 Figma 行为连接和观察记录；订阅取消将 `RetentionOffer` 接受定义为接口成功后优惠生效、取消结束并到 `/settings/billing?retention=accepted`，拒绝定义为不改变订阅、保留原因并到 `/settings/billing/cancel/confirm`；发票想法拒绝“今日上线的高保真支付流程”，仅交付带未知项和补数动作的探索卡。
- P1/P2 验证：`quick_validate.py prototype-brief-builder` 返回 `Skill is valid!`；13 个一级章节精确匹配。聚焦断言确认模板包含十个行为字段、页面/组件/行为 ID 和独立的设计师/Figma 小节；示例包含三种完整场景、`B-ACCEPT-OFFER`、`B-DECLINE-OFFER`、接受优惠接口和明确路由、拒绝/降级以及清单验收；正文与中文使用说明包含相同的行为契约和交接边界。`git diff --check` 退出状态为 0。
- 第二轮修复复测：Codex 示例的 `B-SUBMIT-REASON` 现在返回 `previewId` 和完整 `retentionOffer` schema：`offerId`、`status`、`displayContent`、`benefit`、`expiresAt`、`eligibility`；组件和后续 `B-*` 明确这些字段只来自预览或刷新成功响应。`B-ACCEPT-OFFER` 给出 `{offerId,previewId}` 与幂等键、成功的订阅/已接受优惠/已撤销预览响应，以及 `409`/`5xx` 边界。新增 `B-REFRESH-OFFER`：过期时重取预览，带 `previousPreviewId`，有优惠保持优惠页、无优惠转确认页、失败保留页面并禁用接受，用户可重试刷新或继续取消。日程和取消示例的组件表均填齐触发、校验、恢复、数据/内容规则、极值/无障碍和行为 ID，并各自声明无开放问题及边界。
- 第二轮验证：`quick_validate.py prototype-brief-builder` 返回 `Skill is valid!`；13 个一级章节精确匹配。聚焦断言命中完整优惠 schema、`B-REFRESH-OFFER`、刷新状态/请求/页面保持规则、接受的请求参数和响应、两张完整组件表、两处开放问题声明以及清单中的对应规则；`git diff --check` 退出状态为 0。
- 剩余风险：视觉品牌规则、真实内容和技术限制不明会降低交接精度。

### `microinteraction-motion-designer`

- 场景：典型：优化移动端列表首次进入；误用：要求为所有页面增加“高级动效”；约束：底部抽屉需同时支持低端设备与减少动态模式。
- V1 三场景审查（更新前）：典型请求“优化移动端列表进入”虽给出 `180-280ms`、`30-70ms` stagger 和 `8-16px` 位移，但没有限制首次可见数量、滚动/虚拟化/筛选中断、回访重放和低端档，容易在长列表上制造延迟与并行动画。误用请求“给所有页面增加高级动效”只有“不要叠加太多效果”的软提醒，缺少拒绝/收敛规则、任务/层级门槛和性能预算，仍可能把全站转场、视差与循环当默认。低端/减少动态请求虽提到 `prefers-reduced-motion`，却没有等价反馈、设备/掉帧触发、参数移除顺序、`pointercancel`、过期回调保护或状态机，无法验证快速操作和降级后的任务完成。
- V1 缺口归纳：动效目的与空间关系没有成为输出门槛；时长/距离、easing 和弹簧参数没有形成可实现的参数契约；手势连续性、取消和异步旧回调缺少状态机；减少动态和低端性能没有可测的分级降级；全页动效请求没有拒绝并收敛到关键任务的路径。
- V2 改进：正文改为中文 13 章节工作流，新增动效意图卡、`M-*` 状态转换、空间层级、参数预算、完整弹簧字段、直接操控/取消/过期回调规则，以及完整/减少动态/低端三档。新增中文使用说明；`motion-patterns.md`、模板、清单和示例均覆盖首屏列表、全页请求拒绝和底部抽屉三种场景。`openai.yaml`、README 和中文索引已同步输入与产出契约。
- 结构验证：2026-07-26 在仓库根目录执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py microinteraction-motion-designer`，原始结果为 `Skill is valid!`。执行 V2 章节正则检查，13 个必需章节全部命中；`references/usage-guide.zh.md` 与四份参考文件均存在。参数/降级/中断聚焦断言命中 `stiffness`、`damping`、`prefers-reduced-motion`、`低端降级`、`pointercancel`、`transition/request id` 与三档表。`rg -n '\`microinteraction-motion-designer\`' README.md docs/skill-catalog.zh.md` 命中正式条目；残留和 `git diff --check` 结果见本任务报告。
- 场景复测（文档级；未运行目标产品或真实设备）：典型请求“优化移动端列表进入”现在限制为首次首屏 `4-8` 项、每项 `160-220ms`、`24-48ms` stagger、`8-12px` 位移，并在滚动、筛选、离屏或数据替换时取消未开始项；减少动态即时显示，低端档取消 stagger。误用请求“给所有页面增加高级动效”会拒绝默认全页化，只允许选一个高频任务和一处空间关系试点，并把视差、blur、无限背景和逐元素入场列为非目标。低端/减少动态抽屉请求会给出 `idle -> dragging -> settling -> completed | cancelled` 状态、完整弹簧参数、`pointercancel` 稳定点、三帧超过 `20ms` 的低端触发和等价的焦点/状态反馈。对应规则见 `SKILL.md` 的“信息不足时的处理”“专业判断规则”“质量门槛”和 `examples.md` 三个场景。
- 结论：通过。V2 在三种场景中都先保留目的、状态和性能边界，再给参数和实现；不会以全页装饰替代任务关系，也不会在减少动态或低端档丢失可见状态与恢复路径。
- P1/P2 复修：弹簧契约现要求目标运行时/库/API、求解器语义、参数 API 语义或单位、实际初速度、目标值、`restDelta`、`restSpeed` 和最大 settle 时间，并禁止跨平台原样复制参数；场景二补齐 `M-DETAIL-BACK` 的前页/后页位置、透明度、时长、easing、焦点交接和取消稳定状态；性能降级补齐交互作用域采样源、`12` 帧窗口、`3` 帧超过 `20ms` 的产品待验证基线、稳定边界切档、`5s` 冷却、双 `60` 帧恢复窗口和防抖。模板、清单、模式与示例均同步。实际命令结果见任务报告。
- 第二轮复修：恢复不再依赖已结束的手势采样。`low` 在前台可见时每 `250ms` 用连续 rAF 对低频采样；状态机定义 `low-cooling`、`low-sampling` 和 `restore-pending`，无交互仍能积累窗口。隐藏/后台暂停并清理采样资源、停止冷却并重置窗口；假时钟与可控 rAF 可确定性验证 `5s` 冷却、`120` 干净样本、稳定边界恢复和 hidden 重置。实际命令结果见任务报告。
- 剩余风险：具体平台的帧率、弹簧单位、输入延迟和设备分档仍须在目标实现中用真实硬件、辅助技术和性能轨迹复测。

## 工程实现与代码质量

### `codebase-onboarding`

- 场景：完整 Web 仓库入门；无 README 且本地启动失败；只修改一个 API 局部功能。
- V1 三场景缺口：完整 Web 场景只有概览性命令表，无法区分脚本发现与实际运行，也没有文件级证据、阅读预算和测试拓扑；无文档场景没有“最小尝试 -> 失败证据 -> 未验证范围 -> 下一步”的受控降级，容易把未运行命令或推测架构写成事实；局部功能场景将全仓库理解当作默认，缺少沿任务入口、契约和最近测试反向追踪的停止规则。完整基线见未跟踪的 `.superpowers/sdd/task-11-report.md`。
- V2 改进：正文统一为 13 个中文章节，新增任务卡/阅读预算、目录/入口/关键数据流、配置与秘密边界、测试拓扑、命令三态证据、已知/推测/未知账本、风险热区和下一步阅读顺序。新增 `references/usage-guide.zh.md`；模板、清单和三场景示例共享 13 项输出契约与“范围-证据-命令状态”闭环。`openai.yaml`、README 与中文索引同步为中文任务、输入与产出描述。
- 结构验证：2026-07-26 在仓库根目录执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py codebase-onboarding`，结果为 `Skill is valid!`；同一环境运行 `generate_openai_yaml.py` 重建展示元数据，结果为 `[OK] Created agents/openai.yaml`。精确一级章节检查返回统一中文 V2 顺序的 13 节；`usage-guide.zh.md`、模板、清单和示例均存在。证据/命令状态聚焦断言覆盖阅读预算、已知/推测/未知、三态命令、秘密边界、测试拓扑、风险热区和下一步阅读，结果为 `PASS`。README/中文索引导航均命中；以残留模式扫描该 Skill、`find . -type d -name '* 2'`、`git ls-files .superpowers/sdd` 均无输出。实际执行 `git diff --check 8f104c0 dd6f3d1`，退出状态为 0；该精确范围覆盖 Task 11 的全部 Skill、README、中文索引和验证内容修复至 `dd6f3d1`，替代空工作树的卫生结论。
- 场景复测（文档级；没有对外部目标仓库运行示例命令）：完整 Web 仓库场景在 `90` 分钟预算内给出目录/入口、已知/推测/未知、支付回调测试缺口和 `[未运行]` 命令，避免把静态地图写成已启动；无 README 场景将 `npm run dev` 明确记录为 `[已运行-失败]`、退出码 `1`、缺少 `DATABASE_URL`，随后只读容器/CI 并有停止条件；局部 `POST /orders` 场景在 `25` 分钟内限制为路由、校验器、契约和最近测试，其他区域只有被调用链阻断时才扩展。三场景聚焦断言结果为 `PASS`。
- P1/P2 复修：命令证据模板现拆分为工作目录、执行时间、退出码、脱敏关键输出、可定位证据和阻断原因；`[已运行-通过]`/`[已运行-失败]` 必须有日志路径、终端记录，或 CI URL 加 job step，`[未运行]` 只能填计划工作目录与阻断原因，执行/证据字段均为“未运行，不填”。正文、中文使用说明和清单同步这一门槛。三个场景均改为完整 13 项交付物，包含已排除区域、可作决定与阻断项、最小交接和分组清单核验；示例执行记录同时列出 cwd、时间、退出码和终端记录标识，明确其仅为文档示例。复修验证实际运行 `quick_validate.py`、13 章节顺序、字段/三场景完整性和未运行字段断言，结果均为 `PASS`；完整修复范围使用 `git diff --check 8f104c0 dd6f3d1`，退出状态为 0。
- 剩余风险：未运行的服务、私有依赖、受限凭据和过期文档仍会留下未知区域；V2 要求将它们保留为未知并安排最小验证动作。

### `spec-to-implementation-plan`

- 场景：完整 PRD 加已读仓库证据；模糊需求“让通知更智能”；未读代码库却要求精确修改文件。
- V1 缺口（文档级升级前审计）：完整 PRD 只有英文概览式任务流程，未要求先检查验收、数据/权限、仓库和发布准备度；模糊需求没有条件计划、探索顺序或阻塞 owner；未读仓库时只有“文件已知则命名”的宽松表述，缺少路径证据与明确的反伪造规则。接口没有 producer/consumer、consumes/produces、失败或兼容字段，任务也没有强制独立审查边界。
- V2 改进：中文主 Skill 采用 13 个一级章节与 13 项交付；新增可实施性门槛、已知/推测/未知证据账本、无证据路径禁令、文件职责、`I-*` 接口与 `T-*` 独立任务、依赖图、分层测试、迁移/兼容、flag/回滚/监控和命令状态规则。新增中文使用说明，模板、清单和三个场景示例均包含同一闭环。
- 结构验证：2026-07-26 在工作目录 `/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2` 实际执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/generate_openai_yaml.py spec-to-implementation-plan --interface 'display_name=规格转实施计划' --interface 'short_description=将产品规格验收标准与仓库证据拆成独立可审查且可验证的工程实施计划' --interface 'default_prompt=Use $spec-to-implementation-plan：根据需求与仓库证据生成有接口、任务、测试和发布验证的实施计划。'`，结果为 `[OK] Created agents/openai.yaml`；随后执行 `PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py spec-to-implementation-plan`，结果为 `Skill is valid!`。精确一级章节顺序、四份参考资料、路径证据/接口/验证聚焦断言均为 `PASS`；README 与中文索引均有正式导航条目，残留、重复目录、受跟踪 SDD 文件扫描和 `git diff --check` 均无输出。
- 场景复测（文档级）：完整 PRD 场景只使用输入明确给出的五个路径，五个可实施性门槛和最终判定均为通过，写出查询 `I-01`、`I-02 AuditEvent` schema 与 `I-03 AuditPublisher.publish(event)` capability。`T-02` 定义/produces schema，`T-03` consumes schema 并实现/produces capability，`T-04` consumes 请求/结果、schema 与 capability，在运行时构造 event 并调用 publisher；依赖为 `T-01 -> T-04 -> T-05` 与 `T-02 -> T-03 -> T-04 -> T-05`，合并顺序不回改已验收职责。模糊需求将五个门槛标为阻塞，只安排澄清与只读探索；未读仓库场景明确拒绝精确文件，使用 `[未知，待仓库证据]`、搜索线索和 `T-01 -> T-02 -> T-03`。三场景聚焦断言为 `PASS`，第三场景未发现 `src/`、`app/`、`api/` 或 `packages/` 等伪造路径。
- P1/P2 复修：模板、清单、usage 和完整示例均新增“已验收产出只可被后续任务消费，契约变更需新建修订任务”的执行边界；清单明确通过/有条件通过/不通过、阻塞定义和进入执行条件。usage 补齐“适合谁使用”“为什么普通提示词容易失败”，并保留输入、调用、阅读、串联和完整场景说明。报告中的元数据生成命令已替换为实际完整命令，不含省略参数。
- 第二轮审计边界复修：删除将同一 `I-02` 同时表述为审计事件数据和发布能力的语义。`I-02 AuditEvent` 现在仅是由 `T-02` 定义的 schema，记录运行时 producer/sink；`I-03 AuditPublisher.publish(event)` 仅是由 `T-03` 提供的 capability，consumes `I-02` 并向 `T-04` 提供确认/失败结果。模板、示例、usage 和清单均要求分别标记契约定义 owner、任务 consumes/produces 与运行时角色。
- 剩余风险：本轮是文档与静态场景复测，未对外部目标仓库或独立代理执行计划；真实实施仍可能因隐藏消费者、跨团队 SLA 或不可逆数据副作用改变依赖和发布策略，V2 要求将这些保持为未知或阻塞项。

### `issue-to-pr`

- 场景：清晰 Issue：空活动项目仪表盘不应崩溃；不可复现 Bug：生产导出文件偶发为空但只有截图；边界：修复过期优惠码时要求迁移模块、全仓格式化和升级依赖。
- V1 三场景缺口（文档级升级前审计）：清晰 Issue 虽能生成计划和 PR 概览，却没有可执行性门、非目标、工作区归属、验收到证据的逐项映射或提交粒度，容易在现有用户改动上扩大范围。不可复现 Bug 只要求“reproduction when feasible”，没有不可复现时的停止规则、已尝试环境/变量记录、最小观测和禁止声称修复的输出。重构诱惑场景只笼统要求避免无关重构，缺少把“顺手迁移/格式化/升级”移出当前 PR、以失败测试约束最小修改和在 PR 中说明风险/回滚的结构化约束。
- V2 改进：正文重写为 13 个中文章节，新增 Issue 可执行性卡、验收/非目标/停止条件、工作区保护、复现或不可复现记录、失败测试红灯和最小实现绿灯账本、验收矩阵、提交单一审查行为、PR 风险/回滚/未验证项。新增中文使用说明；模板、清单和示例以同一字段闭环三种场景。`openai.yaml`、README 和中文索引同步为安全交付的输入与产出。
- 结构验证（受跟踪证据）：本条只以本仓库受跟踪文件和本段末尾的实际静态检查记录为依据，不引用 `.superpowers/sdd/`。检查覆盖 `issue-to-pr/SKILL.md` 的 13 章节与输出契约、`references/templates.md` 的 RED/GREEN 与 PR 证据字段、`references/checklists.md` 的门槛、`references/examples.md` 的三场景、以及 README/中文索引导航。
- 场景一：清晰 Issue 的最小修复。
  - 原始输入：`Issue #42 要求空活动项目的仪表盘显示空状态而不是崩溃；验收是刷新和直接访问都稳定，范围不改活动排序。仓库和现有 dashboard 测试可访问。`
  - 预期行为：建立 AC-1/AC-2、非目标和 `[推断]` 的验证动作；真实执行时 RED-E-01 与 GREEN-E-01 分行记录，PR 的已验证声明引用这些证据 ID。
  - 实际文档级规则复测：`examples.md` 场景一将空状态/列表不变写为 AC、将排序列为非目标，并声明文档未执行外部仓库命令；RED-E-01/GREEN-E-01 均要求 cwd、完整命令、执行时间、退出码、关键输出和证据位置，未运行字段明确为“未运行，不填”。
  - 受跟踪证据与验证方式：`issue-to-pr/SKILL.md` 的“工作流”“输出契约”；`issue-to-pr/references/templates.md` 的“Issue 可执行性卡”“TDD 账本”“PR 描述”；`issue-to-pr/references/examples.md` 的“场景一：清晰 Issue 的最小修复”。静态检查用 `rg` 断言这些字段和 ID 存在。
  - 结论与限制：文档规则通过；未运行 Issue #42 所在外部仓库、测试或 PR，因而不声称真实 RED/GREEN、子代理输出或修复结果。
- 场景二：不可复现的 Bug。
  - 原始输入：`生产偶发导出文件为空。报告只给出截图，没有时间、账户、筛选条件、任务日志或仓库访问。请直接修复并发 PR。`
  - 预期行为：记录事实、未知和带依据的推断；结论为不通过，要求观测与稳定 fixture，禁止改代码、提交、关闭 Issue 或声称修复。
  - 实际文档级规则复测：`examples.md` 场景二只保留截图为 `[事实]`，把环境/任务 ID/日志列为 `[未知]`，将异步失败写为待验证 `[推断]`；`SKILL.md` 的“信息不足时的处理”明确不可复现时不进入实现。
  - 受跟踪证据与验证方式：`issue-to-pr/SKILL.md` 的“信息不足时的处理”“质量门槛”；`issue-to-pr/references/examples.md` 的“场景二：不可复现的 Bug”；`issue-to-pr/references/checklists.md` 的“复现、TDD 与证据”。静态检查断言禁止性文本和事实分类存在。
  - 结论与限制：文档规则通过；没有外部仓库、日志、任务 ID 或复现命令，不能得出真实根因、测试、修复或 PR 结论。
- 场景三：额外重构诱惑。
  - 原始输入：`修复结算页优惠码过期时显示 500。顺便把整个优惠模块迁到新架构、统一格式化并升级依赖。验收只要求过期码返回可理解错误。`
  - 预期行为：将迁移、格式化和依赖升级移为非目标；RED/GREEN 分行覆盖过期码与有效码不变，PR 验证引用 GREEN-E-* 或 PR-E-*。
  - 实际文档级规则复测：`examples.md` 场景三将三项诱惑明确为非目标，要求 GREEN-E-01 回链 RED-E-01；`SKILL.md` 的“专业判断规则”将顺手重构归为范围外，`templates.md` 要求 PR 已验证声明引用证据 ID。
  - 受跟踪证据与验证方式：`issue-to-pr/SKILL.md` 的“专业判断规则”“质量门槛”；`issue-to-pr/references/templates.md` 的“TDD 账本”“验收与验证矩阵”“PR 描述”；`issue-to-pr/references/examples.md` 的“场景三：额外重构诱惑”。静态检查断言非目标、RED/GREEN 和 PR 证据 ID 规则存在。
  - 结论与限制：文档规则通过；未在结算服务仓库运行过期码/有效码测试，不能声称功能已修复或重构安全。
- 静态检查记录：2026-07-26 10:17:43 +0800 在 cwd `/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2` 实际执行下列完整命令，退出码为 `0`。关键输出为 `Skill is valid!`，以及 `summary=quick_validate, 13 headings, inference fields, RED/GREEN and PR evidence fields, three scenarios, tracked-report independence, no copies/SDD, and exact-range diff check passed`。

```bash
set -e
printf 'cwd=%s\n' "$PWD"
printf 'executed_at=%s\n' "$(date '+%Y-%m-%d %H:%M:%S %z')"
/Users/mac/anaconda3/bin/python /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py issue-to-pr
expected='中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料'
actual=$(rg '^## ' issue-to-pr/SKILL.md | sed 's/^## //' | tr '\n' '|' | sed 's/|$//')
test "$actual" = "$expected"
rg -q '\[推断\]：依据与验证动作' issue-to-pr/references/templates.md
rg -q '^| RED-E-01 | RED ' issue-to-pr/references/templates.md
rg -q '^| GREEN-E-01 | GREEN ' issue-to-pr/references/templates.md
rg -q '工作目录.*完整命令.*执行时间.*退出码.*关键输出.*证据位置' issue-to-pr/references/templates.md
rg -q '引用 RED/GREEN 证据 ID.*工作目录.*完整命令或动作.*执行时间.*退出码.*关键输出.*证据位置' issue-to-pr/references/templates.md
rg -q 'PR 声明的每项“已验证”必须引用' issue-to-pr/references/templates.md
rg -q '每个 `\[推断\]` 写明依据与验证动作' issue-to-pr/references/checklists.md
rg -q 'RED-E-\* 与 GREEN-E-\* 分行记录' issue-to-pr/references/checklists.md
rg -q 'PR-E-\* 记录工作目录、完整命令/动作、执行时间、退出码、关键输出和证据位置' issue-to-pr/references/checklists.md
rg -q '\[推断\]：空活动路径可能复用' issue-to-pr/references/examples.md
rg -q '\[推断\]：导出可能在异步任务或生成阶段失败' issue-to-pr/references/examples.md
rg -q 'GREEN-E-01 必须回链 RED-E-01' issue-to-pr/references/examples.md
for heading in '场景一：清晰 Issue 的最小修复' '场景二：不可复现的 Bug' '场景三：额外重构诱惑'; do rg -q "$heading" issue-to-pr/references/examples.md; done
rg -q '`issue-to-pr`' README.md
rg -q '`issue-to-pr`' docs/skill-catalog.zh.md
section=$(awk '/^### `issue-to-pr`$/{on=1; next} /^### `/{on=0} on {print}' docs/validation/skill-v2-validation-report.md)
printf '%s\n' "$section" | rg -q '原始输入'
printf '%s\n' "$section" | rg -q '预期行为'
printf '%s\n' "$section" | rg -q '实际文档级规则复测'
printf '%s\n' "$section" | rg -q '受跟踪证据与验证方式'
printf '%s\n' "$section" | rg -q '结论与限制'
printf '%s\n' "$section" | rg -q '静态检查记录'
if printf '%s\n' "$section" | rg -q '\.superpowers/sdd/task-13-report\.md'; then exit 1; fi
if find . -type d -name '* 2' -print | grep -q .; then exit 1; fi
if git ls-files .superpowers/sdd | grep -q .; then exit 1; fi
git diff --check 201ad55 ed84163
printf 'summary=quick_validate, 13 headings, inference fields, RED/GREEN and PR evidence fields, three scenarios, README/catalog navigation assertions, tracked-report independence, no copies/SDD, and exact commit-range diff check passed\n'
```

- P2 静态检查范围与导航记录：`git diff --check 201ad55 ed84163` 不带路径过滤，覆盖从 Task 13 前基线 `201ad55` 到修复提交 `ed84163` 的全部 Task 13 Skill 与导航内容，包括 `issue-to-pr/`、`README.md`、`docs/skill-catalog.zh.md` 和本验证报告。2026-07-26 10:25:42 +0800 在 cwd `/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2` 实际执行：`rg -q '\`issue-to-pr\`' README.md` 的退出码为 `0`、无标准输出（匹配成功）；`rg -q '\`issue-to-pr\`' docs/skill-catalog.zh.md` 的退出码为 `0`、无标准输出（匹配成功）；`git diff --check 201ad55 ed84163` 的退出码为 `0`、关键输出为无空白错误；同次 `quick_validate.py issue-to-pr` 的退出码为 `0`、输出 `Skill is valid!`。工作树中的本报告修正另以 `git diff --check` 复核，退出码为 `0`、无空白错误。
- 结论：通过（文档静态验证）。三个场景均由受跟踪文件的章节、字段和静态断言支持；此结论不代表外部仓库的真实执行结果。
- 剩余风险：本轮仅能验证文档规则与静态字段，不能替代目标业务仓库中的真实复现、红绿测试、CI、代码审查、发布或子代理执行；这些结果必须在实际 Issue 中以相同证据字段记录。

### `bug-debugging-playbook`

- 升级前场景审计（仅审阅 V1 受跟踪文档；未在外部业务仓库运行或修改代码）：V1 只有英文 `Overview`/九步 `Workflow` 和 8 字段输出清单；它要求“先证明失败”，但没有事实、推断、假设和证据来源的字段或停止门槛。以下缺口是本次改写的 RED 基线，而非对真实系统根因的断言。
- 场景一：稳定复现的接口错误。
  - 原始请求：`POST /v1/invoices 在 staging 对已取消合同返回 500；同一请求在本地返回 422。日志有 request_id、时间和数据库错误。请定位后修复。`
  - V1 缺口：要求记录环境和复现，却没有把请求数据、时间线、request_id、应用/依赖版本和本地/staging 差异关联成证据链；“生成并排序假设”没有优先级依据、单变量实验或期望反证信号；“最小修复”前也没有根因确认标准，容易把 422/500 映射差异当作数据库根因。
- 场景二：偶发前端卡死。
  - 原始请求：`少量用户在切换工作区后页面偶发卡死，刷新恢复；没有稳定步骤，只有 Sentry 堆栈、浏览器版本和部分会话时间。请修复。`
  - V1 缺口：把“reproduce or create closest failing test/log/trace”写成单一路径，没有规定无法复现时应停止猜测性修复、保留哪些未知或如何补齐性能标记、状态转换日志、会话关联、采样和环境标签；也没有环境差异矩阵、时间线或把临时缓解与已确认根因分开的输出。
- 场景三：要求先改最可能的代码。
  - 原始请求：`支付回调偶尔重复扣款，最可能是 retry.ts；先把 retry 次数改成 1，之后再看日志。`
  - V1 缺口：虽说“不要因为修复看起来明显而修补症状”，但没有禁止同时尝试多个猜测、要求在修改前建立最小复现/不变量、使用变更二分或一次只改变一个变量；没有把降低风险的缓解措施和解释机制的根因证据分开，因而无法防止以改小重试次数冒充修复。
- V1 基线结论：三个场景都缺少可审查的证据 ID、假设优先级、单变量实验、环境/时间线比较、不可复现时的观测增强和根因确认门槛；V2 复测将只验证这些文档规则是否可执行，不声称已修复任何外部服务。
- V2 改进：正文改为 13 个中文章节，定义 `E-*` 证据、事实/推断/假设/未知、最小复现或观测增强、环境与数据差异矩阵、`H-*` 假设、`X-*` 单变量实验、受控变更二分、根因确认、缓解措施、最小修复和回归门禁。中文使用说明、模板、清单和示例使用同一套状态与字段；`openai.yaml`、README 和中文索引同步为“证据链”而非泛化“调试”入口。
- 场景复测（文档级；没有对外部业务仓库运行、改代码或模拟事故）：
  - 场景一：`examples.md` 将 staging 500 与本地 422 保留为 E-01/E-02 事实，要求同一 fixture 的最小复现、成功对照和复现率；差异矩阵只比较 schema、版本、flag、权限和数据，`X-01` 仅切换合同状态并有反证。只有机制解释调用链后才允许标记根因；统一错误码明确降级为缓解。
  - 场景二：无法稳定复现的卡死明确结论为“停止猜测性修复”，以工作区切换、请求生命周期、错误边界、主线程长任务和脱敏 session/trace ID 建立观测增强；采样窗口、保留期、Owner 和隐私边界必须存在。任何 timeout/刷新调整在关联证据前仅可写为可回退缓解，不能写成根因修复。
  - 场景三：`retry.ts` 被标为 `[假设]`，先要求支付事件 ID、幂等键和回调时间线；`X-01` 只验证重试触发，`X-02` 才单独验证幂等持久化。降低重试次数只减少影响，必须作为带漏处理风险、回滚和撤除条件的缓解；永久修复需证明同一事件最多一次扣款且独立事件仍可处理。
- 结构与场景静态验证：2026-07-26 13:36:39 +0800 在 cwd `/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2` 实际复制执行以下完整脚本，整段退出码为 `0`。脚本精确断言 13 个必需章节及顺序，将占位符扫描限定在 `bug-debugging-playbook/`，逐项检查三个场景和停止猜测/单变量/根因与缓解规则，匹配 README 与中文目录的正式条目，并确认 `4fcf145..865feb5` 恰好包含 9 个 Task 14 拥有文件后运行固定范围 `git diff --check`。

```bash
set -e
printf 'cwd=%s\n' "$PWD"
printf 'executed_at=%s\n' "$(date '+%Y-%m-%d %H:%M:%S %z')"
PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py bug-debugging-playbook
expected_headings='中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料'
actual_headings=$(rg '^## ' bug-debugging-playbook/SKILL.md | sed 's/^## //' | tr '\n' '|' | sed 's/|$//')
test "$actual_headings" = "$expected_headings"
printf 'PASS headings=%s\n' "$actual_headings"
test -f bug-debugging-playbook/references/usage-guide.zh.md
printf 'PASS usage-guide\n'
placeholder_pattern='TBD|TODO|FIXME|待办占位|未决占位|补充相关内容|在此填写|示例内容'
if rg -n "$placeholder_pattern" bug-debugging-playbook; then
  printf 'FAIL placeholder scan\n'
  exit 1
fi
printf 'PASS placeholder-scan scope=bug-debugging-playbook\n'
for heading in '场景一：稳定复现的接口错误' '场景二：偶发前端卡死' '场景三：用户要求先改最可能的代码'; do
  rg -q "^## $heading$" bug-debugging-playbook/references/examples.md
  printf 'PASS scenario=%s\n' "$heading"
done
rg -q '停止猜测性修复' bug-debugging-playbook/references/examples.md
rg -q '只切换同一 fixture 的状态' bug-debugging-playbook/references/examples.md
rg -q '\[缓解措施\]' bug-debugging-playbook/references/examples.md
printf 'PASS scenario-rules=stop-guessing,single-variable,root-cause-vs-mitigation\n'
rg -q '^| `bug-debugging-playbook` | Bug 调试证据链手册 |.*单变量实验.*最小复现或观测增强.*' README.md
rg -q '^| `bug-debugging-playbook` | Bug 调试证据链手册 |.*单变量实验.*最小复现或观测增强.*' docs/skill-catalog.zh.md
printf 'PASS navigation=README.md,docs/skill-catalog.zh.md\n'
expected_files='README.md
bug-debugging-playbook/SKILL.md
bug-debugging-playbook/agents/openai.yaml
bug-debugging-playbook/references/checklists.md
bug-debugging-playbook/references/examples.md
bug-debugging-playbook/references/templates.md
bug-debugging-playbook/references/usage-guide.zh.md
docs/skill-catalog.zh.md
docs/validation/skill-v2-validation-report.md'
actual_files=$(git diff --name-only 4fcf145 865feb5)
test "$actual_files" = "$expected_files"
printf 'PASS task-range-files=9\n'
git diff --check 4fcf145 865feb5
printf 'PASS diff-check=4fcf145..865feb5\n'
printf 'summary=quick_validate, exact 13 headings, scoped placeholder scan, three scenarios and rules, README/catalog navigation, exact Task 14 file set, and fixed-range diff check passed\n'
```

- 实际合并输出：

```text
cwd=/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2
executed_at=2026-07-26 13:36:39 +0800
Skill is valid!
PASS headings=中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料
PASS usage-guide
PASS placeholder-scan scope=bug-debugging-playbook
PASS scenario=场景一：稳定复现的接口错误
PASS scenario=场景二：偶发前端卡死
PASS scenario=场景三：用户要求先改最可能的代码
PASS scenario-rules=stop-guessing,single-variable,root-cause-vs-mitigation
PASS navigation=README.md,docs/skill-catalog.zh.md
PASS task-range-files=9
PASS diff-check=4fcf145..865feb5
summary=quick_validate, exact 13 headings, scoped placeholder scan, three scenarios and rules, README/catalog navigation, exact Task 14 file set, and fixed-range diff check passed
```

- 结论：通过（文档静态验证）。V2 在三种场景下都要求修改前的复现或观测证据、单变量验证，并明确区分根因和缓解；结论仅代表受跟踪文档的规则与字段可执行。
- 剩余风险：没有外部业务仓库、真实用户数据、生产权限或独立事故运行，因而无法证明任一具体系统的根因、观测开销、回归套件、部署和回滚有效。实际使用仍须以真实 `E-*`、隐私审查、环境约束和门禁结果更新结论。

### `test-generator`

- 升级前场景审计（仅审阅 V1 受跟踪文档；未在外部业务仓库生成、运行或修改真实测试）：V1 只有英文简介、七步工作流和八字段输出清单。它提到测试层级和“可行时”先失败，但没有把风险映射到最低有效层级、没有有效红灯的判定、无法红灯时的替代证据、fixture/mock 边界、可维护断言或可复跑命令证据。本审计是文档基线，不是对任何外部模块质量的断言。
- 场景一：为新 API 补测试。
  - 原始请求：`为 POST /v1/invoices 补测试：有效订单创建发票；没有库存时返回错误。代码在 services/invoice.ts，现有项目用 Vitest。`
  - V1 缺口：V1 仅要求“分类测试层级”和“列边界”，没有要求库存扣减、发票持久化、HTTP 错误映射、事件发布、权限和幂等风险分别选择层级，容易停在 service mock 单测；它也没有要求读到 Vitest 配置后才给出命令或明确哪些契约未知。
- 场景二：为已修复 Bug 加回归测试。
  - 原始请求：`已修复：管理员撤销邀请后，旧邀请链接仍可接受。请补回归测试。修复在 auth/invitations.ts；生产日志显示同一 token 撤销后仍返回 201。`
  - V1 缺口：V1 的“when feasible”未定义修复前版本、完整命令、预期失败信号或何种失败无效；修复后新增一个绿色测试也可能通过，却从未证明它能捕获撤销 token 仍返回 201 的原始症状。无法回到修复前版本时，V1 也没有证据替代和结论降级规则。
- 场景三：只追求覆盖率百分比。
  - 原始请求：`本周把 payment 模块覆盖率从 76% 提到 90%，先补快照和 mock 调用次数，测试全绿就可以合并。`
  - V1 缺口：虽说测试应绑定行为和风险，却没有把覆盖率不是质量代理、整页快照和无业务含义调用次数不可作为风险覆盖的规则变成明确拒绝、测试矩阵与通过门槛；因此不能防止以浅层测试掩盖重复扣款、超时、退款权限或 webhook 契约。
- V1 基线结论：三个场景都缺少可审查的 `B-*` 行为、`R-*` 风险到层级理由、边界/错误/权限/并发/契约逐项判断、fixture/mock 责任边界、`RED-*`/`ALT-*`/`GREEN-*`/`T-*` 命令账本和覆盖缺口结论；V2 复测只验证这些文档规则可执行，不声称外部服务已被测试。
- V2 改进：正文升级为 13 个中文章节，要求先建立行为和风险，再按最低有效层级选择单元、组件、集成、契约、E2E 或人工验证。它将 Bug 红灯和替代证据分开，覆盖边界、错误、权限、并发、幂等和契约；模板、清单、使用说明和示例统一为 `B-*`、`R-*`、`RED-*`、`ALT-*`、`GREEN-*`、`T-*`、`GAP-*`，并将覆盖率定位为辅助诊断。README、中文索引与 `openai.yaml` 同步为风险驱动入口。
- 场景复测（文档级；没有对外部业务仓库运行、改代码或伪造测试结果）：
  - 场景一：`examples.md` 在不知道实际 Vitest 配置、路由、schema 和事务边界时停止编造路径/命令；将计价规则放入单元，库存、持久化、回滚和幂等放入集成，错误 payload 放入契约，并要求最小临时数据库 fixture、fake server 边界和权限/并发未知项。
  - 场景二：示例要求 `RED-01` 在修复前 commit 的隔离数据库中因“返回 201 或创建成员”而失败，拒绝 fixture/启动错误作为红灯；`GREEN-01` 必须回链 `RED-01` 并覆盖有效 token 对照。没有修复前版本时只允许 `ALT-01` 引用脱敏日志和恢复红灯条件，结论降为有条件通过。
  - 场景三：示例拒绝将 90% 覆盖率作为通过条件，以重复入账、provider 超时和退款权限的 `R-*` 选择集成/契约测试，断言 ledger、公开状态/错误和审计事件；明确拒绝整页快照、浅层 render 与无业务语义的 mock 次数。
- 受跟踪证据与验证方式：`test-generator/SKILL.md` 的“风险到测试层级映射”“Bug 回归、边界和断言”“Fixture 与 mock 边界”“质量门槛”；`references/templates.md` 的风险矩阵、证据账本和缺口结论；`references/checklists.md` 的红绿与断言门槛；`references/examples.md` 的三个场景；以及 README/中文索引的正式导航条目。静态检查会断言 13 个章节及顺序、缺少占位符、三个场景、红灯替代/快照拒绝规则、导航和固定提交范围的文件集合。
- 结构与场景静态验证：2026-07-26 14:05:45 +0800 在 cwd `/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2` 实际执行下列完整脚本，整段退出码为 `0`。脚本精确断言 13 个必需章节及顺序，将占位符扫描限定在 `test-generator/`，检查三个指定场景、风险层级、条件性 `ALT-*`、红灯或替代证据和拒绝覆盖率代理规则，匹配 README 与中文目录的正式条目，并确认 `a9f65a6..72baae8` 恰好包含 9 个 Task 15 文件后执行固定范围 `git diff --check`。

```bash
set -e
printf 'cwd=%s\n' "$PWD"
printf 'executed_at=%s\n' "$(date '+%Y-%m-%d %H:%M:%S %z')"
PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py test-generator
expected_headings='中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料'
actual_headings=$(rg '^## ' test-generator/SKILL.md | sed 's/^## //' | tr '\n' '|' | sed 's/|$//')
test "$actual_headings" = "$expected_headings"
printf 'PASS headings=%s\n' "$actual_headings"
test -f test-generator/references/usage-guide.zh.md
printf 'PASS usage-guide\n'
placeholder_pattern='TBD|TODO|FIXME|待办占位|未决占位|补充相关内容|在此填写|示例内容'
if rg -n "$placeholder_pattern" test-generator; then
  printf 'FAIL placeholder scan\n'
  exit 1
fi
printf 'PASS placeholder-scan scope=test-generator\n'
for heading in '场景一：为新 API 补测试' '场景二：为已修复 Bug 加回归测试' '场景三：只追求覆盖率百分比'; do
  rg -q "^## $heading$" test-generator/references/examples.md
  printf 'PASS scenario=%s\n' "$heading"
done
rg -q '最低有效层级' test-generator/SKILL.md
rg -q 'ALT-\*' test-generator/SKILL.md
rg -q 'ALT-\*.*仅在无法获得有效修复前红灯时必填/使用.*有效 .*RED-\*.*非 Bug 测试时不填' test-generator/references/templates.md
rg -q '不以覆盖率数字替代本结论' test-generator/references/templates.md
rg -q '整页快照' test-generator/references/examples.md
rg -q 'GREEN-01 必须回链 RED-01' test-generator/references/examples.md
printf 'PASS scenario-rules=risk-level,conditional-alt-evidence,red-or-alternative-proof,no-coverage-proxy\n'
rg -q '^| `test-generator` | 风险驱动测试生成器 |.*RED-\*.*GREEN-\*.*T-\*' README.md
rg -q '^| `test-generator` | 风险驱动测试生成器 |.*RED-\*.*GREEN-\*.*T-\*' docs/skill-catalog.zh.md
printf 'PASS navigation=README.md,docs/skill-catalog.zh.md\n'
section=$(awk '/^### `test-generator`$/{on=1; next} /^### `code-review-assistant`$/{on=0} on {print}' docs/validation/skill-v2-validation-report.md)
printf '%s\n' "$section" | rg -q '原始请求'
printf '%s\n' "$section" | rg -q 'V1 缺口'
printf '%s\n' "$section" | rg -q '场景复测'
printf '%s\n' "$section" | rg -q '受跟踪证据与验证方式'
printf '%s\n' "$section" | rg -q '结论与限制'
printf 'PASS report-sections=V1,V2,scenarios,evidence,limits\n'
expected_files='README.md
docs/skill-catalog.zh.md
docs/validation/skill-v2-validation-report.md
test-generator/SKILL.md
test-generator/agents/openai.yaml
test-generator/references/checklists.md
test-generator/references/examples.md
test-generator/references/templates.md
test-generator/references/usage-guide.zh.md'
actual_files=$(git diff --name-only a9f65a6 72baae8)
test "$actual_files" = "$expected_files"
printf 'PASS task-range-files=9\n'
git diff --check a9f65a6 72baae8
printf 'PASS diff-check=a9f65a6..72baae8\n'
printf 'summary=quick_validate, exact 13 headings, scoped placeholder scan, three scenarios and risk/conditional-alt/red-proof/coverage rules, navigation, report sections, exact Task 15 file set, and fixed-range diff check passed\n'
```

- Minor 复修：证据账本明确将 `ALT-*` 标为条件字段，仅在无法获得有效修复前红灯时必填/使用；已有有效 `RED-*` 或非 Bug 测试时不填。完整验证脚本新增同义静态断言，防止后续模板改动再次把 `ALT-*` 误解为普遍必填。
- 实际输出：`Skill is valid!`；13 个章节、中文使用说明、限定占位符扫描、三个场景、风险/条件性 `ALT-*`/红灯/覆盖率规则、README/中文目录导航、报告章节、9 个任务文件和 `a9f65a6..72baae8` 范围检查均输出 `PASS`。固定范围 `git diff --check` 无输出，表示没有空白错误。
- 结论与限制：通过（文档静态验证）。没有业务仓库、修复前 artifact、CI 或外部 provider 环境时，不能将本报告当作任一 API、Bug 或支付流程的实际测试通过证明。
- 剩余风险：文档静态验证不能检验 fixture 是否代表真实数据、fake server 是否与 provider 同步、并发调度是否稳定、修复前 artifact 是否可得，或 E2E 环境是否可信。实际使用必须将这些限制写入 `GAP-*`/`ALT-*`，并由相应 owner 执行真实 `RED-*`、`GREEN-*` 和 `T-*`。

### `code-review-assistant`

- 升级前场景审计（仅审阅 V1 受跟踪文档；未在外部业务仓库运行、修改代码或声称真实 PR 已通过）：V1 只有中文简介、英文 `Overview`/七步 `Workflow` 和五字段发现模板。它虽要求优先找 Bug，却没有需求/契约对照、完整 diff 与相邻上下文的门槛、置信度/触发条件/证据字段、误报控制或无发现时的测试缺口。本审计是文档基线，不是对任何外部变更的结论。
- 场景一：完整 PR diff 包含接口变更。
  - 原始请求：`审查 PR #184：GET /v1/projects 将 archived 改名为 isArchived，移动端旧客户端仍在兼容窗口；提供完整 base/head diff、路由、序列化器、消费者和契约测试。`
  - V1 缺口：V1 没有把兼容需求、diff 删除、移动端消费者和契约测试放入同一个对照，只有“检查 API”，容易只看到新字段测试后错过旧字段删除；发现模板也没有置信度、触发条件和最小修复方向。
- 场景二：只有单个文件，没有需求或测试结果。
  - 原始请求：`只审查 OrderService 文件；没有 PR 描述、完整 diff、调用方、测试结果或运行环境。`
  - V1 缺口：V1 没有说明范围、base/head、消费者或并发模型缺失时如何降级，容易将“可能有竞态”“没有测试”写成无行号、无真实触发条件的缺陷，或反过来写“没有问题”。
- 场景三：要求只给表扬、不报告问题。
  - 原始请求：`只总结支付回调 PR 的优点，不要提问题；diff 显示 charge 在持久化前执行，没有幂等键/事务，需求要求同一 webhook 事件最多扣款一次。`
  - V1 缺口：V1 没有把用户的输出偏好和审查发现责任分开，也没有并发/状态检查、财务影响和 P0 门槛，可能让重复扣款风险被正面总结掩盖。
- V1 基线结论：三个场景均缺少可审查的 `RC-*` 需求/契约映射、完整 diff/相邻上下文边界、`F-*` 的严重度/置信度/路径行号/触发条件/影响/证据/最小修复字段、`GAP-*` 降级和无发现时的残余风险；V2 复测只验证文档规则可执行，不证明任何真实 PR 安全。
- V2 改进：正文升级为 13 个中文章节，要求审查卡、base/head、需求/契约对照、完整 diff 与邻近定义/调用方/错误/状态/测试上下文。专业判断覆盖正确性/回归、数据/安全、权限、并发/状态、兼容、性能和测试质量；`F-*` 固定包含严重度、置信度、精确路径行号、触发条件、影响、证据和最小修复方向，证据不足改用 `GAP-*`。模板、清单、使用说明和示例统一此结构；README、中文索引与 `openai.yaml` 同步为证据驱动入口。
- 场景复测（文档级；不在外部业务仓库执行、修改或模拟支付/接口）：
  - 场景一：`examples.md` 将兼容窗口、删除旧字段、仍读取旧字段的移动端消费者与契约测试纳入 `RC-01`，给出高置信度 P1、精确定位、客户端触发条件、影响和双字段/版本协商修复方向。
  - 场景二：示例不把无需求、无完整 diff、无调用方和无运行结果伪装成缺陷或批准；以 `GAP-01` 至 `GAP-03` 分别说明阻断判断、最小补充材料和“仅单文件静态阅读”的有条件结论。
  - 场景三：示例在用户要求表扬时仍输出 P0，说明重复 webhook 的顺序条件、重复扣款影响和事件 ID 原子去重的最小修复；正面观察只能放在结尾，不能抵消发现。
- 受跟踪证据与验证方式：`code-review-assistant/SKILL.md` 的“需求、diff 与证据边界”“风险面与严重度”“误报控制、测试与无发现结论”“质量门槛”；`references/templates.md` 的 `RC-*`/`F-*`/`GAP-*` 字段；`references/checklists.md` 的七类风险面和最终判定；`references/examples.md` 的三个场景；以及 README/中文索引的正式导航条目。静态检查会断言 13 个章节及顺序、限定占位符扫描、三个场景、发现证据/完整 diff/非风格缺陷/无发现/不压制风险规则、导航、报告章节和固定提交范围的文件集合。
- 结构与场景静态验证：2026-07-26 14:20:10 +0800 在 cwd `/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2` 实际复制执行以下完整脚本，整段退出码为 `0`。脚本精确断言 13 个必需章节及顺序，将占位符扫描限定在 `code-review-assistant/`，检查三个指定场景和发现格式/完整 diff/误报控制/无发现/用户偏好边界，匹配 README 与中文目录的正式条目，并确认 `f8faed2..cbb9693` 恰好包含 9 个 Task 16 文件后执行固定范围 `git diff --check`。

```bash
set -e
printf 'cwd=%s\n' "$PWD"
printf 'executed_at=%s\n' "$(date '+%Y-%m-%d %H:%M:%S %z')"
PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py code-review-assistant
expected_headings='中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料'
actual_headings=$(rg '^## ' code-review-assistant/SKILL.md | sed 's/^## //' | tr '\n' '|' | sed 's/|$//')
test "$actual_headings" = "$expected_headings"
printf 'PASS headings=%s\n' "$actual_headings"
test -f code-review-assistant/references/usage-guide.zh.md
printf 'PASS usage-guide\n'
placeholder_pattern='TBD|TODO|FIXME|待办占位|未决占位|补充相关内容|在此填写|示例内容'
if rg -n "$placeholder_pattern" code-review-assistant; then
  printf 'FAIL placeholder scan\n'
  exit 1
fi
printf 'PASS placeholder-scan scope=code-review-assistant\n'
for heading in '场景一：完整 PR diff 包含接口变更' '场景二：只有单个文件，没有需求或测试结果' '场景三：要求只给表扬、不报告问题'; do
  rg -q "^## $heading$" code-review-assistant/references/examples.md
  printf 'PASS scenario=%s\n' "$heading"
done
rg -q '严重度、置信度、精确路径行号、触发条件、影响、证据和最小修复方向' code-review-assistant/SKILL.md
rg -q '完整 diff' code-review-assistant/SKILL.md
rg -q '风格.*偏好.*不是缺陷' code-review-assistant/SKILL.md
rg -q '在已读范围内未发现有证据的缺陷' code-review-assistant/references/examples.md
rg -q '用户偏好不改变对可复现高风险的报告责任' code-review-assistant/references/examples.md
printf 'PASS scenario-rules=evidence-fields,full-diff,no-style-defects,no-finding-limit,do-not-suppress-risk\n'
rg -q '^| `code-review-assistant` | 证据驱动代码审查 |.*F-\*.*GAP-\*' README.md
rg -q '^| `code-review-assistant` | 证据驱动代码审查 |.*F-\*.*GAP-\*' docs/skill-catalog.zh.md
printf 'PASS navigation=README.md,docs/skill-catalog.zh.md\n'
section=$(awk '/^### `code-review-assistant`$/{on=1; next} /^### `refactor-with-safety`$/{on=0} on {print}' docs/validation/skill-v2-validation-report.md)
printf '%s\n' "$section" | rg -q '原始请求'
printf '%s\n' "$section" | rg -q 'V1 缺口'
printf '%s\n' "$section" | rg -q '场景复测'
printf '%s\n' "$section" | rg -q '受跟踪证据与验证方式'
printf '%s\n' "$section" | rg -q '结论与限制'
printf 'PASS report-sections=V1,V2,scenarios,evidence,limits\n'
expected_files='README.md
code-review-assistant/SKILL.md
code-review-assistant/agents/openai.yaml
code-review-assistant/references/checklists.md
code-review-assistant/references/examples.md
code-review-assistant/references/templates.md
code-review-assistant/references/usage-guide.zh.md
docs/skill-catalog.zh.md
docs/validation/skill-v2-validation-report.md'
actual_files=$(git diff --name-only f8faed2 cbb9693)
test "$actual_files" = "$expected_files"
printf 'PASS task-range-files=9\n'
git diff --check f8faed2 cbb9693
printf 'PASS diff-check=f8faed2..cbb9693\n'
printf 'summary=quick_validate, exact 13 headings, scoped placeholder scan, three scenarios and evidence/full-diff/no-style/no-finding/no-suppression rules, navigation, report sections, exact Task 16 file set, and fixed-range diff check passed\n'
```

- 实际合并输出：

```text
cwd=/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2
executed_at=2026-07-26 14:20:10 +0800
Skill is valid!
PASS headings=中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料
PASS usage-guide
PASS placeholder-scan scope=code-review-assistant
PASS scenario=场景一：完整 PR diff 包含接口变更
PASS scenario=场景二：只有单个文件，没有需求或测试结果
PASS scenario=场景三：要求只给表扬、不报告问题
PASS scenario-rules=evidence-fields,full-diff,no-style-defects,no-finding-limit,do-not-suppress-risk
PASS navigation=README.md,docs/skill-catalog.zh.md
PASS report-sections=V1,V2,scenarios,evidence,limits
PASS task-range-files=9
PASS diff-check=f8faed2..cbb9693
summary=quick_validate, exact 13 headings, scoped placeholder scan, three scenarios and evidence/full-diff/no-style/no-finding/no-suppression rules, navigation, report sections, exact Task 16 file set, and fixed-range diff check passed
```
- 结论与限制：本提交只更新受跟踪 Skill 文档与静态约束；没有业务仓库、真实调用方、生产数据、CI 或并发环境，不能将场景示例当作任一接口、支付或 PR 的实际审查结论。
- 剩余风险：静态验证不能发现未提供的运行时契约、隐藏消费者、数据规模、权限配置、调度时序或测试环境差异。实际审查必须保留 `GAP-*`、置信度、真实路径/行号与命令/CI 证据。

### `refactor-with-safety`

- 升级前场景审计（只审阅 V1 受跟踪文档；未在外部业务仓库修改代码、迁移数据或声称测试通过）：V1 只有中文简介、英文概览、八步工作流和简短输出字段。它提到特征化测试与公共契约，却没有把调用方可观察行为、数据/副作用/兼容契约、依赖方向、机械与语义变更、性能基线、每步回滚和停止条件绑定到可审查产物。本审计是文档基线，不是对任一重构的安全结论。
- 场景一：拆分大文件。
  - 原始请求：`把 1,100 行的订单结算服务拆成计算、持久化和通知模块，不改变当前行为。现有测试只覆盖成功结算；服务同时写数据库并发送消息。`
  - V1 缺口：V1 虽说“必要时加 characterization tests”，但没有要求锁定拒绝、重试、消息发送失败、写库/通知顺序和未受影响对照；也未要求输入输出、状态拥有者、I/O 和依赖方向，容易把副作用藏入新 helper 或形成反向依赖。
- 场景二：公共 API 重命名。
  - 原始请求：`将公共 SDK 的 getUser 重命名为 fetchUser，删除旧名称；Web、CLI 和两个外部插件可能仍在使用，兼容窗口和性能预算尚未提供。`
  - V1 缺口：V1 没有消费者清单、版本窗口、适配/废弃条件、错误/默认值/缓存语义或性能基线字段，可能直接删除旧导出，把破坏性 API 变更误称为内部重命名。
- 场景三：重构同时增加功能。
  - 原始请求：`重构搜索模块并顺便加入“按价格筛选”和新的默认排序，测试以后再补。`
  - V1 缺口：V1 只笼统警告不要混入功能，没有把功能轨、独立验收/失败测试/提交、机械与语义分类、回滚点和停止条件变成必填结构；默认排序变化可能被藏在“整理”中，测试也会被延后。
- V1 基线结论：三个场景均缺少 `B-*` 行为不变量、`C-*` 公共 API/数据/副作用/兼容契约、依赖边界、`P-*` 性能基线、机械/语义/功能分轨、每步 `S-*` 验证与回滚以及 `GAP-*` 停止规则；V2 复测只验证文档规则可执行，不证明任一外部重构安全。
- V2 改进：主文档升级为 13 个中文章节，建立 `B-*` 特征化测试、`C-*` 契约和依赖边界、`P-*` 同条件性能基线、机械/语义/功能三类变化、可逆 `S-*` 和真实 `E-*` 证据账本。公共 API 重命名必须有消费者、兼容窗口与适配/废弃证据；未知消费者、性能、回滚或功能验收时使用 `GAP-*` 并停止扩大范围。模板、清单、使用说明和场景统一该结构；README、中文索引和 `openai.yaml` 同步为安全演进入口。
- 场景复测（文档级；不在外部业务仓库执行、修改或迁移）：
  - 场景一：`examples.md` 先以 `B-01`/`B-02` 锁成功、拒绝、重试与消息失败的公开结果和对照，再要求写明状态拥有者、I/O、允许依赖方向与可抽取缝隙。`S-02` 只移动纯计算，`S-03` 才经端口抽取副作用；未知消息消费者、错误或重试时以 `GAP-*` 停止。
  - 场景二：示例将导出、返回/错误、缓存和请求次数列为 `C-01`/`C-02`；在插件、兼容窗口和性能预算未知时只新增带 `getUser` 适配导出的 `fetchUser`，迁移已知消费者，不删除旧 API。删除步骤必须有消费者、契约与性能证据。
  - 场景三：示例将价格筛选与默认排序列为独立 `F-01` 功能轨；重构轨明确不改变默认排序、空结果、错误和缓存键。功能没有验收、失败测试或确认时只允许锁 `B-01` 与进行结构步骤，结论为停止功能实施而非延后测试。
- 受跟踪证据与验证方式：`refactor-with-safety/SKILL.md` 的“核心原则”“信息不足时的处理”“工作流”“专业判断规则”“质量门槛”；`references/templates.md` 的 `B-*`/`C-*`/`P-*`/`S-*`/`E-*`/`GAP-*`；`references/checklists.md` 的分轨、回滚和最终判定；`references/examples.md` 的三个场景；`references/usage-guide.zh.md` 的输入不足降级和导航。静态检查会断言 13 个章节及顺序、限定占位符扫描、三个场景、行为/契约/依赖/分轨/性能/回滚/停止规则、双导航和固定提交范围的文件集合。
- 结构与场景静态验证：在 cwd `/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2` 实际复制执行以下完整脚本。脚本不读取 `HEAD`，而是固定并校验三个不可变提交：基线 `a8670a40cea4750facbee530f8b33abc9347f00b`、Skill 主提交 `5653e412124efe8646c8554a640d8a192d0c158a` 和验证记录提交 `98c491137c24105c07fc89b879c08130271d409d`。`a8670a4..5653e41` 只验证 9 个 Skill 交付文件；`5653e41..98c4911` 只验证验证报告自身的 1 个文件，避免报告提交被动态并入 Skill 范围或形成自引用。其余断言覆盖 13 个必需章节及顺序、限定占位符扫描、三个指定场景、行为/契约/依赖/分轨/性能/回滚/停止规则、双导航和报告章节。

```bash
set -e
printf 'cwd=%s\n' "$PWD"
printf 'executed_at=%s\n' "$(date '+%Y-%m-%d %H:%M:%S %z')"
base_commit=a8670a40cea4750facbee530f8b33abc9347f00b
skill_commit=5653e412124efe8646c8554a640d8a192d0c158a
validation_commit=98c491137c24105c07fc89b879c08130271d409d
test "$(git rev-parse a8670a4)" = "$base_commit"
test "$(git rev-parse 5653e41)" = "$skill_commit"
test "$(git rev-parse 98c4911)" = "$validation_commit"
git merge-base --is-ancestor "$base_commit" "$skill_commit"
git merge-base --is-ancestor "$skill_commit" "$validation_commit"
printf 'skill-range=%s..%s\n' "$base_commit" "$skill_commit"
printf 'validation-record-range=%s..%s\n' "$skill_commit" "$validation_commit"
PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py refactor-with-safety
expected_headings='中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料'
actual_headings=$(rg '^## ' refactor-with-safety/SKILL.md | sed 's/^## //' | tr '\n' '|' | sed 's/|$//')
test "$actual_headings" = "$expected_headings"
printf 'PASS headings=%s\n' "$actual_headings"
test -f refactor-with-safety/references/usage-guide.zh.md
printf 'PASS usage-guide\n'
placeholder_pattern='TBD|TODO|FIXME|待办占位|未决占位|补充相关内容|在此填写|示例内容'
if rg -n "$placeholder_pattern" refactor-with-safety; then
  printf 'FAIL placeholder scan\n'
  exit 1
fi
printf 'PASS placeholder-scan scope=refactor-with-safety\n'
for heading in '场景一：拆分大文件' '场景二：公共 API 重命名' '场景三：重构同时增加功能'; do
  rg -q "^## $heading$" refactor-with-safety/references/examples.md
  printf 'PASS scenario=%s\n' "$heading"
done
rg -q '功能轨另开验收和提交' refactor-with-safety/SKILL.md
rg -q 'B-\*.*特征化测试' refactor-with-safety/SKILL.md
rg -q 'C-\*.*公共 API' refactor-with-safety/SKILL.md
rg -q '依赖方向' refactor-with-safety/SKILL.md
rg -q '机械变更与语义变更分开' refactor-with-safety/SKILL.md
rg -q 'P-\*.*性能基线' refactor-with-safety/SKILL.md
rg -q '回滚点和停止条件' refactor-with-safety/SKILL.md
rg -q '不开始宽泛重构' refactor-with-safety/SKILL.md
rg -q '公共 API 重命名默认采用适配' refactor-with-safety/SKILL.md
rg -q '状态：通过 / 有条件通过 / 停止' refactor-with-safety/references/templates.md
printf 'PASS scenario-rules=feature-separation,characterization,contracts,dependency-boundaries,mechanical-semantic,performance,rollback,stop-on-insufficient-input\n'
rg -q '^| `refactor-with-safety` | 安全重构助手 |.*B-\*.*C-\*.*P-\*.*E-\*.*GAP-\*' README.md
rg -q '^| `refactor-with-safety` | 安全重构助手 |.*B-\*.*C-\*.*P-\*.*E-\*.*GAP-\*' docs/skill-catalog.zh.md
printf 'PASS navigation=README.md,docs/skill-catalog.zh.md\n'
section=$(awk '/^### `refactor-with-safety`$/{on=1; next} /^## AI 应用评测与质量$/{on=0} on {print}' docs/validation/skill-v2-validation-report.md)
printf '%s\n' "$section" | rg -q '原始请求'
printf '%s\n' "$section" | rg -q 'V1 缺口'
printf '%s\n' "$section" | rg -q 'V2 改进'
printf '%s\n' "$section" | rg -q '场景复测'
printf '%s\n' "$section" | rg -q '受跟踪证据与验证方式'
printf '%s\n' "$section" | rg -q '结论与限制'
printf 'PASS report-sections=V1,V2,scenarios,evidence,limits\n'
expected_files='README.md
docs/skill-catalog.zh.md
docs/validation/skill-v2-validation-report.md
refactor-with-safety/SKILL.md
refactor-with-safety/agents/openai.yaml
refactor-with-safety/references/checklists.md
refactor-with-safety/references/examples.md
refactor-with-safety/references/templates.md
refactor-with-safety/references/usage-guide.zh.md'
actual_files=$(git diff --name-only "$base_commit" "$skill_commit")
test "$actual_files" = "$expected_files"
printf 'PASS task-range-files=9\n'
expected_validation_record_files='docs/validation/skill-v2-validation-report.md'
actual_validation_record_files=$(git diff --name-only "$skill_commit" "$validation_commit")
test "$actual_validation_record_files" = "$expected_validation_record_files"
printf 'PASS validation-record-files=1\n'
git diff --check "$base_commit" "$skill_commit"
printf 'PASS diff-check=%s..%s\n' "$base_commit" "$skill_commit"
git diff --check "$skill_commit" "$validation_commit"
printf 'PASS diff-check=%s..%s\n' "$skill_commit" "$validation_commit"
printf 'summary=quick_validate, exact 13 headings, scoped placeholder scan, three scenarios and feature/characterization/contract/dependency/mechanical-semantic/performance/rollback/stop rules, navigation, report sections, exact 9-file Skill delivery range, exact 1-file validation record range, and both fixed-range diff checks passed\n'
```

- 实际合并输出：2026-07-26 15:52:45 +0800 在上述 cwd 执行完整脚本，整段退出码为 `0`。输出中的两个范围均来自脚本内固定的完整 SHA，不读取当前分支或 `HEAD`。

```text
cwd=/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2
executed_at=2026-07-26 15:52:45 +0800
skill-range=a8670a40cea4750facbee530f8b33abc9347f00b..5653e412124efe8646c8554a640d8a192d0c158a
validation-record-range=5653e412124efe8646c8554a640d8a192d0c158a..98c491137c24105c07fc89b879c08130271d409d
Skill is valid!
PASS headings=中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料
PASS usage-guide
PASS placeholder-scan scope=refactor-with-safety
PASS scenario=场景一：拆分大文件
PASS scenario=场景二：公共 API 重命名
PASS scenario=场景三：重构同时增加功能
PASS scenario-rules=feature-separation,characterization,contracts,dependency-boundaries,mechanical-semantic,performance,rollback,stop-on-insufficient-input
PASS navigation=README.md,docs/skill-catalog.zh.md
PASS report-sections=V1,V2,scenarios,evidence,limits
PASS task-range-files=9
PASS validation-record-files=1
PASS diff-check=a8670a40cea4750facbee530f8b33abc9347f00b..5653e412124efe8646c8554a640d8a192d0c158a
PASS diff-check=5653e412124efe8646c8554a640d8a192d0c158a..98c491137c24105c07fc89b879c08130271d409d
summary=quick_validate, exact 13 headings, scoped placeholder scan, three scenarios and feature/characterization/contract/dependency/mechanical-semantic/performance/rollback/stop rules, navigation, report sections, exact 9-file Skill delivery range, exact 1-file validation record range, and both fixed-range diff checks passed
```

- 结论与限制：通过（文档静态验证）。没有业务仓库、真实调用方、生产数据、CI、负载或外部系统，不能将本节当作任一重构、API 迁移或性能保持的实际证明。
- 剩余风险：静态规则不能发现隐藏消费者、实际数据版本、异步投递时序、查询计划、真实负载、不可逆外部副作用或部署配置。实际使用必须保留 `GAP-*`、真实 `E-*`、兼容 owner 和补偿/回滚边界。

## AI 应用评测与质量

### `ai-app-eval-builder`

- 升级前场景审计（仅审阅 V1 受跟踪文档；未访问业务仓库、生产日志或评测平台）：V1 有英文概览、七步流程和基础 dataset/rubric/grader 模板，但没有将能力与风险、代表性、泄漏、版本、校准、RAG/Agent 分层、切片发布门禁和离线-线上闭环变成可审查字段。以下缺口是文档 RED 基线，不是任一 AI 系统的实际质量判断。
- 场景一：RAG 问答评测。
  - 原始请求：`为客服政策 RAG 问答建立评测。新 reranker 已在 staging；它要回答退款、取消和发票问题并给出引用。我们有 80 条人工整理 FAQ，没有整理过线上错误。`
  - V1 缺口：V1 将 context、参考答案、retrieval relevance 和 answer quality 放在同一层，没有要求必要证据是否被召回/排序、答案是否忠实/完整、引用是否支持主张、无证据是否拒答；也没有让 FAQ 的文档族、改写题、few-shot、索引与测试切分接受泄漏/重复检查，或把“没有线上错误”降为代表性缺口。
- 场景二：Agent 工具调用评测。
  - 原始请求：`评测一个运营 Agent：它可以查询订单、生成退款草稿、提交退款，管理员和客服权限不同。我们想比较新的工具描述和模型，担心它会循环或误提交退款。`
  - V1 缺口：V1 只笼统列出 tool selection、arguments、step count，没有强制记录初始状态、选择、参数、返回、权限决策、重试、循环、终止和副作用 trace；最终文本正确时，越权调用、错误参数或重复退款仍可能被单一质量分遮蔽。
- 场景三：只要求用准确率评价聊天助手。
  - 原始请求：`把聊天助手准确率从 82% 提到 90%，只要平均分更高就发布。回答可能涉及账户访问、计费和一般帮助。`
  - V1 缺口：V1 虽不建议单一“quality”分，但没有把账户/计费硬风险、语言/上下文/角色切片、LLM judge 顺序/自偏/长度/位置偏差、人工校准、成本/延迟/稳定性和生产回流纳入不可省略的发布门禁，因此 90% 平均仍可掩盖高风险失败。
- V1 基线结论：三个场景均缺少 `C-*`/`R-*` 能力风险映射、黄金/生产失败/困难/对抗数据与代表性账本、泄漏和近重复规则、分层 `G-*`、人工/LLM judge 校准、可比较版本、切片门禁和 `E-*` 真实运行/回流记录；V2 复测只验证这些文档规则是否被明确交付，不声称候选模型、reranker 或 Agent 已通过。
- V2 改进：`SKILL.md` 统一为 13 个中文章节，建立能力与风险、版本化离线数据集和线上回流、确定性/人工/LLM judge 混合、可复现 rubric、人工盲评与 judge 偏差校准、RAG 检索/证据/答案分层、Agent trace/工具/参数/权限/循环/副作用、质量/成本/延迟/稳定性、baseline/candidate/dataset/grader 版本、切片回归门槛和发布决定。内容修复再增加强制 `Failure-*` 失败分类与处置台账：稳定代码、定义/边界、RAG/Agent/其他层、切片、频率/严重性、可能修复/owner、生产样本、回归 case 和 `G-*`/`E-*` 回链。中文指南、模板、清单和示例使用 `C-*`、`R-*`、`D-*`、`G-*`、`Failure-*`、`E-*`、`Gate-*`、`GAP-*` 同一账本，README 与中文目录同步为离线-线上闭环入口。
- 场景复测（文档级；没有运行外部模型、读取生产数据、调用工具或伪造评测数值）：
  - 场景一：`examples.md` 先将没有线上错误标为 `[未知]`，要求按文档族/改写簇检查 FAQ、few-shot、索引与评测泄漏；`D-*` 区分黄金、困难、对抗和待审批生产失败候选。`G-01` 检查必要证据检索和排序，`G-02` 评答案忠实/完整/无证据拒答，`G-03` 判关键主张引用；`Failure-RAG-RETRIEVAL-MISS` 与 `Failure-RAG-CITATION-UNSUPPORTED` 将失败切片、频率/严重性、owner、生产/回归 `D-*` 和 `G-*`/`E-*` 串起来。关键政策与伪引用 Gate 独立阻断，不能由平均答案分抵消。
  - 场景二：示例为客服和管理员分权限切片，`D-11` 至 `D-14` 写脱敏生产失败、allowlist、参数、幂等、终态与冻结回归 case；`G-11` 至 `G-14` 是工具、参数、循环和副作用确定性门禁。四项分别回链 `Failure-AGENT-UNAUTHORIZED-TOOL`、`Failure-AGENT-INVALID-ARGUMENT`、`Failure-AGENT-LOOP-BUDGET` 和 `Failure-AGENT-UNSAFE-SIDE-EFFECT`，每行都有定义/排除边界、切片、频率/严重性、修复/owner、生产/回归 `D-*` 与 `E-*`。任意未授权工具、危险参数、循环或重复副作用都阻断，最终自然语言回答不参与抵消。
  - 场景三：示例明确拒绝“平均准确率 90% 即可发布”，将账户越权列为 0 容忍人工复核，将计费事实/引用、一般帮助/语言/长上下文拆为独立 Gate，并要求 LLM judge 的匿名候选、随机反转顺序/位置、长度控制、同源自偏隔离和人工金标校准。灰度中的脱敏升级、投诉、拒答和成功对照须去重、标注、审核和冻结为下一 dataset version。
- 受跟踪证据与验证方式：`ai-app-eval-builder/SKILL.md` 的“核心原则”“工作流”“数据集、代表性与泄漏”“Grader、rubric 与校准”“失败分类与处置”“RAG、Agent 与运行指标”“门禁、版本与闭环”“输出契约”“质量门槛”；`references/templates.md` 的评测卡、数据集、RAG/Agent、grader/校准、`Failure-*`、`E-*`/Gate/回流模板；`references/checklists.md` 的数据、偏差、失败处置、分层、版本和闭环检查；`references/examples.md` 的三个 V1/V2 场景与 RAG/Agent `Failure-*` 示例；`references/usage-guide.zh.md` 与 README/中文目录的正式导航。
- 验证缺口与修正：第二轮集合断言只比较 `G-*` 编号，没有读取 grader 第四列的 failure label，也没有证明每个 label 对应正确的稳定 Failure 代码与定义；把 `invalid_argument` 偷换成未映射标签仍会错误通过。第三轮脚本在固定 `a89635d` 快照中按 `G-11` 至 `G-14` 连接 grader 与 Failure 台账，逐项精确比较 failure label、稳定代码和完整定义；再对临时副本注入 `unmapped_label`，要求同一断言失败且固定快照保持洁净。脚本还断言 Gate-11 覆盖四个高风险 label，任一失败即阻断，硬门禁不得被平均分抵消。quick_validate、章节、占位符、规则、场景和导航仍只读取 detached worktree，报告内容仍由 `git show` 读取，`trap` 精确清理临时 worktree。
- 静态检查记录：固定基线为 `6924337e018d83845baf994c379e2eea28360fa8`，初始 Skill 提交为 `01a176deca7cd40b4651d6bff1aa77534e5a420f`，初始验证提交为 `1f69d2778fb9c99fc85a02ff2b5663e880e4ffa3`，`Failure-*` 内容修复提交为 `a655906821e01852345a4533646821aef4c5a65e`，固定快照验证提交为 `e446300737334f95302dae4cdba5d71a00d3702a`，完整 Agent 映射提交为 `a89635db47e64cb990bf0aa227eddb72e69b6348`（`Complete agent eval failure mappings`）。这些目标均为脚本中的固定完整 SHA；脚本不读取或推导当前 `HEAD`。

```bash
set -e
printf 'cwd=%s\n' "$PWD"
printf 'executed_at=%s\n' "$(date '+%Y-%m-%d %H:%M:%S %z')"
base_commit='6924337e018d83845baf994c379e2eea28360fa8'
skill_commit='01a176deca7cd40b4651d6bff1aa77534e5a420f'
validation_commit='1f69d2778fb9c99fc85a02ff2b5663e880e4ffa3'
taxonomy_commit='a655906821e01852345a4533646821aef4c5a65e'
snapshot_validation_commit='e446300737334f95302dae4cdba5d71a00d3702a'
mapping_commit='a89635db47e64cb990bf0aa227eddb72e69b6348'
repo_root=$(git rev-parse --show-toplevel)
temp_root=$(mktemp -d "${TMPDIR:-/tmp}/ai-app-eval-pinned.XXXXXX")
skill_tree="$temp_root/skill"
mapping_tree="$temp_root/mapping"
cleanup() {
  git -C "$repo_root" worktree remove --force "$skill_tree" >/dev/null 2>&1 || true
  git -C "$repo_root" worktree remove --force "$mapping_tree" >/dev/null 2>&1 || true
  rm -rf "$temp_root"
}
trap cleanup EXIT INT TERM
for commit in "$base_commit" "$skill_commit" "$validation_commit" "$taxonomy_commit" "$snapshot_validation_commit" "$mapping_commit"; do
  git -C "$repo_root" cat-file -e "${commit}^{commit}"
done
printf 'pinned-skill=%s pinned-report=%s pinned-mapping=%s\n' "$skill_commit" "$snapshot_validation_commit" "$mapping_commit"
git -C "$repo_root" worktree add --detach "$skill_tree" "$skill_commit" >/dev/null
git -C "$repo_root" worktree add --detach "$mapping_tree" "$mapping_commit" >/dev/null
PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill_tree/ai-app-eval-builder"
expected_headings='中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料'
actual_headings=$(rg '^## ' "$skill_tree/ai-app-eval-builder/SKILL.md" | sed 's/^## //' | tr '\n' '|' | sed 's/|$//')
test "$actual_headings" = "$expected_headings"
printf 'PASS headings=%s\n' "$actual_headings"
test -f "$skill_tree/ai-app-eval-builder/references/usage-guide.zh.md"
printf 'PASS usage-guide\n'
placeholder_pattern='TBD|TODO|FIXME|待办占位|未决占位|补充相关内容|在此填写|示例内容'
if rg -n "$placeholder_pattern" "$skill_tree/ai-app-eval-builder"; then
  printf 'FAIL placeholder scan\n'
  exit 1
fi
printf 'PASS placeholder-scan snapshot=%s\n' "$skill_commit"
for heading in '场景一：RAG 问答评测' '场景二：Agent 工具调用评测' '场景三：只要求用准确率评价聊天助手'; do
  rg -q "^## $heading$" "$skill_tree/ai-app-eval-builder/references/examples.md"
  printf 'PASS scenario=%s\n' "$heading"
done
for pattern in '拆能力、风险与切片' '黄金/生产失败/困难/对抗' '近重复.*泄漏' '确定性检查' '顺序、自偏、长度和位置偏差' 'RAG 必须将检索与答案分层' 'Agent 必须保存可审查轨迹' '总体平均不得覆盖' 'baseline/candidate/dataset/grader 版本' '线上信号只在脱敏、去重、标注和版本化后回流'; do
  rg -q "$pattern" "$skill_tree/ai-app-eval-builder"
done
printf 'PASS rules=capability-risk,dataset-leakage,deterministic-rubric-calibration,judge-bias,RAG,Agent,slices,cost-latency-stability,versions,offline-online\n'
rg -q '^| `ai-app-eval-builder` | AI 应用评测设计器 |.*离线数据集和线上失败回流.*' "$skill_tree/README.md"
rg -q '^| `ai-app-eval-builder` | AI 应用评测设计器 |.*离线数据集和线上失败回流.*' "$skill_tree/docs/skill-catalog.zh.md"
printf 'PASS navigation snapshot=%s\n' "$skill_commit"
expected_skill_files='README.md
ai-app-eval-builder/SKILL.md
ai-app-eval-builder/agents/openai.yaml
ai-app-eval-builder/references/checklists.md
ai-app-eval-builder/references/examples.md
ai-app-eval-builder/references/templates.md
ai-app-eval-builder/references/usage-guide.zh.md
docs/skill-catalog.zh.md'
actual_skill_files=$(git -C "$repo_root" diff --name-only "$base_commit" "$skill_commit")
test "$actual_skill_files" = "$expected_skill_files"
git -C "$repo_root" diff --check "$base_commit" "$skill_commit"
printf 'PASS pinned-skill-range-files=8 diff-check=%s..%s\n' "$base_commit" "$skill_commit"
validation_report=$(git -C "$repo_root" show "${snapshot_validation_commit}:docs/validation/skill-v2-validation-report.md")
section=$(printf '%s\n' "$validation_report" | awk '/^### `ai-app-eval-builder`$/{on=1; next} /^## 发布、沟通与仓库治理$/{on=0} on {print}')
for pattern in '原始请求' 'V1 缺口' 'V2 改进' '场景复测' '受跟踪证据与验证方式' '验证缺口与修正' '静态检查记录' '结论与限制'; do
  printf '%s\n' "$section" | rg -q "$pattern"
done
expected_validation_files='docs/validation/skill-v2-validation-report.md'
actual_validation_files=$(git -C "$repo_root" diff --name-only "$skill_commit" "$validation_commit")
test "$actual_validation_files" = "$expected_validation_files"
git -C "$repo_root" diff --check "$skill_commit" "$validation_commit"
actual_snapshot_validation_files=$(git -C "$repo_root" diff --name-only "$taxonomy_commit" "$snapshot_validation_commit")
test "$actual_snapshot_validation_files" = "$expected_validation_files"
git -C "$repo_root" diff --check "$validation_commit" "$taxonomy_commit"
git -C "$repo_root" diff --check "$taxonomy_commit" "$snapshot_validation_commit"
printf 'PASS pinned-report=git-show sections=V1,V2,scenarios,evidence,fix,limits report-ranges=1 diff-checks=%s..%s..%s..%s\n' "$skill_commit" "$validation_commit" "$taxonomy_commit" "$snapshot_validation_commit"
PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$mapping_tree/ai-app-eval-builder"
rg -q 'Failure-\*.*失败分类与处置台账' "$mapping_tree/ai-app-eval-builder/SKILL.md"
rg -q '稳定失败代码.*定义.*RAG/Agent/其他层.*受影响切片.*频率/严重性.*可能修复/责任 owner.*关联生产样本.*回归 case' "$mapping_tree/ai-app-eval-builder/SKILL.md"
rg -q '^| Failure-ID/稳定失败代码 | 定义与纳入/排除边界 | 层：RAG/Agent/其他 | 受影响切片 | 频率/严重性 | 可能修复/责任 owner | 关联生产样本 D-\* | 回归 case D-\* | 关联 G-\*/E-\* |$' "$mapping_tree/ai-app-eval-builder/references/templates.md"
rg -q '每个 `G-\*` fail label 映射一个 `Failure-\*`.*每条失败 `E-\*` case/trace 回链同一代码' "$mapping_tree/ai-app-eval-builder/references/checklists.md"
if rg -n "$placeholder_pattern" "$mapping_tree/ai-app-eval-builder"; then
  printf 'FAIL mapping placeholder scan\n'
  exit 1
fi
agent_section=$(awk '/^## 场景二：Agent 工具调用评测$/{on=1} /^## 场景三：只要求用准确率评价聊天助手$/{on=0} on {print}' "$mapping_tree/ai-app-eval-builder/references/examples.md")
grader_count=$(printf '%s\n' "$agent_section" | rg -c '^\| G-(11|12|13|14) ')
failure_rows=$(printf '%s\n' "$agent_section" | rg -c '^\| Failure-AGENT-')
test "$grader_count" -eq "$failure_rows"
test "$grader_count" -eq 4
unique_failure_ids=$(printf '%s\n' "$agent_section" | awk -F'|' '/^\| Failure-AGENT-/ {gsub(/^ +| +$/, "", $2); print $2}' | sort -u | rg -c '^Failure-AGENT-')
test "$unique_failure_ids" -eq "$failure_rows"
printf '%s\n' "$agent_section" | awk -F'|' '/^\| Failure-AGENT-/ {for (i=2; i<=7; i++) {v=$i; gsub(/^ +| +$/, "", v); if (v=="") exit 1}}'
complete_link_rows=$(printf '%s\n' "$agent_section" | rg -c '^\| Failure-AGENT-.*\| 生产 D-[0-9]+ / 回归 D-[0-9]+ \| G-[0-9]+ / E-[0-9]+:D-[0-9]+ \|$')
test "$complete_link_rows" -eq "$failure_rows"
expected_agent_contract='G-11|unauthorized_tool|Failure-AGENT-UNAUTHORIZED-TOOL|无权限角色调用禁止工具；排除被策略明确允许的草稿调用；Agent 权限
G-12|invalid_argument|Failure-AGENT-INVALID-ARGUMENT|工具参数违反 schema，或订单、金额、币种、幂等键不一致；排除 provider 超时；Agent 参数
G-13|loop_or_budget|Failure-AGENT-LOOP-BUDGET|超过最大步数、重试预算或无终止理由；排除预算内一次重试；Agent 循环
G-14|unsafe_side_effect|Failure-AGENT-UNSAFE-SIDE-EFFECT|产生重复或未批准的外部退款，或失败后缺少必需补偿；排除未提交的草稿；Agent 副作用'
build_agent_contract() {
  contract_file=$1
  contract_section=$(awk '/^## 场景二：Agent 工具调用评测$/{on=1} /^## 场景三：只要求用准确率评价聊天助手$/{on=0} on {print}' "$contract_file")
  for grader_id in G-11 G-12 G-13 G-14; do
    failure_label=$(printf '%s\n' "$contract_section" | awk -F'|' -v target="$grader_id" '
      function trim(value) {gsub(/^ +| +$/, "", value); return value}
      /^\| G-[0-9]+ / && trim($2) == target {print trim($4); matches++}
      END {if (matches != 1) exit 1}
    ') || return 1
    failure_record=$(printf '%s\n' "$contract_section" | awk -F'|' -v target="$grader_id" '
      function trim(value) {gsub(/^ +| +$/, "", value); return value}
      /^\| Failure-AGENT-/ {
        link=trim($7)
        if (link ~ ("^" target " / E-[0-9]+:D-[0-9]+$")) {
          print trim($2) "|" trim($3)
          matches++
        }
      }
      END {if (matches != 1) exit 1}
    ') || return 1
    printf '%s|%s|%s\n' "$grader_id" "$failure_label" "$failure_record"
  done
}
assert_agent_contract() {
  local asserted_agent_contract
  asserted_agent_contract=$(build_agent_contract "$1") || return 1
  test "$asserted_agent_contract" = "$expected_agent_contract"
}
assert_agent_contract "$mapping_tree/ai-app-eval-builder/references/examples.md"
actual_agent_contract=$(build_agent_contract "$mapping_tree/ai-app-eval-builder/references/examples.md")
printf 'PASS agent-label-code-definition-map=%s\n' "$(printf '%s\n' "$actual_agent_contract" | cut -d'|' -f1-3 | tr '\n' ',')"
mutated_examples="$temp_root/examples-unmapped-label.md"
awk '/^\| G-12 / {sub(/\| invalid_argument \|$/, "| unmapped_label |")} {print}' "$mapping_tree/ai-app-eval-builder/references/examples.md" > "$mutated_examples"
rg -q 'G-12 .* unmapped_label' "$mutated_examples"
if assert_agent_contract "$mutated_examples"; then
  printf 'FAIL negative label self-test accepted unmapped_label\n'
  exit 1
fi
git -C "$mapping_tree" diff --quiet
test -z "$(git -C "$mapping_tree" status --short)"
printf 'PASS negative-label-self-test=unmapped_label-rejected snapshot-unchanged=yes\n'
gate_line=$(printf '%s\n' "$agent_section" | rg '^- Gate-11：')
test "$(printf '%s\n' "$gate_line" | rg -c '^- Gate-11：')" -eq 1
printf '%s\n' "$gate_line" | rg -q 'R-01/R-02 的 G-11 至 G-14 任一失败即阻断'
printf '%s\n' "$gate_line" | rg -q '最终自然语言回答不参与抵消'
rg -q '硬门禁.*任一失败即阻断，不用平均分抵消' "$mapping_tree/ai-app-eval-builder/SKILL.md"
gate_failure_labels=$(printf '%s\n' "$actual_agent_contract" | cut -d'|' -f2 | tr '\n' ',' | sed 's/,$//')
test "$gate_failure_labels" = 'unauthorized_tool,invalid_argument,loop_or_budget,unsafe_side_effect'
printf 'PASS Gate-11 labels=%s any-failure-blocks=yes average-score-offset=no\n' "$gate_failure_labels"
expected_taxonomy_files='ai-app-eval-builder/SKILL.md
ai-app-eval-builder/references/checklists.md
ai-app-eval-builder/references/examples.md
ai-app-eval-builder/references/templates.md'
actual_taxonomy_files=$(git -C "$repo_root" diff --name-only "$validation_commit" "$taxonomy_commit")
test "$actual_taxonomy_files" = "$expected_taxonomy_files"
expected_mapping_files='ai-app-eval-builder/references/examples.md'
actual_mapping_files=$(git -C "$repo_root" diff --name-only "$snapshot_validation_commit" "$mapping_commit")
test "$actual_mapping_files" = "$expected_mapping_files"
git -C "$repo_root" diff --check "$snapshot_validation_commit" "$mapping_commit"
printf 'PASS pinned-mapping=%s files=1 diff-check=%s..%s\n' "$mapping_commit" "$snapshot_validation_commit" "$mapping_commit"
printf 'summary=pinned detached snapshots passed quick_validate, original rules/scenarios/navigation, exact Agent G/label/Failure-code/definition mapping, negative mutation rejection, Gate-11 blocking/no-average-offset semantics, fixed file sets, git-show report checks, SHA diff checks, and trap cleanup\n'
```

- 实际复跑记录：2026-07-26 17:09:12 +0800 从后于固定内容快照的 runner `2ca5b9010d51aa43fce1962fa738b4ad642f2644` 执行上方完整脚本，整段退出码为 `0`。所有被验证内容来自固定 `01a176d`/`a89635d` detached worktree 或固定 `e446300` 的 `git show`，当前工作树文件不作为证据；`unmapped_label` 只写入专用临时副本，固定快照保持洁净，脚本结束后没有 `ai-app-eval-pinned.*` worktree 或目录。

```text
cwd=/Users/mac/Desktop/个人skill/ai-product-dev-skills/.worktrees/skill-library-v2
executed_at=2026-07-26 17:09:12 +0800
runner-commit=2ca5b9010d51aa43fce1962fa738b4ad642f2644
pinned-skill=01a176deca7cd40b4651d6bff1aa77534e5a420f pinned-report=e446300737334f95302dae4cdba5d71a00d3702a pinned-mapping=a89635db47e64cb990bf0aa227eddb72e69b6348
Preparing worktree (detached HEAD 01a176d)
Preparing worktree (detached HEAD a89635d)
Skill is valid!
PASS headings=中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料
PASS usage-guide
PASS placeholder-scan snapshot=01a176deca7cd40b4651d6bff1aa77534e5a420f
PASS scenario=场景一：RAG 问答评测
PASS scenario=场景二：Agent 工具调用评测
PASS scenario=场景三：只要求用准确率评价聊天助手
PASS rules=capability-risk,dataset-leakage,deterministic-rubric-calibration,judge-bias,RAG,Agent,slices,cost-latency-stability,versions,offline-online
PASS navigation snapshot=01a176deca7cd40b4651d6bff1aa77534e5a420f
PASS pinned-skill-range-files=8 diff-check=6924337e018d83845baf994c379e2eea28360fa8..01a176deca7cd40b4651d6bff1aa77534e5a420f
PASS pinned-report=git-show sections=V1,V2,scenarios,evidence,fix,limits report-ranges=1 diff-checks=01a176deca7cd40b4651d6bff1aa77534e5a420f..1f69d2778fb9c99fc85a02ff2b5663e880e4ffa3..a655906821e01852345a4533646821aef4c5a65e..e446300737334f95302dae4cdba5d71a00d3702a
Skill is valid!
PASS agent-label-code-definition-map=G-11|unauthorized_tool|Failure-AGENT-UNAUTHORIZED-TOOL,G-12|invalid_argument|Failure-AGENT-INVALID-ARGUMENT,G-13|loop_or_budget|Failure-AGENT-LOOP-BUDGET,G-14|unsafe_side_effect|Failure-AGENT-UNSAFE-SIDE-EFFECT,
PASS negative-label-self-test=unmapped_label-rejected snapshot-unchanged=yes
PASS Gate-11 labels=unauthorized_tool,invalid_argument,loop_or_budget,unsafe_side_effect any-failure-blocks=yes average-score-offset=no
PASS pinned-mapping=a89635db47e64cb990bf0aa227eddb72e69b6348 files=1 diff-check=e446300737334f95302dae4cdba5d71a00d3702a..a89635db47e64cb990bf0aa227eddb72e69b6348
summary=pinned detached snapshots passed quick_validate, original rules/scenarios/navigation, exact Agent G/label/Failure-code/definition mapping, negative mutation rejection, Gate-11 blocking/no-average-offset semantics, fixed file sets, git-show report checks, SHA diff checks, and trap cleanup
```
- 结论与限制：通过（文档静态验证）。三个场景的规则、字段和导航均由受跟踪文档与静态断言支持；没有外部 AI 应用、真实用户样本、生产权限、人工标注、模型运行、负载或发布系统，因此不能声称任何真实 baseline/candidate、成本、延迟、稳定性、judge 校准或线上结果已通过。
- 剩余风险：真实分布可能漂移，失败样本可能受隐私/许可限制，语义去重与代表性判断仍需领域人工复核；LLM judge 会随模型和 prompt 漂移，生产成本、延迟、工具副作用和回滚也只能由实际 `E-*`、Gate、灰度监控与回流流程证明。

## 发布、沟通与仓库治理

### `launch-readiness-checklist`

- 升级前场景审计（仅审阅固定 `489700f` 的受跟踪文档；未访问业务仓库、生产监控、迁移环境或发布系统）：V1 有基础发布领域、风险和回滚提示，但没有让发布类型/风险裁剪、逐项 owner/截止/证据/阻断、AI 风险、灰度、演练、前向兼容、权限与观察退出成为不可省略的可审查字段。以下为文档 RED 基线，不是任一真实发布的结论。
- 场景一：普通 Web 功能上线。
  - 原始请求：`下周发布团队权限管理 Web 功能。产品和 QA 都看过了，帮我出一份 checklist。`
  - V1 缺口：领域表可把“产品和 QA 看过”写成 Ready，没有要求单一 owner、截止、测试/链接/命令及阻断级别；权限迁移、文案、埋点、仪表盘、FAQ、风控和决策权限也不必逐项可复核。
- 场景二：高风险 AI 功能灰度。
  - 原始请求：`把能提交退款的 AI 客服助手从内部测试灰度到 10%，模型评测平均分不错。`
  - V1 缺口：虽然提到 AI eval 和人工 review，但没有将真实 eval、内容质量、提示注入、越权工具/副作用、人工兜底、flag 停流和阶段扩大条件分成硬门禁；一次错误退款可能被平均分掩盖。
- 场景三：截止时间已到但回滚方案缺失。
  - 原始请求：`今晚必须发布订单表迁移。功能测过了，但还没有回滚演练；能不能先 go，出事再说？`
  - V1 缺口：V1 要求 rollback plan，却不要求触发器、执行/验证/沟通 owner、有序步骤、演练证据或数据前向兼容；截止压力可能被误写成带缓解的 go。
- V2 改进：`SKILL.md` 以 13 个中文章节建立风险/发布类型裁剪、`R-*` 就绪账本、事实与缺口边界、功能/QA/迁移/文案/埋点/监控/性能/支持/FAQ/隐私安全/风控/依赖覆盖，及证据、owner、截止和阻断规则。AI 发布单列真实 eval、内容质量、提示注入、越权/副作用和人工接管；feature flag、阶段灰度、回滚触发器/步骤/owner/演练/前向兼容、具名 go/no-go/例外权限和发布后观察/退出条件均为输出契约。中文指南、模板、清单和示例保持同一字段，README 与中文索引同步为发布治理入口。
- 场景复测（文档级；没有执行外部测试、迁移、演练、发布或伪造生产证据）：
  - 场景一：`examples.md` 将“看过了”保留为 `GAP-*`，并在 `R-01` 至 `R-07` 中要求单一 owner、截止、CI/测试/仪表盘等证据和阻断级别。范围、QA、迁移、文案、埋点、支持/FAQ 的未知项不会变成通过；结论为 `No-go` 直到关键证据和具名权限人到位。
  - 场景二：`AI-01` 至 `AI-04` 分别覆盖真实 `E-*`/Gate、提示注入/外泄、越权/金额/幂等副作用和人工兜底；每项都有一个可执行 owner、`进入 1% 灰度前` 的事件截止、缺口证据和 Blocker 级别。`refund_agent_submit` 的灰度从内部到 1%/10% 都需进入、观察、暂停和扩大条件；平均分不能抵消任一 Blocker，因此缺证据时为 `No-go`。
  - 场景三：`R-03` 和 `R-10` 将迁移兼容和未演练回滚列为 Blocker，并分别补充单一 owner、事件截止和 `GAP-*` 证据。回滚表将决策、执行、验证和沟通拆给发布经理、发布工程 owner、数据质量 owner 和客户沟通 owner，不再使用斜杠或多人合并值；模板与清单同步相同契约。仅在具名权限人限定为不执行迁移的可逆发布、写明失效期/阈值/关闭条件时才可能是 `Conditional go`。
- 受跟踪证据与验证方式：`launch-readiness-checklist/SKILL.md` 的“核心原则”“工作流”“风险与发布类型裁剪”“证据、状态与阻断”“数据、依赖与回滚”“AI、灰度与观察”“输出契约”“质量门槛”；模板的 `R-*`、AI、Blocker、flag、rollback、decision/observation 表；清单的证据/领域/AI/回滚/判定门禁；三组 V1/V2 示例；`usage-guide.zh.md` 与 README/中文目录导航。
- 静态检查记录：固定基线为 `489700f`，初始 V2 内容提交为 `c05e6b774339e5731b6bd45143b470ce03f80558`，固定报告 snapshot 为 `a81404b467e8c9a986f7356f8624473f000bb433`，所有权修复内容提交为 `ef58764cb8d1faba0d727fe6a92d6e8f0726dd77`（`Complete launch ownership examples`）。`report_commit` 是脚本内常量并再次断言等于完整 SHA，不接受位置参数、环境变量或当前分支替换。验证只从固定 `ef58764` detached worktree 读取内容，以 `git show a81404b:docs/validation/skill-v2-validation-report.md` 读取报告 snapshot；断言章节、占位符、三场景、11 条 Blocker/Launch risk 的单一 owner/事件截止/证据、回滚四类单值 owner、规则、导航和精确文件集合，并执行固定范围 diff checks。验证器不读取或推导 `HEAD`。

```bash
set -e
repo_root=$(pwd)
base_commit=489700f
initial_content_commit=c05e6b774339e5731b6bd45143b470ce03f80558
report_commit=a81404b467e8c9a986f7356f8624473f000bb433
content_commit=ef58764cb8d1faba0d727fe6a92d6e8f0726dd77
temp_root=$(mktemp -d /tmp/launch-readiness-pinned.XXXXXX)
skill_tree="$temp_root/content"
cleanup() { git -C "$repo_root" worktree remove --force "$skill_tree" 2>/dev/null || true; rm -rf "$temp_root"; }
trap cleanup EXIT
test "$report_commit" = 'a81404b467e8c9a986f7356f8624473f000bb433'
git -C "$repo_root" cat-file -e "${base_commit}^{commit}"
git -C "$repo_root" cat-file -e "${initial_content_commit}^{commit}"
git -C "$repo_root" cat-file -e "${content_commit}^{commit}"
git -C "$repo_root" cat-file -e "${report_commit}^{commit}"
git -C "$repo_root" worktree add --detach "$skill_tree" "$content_commit"
PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill_tree/launch-readiness-checklist"
test "$(rg '^## ' "$skill_tree/launch-readiness-checklist/SKILL.md" | sed 's/^## //' | tr '\n' '|' | sed 's/|$//')" = '中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料'
test -f "$skill_tree/launch-readiness-checklist/references/usage-guide.zh.md"
! rg -n 'TBD|TODO|FIXME|待办占位|未决占位|补充相关内容|在此填写|示例内容' "$skill_tree/launch-readiness-checklist"
for heading in '场景一：普通 Web 功能上线' '场景二：高风险 AI 功能灰度' '场景三：截止时间已到但回滚方案缺失'; do rg -q "^## $heading$" "$skill_tree/launch-readiness-checklist/references/examples.md"; done
for rule in 'owner、截止、证据链接或可执行命令、阻断级别' '“有人看过”不是证据' '提示注入、数据外泄、越权工具调用' '人工兜底' 'feature flag、目标规则与灰度控制' '回滚触发器' '数据前向兼容' 'go/no-go 权限人' '发布后观察'; do rg -q "$rule" "$skill_tree/launch-readiness-checklist"; done
examples_file="$skill_tree/launch-readiness-checklist/references/examples.md"
rg -q '^\| AI-ID \| 风险 \| 证据 \| 状态 \| owner \| 截止 \| 失败动作 \| 阻断级别 \|$' "$examples_file"
rg -q '^\| R-ID \| 检查 \| 状态 \| owner \| 截止 \| 证据 \| 阻断级别 \| 下一动作 \|$' "$examples_file"
rg -q '^\| 触发器 \| 决策 owner \| 执行 owner \| 验证 owner \| 沟通 owner \| 截止 \|' "$examples_file"
awk -F'|' '
function trim(value) { gsub(/^ +| +$/, "", value); return value }
/^\| R-[0-9]+ / {
  owner=trim($5); due=trim($6); evidence=trim($7); level=trim($8)
  if (level == "Blocker" || level == "Launch risk") { checked++; if (owner == "" || owner ~ /\// || due == "" || due !~ /(前|后|时|日|月|年|T)/ || evidence == "") bad++ }
}
/^\| AI-[0-9]+ / {
  evidence=trim($4); owner=trim($6); due=trim($7); level=trim($9)
  if (level == "Blocker" || level == "Launch risk") { checked++; if (owner == "" || owner ~ /\// || due == "" || due !~ /(前|后|时|日|月|年|T)/ || evidence == "") bad++ }
}
END { if (checked != 11 || bad != 0) exit 1 }
' "$examples_file"
rollback_contract=$(awk -F'|' '/^\| 数据校验失败或订单写入错误率超已批准阈值 / { for (i=3; i<=7; i++) { value=$i; gsub(/^ +| +$/, "", value); printf "%s%s", value, (i<7 ? "|" : "\n") } }' "$examples_file")
test "$rollback_contract" = '发布经理|发布工程 owner|数据质量 owner|客户沟通 owner|迁移窗口开始前'
rg -q '^\| 触发器 ID \| 可观测信号/阈值 \| 决策 owner \| 执行 owner \| 验证 owner \| 沟通 owner \| 截止 \|' "$skill_tree/launch-readiness-checklist/references/templates.md"
rg -q '决策、执行、验证和沟通分别由单一 owner 负责' "$skill_tree/launch-readiness-checklist/references/checklists.md"
rg -q '^| `launch-readiness-checklist` | 上线就绪与发布决策 |.*R-\*.*就绪账本.*' "$skill_tree/README.md"
rg -q '^| `launch-readiness-checklist` | 上线就绪与发布决策 |.*R-\*.*就绪账本.*' "$skill_tree/docs/skill-catalog.zh.md"
test "$(git -C "$repo_root" diff --name-only "$base_commit" "$initial_content_commit")" = "$(printf 'README.md\ndocs/skill-catalog.zh.md\nlaunch-readiness-checklist/SKILL.md\nlaunch-readiness-checklist/agents/openai.yaml\nlaunch-readiness-checklist/references/checklists.md\nlaunch-readiness-checklist/references/examples.md\nlaunch-readiness-checklist/references/templates.md\nlaunch-readiness-checklist/references/usage-guide.zh.md')"
test "$(git -C "$repo_root" diff --name-only "$report_commit" "$content_commit")" = "$(printf 'launch-readiness-checklist/references/checklists.md\nlaunch-readiness-checklist/references/examples.md\nlaunch-readiness-checklist/references/templates.md')"
git -C "$repo_root" diff --check "$base_commit" "$initial_content_commit"
git -C "$repo_root" diff --check "$report_commit" "$content_commit"
report=$(git -C "$repo_root" show "${report_commit}:docs/validation/skill-v2-validation-report.md")
section=$(printf '%s\n' "$report" | awk '/^### `launch-readiness-checklist`$/{on=1; next} /^### `stakeholder-update-writer`$/{on=0} on {print}')
for field in '原始请求' 'V1 缺口' 'V2 改进' '场景复测' '受跟踪证据与验证方式' '静态检查记录' '结论与限制' '剩余风险'; do printf '%s\n' "$section" | rg -q "$field"; done
test "$(git -C "$repo_root" diff --name-only "$initial_content_commit" "$report_commit")" = 'docs/validation/skill-v2-validation-report.md'
git -C "$repo_root" diff --check "$initial_content_commit" "$report_commit"
git -C "$repo_root" worktree remove --force "$skill_tree"
rm -rf "$temp_root"
trap - EXIT
test ! -e "$skill_tree"
! git -C "$repo_root" worktree list | rg -q 'launch-readiness-pinned\.'
```

- 实际复跑记录：所有权修复内容已从固定 `ef58764` detached worktree 完成 `quick_validate.py`、11 条 blocker/风险完整性、回滚 owner 单值、精确三文件范围、diff check 和清理验证；固定 `a81404b` 报告由 `git show` 读取。独立验证提交后的完整输出和固定验证提交范围记录在 `.superpowers/sdd/task-19-report.md`（不跟踪）。
- 结论与限制：通过（文档静态验证）。三个场景均有结构化输入边界、证据/owner/blocker、AI/灰度/回滚和决策规则；没有业务仓库、真实 CI、迁移环境、生产用户、监控、支持队列或审批系统，不能把本节当作任何真实发布、演练、阈值或 go/no-go 的证明。
- 剩余风险：真实依赖、数据量、性能、组织响应、权限和用户分布可能改变结论；阈值、例外和人工兜底仍需实际负责人批准并在受控环境中演练，发布后必须按真实观测执行暂停、回滚或扩大。

### `stakeholder-update-writer`

- 原始请求：`把本周进展、风险和决策请求写给管理层；跨团队升级一个依赖风险；输入只有零散笔记时要求“包装成进展顺利”。`
- V1 缺口：V1 只有英文概览与宽泛输出清单，未把受众/渠道/决策目的、事实来源、RAG 判定、事实与判断分离、业务/用户影响、风险升级、决策日志、单一 owner/截止和敏感信息权限设为不可省略字段。它也没有明确拒绝把延期、Blocker、坏指标或未知改写为“顺利”，因此老板周报可能把活动当成果，跨团队风险可能没有决定者和日期，零散笔记可能被伪装成事实。
- V2 改进：`SKILL.md` 以 13 个中文章节建立沟通卡、`F-*`/`I-*`/`P-*`/`A-*`/`GAP-*` 事实账本、来源/观察日期/置信度、绿黄红/待确认的明确规则，以及将活动转为业务/用户影响的边界。风险升级强制触发、影响、缓解、单一 owner、截止和请求；决策日志强制选择、理由、决定者、日期；行动项强制一个 accountable owner 和截止。敏感信息按 need-to-know 与渠道权限处理；遇到粉饰要求时拒绝改写事实，但可提供更清晰、分层或脱敏的真实版本。中文指南、模板、清单、三场景示例、`openai.yaml`、README 和中文目录采用同一契约。
- 场景复测（文档级；没有发送真实邮件/Slack、访问业务数据、验证实际权限或伪造生产证据）：
  - 场景一：`examples.md` 的 VP 周报先给邮件受众、决策目的、黄色规则和 `F-03` 法务依赖，再将 `F-01` 开发完成、`F-02` 实验变化、`I-01` 解释与 `P-01` 预测拆开。它把“是否保留周一全量窗口”写成有 VP、日期与完成证据的 `A-01`，不以开发完成掩盖法务风险。
  - 场景二：跨团队 Slack 升级按红色规则说明启动关键路径的 Blocker 与决策窗口缺少 owner/日期，保留预算损失为 `GAP-01` 而不编造金额。`R-01` 写明 2026-07-28 触发、归因影响、映射/汇总替代、数据负责人、截止、双方决定与暂停渠道动作。
  - 场景三：面对“包装成进展顺利”，示例先明确拒绝；原始支付失败/投诉笔记因来源、触发、范围和权限不全被记为 `GAP-01`/`GAP-02` 与低置信度 `F-01` 候选，当前状态为待确认。受限消息只向支付值班、客服和事件协调必要受众提示潜在影响与验证动作；只有工单/事件和监控确认失败率达到已批准阈值，或确认支付关键路径不可用时才转红。
- 受跟踪证据与验证方式：`stakeholder-update-writer/SKILL.md` 的“核心原则”“输入要求”“信息不足时的处理”“工作流”“专业判断规则”“输出契约”“质量门槛”“常见失败与修正”；`references/templates.md` 的沟通卡、事实账本、周报、风险、决策、行动和粉饰回应；`references/checklists.md` 的 RAG、事实边界、权限与判定；`references/examples.md` 的三个 V1/V2 场景；`references/usage-guide.zh.md` 与 README/中文目录的导航。
- 静态检查记录：固定基线为 `bbd9a9e17bfb0aa607740e8930eb5acdf208c604`，V2 内容提交为 `ba7159f4f1b5d9e4a623e17f931c74975ea7f55e`（`Upgrade stakeholder update skill to V2`），验证报告快照为 `442ee7c19588252fdf4dc6682e1b289f7de0d1c2`（`Record stakeholder update V2 validation`）。三个 SHA 均是脚本常量；脚本不读取、不推导也不接受替换当前 `HEAD`。内容只从明确提交的 detached worktree 读取，报告只用 `git show` 读取固定报告快照；断言章节、占位符、三场景、RAG 规则、事实/判断分离、风险/决策/owner/日期、敏感信息、导航、精确文件集合和 diff checks，最后清理临时 worktree。

```bash
set -e
repo_root=$(pwd)
base_commit='bbd9a9e17bfb0aa607740e8930eb5acdf208c604'
content_commit='ba7159f4f1b5d9e4a623e17f931c74975ea7f55e'
report_commit='442ee7c19588252fdf4dc6682e1b289f7de0d1c2'
temp_root=$(mktemp -d /tmp/stakeholder-update-pinned.XXXXXX)
skill_tree="$temp_root/content"
cleanup() {
  git -C "$repo_root" worktree remove --force "$skill_tree" >/dev/null 2>&1 || true
  rm -rf "$temp_root"
}
trap cleanup EXIT INT TERM
test "$base_commit" = 'bbd9a9e17bfb0aa607740e8930eb5acdf208c604'
test "$content_commit" = 'ba7159f4f1b5d9e4a623e17f931c74975ea7f55e'
test "$report_commit" = '442ee7c19588252fdf4dc6682e1b289f7de0d1c2'
for commit in "$base_commit" "$content_commit" "$report_commit"; do
  git -C "$repo_root" cat-file -e "${commit}^{commit}"
done
git -C "$repo_root" worktree add --detach "$skill_tree" "$content_commit" >/dev/null
PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill_tree/stakeholder-update-writer"
expected_headings='中文简介|使用背景|核心原则|适用场景|不适用场景|输入要求|信息不足时的处理|工作流|专业判断规则|输出契约|质量门槛|常见失败与修正|参考资料'
actual_headings=$(rg '^## ' "$skill_tree/stakeholder-update-writer/SKILL.md" | sed 's/^## //' | tr '\n' '|' | sed 's/|$//')
test "$actual_headings" = "$expected_headings"
test -f "$skill_tree/stakeholder-update-writer/references/usage-guide.zh.md"
! rg -n 'TBD|TODO|FIXME|待办占位|未决占位|补充相关内容|在此填写|示例内容' "$skill_tree/stakeholder-update-writer"
for heading in '场景一：给老板的周报' '场景二：跨团队风险升级' '场景三：零散笔记加粉饰要求'; do
  rg -q "^## $heading$" "$skill_tree/stakeholder-update-writer/references/examples.md"
done
for rule in '受众、渠道、决策目的' 'RAG 是规则结果，不是语气' '绿（Green）' '黄（Yellow）' '红（Red）' '状态待确认' '事实、解释、预测与请求' '来源和置信度' '触发器或早期信号' '选择、理由、决定者、日期' '单一 owner' '最小必要范围共享' '不能把已知延期、Blocker、坏指标或未确认信息改写成“进展顺利”'; do
  rg -q "$rule" "$skill_tree/stakeholder-update-writer"
done
templates="$skill_tree/stakeholder-update-writer/references/templates.md"
rg -Fq '| 类型 | ID | 内容 | 来源与观察日期 | 置信度 | 影响/前提 | 可共享范围 |' "$templates"
rg -Fq '| ID | 触发器/早期信号 | 业务/用户影响 | 缓解 | 单一 owner | 截止 | 升级对象与所需决定 | 状态 |' "$templates"
rg -Fq '| D-ID | 选择/待选项 | 理由与证据 | 决定者 | 日期 | 状态/复核点 |' "$templates"
rg -Fq '| A-ID | 动作与完成证据 | 单一 owner | 截止 | 依赖/协作方 |' "$templates"
examples="$skill_tree/stakeholder-update-writer/references/examples.md"
awk -F'|' '
function trim(value) { gsub(/^ +| +$/, "", value); return value }
/^\| R-[0-9]+ / {
  owner=trim($6); due=trim($7); checked++
  if (owner == "" || owner ~ /\// || due == "") bad++
}
END { if (checked != 3 || bad != 0) exit 1 }
' "$examples"
rg -q 'need-to-know' "$skill_tree/stakeholder-update-writer/SKILL.md"
rg -q '受限风险升级草稿' "$examples"
rg -q '^| `stakeholder-update-writer` | 干系人状态与风险汇报 |.*RAG/待确认.*事实/解释/预测/请求.*单一 owner/截止.*' "$skill_tree/README.md"
rg -q '^| `stakeholder-update-writer` | 干系人状态与风险汇报 |.*RAG/待确认.*F-\*.*I-\*.*P-\*.*A-\*.*GAP-\*.*单一 owner/截止.*' "$skill_tree/docs/skill-catalog.zh.md"
expected_content_files=$(printf 'README.md\ndocs/skill-catalog.zh.md\nstakeholder-update-writer/SKILL.md\nstakeholder-update-writer/agents/openai.yaml\nstakeholder-update-writer/references/checklists.md\nstakeholder-update-writer/references/examples.md\nstakeholder-update-writer/references/templates.md\nstakeholder-update-writer/references/usage-guide.zh.md')
test "$(git -C "$repo_root" diff --name-only "$base_commit" "$content_commit")" = "$expected_content_files"
git -C "$repo_root" diff --check "$base_commit" "$content_commit"
report=$(git -C "$repo_root" show "${report_commit}:docs/validation/skill-v2-validation-report.md")
section=$(printf '%s\n' "$report" | awk '/^### `stakeholder-update-writer`$/{on=1; next} /^### `skill-repo-release-verifier`$/{on=0} on {print}')
for field in '原始请求' 'V1 缺口' 'V2 改进' '场景复测' '受跟踪证据与验证方式' '静态检查记录' '结论与限制' '剩余风险'; do
  printf '%s\n' "$section" | rg -q "$field"
done
test "$(git -C "$repo_root" diff --name-only "$content_commit" "$report_commit")" = 'docs/validation/skill-v2-validation-report.md'
git -C "$repo_root" diff --check "$content_commit" "$report_commit"
git -C "$repo_root" worktree remove --force "$skill_tree" >/dev/null
rm -rf "$temp_root"
trap - EXIT INT TERM
test ! -e "$skill_tree"
! git -C "$repo_root" worktree list | rg -q 'stakeholder-update-pinned\.'
printf 'PASS pinned-base=%s content=%s report=%s\n' "$base_commit" "$content_commit" "$report_commit"
printf 'PASS headings, placeholders, scenarios, RAG, fact-separation, risk-decision-owner-date, sensitive-info, navigation, exact-files, diff-checks, detached-cleanup\n'
```

- 实际复跑记录：从后于固定内容与报告快照的 runner 执行上方脚本，整段退出码为 `0`。内容仅来自 `ba7159f4f1b5d9e4a623e17f931c74975ea7f55e` detached worktree；报告仅来自 `git show 442ee7c19588252fdf4dc6682e1b289f7de0d1c2:docs/validation/skill-v2-validation-report.md`；没有读取或推导 `HEAD`。临时 `stakeholder-update-pinned.*` worktree 和目录均已移除。

```text
Preparing worktree (detached HEAD ba7159f)
Skill is valid!
PASS pinned-base=bbd9a9e17bfb0aa607740e8930eb5acdf208c604 content=ba7159f4f1b5d9e4a623e17f931c74975ea7f55e report=442ee7c19588252fdf4dc6682e1b289f7de0d1c2
PASS headings, placeholders, scenarios, RAG, fact-separation, risk-decision-owner-date, sensitive-info, navigation, exact-files, diff-checks, detached-cleanup
```

#### P1 固定快照验证

- P1 修正：场景三不再把未定位来源、未确认范围/权限和低置信度 `F-01` 直接判为红色。当前只生成“待确认的受限风险升级”，拒绝粉饰与拒绝猜测同时成立；必要受众先执行工单、监控、投诉基线和权限验证，满足明确触发后才转红。
- 固定边界：基线与报告快照均固定为 `2752e7ccc7901d01d86fa6e8953f81d1c53f45a1`，P1 内容提交固定为 `2c3066819e4dc472040af719fbaaad36a643c8b4`。脚本不读取或推导当前 `HEAD`，也不接受参数替换这些 SHA；内容只从 P1 内容提交的 detached worktree 读取，报告只通过 `git show` 读取固定快照。

```bash
set -e
repo_root=$(pwd)
base_commit='2752e7ccc7901d01d86fa6e8953f81d1c53f45a1'
content_commit='2c3066819e4dc472040af719fbaaad36a643c8b4'
report_commit='2752e7ccc7901d01d86fa6e8953f81d1c53f45a1'
temp_root=$(mktemp -d /tmp/stakeholder-status-p1-pinned.XXXXXX)
content_tree="$temp_root/content"
cleanup() {
  git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null 2>&1 || true
  rm -rf "$temp_root"
}
trap cleanup EXIT INT TERM
test "$base_commit" = '2752e7ccc7901d01d86fa6e8953f81d1c53f45a1'
test "$content_commit" = '2c3066819e4dc472040af719fbaaad36a643c8b4'
test "$report_commit" = '2752e7ccc7901d01d86fa6e8953f81d1c53f45a1'
for commit in "$base_commit" "$content_commit" "$report_commit"; do
  git -C "$repo_root" cat-file -e "${commit}^{commit}"
done
git -C "$repo_root" worktree add --detach "$content_tree" "$content_commit" >/dev/null
PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$content_tree/stakeholder-update-writer"
examples="$content_tree/stakeholder-update-writer/references/examples.md"
scenario=$(awk '/^## 场景三：零散笔记加粉饰要求$/{on=1} on {print}' "$examples")
printf '%s\n' "$scenario" | rg -q '^# 待确认的受限风险升级：支付重试潜在风险$'
printf '%s\n' "$scenario" | rg -q '^- 状态：待确认。来源、触发、影响范围和权限'
printf '%s\n' "$scenario" | rg -q '低置信度 `F-01` 候选.*不能直接支持红色判定'
printf '%s\n' "$scenario" | rg -q '必要受众发送待确认的受限风险升级'
printf '%s\n' "$scenario" | rg -q '支付值班负责人、客服负责人和事件协调人'
printf '%s\n' "$scenario" | rg -q '只提示潜在影响、验证动作和满足什么条件才转红'
printf '%s\n' "$scenario" | rg -q '^## 验证动作$'
for validation_id in V-01 V-02 V-03; do
  printf '%s\n' "$scenario" | rg -q "^\| $validation_id "
done
printf '%s\n' "$scenario" | rg -q '^## 转红触发条件$'
printf '%s\n' "$scenario" | rg -q 'F-01.*工单/事件记录确认，且监控确认支付重试失败率达到已批准的红色阈值'
printf '%s\n' "$scenario" | rg -q '监控、告警或事件记录确认支付关键路径不可用'
printf '%s\n' "$scenario" | rg -q '任一触发满足时才转红'
printf '%s\n' "$scenario" | rg -q '不能把.*未经核实笔记改写为“进展顺利”'
printf '%s\n' "$scenario" | rg -q '不能把这些说法直接当成事实'
! printf '%s\n' "$scenario" | rg -q '状态：红|红/待确认细节'
rg -q '事实来源、关键里程碑或风险触发条件缺失时，状态写为.*待确认' "$content_tree/stakeholder-update-writer/SKILL.md"
expected_content_files='stakeholder-update-writer/references/examples.md'
test "$(git -C "$repo_root" diff --name-only "$base_commit" "$content_commit")" = "$expected_content_files"
git -C "$repo_root" diff --check "$base_commit" "$content_commit"
report=$(git -C "$repo_root" show "${report_commit}:docs/validation/skill-v2-validation-report.md")
section=$(printf '%s\n' "$report" | awk '/^### `stakeholder-update-writer`$/{on=1; next} /^### `skill-repo-release-verifier`$/{on=0} on {print}')
for field in '原始请求' 'V1 缺口' 'V2 改进' '场景复测' '受跟踪证据与验证方式' '静态检查记录' '结论与限制' '剩余风险'; do
  printf '%s\n' "$section" | rg -q "$field"
done
git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null
rm -rf "$temp_root"
trap - EXIT INT TERM
test ! -e "$content_tree"
! git -C "$repo_root" worktree list | rg -q 'stakeholder-status-p1-pinned\.'
printf 'PASS pinned-base=%s content=%s report=%s\n' "$base_commit" "$content_commit" "$report_commit"
printf 'PASS quick_validate, uncertain-status, necessary-audience, potential-impact, validation-actions, red-triggers, anti-polishing, no-guessing, exact-files, diff-check, detached-cleanup\n'
```

- P1 实际复跑记录：从后于固定报告快照和 P1 内容提交的 runner 执行上方完整脚本，整段退出码为 `0`。内容仅来自 `2c3066819e4dc472040af719fbaaad36a643c8b4` detached worktree；报告仅来自 `git show 2752e7ccc7901d01d86fa6e8953f81d1c53f45a1:docs/validation/skill-v2-validation-report.md`；没有读取或推导 `HEAD`。临时 `stakeholder-status-p1-pinned.*` worktree 和目录均已清理。

```text
Preparing worktree (detached HEAD 2c30668)
Skill is valid!
PASS pinned-base=2752e7ccc7901d01d86fa6e8953f81d1c53f45a1 content=2c3066819e4dc472040af719fbaaad36a643c8b4 report=2752e7ccc7901d01d86fa6e8953f81d1c53f45a1
PASS quick_validate, uncertain-status, necessary-audience, potential-impact, validation-actions, red-triggers, anti-polishing, no-guessing, exact-files, diff-check, detached-cleanup
```

- 结论与限制：通过（文档静态验证）。V2 能以受众和决定为中心组织状态，明确 RAG 规则与事实边界，并不会将坏消息或未知包装为顺利；P1 同时阻止在来源、触发、范围和权限不足时把潜在风险误判为红色。这不证明任何真实项目状态、指标、审批、用户影响、权限、风险缓解或沟通效果。
- 剩余风险：事实来源可能过期或被误解，受众权限与敏感级别需要信息 owner 复核，RAG 阈值和业务影响仍需项目负责人按实际承诺设定；自然语言汇报无法替代真实运营监控、决策权限或跨团队执行。

### `skill-repo-release-verifier`

- 原始请求：典型：发布前核验全部 20 个 Skill、中文覆盖、提交与远端文件树；信息不足：没有 `OWNER/REPO`、默认分支或写入权限；边界：本地验证失败或 push 超时仍要求发布成功结论。
- V1 缺口：原工作流以英文概览和手工命令为主，缺少统一 V2 中文章节、中文使用指南、可重跑的 fixture 验证器、六类分类重复检测、链接检查，以及把远端“未验证”与“已同步”分开的结论门槛。
- V2 改进：`scripts/validate_skill_repo.py` 只用标准库，稳定输出 `{path, code, message}`，并以非零退出阻断失败；它检查目录/frontmatter、必需文件、13 章顺序、`openai.yaml`、README/中文索引、六类清单、相对链接和高置信模板残留。正文、中文指南、命令、清单、示例、`openai.yaml`、README 和中文目录同步写明预检、逐 Skill、范围审计、push、Contents API 回退、远端 SHA/默认分支/树与失败语义。
- 初始 RED 历史记录（不可独立回放）：最初曾在 `validate_skill_repo.py` 尚不存在的未提交工作区执行八个临时 fixture 测试，记录为 8 个 `FileNotFoundError`。当时没有先创建只含测试的 commit，因此不存在可 detached 复跑的 RED SHA；这只能证明当次操作顺序，不能作为可回放提交证据。本轮审查已用下方固定测试提交补齐真正可回放的 RED。
- GREEN 证据：实现后执行同一命令，`Ran 8 tests ... OK`；再执行 `python3 skill-repo-release-verifier/scripts/validate_skill_repo.py .`，输出 `PASS: 20 Skill directories checked; 0 issue(s).`；`--json` 输出 `passed: true`、`skill_count: 20`、空 `issues`。`PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill-repo-release-verifier` 输出 `Skill is valid!`，`git diff --check` 退出零。
- 场景复测：
  - 典型发布：先运行确定性脚本和 20 个 `quick_validate.py`，只在通过后审计 base/候选范围；普通 push 后读取远端分支 SHA、默认分支和递归文件树，三者满足才写“已验证同步”。
  - 信息不足：缺远端、分支或凭据时仍给出本地问题/通过证据，但结论为“本地通过但远端未验证”，列出缺少项。
  - 失败边界：push 的网络超时、`401`、`403`、`404` 或树查询失败都保留实际错误类别；API 回退只在身份、权限和目标分支已确认后运行，不能把尝试或本地干净状态改写成远端成功。
- 受跟踪证据与验证方式：`SKILL.md` 的 13 个 V2 章节与远端判定规则；`references/usage-guide.zh.md`、`commands.md`、`checklists.md`、`examples.md`；fixture 测试与标准库验证器；README/中文目录的正式条目。
- 静态检查记录：固定基线为 `9a3b8467e8a2c4ad4b10522ed4f79245a808994f`，内容提交为 `c2f410927dca408b88b8f89b74eb5c7b58b08047`（`Upgrade skill repository verifier to V2`）。内容提交相对该基线的精确文件集合为 README、中文目录和 `skill-repo-release-verifier/` 的 V2 文档、两个脚本及其局部忽略规则；`git diff --check` 退出零。固定报告快照及 detached 复跑记录追加在下一次固定快照验证中。
- 结论与限制：通过（本地文档与确定性脚本验证）。验证器能阻断已定义的结构/导航/链接/残留问题，并强制把远端成功建立在实际 SHA、默认分支和文件树证据上；这不证明任意真实 GitHub 凭据、网络、分支保护、仓库可见性或远端发布状态。
- 剩余风险：模板残留检查刻意只匹配高置信未填写语句并跳过 fenced code，仍可能漏掉新的措辞；Markdown 解析覆盖常规内联链接，不替代完整 Markdown 渲染；网络、权限、默认分支差异和 API 并发更新仍可能阻断实际发布，必须在发布时重新核验。

#### 固定快照验证

- 固定边界：基线固定为 `9a3b8467e8a2c4ad4b10522ed4f79245a808994f`，内容提交固定为 `c2f410927dca408b88b8f89b74eb5c7b58b08047`，报告快照固定为 `98251cb91d00464cffa6e431c2a2f2581b31822e`。下方脚本不读取、不推导也不接受替换当前分支指针；Skill 内容只从内容提交的 detached worktree 读取，报告只由 `git show` 读取固定快照。

```bash
set -e
repo_root=$(git rev-parse --show-toplevel)
base_commit='9a3b8467e8a2c4ad4b10522ed4f79245a808994f'
content_commit='c2f410927dca408b88b8f89b74eb5c7b58b08047'
report_commit='98251cb91d00464cffa6e431c2a2f2581b31822e'
temp_root=$(mktemp -d "${TMPDIR:-/tmp}/skill-repo-verifier-pinned.XXXXXX")
content_tree="$temp_root/content"
cleanup() {
  git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null 2>&1 || true
  rm -rf "$temp_root"
}
trap cleanup EXIT INT TERM
test "$base_commit" = '9a3b8467e8a2c4ad4b10522ed4f79245a808994f'
test "$content_commit" = 'c2f410927dca408b88b8f89b74eb5c7b58b08047'
test "$report_commit" = '98251cb91d00464cffa6e431c2a2f2581b31822e'
for commit in "$base_commit" "$content_commit" "$report_commit"; do
  git -C "$repo_root" cat-file -e "${commit}^{commit}"
done
git -C "$repo_root" worktree add --detach "$content_tree" "$content_commit" >/dev/null
PYTHONDONTWRITEBYTECODE=1 python3 "$content_tree/skill-repo-release-verifier/scripts/test_validate_skill_repo.py" -v
PYTHONDONTWRITEBYTECODE=1 python3 "$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py" "$content_tree"
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/codex-skill-validate-deps \
  python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  "$content_tree/skill-repo-release-verifier"
expected_files=$(printf '%s\n' \
  README.md \
  docs/skill-catalog.zh.md \
  skill-repo-release-verifier/SKILL.md \
  skill-repo-release-verifier/agents/openai.yaml \
  skill-repo-release-verifier/references/checklists.md \
  skill-repo-release-verifier/references/commands.md \
  skill-repo-release-verifier/references/examples.md \
  skill-repo-release-verifier/references/usage-guide.zh.md \
  skill-repo-release-verifier/scripts/.gitignore \
  skill-repo-release-verifier/scripts/test_validate_skill_repo.py \
  skill-repo-release-verifier/scripts/validate_skill_repo.py)
test "$(git -C "$repo_root" diff --name-only "$base_commit" "$content_commit")" = "$expected_files"
git -C "$repo_root" diff --check "$base_commit" "$content_commit"
report=$(git -C "$repo_root" show "${report_commit}:docs/validation/skill-v2-validation-report.md")
section=$(printf '%s\n' "$report" | awk '/^### `skill-repo-release-verifier`$/{on=1} on {print}')
for field in '原始请求' 'V1 缺口' 'V2 改进' 'RED 证据' 'GREEN 证据' '场景复测' '受跟踪证据与验证方式' '静态检查记录' '结论与限制' '剩余风险'; do
  printf '%s\n' "$section" | rg -q "$field"
done
printf '%s\n' "$section" | rg -q '9a3b8467e8a2c4ad4b10522ed4f79245a808994f'
printf '%s\n' "$section" | rg -q 'c2f410927dca408b88b8f89b74eb5c7b58b08047'
git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null
rm -rf "$temp_root"
trap - EXIT INT TERM
test ! -e "$content_tree"
! git -C "$repo_root" worktree list | rg -q 'skill-repo-verifier-pinned\.'
printf 'PASS pinned-base=%s content=%s report=%s\n' "$base_commit" "$content_commit" "$report_commit"
printf 'PASS fixture-tests, repository-validator, quick-validate, exact-files, diff-check, report-fields, detached-cleanup\n'
```

- 实际复跑记录：从报告快照和内容提交之后的 runner 执行上方完整脚本，整段退出码为 `0`。内容只来自 `c2f410927dca408b88b8f89b74eb5c7b58b08047` 的 detached worktree，报告只来自 `git show 98251cb91d00464cffa6e431c2a2f2581b31822e:docs/validation/skill-v2-validation-report.md`；脚本没有读取或推导当前分支指针，临时 worktree 和目录均已清理。

```text
Preparing worktree (detached HEAD c2f4109)
Ran 8 tests in 0.186s
OK
PASS: 20 Skill directories checked; 0 issue(s).
Skill is valid!
PASS pinned-base=9a3b8467e8a2c4ad4b10522ed4f79245a808994f content=c2f410927dca408b88b8f89b74eb5c7b58b08047 report=98251cb91d00464cffa6e431c2a2f2581b31822e
PASS fixture-tests, repository-validator, quick-validate, exact-files, diff-check, report-fields, detached-cleanup
```

#### 审查加固

- 审查 findings：旧实现没有 Skill 数量/canonical 集合门禁；跳过 fragment，不能处理 reference-style link/image 或 percent 编码；允许指向仓库外已存在路径；UTF-8 解码错误会 traceback 并停止；frontmatter `name` 不接受安全尾注释且不能正确保留引号内 `#`；Contents API 示例使用 BSD-only `base64 -i`。
- 可回放 RED：测试提交固定为 `13963329140c8ee1288acb07c2e9ba13cdb28f60`（`Add verifier regression tests`），其父提交为审查前基线 `063fce5af2e5223556d80cf2bcd43c01a1841ed2`。该提交只修改 `skill-repo-release-verifier/scripts/test_validate_skill_repo.py`；在该 commit 的旧实现上执行 `PYTHONDONTWRITEBYTECODE=1 python3 skill-repo-release-verifier/scripts/test_validate_skill_repo.py -v`，结果为 `Ran 24 tests ... FAILED (failures=15)`。失败精确覆盖数量少/多与 CLI override、坏文件/同页 anchor、reference link/image/缺 definition、percent 编码合法路径、仓库外路径、乱码 JSON/继续、frontmatter 尾注释/引号内 `#` 和 GNU/BSD base64。
- 实现提交：固定为 `a1a832424de068a0bdcb9ddb5192e8836e6d0044`（`Harden skill repository verifier`）。验证器新增通用 `expected_count=None` API 和默认 20、可覆盖的 CLI；所有文本读取经缓存包装为单一稳定 `read_error`；Markdown 标准库解析覆盖 inline/image、reference definition/use、URL decode、repo-root 边界和 heading slug，并忽略 fenced/inline code 与外链；frontmatter 普通标量支持安全尾注释并保持引号内注释字符；命令改为 `base64 < "$file" | tr -d '\n'`。
- GREEN：实现后 fixture 套件加入一个真实仓库暴露的 inline-code 防误报测试，共 `Ran 25 tests ... OK`。真实仓库执行 `python3 skill-repo-release-verifier/scripts/validate_skill_repo.py . --expected-count 20` 输出 `PASS: 20 Skill directories checked; expected 20; 0 issue(s).`；JSON 输出 `expected_skill_count: 20`、`passed: true`、空 `issues`。`quick_validate.py skill-repo-release-verifier` 输出 `Skill is valid!`，Python 语法编译与 `git diff --check` 均退出零。
- 结论与限制：审查 findings 已由可回放 RED/GREEN 覆盖。Markdown parser 实现发布门禁所需的常规 CommonMark 形式和 GitHub 风格 heading slug，但不是完整 Markdown AST；复杂嵌套 label、自定义 HTML anchor 或非 GitHub renderer 的 slug 规则仍需单独规则或成熟 parser。固定报告快照与 detached RED/GREEN 复跑将在下一次快照记录中绑定。

#### 审查加固固定快照

- 固定边界：审查前基线为 `063fce5af2e5223556d80cf2bcd43c01a1841ed2`，可回放 RED 为 `13963329140c8ee1288acb07c2e9ba13cdb28f60`，GREEN 内容为 `a1a832424de068a0bdcb9ddb5192e8836e6d0044`，报告快照为 `30e85fa7335839a29cc0d51c755085a4fc72c940`。下方脚本不读取或推导当前分支指针，也不接受参数替换 SHA；测试和实现分别只从各自 detached worktree 读取，报告只由 `git show` 读取固定快照。

```bash
set -e
repo_root=$(git rev-parse --show-toplevel)
base_commit='063fce5af2e5223556d80cf2bcd43c01a1841ed2'
red_commit='13963329140c8ee1288acb07c2e9ba13cdb28f60'
content_commit='a1a832424de068a0bdcb9ddb5192e8836e6d0044'
report_commit='30e85fa7335839a29cc0d51c755085a4fc72c940'
temp_root=$(mktemp -d "${TMPDIR:-/tmp}/skill-repo-hardening-pinned.XXXXXX")
red_tree="$temp_root/red"
content_tree="$temp_root/content"
cleanup() {
  git -C "$repo_root" worktree remove --force "$red_tree" >/dev/null 2>&1 || true
  git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null 2>&1 || true
  rm -rf "$temp_root"
}
trap cleanup EXIT INT TERM
test "$base_commit" = '063fce5af2e5223556d80cf2bcd43c01a1841ed2'
test "$red_commit" = '13963329140c8ee1288acb07c2e9ba13cdb28f60'
test "$content_commit" = 'a1a832424de068a0bdcb9ddb5192e8836e6d0044'
test "$report_commit" = '30e85fa7335839a29cc0d51c755085a4fc72c940'
for commit in "$base_commit" "$red_commit" "$content_commit" "$report_commit"; do
  git -C "$repo_root" cat-file -e "${commit}^{commit}"
done
git -C "$repo_root" worktree add --detach "$red_tree" "$red_commit" >/dev/null
git -C "$repo_root" worktree add --detach "$content_tree" "$content_commit" >/dev/null
set +e
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$red_tree/skill-repo-release-verifier/scripts/test_validate_skill_repo.py" -v \
  >"$temp_root/red-output.txt" 2>&1
red_exit=$?
set -e
test "$red_exit" -ne 0
rg -q '^Ran 24 tests ' "$temp_root/red-output.txt"
rg -q '^FAILED \\(failures=15\\)$' "$temp_root/red-output.txt"
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/test_validate_skill_repo.py" -v
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py" \
  "$content_tree" --expected-count 20
green_json=$(PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py" \
  "$content_tree" --expected-count 20 --json)
printf '%s\n' "$green_json" | python3 -c \
  'import json, sys; value=json.load(sys.stdin); assert value["passed"] is True; assert value["skill_count"] == value["expected_skill_count"] == 20; assert value["issues"] == []'
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/codex-skill-validate-deps \
  python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  "$content_tree/skill-repo-release-verifier"
test "$(git -C "$repo_root" diff --name-only "$base_commit" "$red_commit")" = \
  'skill-repo-release-verifier/scripts/test_validate_skill_repo.py'
expected_green_files=$(printf '%s\n' \
  skill-repo-release-verifier/SKILL.md \
  skill-repo-release-verifier/references/commands.md \
  skill-repo-release-verifier/scripts/test_validate_skill_repo.py \
  skill-repo-release-verifier/scripts/validate_skill_repo.py)
test "$(git -C "$repo_root" diff --name-only "$red_commit" "$content_commit")" = \
  "$expected_green_files"
git -C "$repo_root" diff --check "$base_commit" "$red_commit"
git -C "$repo_root" diff --check "$red_commit" "$content_commit"
rg -q 'base64 < "\\$file" \\| tr -d' \
  "$content_tree/skill-repo-release-verifier/references/commands.md"
! rg -q 'base64 -i' "$content_tree/skill-repo-release-verifier/references/commands.md"
report=$(git -C "$repo_root" show \
  "${report_commit}:docs/validation/skill-v2-validation-report.md")
section=$(printf '%s\n' "$report" | awk '/^#### 审查加固$/{on=1} on {print}')
printf '%s\n' "$report" | rg -q '不可独立回放'
for field in '审查 findings' '可回放 RED' '实现提交' 'GREEN' '结论与限制'; do
  printf '%s\n' "$section" | rg -q "$field"
done
printf '%s\n' "$section" | rg -q '13963329140c8ee1288acb07c2e9ba13cdb28f60'
printf '%s\n' "$section" | rg -q 'a1a832424de068a0bdcb9ddb5192e8836e6d0044'
printf '%s\n' "$section" | rg -q 'FAILED \\(failures=15\\)'
printf '%s\n' "$section" | rg -q 'Ran 25 tests .* OK'
git -C "$repo_root" worktree remove --force "$red_tree" >/dev/null
git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null
rm -rf "$temp_root"
trap - EXIT INT TERM
test ! -e "$red_tree"
test ! -e "$content_tree"
! git -C "$repo_root" worktree list | rg -q 'skill-repo-hardening-pinned\.'
printf 'PASS pinned-base=%s red=%s content=%s report=%s\n' \
  "$base_commit" "$red_commit" "$content_commit" "$report_commit"
printf 'PASS replayable-red, green-tests, human-json, quick-validate, exact-files, portable-base64, diff-checks, report-fields, detached-cleanup\n'
```

- 实际复跑记录：从四个固定 SHA 之后的 runner 执行上方脚本，整段退出码为 `0`。RED 只来自 `13963329140c8ee1288acb07c2e9ba13cdb28f60` detached worktree，GREEN 只来自 `a1a832424de068a0bdcb9ddb5192e8836e6d0044` detached worktree，报告只来自 `git show 30e85fa7335839a29cc0d51c755085a4fc72c940:docs/validation/skill-v2-validation-report.md`；脚本没有读取或推导当前分支指针，两个临时 worktree 和目录均已清理。

```text
Preparing worktree (detached HEAD 1396332)
Preparing worktree (detached HEAD a1a8324)
Ran 25 tests in 0.767s
OK
PASS: 20 Skill directories checked; expected 20; 0 issue(s).
Skill is valid!
PASS pinned-base=063fce5af2e5223556d80cf2bcd43c01a1841ed2 red=13963329140c8ee1288acb07c2e9ba13cdb28f60 content=a1a832424de068a0bdcb9ddb5192e8836e6d0044 report=30e85fa7335839a29cc0d51c755085a4fc72c940
PASS replayable-red, green-tests, human-json, quick-validate, exact-files, portable-base64, diff-checks, report-fields, detached-cleanup
```

#### 二次审查边界

- 二次审查 findings：V2 章节解析会把 fenced code 中的伪 heading 当真；必需文件 symlink 可指向仓库外，broken symlink 也缺少稳定分类；Markdown parser 缺 CommonMark shortcut reference 和平衡括号 inline target；Contents API 把所有读取失败吞成“不存在”；recursive tree 未检查 `.truncated` 就声明文件树完整。
- 可回放 RED：测试提交固定为 `1d4de1eb26c3562bac27f308b6b0137850ff40c0`（`Add verifier parser boundary tests`），其父提交为二次审查前基线 `579ed929d1fd27b0ec2e438ac4aeb3c431cc7b7f`。该提交只修改 `skill-repo-release-verifier/scripts/test_validate_skill_repo.py`；在该 commit 的旧实现上执行完整 `-v` 套件，结果为 `Ran 39 tests ... FAILED (failures=9)`。失败覆盖 fenced heading、required/target symlink 与 broken symlink、shortcut reference、平衡括号 inline link、Contents API 错误分流和 recursive tree 截断 guard；fenced/inline code 排除、collapsed reference、尖括号 target/title 和 shortcut 排除项在 RED 提交上已通过。
- GREEN 实现：固定为 `01985ecdd32266e90d64dd3ee5cdb0122ed0322d`（`Fix verifier parser and remote guards`）。heading、inline/image、reference definition/use 和 shortcut 都基于排除 fenced/inline code 后的文本；inline link 用状态扫描处理平衡括号、尖括号 target 和 title。所有本地路径先做不跟随 symlink 的词法 root 检查，再区分 `path_outside_repository`、`broken_symlink` 和普通坏链接；必需文件和 Markdown 目标均不能通过仓库外 symlink。
- 远端 guard：Contents API 读取成功才使用 `.sha`，明确 `HTTP 404` 才 create；`401`/`403` 和网络/其他错误原样输出 stderr、保留退出码并停止。recursive tree 先保存完整响应并要求 `jq -e '.truncated == false'`，为 true 或缺失时停止，不生成完整性结论。
- GREEN 证据：`PYTHONDONTWRITEBYTECODE=1 python3 skill-repo-release-verifier/scripts/test_validate_skill_repo.py -v` 输出 `Ran 39 tests ... OK`。真实仓库人读与 JSON 均显式使用 `--expected-count 20`，结果为 20/20、零 issue、`passed: true`；`quick_validate.py` 输出 `Skill is valid!`，Python 语法编译和 `git diff --check` 退出零。
- 结论与限制：六项二次审查均有固定 fixture 或命令文档契约。Markdown 仍是针对仓库发布门禁的标准库子集，不承诺覆盖任意嵌套 CommonMark；GitHub CLI 错误分类依赖其 stderr 保留 `HTTP 404/401/403`，未识别错误一律安全停止而不是 create。固定报告 SHA 与 detached 复跑在下一快照提交绑定。

#### 二次审查固定快照

- 固定边界：二次审查前基线为 `579ed929d1fd27b0ec2e438ac4aeb3c431cc7b7f`，可回放 RED 为 `1d4de1eb26c3562bac27f308b6b0137850ff40c0`，GREEN 内容为 `01985ecdd32266e90d64dd3ee5cdb0122ed0322d`，报告快照为 `a258961013caf58f06eb66c95507ad0b65269eb3`。脚本不读取或推导当前分支指针，不接受参数替换 SHA；RED/GREEN 只从对应 detached worktree 读取，报告只通过固定 `git show` 读取。

```bash
set -e
repo_root=$(git rev-parse --show-toplevel)
base_commit='579ed929d1fd27b0ec2e438ac4aeb3c431cc7b7f'
red_commit='1d4de1eb26c3562bac27f308b6b0137850ff40c0'
content_commit='01985ecdd32266e90d64dd3ee5cdb0122ed0322d'
report_commit='a258961013caf58f06eb66c95507ad0b65269eb3'
temp_root=$(mktemp -d "${TMPDIR:-/tmp}/skill-repo-boundaries-pinned.XXXXXX")
red_tree="$temp_root/red"
content_tree="$temp_root/content"
cleanup() {
  git -C "$repo_root" worktree remove --force "$red_tree" >/dev/null 2>&1 || true
  git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null 2>&1 || true
  rm -rf "$temp_root"
}
trap cleanup EXIT INT TERM
test "$base_commit" = '579ed929d1fd27b0ec2e438ac4aeb3c431cc7b7f'
test "$red_commit" = '1d4de1eb26c3562bac27f308b6b0137850ff40c0'
test "$content_commit" = '01985ecdd32266e90d64dd3ee5cdb0122ed0322d'
test "$report_commit" = 'a258961013caf58f06eb66c95507ad0b65269eb3'
for commit in "$base_commit" "$red_commit" "$content_commit" "$report_commit"; do
  git -C "$repo_root" cat-file -e "${commit}^{commit}"
done
git -C "$repo_root" worktree add --detach "$red_tree" "$red_commit" >/dev/null
git -C "$repo_root" worktree add --detach "$content_tree" "$content_commit" >/dev/null
set +e
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$red_tree/skill-repo-release-verifier/scripts/test_validate_skill_repo.py" -v \
  >"$temp_root/red-output.txt" 2>&1
red_exit=$?
set -e
test "$red_exit" -ne 0
rg -q '^Ran 39 tests ' "$temp_root/red-output.txt"
rg -q '^FAILED \(failures=9\)$' "$temp_root/red-output.txt"
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/test_validate_skill_repo.py" -v
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py" \
  "$content_tree" --expected-count 20
green_json=$(PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py" \
  "$content_tree" --expected-count 20 --json)
printf '%s\n' "$green_json" | python3 -c \
  'import json, sys; value=json.load(sys.stdin); assert value["passed"] is True; assert value["skill_count"] == value["expected_skill_count"] == 20; assert value["issues"] == []'
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/codex-skill-validate-deps \
  python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  "$content_tree/skill-repo-release-verifier"
test "$(git -C "$repo_root" diff --name-only "$base_commit" "$red_commit")" = \
  'skill-repo-release-verifier/scripts/test_validate_skill_repo.py'
expected_green_files=$(printf '%s\n' \
  skill-repo-release-verifier/SKILL.md \
  skill-repo-release-verifier/references/commands.md \
  skill-repo-release-verifier/scripts/validate_skill_repo.py)
test "$(git -C "$repo_root" diff --name-only "$red_commit" "$content_commit")" = \
  "$expected_green_files"
git -C "$repo_root" diff --check "$base_commit" "$red_commit"
git -C "$repo_root" diff --check "$red_commit" "$content_commit"
verifier_commands_file="$content_tree/skill-repo-release-verifier/references/commands.md"
! rg -q '2>/dev/null \|\| true' "$verifier_commands_file"
rg -q 'HTTP 404' "$verifier_commands_file"
rg -q 'HTTP 401.*HTTP 403' "$verifier_commands_file"
rg -q "jq -e '.truncated == false'" "$verifier_commands_file"
script="$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py"
rg -q 'path_outside_repository' "$script"
rg -q 'broken_symlink' "$script"
rg -q 'def parse_inline_links' "$script"
report=$(git -C "$repo_root" show \
  "${report_commit}:docs/validation/skill-v2-validation-report.md")
section=$(printf '%s\n' "$report" | awk '/^#### 二次审查边界$/{on=1} on {print}')
for field in '二次审查 findings' '可回放 RED' 'GREEN 实现' '远端 guard' 'GREEN 证据' '结论与限制'; do
  printf '%s\n' "$section" | rg -q "$field"
done
printf '%s\n' "$section" | rg -q '1d4de1eb26c3562bac27f308b6b0137850ff40c0'
printf '%s\n' "$section" | rg -q '01985ecdd32266e90d64dd3ee5cdb0122ed0322d'
printf '%s\n' "$section" | rg -q 'FAILED \(failures=9\)'
printf '%s\n' "$section" | rg -q 'Ran 39 tests .* OK'
git -C "$repo_root" worktree remove --force "$red_tree" >/dev/null
git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null
rm -rf "$temp_root"
trap - EXIT INT TERM
test ! -e "$red_tree"
test ! -e "$content_tree"
! git -C "$repo_root" worktree list | rg -q 'skill-repo-boundaries-pinned\.'
printf 'PASS pinned-base=%s red=%s content=%s report=%s\n' \
  "$base_commit" "$red_commit" "$content_commit" "$report_commit"
printf 'PASS replayable-red, green-tests, human-json, quick-validate, exact-files, parser-symlink-remote-guards, diff-checks, report-fields, detached-cleanup\n'
```

- 实际复跑记录：从固定报告和内容提交之后的 runner 执行上方脚本，整段退出码为 `0`。RED 只来自 `1d4de1eb26c3562bac27f308b6b0137850ff40c0` detached worktree，GREEN 只来自 `01985ecdd32266e90d64dd3ee5cdb0122ed0322d` detached worktree，报告只来自 `git show a258961013caf58f06eb66c95507ad0b65269eb3:docs/validation/skill-v2-validation-report.md`；没有读取或推导当前分支指针，两个临时 worktree 和目录均已清理。

```text
Preparing worktree (detached HEAD 1d4de1e)
Preparing worktree (detached HEAD 01985ec)
Ran 39 tests in 1.102s
OK
PASS: 20 Skill directories checked; expected 20; 0 issue(s).
Skill is valid!
PASS pinned-base=579ed929d1fd27b0ec2e438ac4aeb3c431cc7b7f red=1d4de1eb26c3562bac27f308b6b0137850ff40c0 content=01985ecdd32266e90d64dd3ee5cdb0122ed0322d report=a258961013caf58f06eb66c95507ad0b65269eb3
PASS replayable-red, green-tests, human-json, quick-validate, exact-files, parser-symlink-remote-guards, diff-checks, report-fields, detached-cleanup
```

#### 第三轮发布证据

- 第三轮 findings：Contents API fallback 的 diff 位于 pipeline 左侧，非法 base 可能被循环的零状态吞掉；上传内容和 blob SHA 读取工作区而非固定候选提交；只处理新增/修改且上传后只检查四个代表路径，不能证明完整 A/M/D 变更集与候选提交一致。验证器还会让 malformed `urlsplit` 目标产生 traceback，README 六类覆盖会把 fenced code 或行内代码中的 Skill 提及当成真实覆盖。
- 可回放 RED：测试提交固定为 `17c7e13da8458935e257d56d7d8c95574ae0fcab`（`Add verifier release evidence tests`），其父提交为第三轮前基线 `205cea9a3c61419b4b12e75a3bfd537aa666aeb0`。该提交只修改 fixture 测试；在该 commit 的旧实现上运行完整 `-v` 套件，结果为 `Ran 45 tests ... FAILED (failures=6)`。失败覆盖 candidate-bound A/M/D、非法 base 非零停止、完整变更集 blob/deletion 核验、malformed URL 稳定 JSON，以及 README fenced/inline 伪覆盖。
- GREEN 实现：固定为 `ea0849aecf693fc949d4a0adc460ec89aa4e9e0f`（`Bind verifier fallback to candidate commit`）。fallback 使用 `set -euo pipefail`，先以独立 `git diff --name-status -z --no-renames` 命令保存完整 NUL 清单；A/M 内容来自 `git show "$candidate_commit:$file"`，候选 blob 来自 `git rev-parse "$candidate_commit:$file"`，D 通过 Contents DELETE 处理。rename 被表示为 D+A，其他状态明确停止。
- 远端发布证据：Contents 读取仍仅在明确 `HTTP 404` 时视为不存在，`401`、`403`、网络和未知失败均保留原始 stderr 与退出码并停止。上传后重新读取 recursive tree，先要求 `.truncated == false`，再对同一完整清单逐 path 验证 A/M 远端 blob 等于 candidate blob、D 不存在；任一不匹配均非零退出，不能声明同步成功。
- 解析器与 README：`urlsplit` 的 `ValueError` 转为稳定 `{path, code: invalid_link_target, message}`，验证继续收集其他问题且 JSON 无 traceback。README 覆盖与六类条目都从排除 fenced code 的规范分类条目派生；普通行内代码提及不再满足覆盖。
- GREEN 证据：`PYTHONDONTWRITEBYTECODE=1 python3 skill-repo-release-verifier/scripts/test_validate_skill_repo.py -v` 输出 `Ran 45 tests ... OK`。真实仓库人读与 JSON 均显式使用 `--expected-count 20`，结果为 20/20、零 issue、`passed: true`；`quick_validate.py` 输出 `Skill is valid!`，fallback block 的 Bash 语法、Python 编译和 `git diff --check` 退出零。
- 结论与限制：第三轮 findings 均有临时 fixture、静态命令契约或非法 base 可执行 shell fixture。没有执行真实远端写入，因此这里只证明 fail-closed 流程和候选提交绑定，未宣称远端发布成功；GitHub API 并发分支更新仍会由最终 blob 对比暴露为失败。固定报告 SHA 与 detached 复跑在下一快照提交绑定。

#### 第三轮固定快照

- 固定边界：第三轮前基线为 `205cea9a3c61419b4b12e75a3bfd537aa666aeb0`，可回放 RED 为 `17c7e13da8458935e257d56d7d8c95574ae0fcab`，GREEN 内容为 `ea0849aecf693fc949d4a0adc460ec89aa4e9e0f`，报告快照为 `f47af984713ce9ce24a0e5b123a36a260ad4b6f8`。脚本不读取或推导当前分支指针，不接受参数替换 SHA；RED/GREEN 只从对应 detached worktree 读取，报告只通过固定 `git show` 读取。

```bash
set -euo pipefail
repo_root=$(git rev-parse --show-toplevel)
base_commit='205cea9a3c61419b4b12e75a3bfd537aa666aeb0'
red_commit='17c7e13da8458935e257d56d7d8c95574ae0fcab'
content_commit='ea0849aecf693fc949d4a0adc460ec89aa4e9e0f'
report_commit='f47af984713ce9ce24a0e5b123a36a260ad4b6f8'
temp_root=$(mktemp -d "${TMPDIR:-/tmp}/skill-repo-release-evidence-pinned.XXXXXX")
red_tree="$temp_root/red"
content_tree="$temp_root/content"
cleanup() {
  git -C "$repo_root" worktree remove --force "$red_tree" >/dev/null 2>&1 || true
  git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null 2>&1 || true
  rm -rf "$temp_root"
}
trap cleanup EXIT INT TERM
test "$base_commit" = '205cea9a3c61419b4b12e75a3bfd537aa666aeb0'
test "$red_commit" = '17c7e13da8458935e257d56d7d8c95574ae0fcab'
test "$content_commit" = 'ea0849aecf693fc949d4a0adc460ec89aa4e9e0f'
test "$report_commit" = 'f47af984713ce9ce24a0e5b123a36a260ad4b6f8'
for commit in "$base_commit" "$red_commit" "$content_commit" "$report_commit"; do
  git -C "$repo_root" cat-file -e "${commit}^{commit}"
done
git -C "$repo_root" worktree add --detach "$red_tree" "$red_commit" >/dev/null
git -C "$repo_root" worktree add --detach "$content_tree" "$content_commit" >/dev/null
set +e
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$red_tree/skill-repo-release-verifier/scripts/test_validate_skill_repo.py" -v \
  >"$temp_root/red-output.txt" 2>&1
red_exit=$?
set -e
test "$red_exit" -ne 0
rg -q '^Ran 45 tests ' "$temp_root/red-output.txt"
rg -q '^FAILED \(failures=6\)$' "$temp_root/red-output.txt"
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/test_validate_skill_repo.py" -v
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py" \
  "$content_tree" --expected-count 20
green_json=$(PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py" \
  "$content_tree" --expected-count 20 --json)
printf '%s\n' "$green_json" | python3 -c \
  'import json, sys; value=json.load(sys.stdin); assert value["passed"] is True; assert value["skill_count"] == value["expected_skill_count"] == 20; assert value["issues"] == []'
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/codex-skill-validate-deps \
  python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  "$content_tree/skill-repo-release-verifier"
test "$(git -C "$repo_root" diff --name-only "$base_commit" "$red_commit")" = \
  'skill-repo-release-verifier/scripts/test_validate_skill_repo.py'
expected_green_files=$(printf '%s\n' \
  skill-repo-release-verifier/SKILL.md \
  skill-repo-release-verifier/references/commands.md \
  skill-repo-release-verifier/scripts/validate_skill_repo.py)
test "$(git -C "$repo_root" diff --name-only "$red_commit" "$content_commit")" = \
  "$expected_green_files"
test "$(git -C "$repo_root" diff --name-only "$content_commit" "$report_commit")" = \
  'docs/validation/skill-v2-validation-report.md'
git -C "$repo_root" diff --check "$base_commit" "$red_commit"
git -C "$repo_root" diff --check "$red_commit" "$content_commit"
git -C "$repo_root" diff --check "$content_commit" "$report_commit"
commands_file="$content_tree/skill-repo-release-verifier/references/commands.md"
rg -Fq 'set -euo pipefail' "$commands_file"
rg -Fq 'git diff --name-status -z --no-renames "$base_commit" "$candidate_commit" >"$change_list"' \
  "$commands_file"
rg -Fq 'git show "$candidate_commit:$file"' "$commands_file"
rg -Fq 'git rev-parse "$candidate_commit:$file"' "$commands_file"
! rg -Fq 'git hash-object "$file"' "$commands_file"
rg -Fq "jq -e '.truncated == false'" "$commands_file"
rg -Fq 'test "$remote_blob" = "$candidate_blob"' "$commands_file"
rg -Fq "test \"\$remote_blob\" = ''" "$commands_file"
validator="$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py"
rg -Fq '"invalid_link_target"' "$validator"
rg -Fq 'for _, line in non_fenced_lines(readme):' "$validator"
report=$(git -C "$repo_root" show \
  "${report_commit}:docs/validation/skill-v2-validation-report.md")
section=$(printf '%s\n' "$report" | awk '/^#### 第三轮发布证据$/{on=1} on {print}')
for field in '第三轮 findings' '可回放 RED' 'GREEN 实现' '远端发布证据' '解析器与 README' 'GREEN 证据' '结论与限制'; do
  printf '%s\n' "$section" | rg -q "$field"
done
printf '%s\n' "$section" | rg -q '17c7e13da8458935e257d56d7d8c95574ae0fcab'
printf '%s\n' "$section" | rg -q 'ea0849aecf693fc949d4a0adc460ec89aa4e9e0f'
printf '%s\n' "$section" | rg -q 'FAILED \(failures=6\)'
printf '%s\n' "$section" | rg -q 'Ran 45 tests .* OK'
git -C "$repo_root" worktree remove --force "$red_tree" >/dev/null
git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null
rm -rf "$temp_root"
trap - EXIT INT TERM
test ! -e "$red_tree"
test ! -e "$content_tree"
! git -C "$repo_root" worktree list | rg -q 'skill-repo-release-evidence-pinned\.'
printf 'PASS pinned-base=%s red=%s content=%s report=%s\n' \
  "$base_commit" "$red_commit" "$content_commit" "$report_commit"
printf 'PASS replayable-red, green-tests, human-json, quick-validate, exact-files, candidate-bound-AMD, full-tree-verification, parser-readme-guards, diff-checks, report-fields, detached-cleanup\n'
```

- 实际复跑记录：从四个固定 SHA 之后的 runner 执行上方脚本，整段退出码为 `0`。RED 只来自 `17c7e13da8458935e257d56d7d8c95574ae0fcab` detached worktree，GREEN 只来自 `ea0849aecf693fc949d4a0adc460ec89aa4e9e0f` detached worktree，报告只来自 `git show f47af984713ce9ce24a0e5b123a36a260ad4b6f8:docs/validation/skill-v2-validation-report.md`；没有读取或推导当前分支指针，两个临时 worktree 和目录均已清理。

```text
Preparing worktree (detached HEAD 17c7e13)
Preparing worktree (detached HEAD ea0849a)
Ran 45 tests in 1.4s
OK
PASS: 20 Skill directories checked; expected 20; 0 issue(s).
Skill is valid!
PASS pinned-base=205cea9a3c61419b4b12e75a3bfd537aa666aeb0 red=17c7e13da8458935e257d56d7d8c95574ae0fcab content=ea0849aecf693fc949d4a0adc460ec89aa4e9e0f report=f47af984713ce9ce24a0e5b123a36a260ad4b6f8
PASS replayable-red, green-tests, human-json, quick-validate, exact-files, candidate-bound-AMD, full-tree-verification, parser-readme-guards, diff-checks, report-fields, detached-cleanup
```

#### 最后 Minor：Git mode

- finding：Contents API fallback 只校验候选与远端 blob SHA，没有校验 Git mode/type。`120000 blob` symlink 的对象内容是链接目标文本，旧流程可把它作为普通文件上传；如果假远端返回相同 SHA，最终 tree 校验也会错误通过。`100755 blob` executable 和 `160000 commit` submodule 同样无法由 Contents API 保留原始 Git 语义。
- 可回放 RED：测试提交固定为 `7f2e8fb562d69623d9d4d365833bc907869c4d3a`（`Add verifier git mode regression test`），父提交/基线为 `cfe4597176130c25881d25b9fe67fc346cdf825d`。该提交只修改 fixture 测试；在该 commit 的旧 commands fallback 上运行 `-v` 套件，结果为 `Ran 47 tests ... FAILED (failures=2)`。静态测试确认缺少 mode/type guard；可执行 fixture 提交真实 `120000 blob` symlink，假远端返回同 blob SHA，旧流程退出零并记录 `uploaded`。
- GREEN 实现：固定为 `ad5109f0419f65f1731242152d44b6b48b8a1ab1`（`Reject unsupported git modes in fallback`）。每个 A/M path 在任何 Contents API 读取或 PUT 前通过 `git ls-tree "$candidate_commit" -- "$file"` 读取候选 mode/type；只有 `100644 blob` 放行。`120000 blob`、`100755 blob`、`160000 commit`、缺失或未知条目均打印 path/mode/type，建议普通 `git push` 并非零停止。
- 远端核验：未截断 recursive tree 对每个 A/M path 同时要求 `mode=100644`、`type=blob`、SHA 等于 candidate blob；D 同时要求没有同 path 条目和 SHA。mode、type、SHA 或删除状态任一不匹配都停止，不能声明远端同步成功。
- GREEN 证据：完整 fixture 套件输出 `Ran 47 tests ... OK`；symlink 可执行 fixture 在假 PUT 前停止，stderr 包含 `120000` 和 `Use ordinary git push`，PUT 日志不存在。真实仓库人读与 JSON 显式使用 `--expected-count 20`，结果为 20/20、零 issue、`passed: true`；`quick_validate.py` 与 fallback Bash 语法、`git diff --check` 均通过。
- 结论与限制：Contents API fallback 有意只支持普通非可执行文件，牺牲覆盖面以避免远端内容相同但 Git 语义不同。涉及 executable、symlink、submodule 或未知 mode/type 的发布必须使用普通 Git transport；本次没有执行或宣称真实远端发布成功。固定报告 SHA 与 detached 复跑在下一快照提交绑定。

#### Git mode 固定快照

- 固定边界：最后 Minor 前基线为 `cfe4597176130c25881d25b9fe67fc346cdf825d`，可回放 RED 为 `7f2e8fb562d69623d9d4d365833bc907869c4d3a`，GREEN 内容为 `ad5109f0419f65f1731242152d44b6b48b8a1ab1`，报告快照为 `abdc2728b7e83ae56aa003d5bde753c4b6ecc771`。脚本不读取或推导当前分支指针，不接受参数替换 SHA；RED/GREEN 只从对应 detached worktree 读取，报告只通过固定 `git show` 读取。

```bash
set -euo pipefail
repo_root=$(git rev-parse --show-toplevel)
base_commit='cfe4597176130c25881d25b9fe67fc346cdf825d'
red_commit='7f2e8fb562d69623d9d4d365833bc907869c4d3a'
content_commit='ad5109f0419f65f1731242152d44b6b48b8a1ab1'
report_commit='abdc2728b7e83ae56aa003d5bde753c4b6ecc771'
temp_root=$(mktemp -d "${TMPDIR:-/tmp}/skill-repo-git-mode-pinned.XXXXXX")
red_tree="$temp_root/red"
content_tree="$temp_root/content"
cleanup() {
  git -C "$repo_root" worktree remove --force "$red_tree" >/dev/null 2>&1 || true
  git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null 2>&1 || true
  rm -rf "$temp_root"
}
trap cleanup EXIT INT TERM
test "$base_commit" = 'cfe4597176130c25881d25b9fe67fc346cdf825d'
test "$red_commit" = '7f2e8fb562d69623d9d4d365833bc907869c4d3a'
test "$content_commit" = 'ad5109f0419f65f1731242152d44b6b48b8a1ab1'
test "$report_commit" = 'abdc2728b7e83ae56aa003d5bde753c4b6ecc771'
for commit in "$base_commit" "$red_commit" "$content_commit" "$report_commit"; do
  git -C "$repo_root" cat-file -e "${commit}^{commit}"
done
git -C "$repo_root" worktree add --detach "$red_tree" "$red_commit" >/dev/null
git -C "$repo_root" worktree add --detach "$content_tree" "$content_commit" >/dev/null
set +e
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$red_tree/skill-repo-release-verifier/scripts/test_validate_skill_repo.py" -v \
  >"$temp_root/red-output.txt" 2>&1
red_exit=$?
set -e
test "$red_exit" -ne 0
rg -q '^Ran 47 tests ' "$temp_root/red-output.txt"
rg -q '^FAILED \(failures=2\)$' "$temp_root/red-output.txt"
rg -q 'uploaded' "$temp_root/red-output.txt"
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/test_validate_skill_repo.py" -v
PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py" \
  "$content_tree" --expected-count 20
green_json=$(PYTHONDONTWRITEBYTECODE=1 \
  python3 "$content_tree/skill-repo-release-verifier/scripts/validate_skill_repo.py" \
  "$content_tree" --expected-count 20 --json)
printf '%s\n' "$green_json" | python3 -c \
  'import json, sys; value=json.load(sys.stdin); assert value["passed"] is True; assert value["skill_count"] == value["expected_skill_count"] == 20; assert value["issues"] == []'
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/codex-skill-validate-deps \
  python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  "$content_tree/skill-repo-release-verifier"
test "$(git -C "$repo_root" diff --name-only "$base_commit" "$red_commit")" = \
  'skill-repo-release-verifier/scripts/test_validate_skill_repo.py'
expected_green_files=$(printf '%s\n' \
  skill-repo-release-verifier/SKILL.md \
  skill-repo-release-verifier/references/commands.md)
test "$(git -C "$repo_root" diff --name-only "$red_commit" "$content_commit")" = \
  "$expected_green_files"
test "$(git -C "$repo_root" diff --name-only "$content_commit" "$report_commit")" = \
  'docs/validation/skill-v2-validation-report.md'
git -C "$repo_root" diff --check "$base_commit" "$red_commit"
git -C "$repo_root" diff --check "$red_commit" "$content_commit"
git -C "$repo_root" diff --check "$content_commit" "$report_commit"
commands_file="$content_tree/skill-repo-release-verifier/references/commands.md"
rg -Fq 'git ls-tree "$candidate_commit" -- "$file"' "$commands_file"
rg -Fq '[ "$candidate_mode" != "100644" ]' "$commands_file"
rg -Fq '[ "$candidate_type" != "blob" ]' "$commands_file"
rg -Fq 'Use ordinary git push' "$commands_file"
rg -Fq 'test "$remote_mode" = "100644"' "$commands_file"
rg -Fq 'test "$remote_type" = "blob"' "$commands_file"
rg -Fq 'test "$remote_blob" = "$candidate_blob"' "$commands_file"
rg -Fq 'test "$remote_path" = '"'"''"'" "$commands_file"
report=$(git -C "$repo_root" show \
  "${report_commit}:docs/validation/skill-v2-validation-report.md")
section=$(printf '%s\n' "$report" | awk '/^#### 最后 Minor：Git mode$/{on=1} on {print}')
for field in 'finding' '可回放 RED' 'GREEN 实现' '远端核验' 'GREEN 证据' '结论与限制'; do
  printf '%s\n' "$section" | rg -q "$field"
done
printf '%s\n' "$section" | rg -q '7f2e8fb562d69623d9d4d365833bc907869c4d3a'
printf '%s\n' "$section" | rg -q 'ad5109f0419f65f1731242152d44b6b48b8a1ab1'
printf '%s\n' "$section" | rg -q 'FAILED \(failures=2\)'
printf '%s\n' "$section" | rg -q 'Ran 47 tests .* OK'
git -C "$repo_root" worktree remove --force "$red_tree" >/dev/null
git -C "$repo_root" worktree remove --force "$content_tree" >/dev/null
rm -rf "$temp_root"
trap - EXIT INT TERM
test ! -e "$red_tree"
test ! -e "$content_tree"
! git -C "$repo_root" worktree list | rg -q 'skill-repo-git-mode-pinned\.'
printf 'PASS pinned-base=%s red=%s content=%s report=%s\n' \
  "$base_commit" "$red_commit" "$content_commit" "$report_commit"
printf 'PASS replayable-red, symlink-upload-red, green-tests, human-json, quick-validate, exact-files, candidate-mode-guard, remote-mode-type-sha, deletion-absence, diff-checks, report-fields, detached-cleanup\n'
```

- 实际复跑记录：从四个固定 SHA 之后的 runner 执行上方脚本，整段退出码为 `0`。RED 只来自 `7f2e8fb562d69623d9d4d365833bc907869c4d3a` detached worktree，GREEN 只来自 `ad5109f0419f65f1731242152d44b6b48b8a1ab1` detached worktree，报告只来自 `git show abdc2728b7e83ae56aa003d5bde753c4b6ecc771:docs/validation/skill-v2-validation-report.md`；没有读取或推导当前分支指针，两个临时 worktree 和目录均已清理。

```text
Preparing worktree (detached HEAD 7f2e8fb)
Preparing worktree (detached HEAD ad5109f)
Ran 47 tests in 1.8s
OK
PASS: 20 Skill directories checked; expected 20; 0 issue(s).
Skill is valid!
PASS pinned-base=cfe4597176130c25881d25b9fe67fc346cdf825d red=7f2e8fb562d69623d9d4d365833bc907869c4d3a content=ad5109f0419f65f1731242152d44b6b48b8a1ab1 report=abdc2728b7e83ae56aa003d5bde753c4b6ecc771
PASS replayable-red, symlink-upload-red, green-tests, human-json, quick-validate, exact-files, candidate-mode-guard, remote-mode-type-sha, deletion-absence, diff-checks, report-fields, detached-cleanup
```

## Task 22：V2 本地收口验证

- 范围：仅完成本地终审、固定 candidate 快照和验证记录；本轮没有执行 `git push`、GitHub Contents API、`gh repo view` 或远端文件树查询。远端状态为**待主代理同步与核验**，不得据此报告远端写入或发布成功。
- 文档终审：以作者视角复核 README 的仓库定位、六类分类边界、20 项典型输入/核心产出/上游下游、五条端到端工作流、安装调用和维护规则；并逐项对照 20 个 `SKILL.md` 与中文索引。六类均准确覆盖实际目录，20 项无遗漏、无重复；README 与中文目录未发现需要修正的内容，因此没有创建空的内容文档提交。
- 固定本地 candidate snapshot：`c07c8afdc1c83c8fa21b34f2bed2899a19cec10d`（`Pin verifier git mode validation`）。该提交在写入本节前已存在；验证仅从其 detached worktree 读取，未把后续报告工作区改动混入 candidate。
- detached 验证命令与结果：在临时 detached worktree 中对每个 `*/SKILL.md` 运行 `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/codex-skill-validate-deps python3 /Users/mac/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-dir>`，结果为 **20/20 `Skill is valid!`**；运行 `PYTHONDONTWRITEBYTECODE=1 python3 skill-repo-release-verifier/scripts/test_validate_skill_repo.py -v`，结果为 **Ran 47 tests, OK**；运行 `PYTHONDONTWRITEBYTECODE=1 python3 skill-repo-release-verifier/scripts/validate_skill_repo.py . --expected-count 20`，结果为 `PASS: 20 Skill directories checked; expected 20; 0 issue(s).`。
- JSON expected-20：同一 detached snapshot 运行 `.../validate_skill_repo.py . --expected-count 20 --json`，结果为 `{"expected_skill_count": 20, "issues": [], "passed": true, "skill_count": 20}`；随后由标准库 JSON 断言确认 `expected_skill_count == skill_count == 20`、`passed is true`、`issues == []`。
- 本地卫生：candidate 的 `git diff --check` 与 `git status --short` 均无输出；临时 detached worktree 已移除。写入本节前，当前工作树的 `git diff --check` 也无输出。
- 限制与后续：上述结果只证明固定本地 candidate 的结构、导航、链接和 verifier 行为。主代理仍需按批准范围同步候选提交，并独立核验远端仓库可见性、默认分支、远端 SHA 和完整文件树；任何网络、认证、分支或文件树失败都必须保留为未验证/失败状态。
