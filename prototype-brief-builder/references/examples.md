# 原型说明示例

以下是按模板压缩后的完整实例。前两个用于不同接收方，第三个展示信息不足时的拒绝与降级；它们不代表可直接复用的产品事实。

## 场景一：设计师可用性原型

**调用：** 为首次使用日程助手的新管理员测试：他们是否理解连接日历的理由，并能否在拒绝权限后继续探索。交给设计师和 Figma 制作人，不做生产实现。

### 原型决策卡

- 目的与决定：验证权限说明和拒绝后的恢复是否可理解，决定是否进入实现评审。
- 用户/任务/退出：首次创建团队的管理员；连接日历或选择先看建议；看到建议预览或“稍后连接”确认。
- 保真度与非目标：中保真；不制作 OAuth、完整设置中心、品牌动效或生产数据。

### 关键任务流

1. 从 `P-WELCOME` 阅读“连接日历可减少手动安排”。
2. 在 `P-CALENDAR-EXPLAIN` 点击连接，进入模拟权限结果。
3. 接受时到 `P-SUGGESTION-PREVIEW`；拒绝时到 `M-PERMISSION-DENIED`，可返回解释或选择稍后连接。

### 页面、组件与行为

| 页面 ID | 页面/弹层 | 存在理由 | 进入/离开条件 | 内容与状态 | 行为 ID | 本轮不做 |
|---|---|---|---|---|---|---|
| P-WELCOME | 欢迎页 | 解释价值 | 进入原型；点击继续离开 | 脱敏日程示例；默认 | B-WELCOME-CONTINUE | 账户设置 |
| P-CALENDAR-EXPLAIN | 权限说明 | 测试数据用途理解 | 点击连接或稍后连接离开 | 默认、请求中 | B-CALENDAR-CONNECT, B-SKIP-CONNECT | 真实授权 |
| M-PERMISSION-DENIED | 拒绝弹层 | 测试恢复 | 模拟拒绝进入；选择恢复离开 | 拒绝、焦点可见 | B-RECOVER-DENIAL | 原生系统弹层 |
| P-SUGGESTION-PREVIEW | 建议预览 | 成功退出 | 接受模拟权限或稍后连接进入 | 已连接/示例 | 无接口 | 推荐编辑 |

| 组件 ID | 组件 | 变体与状态 | 触发/校验/恢复 | 数据与内容规则 | 极值与无障碍 | 行为 ID |
|---|---|---|---|---|---|---|
| C-CALENDAR-CONNECT | 连接按钮 | 默认、请求中、禁用 | 点击触发模拟权限；请求中禁用重复点击；拒绝后由恢复操作回到说明 | 固定研究文案与脱敏日程样本；不读取真实日历 | 44px 触控目标；可见焦点；请求中读屏播报 | B-CALENDAR-CONNECT |
| C-DENIAL-RECOVERY | 拒绝恢复操作 | “再看说明”“稍后连接” | 拒绝状态才可用；各按钮进入对应恢复分支 | 固定、非引导的恢复文案；不声明已获授权 | 弹层标题获焦；Escape 关闭后焦点回连接按钮 | B-RECOVER-DENIAL |

### 原型行为连接

研究原型不调用生产接口，但仍填写连接、状态和恢复，避免 Figma 制作人猜测分支。

