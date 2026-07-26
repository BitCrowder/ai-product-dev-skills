# Skill 仓库发布验证器使用指南

## 它解决什么问题

它把“目录看起来没问题”“我已经 push 了”变成可复跑的本地与远端证据，适合多 Skill 仓库的发布关卡。

## 为什么普通提示词容易失败

普通提示词往往只搜索 `SKILL.md`、忽略中文导航和分类重复，或把 Git transport 成功等同于远端已正确发布。它也容易在权限和网络失败时猜测原因。

## 适合谁使用

维护 Codex Skill 库的作者、负责发布的工程师，以及需要审核仓库交付证据的协作者。

## 使用前准备

准备仓库路径、预期 `OWNER/REPO`、默认分支、发布文件范围和写入授权。要使用 API 回退时，确认 `gh auth status` 已对目标仓库有效；没有这些信息时只进行本地检查。

## 推荐调用方式

说明本次发布的 base/候选提交、是否允许 push、目标远端与分支，并要求输出本地问题 JSON、提交范围和远端核验结论。先执行 `validate_skill_repo.py`，再逐 Skill 执行 `quick_validate.py`。

## 输入不足时会发生什么

缺少远端、分支、权限或网络时，输出应停在“本地通过但远端未验证”或“同步失败”，并列出缺少的输入或实际错误；不会承诺已经发布。

## 如何阅读输出

本地脚本的每项问题都含 `path`、`code` 和 `message`。发布报告再分别阅读提交 SHA、同步方法、远端默认分支/SHA/树和最终状态；三项远端证据不齐全时，不把状态读作成功。

## 如何与其他 Skill 串联

在 `issue-to-pr`、`test-generator`、`code-review-assistant` 和 `launch-readiness-checklist` 完成改动与证据后使用本 Skill，发布后可将准确状态交给 `stakeholder-update-writer`。

## 精简实际场景

20 个 Skill 完成 V2 文档更新后，维护者提供本地仓库、候选 SHA、`BitCrowder/ai-product-dev-skills` 和 `main`。本 Skill 先输出零问题的本地 JSON 和逐 Skill 校验，再只暂存批准文件；push 后读取 `main` SHA 与递归树。若树中缺少中文索引，则报告同步未验证完成并停止，而不是宣称发布成功。
