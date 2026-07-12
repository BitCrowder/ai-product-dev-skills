# Microinteraction Examples

## Invocation

```text
Use $microinteraction-motion-designer to make this mobile dashboard feel less stiff. Focus on loading, tab switching, chart updates, and button feedback.
```

## Compact Motion Plan

```markdown
| Moment | Pattern | Spec |
|---|---|---|
| Dashboard load | Skeleton shimmer + staggered entrance | Skeleton 1200ms shimmer; cards enter with 40ms stagger, 220ms ease-out |
| Tab switch | Sliding tabs + content crossfade | Indicator 220ms ease-out; content crossfades 180ms with 4px horizontal offset |
| Chart reveal | Chart growth | Bars grow from baseline over 700ms; labels count up in sync |
| Save action | State morph | Icon crossfades and button color transitions over 180ms; subtle scale 0.98 -> 1 |
```

## VibeCoding Prompt: Sliding Tabs

```text
请给当前 Tab 切换添加微动效，只改动 Tab 和内容切换相关代码，不要重写页面。

要求：
1. Tab 下方的指示条跟随当前选中项滑动，而不是瞬间跳转。
2. 指示条动画时长 220ms，使用 ease-out。
3. 内容区域切换时做 180ms 交叉淡入淡出，并带 4px 的轻微水平位移，方向与切换方向一致。
4. 用户快速连续点击 Tab 时，取消上一段动画并过渡到最新状态。
5. 支持 prefers-reduced-motion：关闭位移动画，只保留即时状态变化或非常短的 opacity 变化。
6. 不允许出现布局跳动、文字重叠或内容高度突变。

完成后请说明修改文件、动效参数和验证方式。
```

## VibeCoding Prompt: Spring Bottom Sheet

```text
请为底部抽屉面板添加带弹簧阻尼感的拖拽微动效。

要求：
1. 面板跟随手指拖拽，不能硬停。
2. 设置收起、半展开、全展开三个 snap points。
3. 超出边界时加入轻微 rubber-band 阻力。
4. 松手时根据拖拽速度和当前位置吸附到最近 snap point。
5. 弹簧要有阻尼感，不能夸张弹跳。
6. 背景遮罩 opacity 跟随展开程度变化。
7. 支持 reduced motion：禁用弹簧位移，直接切换到 snap point。

请只修改底部抽屉相关代码，保留现有业务逻辑。
```

## VibeCoding Prompt: Skeleton Loading

```text
请为当前加载状态添加骨架屏高光微动效。

要求：
1. 骨架形状必须匹配最终内容布局，真实内容出现时不能产生布局跳动。
2. 高光从左到右扫过，循环时长 1200ms，颜色对比要克制。
3. 数据加载完成后，骨架淡出 120ms，真实内容淡入 180ms。
4. 如果 prefers-reduced-motion 开启，关闭高光扫动，只显示静态骨架。
5. 不要为很小或瞬时加载区域添加过度动效。
```