| 行为 ID | 关联页面 ID/组件 ID | 当前状态 | 用户/系统事件 | 守卫/前置条件 | 下一状态 | 明确路由目标 | 副作用 | 接口请求 | 成功响应 | 失败响应 | 失败恢复 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-WELCOME-CONTINUE | P-WELCOME | `welcome` | 点击继续 | 无 | `explaining` | `Figma:P-CALENDAR-EXPLAIN` | 记录观察起点 | 无接口 | 无接口 | 无接口 | 返回 `Figma:P-WELCOME` |
| B-CALENDAR-CONNECT | P-CALENDAR-EXPLAIN/C-CALENDAR-CONNECT | `explaining` | 点击连接；研究主持人选择模拟接受/拒绝 | 已阅读说明 | `connected` 或 `denied` | 接受：`Figma:P-SUGGESTION-PREVIEW`；拒绝：`Figma:M-PERMISSION-DENIED` | `calendar_connect_started` | 无接口，模拟权限 | 接受分支进入建议预览 | 拒绝分支进入拒绝弹层 | 使用 B-RECOVER-DENIAL |
| B-SKIP-CONNECT | P-CALENDAR-EXPLAIN | `explaining` | 点击稍后连接 | 无 | `previewing` | `Figma:P-SUGGESTION-PREVIEW` | `calendar_connect_skipped` | 无接口 | 无接口 | 无接口 | 返回 `Figma:P-CALENDAR-EXPLAIN` |
| B-RECOVER-DENIAL | M-PERMISSION-DENIED/C-DENIAL-RECOVERY | `denied` | 点击再看说明或稍后连接 | 模拟拒绝已发生 | `explaining` 或 `previewing` | 说明：`Figma:P-CALENDAR-EXPLAIN`；稍后：`Figma:P-SUGGESTION-PREVIEW` | `calendar_connect_declined` | 无接口 | 无接口 | 无接口 | 保留两个可点击恢复选项 |

### 跨端、无障碍与观测

| 主题 | 规则 | 验收或观察方式 |
|---|---|---|
| 响应式 | 375px 原型；桌面仅等比展示，不增加未测导航 | 任务路径在目标手机宽度可完成 |
| 无障碍 | 连接按钮有名称；拒绝弹层打开时聚焦标题，关闭后回连接按钮 | 键盘走完接受、拒绝和恢复分支 |
| 观察 | 记录 `onboarding_permission_explained`、`calendar_connect_started`、`calendar_connect_declined`、`suggestion_previewed` | 研究记录与行为连接对应 |

### 设计师交接

- 研究任务：“你刚创建团队，请让助手依据日历提出一条建议。”不提示按钮位置。
- 观察记录：记录完成/放弃、是否能复述数据用途、拒绝后的首个动作、犹豫点、原话和耗时；不记录真实日程或身份。
- 评审标准：至少能从拒绝弹层恢复到说明或建议预览，且不把模拟权限误解为已授权。

### Figma 交接

- 页面树：`Onboarding/P-WELCOME`、`P-CALENDAR-EXPLAIN`、`M-PERMISSION-DENIED`、`P-SUGGESTION-PREVIEW`；起点为 `P-WELCOME`。
- 组件/变量：`C-CALENDAR-CONNECT` 的 `default/requesting/disabled`，日程示例使用脱敏内容变量。
- 连接：`B-CALENDAR-CONNECT` 的接受分支连预览、拒绝分支连弹层；`B-RECOVER-DENIAL` 回说明或连预览；弹层关闭时焦点回 `C-CALENDAR-CONNECT`。

### 清单验收

- 范围与保真度：通过。四页都服务于理解、连接或恢复。
- 设计师交接：通过。任务、观察记录与隐私边界明确。
- Figma 交接：通过。页面树、组件变量和分支连接明确。
- 编程代理行为契约：不适用；本例明确为研究原型，未交给代理实现。

### 开放问题

无开放问题：本例运行研究所需的模拟分支、脱敏内容、观察记录和 Figma 连接均已定义；真实 OAuth 与日历数据已明确为非目标。

## 场景二：Codex 高保真实现说明

**调用：** 为桌面和手机网页实现订阅取消流程。用户可比较当前方案、选择取消原因、查看保留优惠或确认取消。交给 Codex；沿用现有设计系统，必须能键盘操作并接入现有事件规范。不可假设优惠一定可用。

### 原型决策卡

- 目的与决定：实现已确认的取消流程，保留优惠只能来自已有服务响应。
- 用户/任务/退出：现有订阅者；提交原因后接受优惠或确认取消；到 `P-BILLING` 的保留结果或 `P-CANCELLED` 的取消结果。
- 保真度与非目标：高保真；不实现退款、客服工单、新套餐购买或自行计算优惠。

### 关键任务流

1. `P-SUBSCRIPTION-DETAIL` 的订阅者开始取消，到 `P-CANCEL-REASON`。
2. 选择原因并提交：服务返回优惠则到 `P-RETENTION-OFFER`，否则到 `P-CANCEL-CONFIRM`。
3. 接受优惠保留订阅并返回账单；拒绝优惠到确认页；确认取消后到取消结果页。

