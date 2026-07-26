# 微动效闭环示例

## 场景一：移动端列表首次进入

**请求：** “优化移动端订单列表进入，让它不那么生硬。”

**动效意图：** 用户从订单 Tab 首次进入已加载的首屏结果，动效只建立自上而下的扫描顺序；不延迟点击、不是每次滚动都播放。

| 动效 ID | 当前状态 | 事件与守卫 | 目标状态 | 参数 | 取消/保护 |
|---|---|---|---|---|---|
| M-LIST-ENTER | `loaded-hidden` | 首次进入且 `visibleItems <= 8` | `loaded-visible` | 每项 `opacity 0 -> 1`、`translateY(10px) -> 0`、`180ms`、`32ms` stagger、`cubic-bezier(0.2,0,0,1)` | 滚动、筛选、离屏或数据替换取消未开始项；`transitionId` 只允许最新列表提交 |

| 档位 | 行为 | 等价反馈 |
|---|---|---|
| 完整 | 首屏最多 8 项依次进入，总延迟不超 224ms | 标题、数量和可点按订单立即可见 |
| 减少动态 | 容器即时显示 | 同一标题、数量和空/错误提示 |
| 低端降级 | 取消 stagger，容器 `opacity 0 -> 1`，`100ms` | 同一内容和操作 |

**验收：** 首屏外项目不动画；虚拟化回收和回访不重放；用户在 `100ms` 内可点第一项；快速筛选后旧列表不会闪回；减少动态和低端档仍显示加载/空/错误文本。

## 场景二：要求全页高级动效

**请求：** “给所有页面增加高级动效，越丰富越好。”

**实际处理：** 不接受为规格。先收敛为：“结账完成后进入订单详情，用户需要理解自己进入了下一级并能立即返回。”其余页面、滚动视差、无限背景和逐元素入场均列为非目标。

| 动效 ID | 当前状态 | 事件与守卫 | 目标状态 | 参数 | 取消/保护 |
|---|---|---|---|---|---|
| M-CHECKOUT-DETAIL | `checkout-success` | 成功响应含 `orderId` | `detail-entering -> detail-idle` | 后页 `translateX(16px) -> 0`、`opacity 0 -> 1`；前页 `translateX(0) -> -8px`、`opacity 1 -> 0.72`；全部 `260ms`、`cubic-bezier(0.2,0,0,1)` | 返回、路由替换、卸载取消控制器；若返回先发生，稳定为 `checkout-success`；若替换路由，稳定为替换目标；transition id 防旧完成回写 |
| M-DETAIL-BACK | `detail-idle` | 用户返回且 history 有结账成功页 | `checkout-returning -> checkout-success` | 前页（详情）`translateX(0) -> 16px`、`opacity 1 -> 0`；后页（结账成功）`translateX(-8px) -> 0`、`opacity 0.72 -> 1`；全部 `260ms`、`cubic-bezier(0.2,0,0,1)` | 新路由/卸载取消控制器；取消后稳定为最新已提交路由，未提交时保持 `detail-idle`；transition id 拒绝旧回调 |

**焦点交接：** 前进时先提交详情路由并在 `260ms` 完成后将焦点移到订单详情 `h1`，再播报“订单已提交，已打开订单详情”。返回时在详情卸载后恢复到结账成功页的“查看订单”触发控件；若该控件不存在，移到结账成功 `h1`。取消或路由替换不执行过期页面的焦点移动。

**取消后稳定状态：** 返回尚未提交时保留 `detail-idle` 和详情页当前焦点；返回已提交时保留 `checkout-success` 并按焦点交接规则恢复。任意路由替换以替换目标为唯一稳定状态，旧 transition id 只能清理资源。

**降级：** 减少动态和低端档立即进入详情、移动焦点到页面标题、播报“订单已提交，已打开订单详情”；没有视差、blur、stagger 或页面常驻动画。

