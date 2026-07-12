# Motion Spec Templates

## Full Motion Spec

```markdown
# Motion Spec: [Component or Flow]

## Intent
- User moment:
- What the motion communicates:
- Primary pattern:
- Secondary pattern:
- Should not feel:

## Trigger
| Trigger | User/system action | Frequency | Interruptible? |
|---|---|---:|---|

## Animation Objects
| Object | Starting state | Ending state | Notes |
|---|---|---|---|

## Timing
| Object | Duration | Delay/stagger | Easing/spring | Repeat |
|---|---:|---:|---|---|

## Behavior Details
- Entrance:
- Exit:
- Press or gesture feedback:
- State transition:
- Scroll or navigation relationship:
- Interruption behavior:
- Reduced-motion fallback:

## Implementation Notes
- Recommended approach:
- Properties to animate:
- Properties to avoid:
- Library/API:
- Performance considerations:

## Acceptance Criteria
- [ ] Motion starts from the user or system trigger.
- [ ] Motion explains what changed.
- [ ] Motion does not block frequent tasks.
- [ ] Layout does not jump.
- [ ] Reduced-motion users get a non-motion fallback.
- [ ] Mobile and desktop behavior are checked where relevant.
```

## VibeCoding Prompt Template

```text
请为【组件/页面】添加【动效模式】微动效，目标是【用户感知/产品意图】。

请只修改与动效相关的代码，不要重写页面结构和业务逻辑。

动效规格：
1. 触发条件：【点击/加载/滚动/拖拽/状态变化/页面进入】
2. 动效对象：【按钮/列表项/Tab 指示条/卡片/图表/页面容器】
3. 起始状态：【opacity/transform/scale/position/color】
4. 结束状态：【opacity/transform/scale/position/color】
5. 时长：【例如 180ms / 240ms / 600ms】
6. 缓动：【ease-out / ease-in-out / spring with damping】
7. 延迟或依次出现：【例如每项延迟 50ms】
8. 中断行为：【用户快速切换时取消上一段动画并进入新状态】
9. 无障碍：【尊重 prefers-reduced-motion，减少或关闭位移动画】
10. 验收标准：【没有文字重叠、没有布局跳动、移动端自然】

完成后请说明改了哪些文件、使用了哪些动效参数、如何验证。
```

## Motion Audit Template

```markdown
| UI moment | Current issue | Recommended pattern | Spec summary | Priority |
|---|---|---|---|---|
| Button tap | No feedback | Press ripple or pressed scale | 180ms scale 0.98 then restore | High |
```