### 页面、组件与行为

| 页面 ID | 页面 | 存在理由 | 进入/离开条件 | 内容与状态 | 行为 ID | 本轮不做 |
|---|---|---|---|---|---|---|
| P-SUBSCRIPTION-DETAIL | 订阅详情 | 提供取消入口 | 活跃订阅进入；开始取消离开 | `planName`、`renewalDate`、`price`；默认 | B-START-CANCEL | 修改套餐 |
| P-CANCEL-REASON | 取消原因 | 收集原因并请求预览 | 选择原因后提交；失败可重试 | 默认、校验失败、提交中、失败 | B-SUBMIT-REASON | 自由文本原因上报 |
| P-RETENTION-OFFER | 保留优惠 | 仅在服务给出优惠时展示 | 接受、拒绝或刷新后离开/保持 | 可用、接受中、接受失败、过期、刷新中、刷新失败 | B-ACCEPT-OFFER, B-REFRESH-OFFER, B-DECLINE-OFFER | 自行生成优惠 |
| P-CANCEL-CONFIRM | 取消确认 | 明示业务后果并确认 | 确认取消后离开 | 默认、提交中、失败 | B-CONFIRM-CANCEL | 立即退款 |
| P-CANCELLED | 取消结果 | 告知已计划取消 | 成功响应进入 | `cancellationEffectiveDate` | 无接口 | 重新订阅 |

| 组件 ID | 组件 | 变体与状态 | 触发/校验/恢复 | 数据与内容规则 | 极值与无障碍 | 行为 ID |
|---|---|---|---|---|---|---|
| C-CANCEL-REASON-FORM | 原因表单 | 未选、有效、提交中、失败 | 选择 `reasonId` 后才可继续；失败重试 B-SUBMIT-REASON；返回账单放弃 | `cancellationReasons` 与 `subscriptionId` 由订阅详情入口提供；只提交枚举 `reasonId` | 错误摘要关联单选组；长原因标签换行；提交中按钮禁用 | B-SUBMIT-REASON |
| C-RETENTION-OFFER | 保留优惠 | 可用、接受中、接受失败、过期、刷新中、刷新失败 | 仅 `status=available`、未过期且 `eligibility.canAccept=true` 时可接受；过期/失败触发 B-REFRESH-OFFER 或 B-DECLINE-OFFER | `offerId`、`status`、`displayContent`、`benefit`、`expiresAt`、`eligibility`、`previewId` 均来自 B-SUBMIT-REASON 或 B-REFRESH-OFFER 的 `200`；不自行计算金额/权益 | 长标题和权益文案换行；到期信息读屏播报；失效优惠不可接受；刷新错误聚焦错误摘要 | B-ACCEPT-OFFER, B-DECLINE-OFFER, B-REFRESH-OFFER |
| C-CANCEL-CONFIRM | 确认操作 | 默认、提交中、失败、预览过期 | 只有 `reasonId` 与未过期 `previewId` 才可确认；`409 preview_expired` 后回 B-SUBMIT-REASON 重取预览 | `previewId`、取消生效日期和订阅摘要来自 B-SUBMIT-REASON/B-REFRESH-OFFER `200` | 确认后禁用重复提交；错误摘要获焦；键盘可取消返回 | B-CONFIRM-CANCEL |

### 编程代理行为契约

