# kawaii-vscode-pylance

让 Pylance 的中文报错变得可爱一点。

参考 [Gary-0925/kawaii-vscode-cpptools](https://github.com/Gary-0925/kawaii-vscode-cpptools) 的 Pylance 实现。

```text
未定义“name”
→ 笨蛋！“name” 不定义就想用？你以为别的女孩子也会像我一样提醒你吗？

应为 ":"
→ 笨蛋！还要人家告诉你这里要写“:”吗？

类型“str”不可分配给声明的类型“int”
→ 不可以将“str”类型的值分配到声明为“int”的变量…你说你，气不气人呐
```

## 特性

- 269 条通用诊断设有独立文案：未定义、导入失败、缩进、括号、类型、参数、返回值等。
- 其余 396 条主要诊断保留技术原文，加上轻量语气词；合计覆盖 665 条 Pyright 主要中文诊断。
- 使用 Python 标准库，不需要安装依赖。

## Quick Start

下载并解压zip，在根目录执行：

```powershell
py -3 .\kawaii_pylance.py apply
```

配合 [Error Lens](https://github.com/usernamehw/vscode-error-lens) 使用体验更佳。

## 还原

```powershell
py -3 .\kawaii_pylance.py status
py -3 .\kawaii_pylance.py restore
```

如应用时指定了 `--extension`，状态和还原也使用同一路径。备份目录在pylance根目录 `.kawaii-pylance-backup`。

若想修改词库，先 `restore`再编辑 `patches/zh-cn.json`，然后重新应用。

## 自定义

编辑文件`patches/zh-cn.json` 

- `Diagnostic`：通用 Pyright 诊断键与手写文案。
- `PylanceDiagnostic`：Pylance 对通用诊断的独立覆盖文案。
- `fallbackPrefixes`：没有单独改写的主要诊断使用的语气前缀。

导出词库：

```powershell
py -3 .\kawaii_pylance.py export --output .\generated.zh-cn.json
```

## 测试

```powershell
py -3 -m unittest discover -s tests -v
```

## LICENSE

- 文案来源：[kawaii-vscode-cpptools](https://github.com/Gary-0925/kawaii-vscode-cpptools)。可对应的文案尽量沿用，涉及 Python 语义、格式参数或额外诊断信息时作最小必要适配。原作者署名与 MIT 许可证保留在 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
- 本地化架构参考：[Pyright localize.ts](https://github.com/microsoft/pyright/blob/main/packages/pyright-internal/src/localization/localize.ts)。Pyright 使用 MIT 许可证。
- Pylance 相关：[microsoft/pylance-release](https://github.com/microsoft/pylance-release)。本项目不包含或重新分发 Pylance 的程序 bundle、原始词库或修改后的扩展包。
- 本项目工具及原创文案采用 [MIT License](LICENSE)；复用部分的版权与许可证见第三方声明。