**验收：** 前进和 `M-DETAIL-BACK` 的每个前页/后页起止位置、透明度、`260ms` 和 easing 均可逐项测量；成功反馈不等待转场；返回可立即触发；焦点按上述规则交接；取消后只保留最新已提交路由的稳定状态；每帧只动页面容器的 transform/opacity；未批准的全页效果没有被加入。

## 场景三：低端设备与减少动态模式的底部抽屉

**请求：** “底部抽屉可拖拽，但低端设备和减少动态模式也要好用。”

| 动效 ID | 状态与事件 | 完整档 | 减少动态 | 低端降级 |
|---|---|---|---|---|
| M-SHEET-DRAG | `idle -> dragging` on pointer down；`pointercancel -> lastSnap` | 逐帧映射 `translateY`；边界采用单调阻尼 | 保持跟手，不加 rubber-band | 保持跟手，不计算遮罩连续 blur |
| M-SHEET-SETTLE | pointer up；当前 `translateY=510px`、释放 `velocity=-1200px/s`，按阈值选 `360px` snap | 目标运行时：Motion `animate(..., { type: "spring" })`；求解器：该库数值 spring；`stiffness:260,damping:28,mass:1,velocity:-1200px/s,target:360px,restDelta:0.5px,restSpeed:5px/s,maxSettle:420ms` | 直接到已计算的 `360px` snap point | `160ms` `translateY(510px) -> 360px`，`cubic-bezier(0.2,0,0,1)`；无阴影/模糊 |

**中断：** 新 pointer down 取消 settle 并从当前值跟手；路由关闭、卸载和 `pointercancel` 清理监听器/rAF，回到最后稳定 snap；过期完成不能重新打开抽屉。

**性能协议：** 采样源为抽屉交互中的 rAF 时间戳；这是本产品的**待验证基线**。最近 `12` 帧中至少 `3` 帧超过 `20ms` 时标记 `pending-low`，但不在 `dragging` 中切档；只有当前 settle 到 `360px` 稳定点或下一次 pointerdown 前才提交 `low`。

**恢复生命周期：** `full -> pending-low -> low-cooling -> low-sampling -> restore-pending -> full`。提交 `low` 后，在 document visible 且 app foreground 时启动低频探针：每 `250ms` 调度连续两个 rAF，只记录这两个 rAF 的间隔；没有新 pointer 事件也持续运行。`low-cooling` 按累计前台可见时间达到 `5s` 后转为 `low-sampling`；随后每个干净样本填入 `60` 样本窗口，连续两个窗口都无超过 `20ms` 的帧时进入 `restore-pending`。任何 long frame 清空两个窗口并重启 `5s` 冷却。

**暂停、清理与恢复：** document hidden 或 app background 时暂停并清理 timeout、两个 rAF 句柄和平台帧订阅，停止累计前台冷却时间并重置恢复窗口；foreground/visible 后保持 `low`，从剩余冷却和新窗口继续。路由卸载、销毁监控或减少动态接管也移除 visibility/app-state 监听器。`restore-pending` 只在抽屉 idle、当前 transition 完成或 `360px` 稳定 snap point 提交 `full`，不在 dragging/settling 中跳档。

**确定性测试：** 用假时钟推进 `5s` 前台可见时间，再用可控 rAF 输入 `120` 个 `16ms` 的 rAF 对；期望 `low-sampling -> restore-pending`，然后触发稳定 snap point，期望 `full`。在第 `59` 个样本后触发 document hidden，期望取消探针并清空窗口；回前台后必须重新累计，不得提前恢复。

**验收：** 三个档位都能关闭、半展开和全展开；Motion 示例的 API、求解器、参数语义/单位、`-1200px/s` 初速度、`360px` 目标、rest 阈值和 `420ms` settle 均可验收；焦点始终在抽屉语义范围内，关闭后返回触发控件；low 在无交互时可通过低频探针进入 `restore-pending`，只在稳定边界恢复 full，hidden/background 会取消探针并重置窗口；视觉降级不移除展开状态、遮罩可达性或关闭路径。