| 行为 ID | 关联页面 ID/组件 ID | 当前状态 | 用户/系统事件 | 守卫/前置条件 | 下一状态 | 明确路由目标 | 副作用 | 接口请求 | 成功响应 | 失败响应 | 失败恢复 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B-START-CANCEL | P-SUBSCRIPTION-DETAIL | `viewing` | 点击“取消订阅” | `subscription.status=active` | `reason-editing` | `/settings/billing/cancel/reason` | `subscription_cancel_started` | 无接口 | 无接口 | 无接口 | 返回 `/settings/billing` |
| B-SUBMIT-REASON | P-CANCEL-REASON/C-CANCEL-REASON-FORM | `reason-editing` | 点击“继续” | 已选 `reasonId` | `offer-loading` 或 `confirmation-ready` | 有优惠：`/settings/billing/cancel/offer`；无优惠：`/settings/billing/cancel/confirm` | `cancellation_reason_selected`；禁用表单 | `POST /api/subscriptions/{subscriptionId}/cancellation-preview`，`{reasonId}` | `200 {previewId,cancellationEffectiveDate,retentionOffer:{offerId,status:"available",displayContent:{headline,body},benefit:{type,value,currency},expiresAt,eligibility:{canAccept,reasonIds,subscriptionStatus}}}`：有优惠进入优惠；`200 {previewId,retentionOffer:null,cancellationEffectiveDate}`：进入确认。后续 B-* 只使用此响应或刷新响应中的同名字段 | 网络或 `5xx`：`reason-submit-failed`，留在原因页 | 显示错误摘要；“重试”重发同一请求，“返回”到 `/settings/billing` |
| B-ACCEPT-OFFER | P-RETENTION-OFFER/C-RETENTION-OFFER | `offer-available` | 点击“接受优惠” | `offerId`、`previewId` 来自预览响应；`status=available`、`expiresAt` 未过期且 `eligibility.canAccept=true` | `offer-accepting` 后 `retained` | 成功：`/settings/billing?retention=accepted`；失败：保持 `/settings/billing/cancel/offer` | 记录 `retention_offer_accepted`；取消取消意图 | `POST /api/subscriptions/{subscriptionId}/retention-offer/accept`，请求体 `{offerId,previewId}`，Header `Idempotency-Key` | `200 {subscription:{status:"active",planName,renewalDate},cancellationPreview:{previewId,status:"withdrawn"},retentionOffer:{offerId,status:"accepted",benefit}}`：优惠生效、订阅继续、取消流程结束 | `409 {code:"offer_expired"|"offer_ineligible",retentionOffer:{offerId,status:"expired"|"ineligible"}}`：`offer-accept-failed`；`5xx`：同状态且保留上次优惠 | `409` 时触发 B-REFRESH-OFFER；`5xx` 时重试 B-ACCEPT-OFFER 或用 B-DECLINE-OFFER 继续取消 |
| B-REFRESH-OFFER | P-RETENTION-OFFER/C-RETENTION-OFFER | `offer-accept-failed` 或 `offer-stale` | 点击“刷新优惠” | `reasonId` 与旧 `previewId` 存在；仅 `409` 或优惠过期时显示 | `offer-refreshing` 后 `offer-available` 或 `confirmation-ready` | 有新优惠时保持 `/settings/billing/cancel/offer`；无优惠时转 `/settings/billing/cancel/confirm`；失败时保持优惠页 | 记录 `retention_offer_refresh_requested`；禁用接受/刷新按钮 | `POST /api/subscriptions/{subscriptionId}/cancellation-preview`，`{reasonId,refresh:true,previousPreviewId}` | `200 {previewId,cancellationEffectiveDate,retentionOffer:{offerId,status:"available",displayContent:{headline,body},benefit:{type,value,currency},expiresAt,eligibility:{canAccept,reasonIds,subscriptionStatus}}}`：替换旧字段并恢复可接受；`200 {previewId,retentionOffer:null,cancellationEffectiveDate}`：进入确认 | 网络或 `5xx`：`offer-refresh-failed`，保留旧优惠但禁用接受 | “重试刷新”重触发 B-REFRESH-OFFER 并保持优惠页；“继续取消”触发 B-DECLINE-OFFER |
| B-DECLINE-OFFER | P-RETENTION-OFFER/C-RETENTION-OFFER | `offer-available` 或 `offer-refresh-failed` | 点击“不接受，继续取消” | `reasonId` 和当前 `previewId` 存在 | `confirmation-ready` | `/settings/billing/cancel/confirm` | 记录 `retention_offer_declined`；保留 `reasonId`、`previewId` | 无接口 | 无接口：不改变订阅，不接受优惠 | 无接口 | 浏览器返回时保持优惠页与当前数据；确认页可返回优惠页 |
| B-CONFIRM-CANCEL | P-CANCEL-CONFIRM/C-CANCEL-CONFIRM | `confirmation-ready` | 点击“确认取消” | `reasonId`、`previewId` 来自 B-SUBMIT-REASON/B-REFRESH-OFFER，且预览未过期 | `cancellation-submitting` 后 `cancelled` | 成功：`/settings/billing/cancelled`；失败：当前 `/settings/billing/cancel/confirm` | `subscription_cancel_confirmed`；禁用确认 | `POST /api/subscriptions/{subscriptionId}/cancel`，`{reasonId,previewId}` | `200 {subscription:{status:"cancel_scheduled"},cancellationEffectiveDate}`：到期日展示在结果页 | `409 preview_expired` 或 `5xx`：`cancel-confirm-failed`，订阅保持 active | `409` 回 `/settings/billing/cancel/reason` 触发 B-SUBMIT-REASON 重取预览；`5xx` 在确认页重试 B-CONFIRM-CANCEL |

