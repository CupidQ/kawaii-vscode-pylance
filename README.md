# kawaii-vscode-pylance

让 Pylance 的中文报错变得可爱一点。

参考 [Gary-0925/kawaii-vscode-cpptools](https://github.com/Gary-0925/kawaii-vscode-cpptools) 的“替换中文诊断文案”思路，针对 Pylance 单独实现。不是微软官方项目。

```text
未定义“name”
→ 笨蛋！“name” 不定义就想用？你以为别的女孩子也会像我一样提醒你吗？

应为 ":"
→ 笨蛋！还要人家告诉你这里要写“:”吗？

类型“str”不可分配给声明的类型“int”
→ 不可以将“str”类型的值分配到声明为“int”的变量…你说你，气不气人呐
```

## 这版做了什么

- 269 条通用诊断设有独立文案：未定义、导入失败、缩进、括号、类型、参数、返回值等。
- 当前词库其余 396 条主要诊断保留技术原文，加上轻量语气词；合计覆盖 665 条 Pyright 主要中文诊断。
- 另外处理 Pylance 专属的两条导入失败提示，避免它们覆盖已改写的通用文案。
- 共 255 条文案复用或适配 C/C++ 原项目：13 条原句沿用、17 条仅替换占位符、126 条按 Python 语义适配、99 条套用句式。具体来源见 [COPY_REVIEW.md](COPY_REVIEW.md)。
- 补充诊断、代码操作、设置、其他语言词库保持原样。
- 校验所有 `{name}`、`{type}` 等占位符的名称及出现次数。
- 自动识别词库、预览、只读试运行、原文件备份、SHA-256 校验、重复应用保护及还原。
- 只使用 Python 标准库，不需要安装依赖。

这是一套本地补丁工具，不是 VSIX。Pylance 的词库嵌在 bundle 里，根目录的 `package.nls.zh-cn.json` 主要用于扩展界面，修改它不能替换这里的诊断。工具只更换识别出的中文词库数据，不改变诊断规则、严重级别、定位范围或代码修复逻辑。

## 快速使用

需要 Python 3.10+、VS Code、已安装的 Pylance 和 Python 扩展。安装中文语言包 `ms-ceintl.vscode-language-pack-zh-hans`，将 VS Code 的显示语言设为简体中文 `zh-cn`，并确认设置：

```json
{
  "python.analysis.displayEnglishDiagnostics": false
}
```

在此项目目录打开终端：

```powershell
# 查看前几条改写后的文案；不修改扩展
py -3 .\kawaii_pylance.py preview

# 检查兼容性和将修改的文件；不写入文件
py -3 .\kawaii_pylance.py apply --dry-run
```

确认预览后，保存工作并关闭 VS Code，再运行：

```powershell
py -3 .\kawaii_pylance.py apply
```

重新打开 VS Code，在 `examples` 目录查看故意写错的 Python 示例。安装 Error Lens 后，同一套修改后的诊断也可显示在行尾；是否显示仍受 Error Lens 的筛选设置影响。

自动查找仅适用于用户目录里恰好有一个 Pylance 安装目录的情况。有多个版本、便携版、WSL、SSH、容器等环境时，明确传入**实际运行语言服务器的那一侧**的扩展目录。例如：

```powershell
py -3 .\kawaii_pylance.py apply --dry-run --extension "C:\Users\你的用户名\.vscode\extensions\ms-python.vscode-pylance-版本号"
py -3 .\kawaii_pylance.py apply --extension "C:\Users\你的用户名\.vscode\extensions\ms-python.vscode-pylance-版本号"
```

不要把整个 `.vscode\extensions` 目录作为 `--extension` 的参数。

## 状态与还原

```powershell
py -3 .\kawaii_pylance.py status
py -3 .\kawaii_pylance.py restore
```

如应用时指定了 `--extension`，状态和还原也使用同一路径。

备份在目标 Pylance 目录内的 `.kawaii-pylance-backup`。不要手动删除它。还原前会验证全部备份与目标文件；遇到其他程序修改或文件损坏会停止，保留备份。还原后重新打开 VS Code。

相同词库重复执行 `apply` 不会叠加语气词。想修改词库时，先 `restore`，再编辑 `patches/zh-cn.json`，然后重新应用。

## 改写文案

`patches/zh-cn.json` 是主要编辑入口：

- `Diagnostic`：通用 Pyright 诊断键与手写文案。
- `PylanceDiagnostic`：Pylance 对通用诊断的独立覆盖文案。
- `fallbackPrefixes`：没有单独改写的主要诊断使用的语气前缀。

`patches/cpp-reuse.json` 记录采用的 C++ 原句及其数组下标。编辑这些条目时，也同步更新来源记录中的 `message` 和必要的适配说明，避免记录与实际文案不一致。

不要删除、重复或改名 `{name}` 等占位符；必须与对应原文完全一致。想保留某条原文，也可以在 `Diagnostic` 里为该键直接填写原文，以覆盖默认前缀。

可导出本机生成的完整通用词库作检查：

```powershell
py -3 .\kawaii_pylance.py export --output .\generated.zh-cn.json
```

导出文件不是 Pylance 可直接加载的外置语言包；实际应用仍需运行补丁。导出仅包括通用词库，Pylance 独立覆盖文案在 `PylanceDiagnostic` 中维护。已有输出文件不会被覆盖。

## 兼容性

开发时使用 Windows x64、VS Code 1.142.0、Pylance 2026.4.1。当前版本识别到 9 个包含相应词库的 bundle；不同版本数量可能不同。工具根据数据指纹识别词库，不依赖压缩变量名和固定偏移。

Pylance 更新通常会替换补丁。更新后先运行 `apply --dry-run`；词库结构、诊断键或占位符不兼容时会停止，不应绕过检查强行替换。不要把旧版本的整个 bundle 或备份复制进新版本目录。

只声明验证过的版本；其他版本、Insiders、远程和 Web 环境需要分别验证。`browser.*` 文件被识别和修改不代表已经在浏览器版 VS Code 验证运行。

## 测试

```powershell
py -3 -m unittest discover -s tests -v
```

测试覆盖：双层字符串编码、多个语言词库、同一 bundle 的两类中文词库、占位符丢失或重复、重复应用、精确还原、外部修改冲突、备份损坏、写入失败回滚和不安全的备份路径。

实际验证记录见 [VALIDATION.md](VALIDATION.md)。`examples/*.py` 故意包含错误，不能用于判断项目代码是否通过 Python 语法检查。

## 来源与许可

- 文案来源：[kawaii-vscode-cpptools](https://github.com/Gary-0925/kawaii-vscode-cpptools)。可对应的文案尽量沿用，涉及 Python 语义、格式参数或额外诊断信息时作最小必要适配。原作者署名与 MIT 许可证保留在 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
- 本地化架构参考：[Pyright localize.ts](https://github.com/microsoft/pyright/blob/main/packages/pyright-internal/src/localization/localize.ts)。Pyright 使用 MIT 许可证。
- Pylance 相关：[microsoft/pylance-release](https://github.com/microsoft/pylance-release)。本项目不包含或重新分发 Pylance 的程序 bundle、原始词库或修改后的扩展包。
- 本项目工具及原创文案采用 [MIT License](LICENSE)；复用部分的版权与许可证见第三方声明。