### 跨端、无障碍与埋点

| 主题 | 规则 | 验收 |
|---|---|---|
| 响应式 | 320px 将步骤栏改为进度文本，主操作保持在可见区域 | 原因、优惠、确认三页均可完成 |
| 无障碍 | 表单标签和错误摘要关联；状态变更读屏播报；失败焦点移到错误摘要 | 仅键盘完成接受、拒绝、确认和重试 |
| 埋点 | `subscription_cancel_started`、`cancellation_reason_selected`、`retention_offer_viewed`、`retention_offer_accepted`、`retention_offer_declined`、`subscription_cancel_confirmed`；不记录自由文本原因 | 每个事件能追到 `B-*`，仅含方案标识、路径和状态 |

### 编程代理交接

- 使用 `P-*`、`C-*` 和 `B-*` 原样命名实现边界；不可补造优惠、金额、退款或接口字段。
- 320px 时步骤栏改为进度文本；表单有标签、错误摘要和焦点移动，弹层可 Escape 关闭；事件不记录自由文本原因。

### 清单验收

- 页面/组件到行为契约：通过。所有交互 `P-*`/`C-*` 都引用 `B-*`。
- 接口与失败恢复：通过。预览、接受和刷新均给出请求参数、响应 schema、路由和可执行恢复。
- RetentionOffer：通过。接受使优惠生效、取消意图结束并到账单；拒绝不改订阅、保留 `reasonId`/`previewId` 并到确认页；过期刷新有独立 `B-REFRESH-OFFER`。
- 组件完整性：通过。三项组件均填入触发、校验、恢复、数据来源、极值与无障碍。
- 未确认逻辑：通过。优惠字段只由预览或刷新响应提供。

### 开放问题

无开放问题：本例假定列出的三个端点、枚举原因和现有设计系统已经获产品/工程 owner 批准；新增优惠计算、退款、客服与订阅变更仍为非目标。

## 场景三：一句话想法与误用降级

**调用：** “做一个帮助自由职业者管理发票的网站。今天给我一套可上线的高保真页面和支付流程。”

### 拒绝与降级

拒绝生产规格和支付流程：没有目标用户、地区/税务责任、支付服务、平台、内容来源、成功条件或合规边界。降级为以下低保真探索卡，不生成 `P-*`/`C-*`/`B-*` 或接口契约。

### 低保真探索卡

- 想法原文：帮助自由职业者管理发票的网站。
- 候选用户与待验证问题：独立服务提供者是否能理解“创建一张可核对发票”的最小流程。
- 候选核心任务：填写客户和服务信息，预览后保存草稿。
- 最小流程：入口 -> 客户/服务信息 -> 发票预览 -> 保存草稿 -> 退出。
- 低保真范围：信息层级、字段分组和保存草稿反馈；不制作品牌、支付、自动催款、税务计算、发送或移动端。
- `[待确认]`：用户分群、地区、税务责任、平台、客户数据来源、发送渠道、付款方式、成功条件和隐私要求。
- 补数动作：访谈三位目标用户；由产品 owner 确认地区和税务边界；核对现有发票模板/字段来源。
- 下一次评审决定：仅决定是否制作“创建发票是否可理解”的中保真可用性原型。

### 清单验收

- 信息不足处理：通过。未知项与补数动作可见。
- 误用处理：通过。拒绝把一句想法伪装成生产、高保真或支付规格。
- 编程代理行为契约：不适用；未进入实现交接。
