# Pylance 文案核对稿 · 优先复用 C/C++ 原项目

本轮共 255 条复用或适配 C/C++ 原项目：13 条原句沿用、17 条仅替换占位符、126 条语义适配、99 条句式套用。

当前 665 条通用诊断中，269 条有独立文案，396 条保留原技术文案并添加前缀；另有 2 条 Pylance 专属文案。没有明确对应的 Python 专有规则，不冒充为 C++ 原句。

**编号保持上一份 667 条核对稿不变**，可以继续按原编号反馈。本稿列出 271 条独立文案，因此编号不连续。C++ 来源下标为 JSON 数组的 **0 起始下标**，与核对编号不同。

每条依次列出 Pylance 原文、当前文案、采用的 C++ 原句、适配说明与英文依据。占位符名称及出现次数已校验一致。此前 050 的精确数量、085 的静态方法措辞、666 的 yield 禁止含义已修正。

来源：[Gary-0925/kawaii-vscode-cpptools](https://github.com/Gary-0925/kawaii-vscode-cpptools)，许可证及署名见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。


### 001 · symbolIsUndefined

方式：语义适配

**Pylance 原中文**：未定义“{name}”

**当前文案**：笨蛋！“{name}” 不定义就想用？你以为别的女孩子也会像我一样提醒你吗？

**C++ 原句〔数组下标 20〕**：笨蛋！%sq 不声明就想用？你以为别的女孩子也会像我一样提醒你吗？

适配说明：将 C/C++ 的声明改为 Python 定义；其余原句沿用。

英文依据："{name}" is not defined

---

### 002 · symbolIsUnbound

方式：语义适配

**Pylance 原中文**：“{name}”未绑定

**当前文案**：“{name}”你只喊名字却不给它绑定值，人家怎么凭空把它变出来呀

**C++ 原句〔数组下标 114〕**：%n 你只喊名字却不给它定义，人家怎么凭空把它变出来呀

英文依据："{name}" is unbound

---

### 003 · symbolIsPossiblyUnbound

方式：语义适配

**Pylance 原中文**：“{name}”可能未绑定

**当前文案**：“{name}”可能还没绑定值呢，你只喊名字，人家怎么凭空把它变出来呀

**C++ 原句〔数组下标 114〕**：%n 你只喊名字却不给它定义，人家怎么凭空把它变出来呀

英文依据："{name}" is possibly unbound

---

### 004 · importResolveFailure

方式：语义适配

**Pylance 原中文**：无法解析导入“{importName}”

**当前文案**：唉，真是的…模块“{importName}”在哪里呀？人家找不到哦

**C++ 原句〔数组下标 3275〕**：唉，真是的…模块 %sq 的模块文件在哪里呀？人家找不到哦

英文依据：Import "{importName}" could not be resolved

---

### 005 · importSourceResolveFailure

方式：语义适配

**Pylance 原中文**：无法从源解析导入“{importName}”

**当前文案**：唉，真是的…模块“{importName}”的源文件在哪里呀？人家找不到哦

**C++ 原句〔数组下标 3275〕**：唉，真是的…模块 %sq 的模块文件在哪里呀？人家找不到哦

英文依据：Import "{importName}" could not be resolved from source

---

### 006 · importSymbolUnknown

方式：语义适配

**Pylance 原中文**：“{name}”是未知的导入符号

**当前文案**：导入里翻遍了，也没有“{name}”这个名字

**C++ 原句〔数组下标 282〕**：全局范围里翻遍了，也没有 %sq 这个名字

英文依据："{name}" is unknown import symbol

---

### 007 · duplicateImport

方式：占位符替换

**Pylance 原中文**：已多次导入“{importName}”

**当前文案**：小笨蛋，「“{importName}” 已导入」，人家看到了咯

**C++ 原句〔数组下标 3273〕**：小笨蛋，「%m 已导入」，人家看到了咯

英文依据："{importName}" is imported more than once

---

### 008 · stubFileMissing

方式：语义适配

**Pylance 原中文**：找不到 "{importName}" 的 Stub 文件

**当前文案**：唉，真是的…“{importName}”的类型 Stub 文件在哪里呀？人家找不到哦

**C++ 原句〔数组下标 3275〕**：唉，真是的…模块 %sq 的模块文件在哪里呀？人家找不到哦

英文依据：Stub file not found for "{importName}"

---

### 009 · expectedColon

方式：原句沿用

**Pylance 原中文**：应为 ":"

**当前文案**：笨蛋！还要人家告诉你这里要写“:”吗？

**C++ 原句〔数组下标 53〕**：笨蛋！还要人家告诉你这里要写“:”吗？

英文依据：Expected ":"

---

### 010 · expectedCloseParen

方式：原句沿用

**Pylance 原中文**："(" 未关闭

**当前文案**：笨蛋！还要人家告诉你这里要写“)”吗？

**C++ 原句〔数组下标 18〕**：笨蛋！还要人家告诉你这里要写“)”吗？

英文依据："(" was not closed

---

### 011 · expectedCloseBracket

方式：原句沿用

**Pylance 原中文**：“[”未关闭

**当前文案**：笨蛋！还要人家告诉你这里要写“]”吗？

**C++ 原句〔数组下标 17〕**：笨蛋！还要人家告诉你这里要写“]”吗？

英文依据："[" was not closed

---

### 012 · expectedCloseBrace

方式：原句沿用

**Pylance 原中文**："{" 未关闭

**当前文案**：笨蛋！还要人家告诉你这里要写“}”吗？

**C++ 原句〔数组下标 67〕**：笨蛋！还要人家告诉你这里要写“}”吗？

英文依据："{" was not closed

---

### 013 · expectedOpenParen

方式：原句沿用

**Pylance 原中文**：应为 "("

**当前文案**：笨蛋！还要人家告诉你这里要写“(”？

**C++ 原句〔数组下标 125〕**：笨蛋！还要人家告诉你这里要写“(”？

英文依据：Expected "("

---

### 014 · expectedIndentedBlock

方式：句式套用

**Pylance 原中文**：应为缩进块

**当前文案**：笨蛋！还要人家告诉你这里要写缩进块吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected indented block

---

### 015 · unexpectedIndent

方式：Python 专有改写

**Pylance 原中文**：意外缩进

**当前文案**：这行怎么突然缩进啦？人家差点跟丢了呢

英文依据：Unexpected indentation

---

### 016 · unexpectedUnindent

方式：Python 专有改写

**Pylance 原中文**：不应取消缩进

**当前文案**：先别取消缩进呀，这里还没到退回去的时候呢

英文依据：Unindent not expected

---

### 017 · inconsistentIndent

方式：Python 专有改写

**Pylance 原中文**：取消缩进量与以前的缩进不匹配

**当前文案**：退回去的缩进和前面对不上啦，帮人家排整齐嘛

英文依据：Unindent amount does not match previous indent

---

### 018 · stringUnterminated

方式：原句沿用

**Pylance 原中文**：字符串文本未终止

**当前文案**：唔…是不是缺了一个右引号呀？

**C++ 原句〔数组下标 8〕**：唔…是不是缺了一个右引号呀？

英文依据：String literal is unterminated

---

### 019 · unexpectedEof

方式：语义适配

**Pylance 原中文**：意外的 EOF

**当前文案**：嗳，文件意外结束啦

**C++ 原句〔数组下标 807〕**：嗳，默认参数表达式意外结束啦

英文依据：Unexpected EOF

---

### 020 · unexpectedExprToken

方式：语义适配

**Pylance 原中文**：表达式末尾出现意外标记

**当前文案**：就…就在表达式的预期结尾后面，是不是多了点东西呀

**C++ 原句〔数组下标 19〕**：就…就在编号的预期结尾后面，是不是多了点东西呀

英文依据：Unexpected token at end of expression

---

### 021 · expectedExpr

方式：原句沿用

**Pylance 原中文**：应为表达式

**当前文案**：这里要写表达式的啦，你个笨蛋

**C++ 原句〔数组下标 29〕**：这里要写表达式的啦，你个笨蛋

英文依据：Expected expression

---

### 022 · expectedIdentifier

方式：原句沿用

**Pylance 原中文**：预期标识符

**当前文案**：人家一下就看出来这里应该输入标识符了呢，小~杂~鱼~

**C++ 原句〔数组下标 40〕**：人家一下就看出来这里应该输入标识符了呢，小~杂~鱼~

英文依据：Expected identifier

---

### 023 · expectedFunctionName

方式：句式套用

**Pylance 原中文**：“def”后应为函数名称

**当前文案**：笨蛋！还要人家告诉你这里要写“def”后面的函数名吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected function name after "def"

---

### 024 · expectedClassName

方式：句式套用

**Pylance 原中文**：预期的类名

**当前文案**：笨蛋！还要人家告诉你这里要写类名吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected class name

---

### 025 · expectedParamName

方式：句式套用

**Pylance 原中文**：应为参数名称

**当前文案**：笨蛋！还要人家告诉你这里要写参数名吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected parameter name

---

### 026 · expectedMemberName

方式：语义适配

**Pylance 原中文**："." 后应为属性名称

**当前文案**：笨蛋！还要人家告诉你“.”后面要写属性名吗？

**C++ 原句〔数组下标 133〕**：笨蛋！还要人家告诉你这里要写成员名吗？

英文依据：Expected attribute name after "."

---

### 027 · expectedModuleName

方式：句式套用

**Pylance 原中文**：预期模块名称

**当前文案**：笨蛋！还要人家告诉你这里要写模块名吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected module name

---

### 028 · expectedImport

方式：句式套用

**Pylance 原中文**：应为 "import"

**当前文案**：笨蛋！还要人家告诉你这里要写“import”吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected "import"

---

### 029 · expectedImportSymbols

方式：句式套用

**Pylance 原中文**："import" 后应有一个或多个符号名称

**当前文案**：笨蛋！还要人家告诉你这里要写“import”后面的一个或多个名字吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected one or more symbol names after "import"

---

### 030 · expectedIn

方式：句式套用

**Pylance 原中文**：应为 "in"

**当前文案**：笨蛋！还要人家告诉你这里要写“in”吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected "in"

---

### 031 · expectedElse

方式：句式套用

**Pylance 原中文**：应为 "else"

**当前文案**：笨蛋！还要人家告诉你这里要写“else”吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected "else"

---

### 032 · expectedEquals

方式：句式套用

**Pylance 原中文**：应为 "="

**当前文案**：笨蛋！还要人家告诉你这里要写“=”吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected "="

---

### 033 · expectedNewline

方式：句式套用

**Pylance 原中文**：需要换行符

**当前文案**：笨蛋！还要人家告诉你这里要写换行符吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected newline

---

### 034 · expectedNewlineOrSemicolon

方式：句式套用

**Pylance 原中文**：语句必须用换行符或分号分隔

**当前文案**：笨蛋！还要人家告诉你这里要写分隔语句的换行符或分号吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Statements must be separated by newlines or semicolons

---

### 035 · expectedAssignRightHandExpr

方式：句式套用

**Pylance 原中文**：应为 “=” 右侧的表达式

**当前文案**：笨蛋！还要人家告诉你这里要写“=”右边的表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected expression to the right of "="

---

### 036 · expectedBinaryRightHandExpr

方式：句式套用

**Pylance 原中文**：应为运算符右侧的表达式

**当前文案**：笨蛋！还要人家告诉你这里要写运算符右边的表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected expression to the right of operator

---

### 037 · expectedFunctionAfterAsync

方式：句式套用

**Pylance 原中文**："async"后面应有函数定义

**当前文案**：笨蛋！还要人家告诉你这里要写“async”后面的函数定义吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected function definition after "async"

---

### 038 · expectedDecoratorNewline

方式：句式套用

**Pylance 原中文**：修饰器末尾应有新行

**当前文案**：笨蛋！还要人家告诉你这里要写装饰器后面的换行符吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected new line at end of decorator

---

### 039 · expectedAfterDecorator

方式：句式套用

**Pylance 原中文**：修饰器后应有函数或类声明

**当前文案**：笨蛋！还要人家告诉你这里要写装饰器后面的函数或类声明吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected function or class declaration after decorator

---

### 040 · expectedReturnExpr

方式：句式套用

**Pylance 原中文**：“return” 后应有表达式

**当前文案**：笨蛋！还要人家告诉你这里要写“return”后面的表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected expression after "return"

---

### 041 · argAssignment

方式：占位符替换

**Pylance 原中文**：无法将“{argType}”类型的参数分配给“{paramType}”类型的参数

**当前文案**：“{argType}” 类型的实参与 “{paramType}” 类型的形参？差得远呢，完全对不上嘛

**C++ 原句〔数组下标 167〕**：%t1 类型的实参与 %t2 类型的形参？差得远呢，完全对不上嘛

英文依据：Argument of type "{argType}" cannot be assigned to parameter of type "{paramType}"

---

### 042 · argAssignmentFunction

方式：语义适配

**Pylance 原中文**：无法将"{argType}"类型的参数分配给函数"{functionName}"中的"{paramType}"类型参数

**当前文案**：函数“{functionName}”里，“{argType}”类型的实参与“{paramType}”类型的形参？差得远呢，完全对不上嘛

**C++ 原句〔数组下标 167〕**：%t1 类型的实参与 %t2 类型的形参？差得远呢，完全对不上嘛

英文依据：Argument of type "{argType}" cannot be assigned to parameter of type "{paramType}" in function "{functionName}"

---

### 043 · argAssignmentParam

方式：语义适配

**Pylance 原中文**：无法将“{argType}”类型的参数分配给“{paramType}”类型的参数“{paramName}”

**当前文案**：“{argType}”类型的实参与“{paramType}”类型的形参“{paramName}”？差得远呢，完全对不上嘛

**C++ 原句〔数组下标 167〕**：%t1 类型的实参与 %t2 类型的形参？差得远呢，完全对不上嘛

英文依据：Argument of type "{argType}" cannot be assigned to parameter "{paramName}" of type "{paramType}"

---

### 044 · argAssignmentParamFunction

方式：语义适配

**Pylance 原中文**：无法将“{argType}”类型的参数分配给函数“{functionName}”中类型为“{paramType}”的参数“{paramName}”

**当前文案**：函数“{functionName}”里，“{argType}”类型的实参与“{paramType}”类型的形参“{paramName}”？差得远呢，完全对不上嘛

**C++ 原句〔数组下标 167〕**：%t1 类型的实参与 %t2 类型的形参？差得远呢，完全对不上嘛

英文依据：Argument of type "{argType}" cannot be assigned to parameter "{paramName}" of type "{paramType}" in function "{functionName}"

---

### 045 · argMissingForParam

方式：语义适配

**Pylance 原中文**：参数 {name} 缺少参数

**当前文案**：行啦行啦，参数 {name} 还没收到值呐！才不是担心你写不对呢

**C++ 原句〔数组下标 165〕**：行啦行啦，函数调用中的参数少得可怜呐！才不是担心你编译不过呢

英文依据：Argument missing for parameter {name}

---

### 046 · argMissingForParams

方式：语义适配

**Pylance 原中文**：参数 {names} 缺少参数

**当前文案**：行啦行啦，参数 {names} 还没收到值呐！才不是担心你写不对呢

**C++ 原句〔数组下标 165〕**：行啦行啦，函数调用中的参数少得可怜呐！才不是担心你编译不过呢

英文依据：Arguments missing for parameters {names}

---

### 047 · argPositionalExpectedCount

方式：语义适配

**Pylance 原中文**：应为 {expected} 个位置参数

**当前文案**：位置参数的个数不对啦，应该是 {expected} 个，个数要给人家对上哟

**C++ 原句〔数组下标 1941〕**：哈、哈啊？访问器函数的参数多得离谱了啦，个数要给人家对上哟

英文依据：Expected {expected} positional arguments

---

### 048 · argPositionalExpectedOne

方式：语义适配

**Pylance 原中文**：应为 1 个位置参数

**当前文案**：位置参数的个数不对啦，应该是 1 个，个数要给人家对上哟

**C++ 原句〔数组下标 1941〕**：哈、哈啊？访问器函数的参数多得离谱了啦，个数要给人家对上哟

英文依据：Expected 1 positional argument

---

### 049 · argMorePositionalExpectedCount

方式：语义适配

**Pylance 原中文**：预期还有 {expected} 个位置参数

**当前文案**：小杂鱼~位置参数太少了啦，还缺 {expected} 个呢

**C++ 原句〔数组下标 442〕**：小杂鱼~%nf 的参数太少了啦

英文依据：Expected {expected} more positional arguments

---

### 050 · argMorePositionalExpectedOne

方式：语义适配

**Pylance 原中文**：应为 1 个以上位置参数

**当前文案**：小杂鱼~位置参数太少了啦，还缺 1 个呢

**C++ 原句〔数组下标 442〕**：小杂鱼~%nf 的参数太少了啦

适配说明：英文是 Expected 1 more，保留精确的 1 个，不再写成“至少 1 个”。

英文依据：Expected 1 more positional argument

---

### 051 · argTypeUnknown

方式：Python 专有改写

**Pylance 原中文**：参数类型未知

**当前文案**：呜…这个实参的类型，人家还看不出来呢

英文依据：Argument type is unknown

---

### 052 · argTypePartiallyUnknown

方式：Python 专有改写

**Pylance 原中文**：参数类型部分未知

**当前文案**：这个实参的类型还有一部分不清楚呢，再帮人家看看嘛

英文依据：Argument type is partially unknown

---

### 053 · typeAssignmentMismatch

方式：语义适配

**Pylance 原中文**：类型“{sourceType}”不可分配给声明的类型“{destType}”

**当前文案**：不可以将“{sourceType}”类型的值分配到声明为“{destType}”的变量…你说你，气不气人呐

**C++ 原句〔数组下标 513〕**：不可以将 %t1 类型的值分配到 %t2 类型的实体…你说你，气不气人呐

英文依据：Type "{sourceType}" is not assignable to declared type "{destType}"

---

### 054 · returnTypeMismatch

方式：语义适配

**Pylance 原中文**：类型“{exprType}”不可分配给返回类型“{returnType}”

**当前文案**：欸…返回值类型“{exprType}”和声明的返回类型“{returnType}”这两边对不上啦，你打算让人家帮你拼起来吗

**C++ 原句〔数组下标 120〕**：欸…返回值类型和函数类型这两边对不上啦，你打算让人家帮你拼起来吗

英文依据：Type "{exprType}" is not assignable to return type "{returnType}"

---

### 055 · returnMissing

方式：语义适配

**Pylance 原中文**：所声明的返回类型为“{returnType}”的函数必须在所有代码路径上返回值

**当前文案**：返回类型为“{returnType}”的函数是要在每条代码路径上吐出返回值来的啦，你让人家空着手收？

**C++ 原句〔数组下标 117〕**：非 void 的 %n 是要吐出返回值来的啦，你让人家空着手收？

英文依据：Function with declared return type "{returnType}" must return value on all code paths

---

### 056 · returnOutsideFunction

方式：语义适配

**Pylance 原中文**：“return”只能在函数中使用

**当前文案**：不准在函数范围之外用 return 语句，人家给你三秒钟改好咯

**C++ 原句〔数组下标 2747〕**：不准在函数范围之外用 co_yield 表达式，人家给你三秒钟改好咯

英文依据："return" can be used only within a function

---

### 057 · breakOutsideLoop

方式：语义适配

**Pylance 原中文**：“break”只能在循环中使用

**当前文案**：break 只肯待在循环里哦，别的地方它是不认生的啦

**C++ 原句〔数组下标 116〕**：break 只肯待在循环或者开关里哦，别的地方它是不认生的啦

适配说明：移除 C/C++ switch 上下文；Python 的 match 不能作为 break 目标。

英文依据："break" can be used only within a loop

---

### 058 · continueOutsideLoop

方式：原句沿用

**Pylance 原中文**：“continue”只能在循环中使用

**当前文案**：continue 离开循环就活不了啦，乖乖把它放回循环里去

**C++ 原句〔数组下标 115〕**：continue 离开循环就活不了啦，乖乖把它放回循环里去

英文依据："continue" can be used only within a loop

---

### 059 · awaitNotInAsync

方式：语义适配

**Pylance 原中文**：仅允许在 async 函数内使用 "await"

**当前文案**：不准在 async 函数范围之外用 await 表达式，人家给你三秒钟改好咯

**C++ 原句〔数组下标 2747〕**：不准在函数范围之外用 co_yield 表达式，人家给你三秒钟改好咯

英文依据："await" allowed only within async function

---

### 060 · asyncNotInAsyncFunction

方式：语义适配

**Pylance 原中文**：不允许在 async 函数之外使用 "async"

**当前文案**：不准在 async 函数范围之外用 async，人家给你三秒钟改好咯

**C++ 原句〔数组下标 2747〕**：不准在函数范围之外用 co_yield 表达式，人家给你三秒钟改好咯

英文依据：Use of "async" not allowed outside of async function

---

### 061 · yieldOutsideFunction

方式：语义适配

**Pylance 原中文**：不允许在函数或 lambda 之外使用“yield”

**当前文案**：不准在函数或 lambda 范围之外用 yield 表达式，人家给你三秒钟改好咯

**C++ 原句〔数组下标 2747〕**：不准在函数范围之外用 co_yield 表达式，人家给你三秒钟改好咯

英文依据："yield" not allowed outside of a function or lambda

---

### 062 · unusedExpression

方式：原句沿用

**Pylance 原中文**：表达式值未使用

**当前文案**：这个表达式一个字都没干成，站在那儿好看吗？

**C++ 原句〔数组下标 174〕**：这个表达式一个字都没干成，站在那儿好看吗？

英文依据：Expression value is unused

---

### 063 · unusedCoroutine

方式：语义适配

**Pylance 原中文**：未使用 async 函数调用的结果; 请使用 "await" 或将结果分配给变量

**当前文案**：async 函数的调用结果没被用到，人家可不讲情面哦。用 await 或把结果交给变量嘛。别、别误会了，人家才不是特意帮你检查的！

**C++ 原句〔数组下标 1650〕**：没被用到调用结果，人家可不讲情面哦。别、别误会了，人家才不是特意帮你检查的！

英文依据：Result of async function call is not used; use "await" or assign result to variable

---

### 064 · unusedCallResult

方式：语义适配

**Pylance 原中文**：调用表达式的结果类型为 "{type}" 且未使用；如果这是有意为之，则分配给变量 “_”

**当前文案**：“{type}”类型的调用结果没被用到，人家可不讲情面哦。如果是故意的就交给“_”嘛。别、别误会了，人家才不是特意帮你检查的！

**C++ 原句〔数组下标 1650〕**：没被用到调用结果，人家可不讲情面哦。别、别误会了，人家才不是特意帮你检查的！

英文依据：Result of call expression is of type "{type}" and is not used; assign to variable "_" if this is intentional

---

### 065 · unaccessedImport

方式：语义适配

**Pylance 原中文**：未存取导入“{name}”

**当前文案**：欸？“{name}”已导入但写了却没被用到啦，它在角落里哭哦

**C++ 原句〔数组下标 177〕**：欸？%n 已声明但写了却没被用到啦，它在角落里哭哦

英文依据：Import "{name}" is not accessed

---

### 066 · unaccessedVariable

方式：占位符替换

**Pylance 原中文**：无法存取变量“{name}”

**当前文案**：欸？变量“{name}” 已声明但写了却没被用到啦，它在角落里哭哦

**C++ 原句〔数组下标 177〕**：欸？%n 已声明但写了却没被用到啦，它在角落里哭哦

英文依据：Variable "{name}" is not accessed

---

### 067 · unaccessedFunction

方式：占位符替换

**Pylance 原中文**：无法存取函数"{name}"

**当前文案**：欸？函数“{name}” 已声明但写了却没被用到啦，它在角落里哭哦

**C++ 原句〔数组下标 177〕**：欸？%n 已声明但写了却没被用到啦，它在角落里哭哦

英文依据：Function "{name}" is not accessed

---

### 068 · unaccessedClass

方式：占位符替换

**Pylance 原中文**：未存取类“{name}”

**当前文案**：欸？类“{name}” 已声明但写了却没被用到啦，它在角落里哭哦

**C++ 原句〔数组下标 177〕**：欸？%n 已声明但写了却没被用到啦，它在角落里哭哦

英文依据：Class "{name}" is not accessed

---

### 069 · unaccessedSymbol

方式：占位符替换

**Pylance 原中文**：未存取“{name}”

**当前文案**：欸？“{name}” 已声明但写了却没被用到啦，它在角落里哭哦

**C++ 原句〔数组下标 177〕**：欸？%n 已声明但写了却没被用到啦，它在角落里哭哦

英文依据："{name}" is not accessed

---

### 070 · typeNotIterable

方式：Python 专有改写

**Pylance 原中文**：“{type}”不可迭代

**当前文案**：“{type}”可不能迭代呀，小笨蛋别硬拉着它走嘛

英文依据："{type}" is not iterable

---

### 071 · typeNotSubscriptable

方式：Python 专有改写

**Pylance 原中文**：类型为“{type}”的对象不可下标

**当前文案**：“{type}”类型的对象不能用下标啦，别乱戳人家呀

英文依据：Object of type "{type}" is not subscriptable

---

### 072 · typeNotAwaitable

方式：Python 专有改写

**Pylance 原中文**："{type}" 并非 awaitable

**当前文案**：“{type}”不是 awaitable 呢，不能让它陪你 await 啦

英文依据："{type}" is not awaitable

---

### 073 · typeNotIntantiable

方式：语义适配

**Pylance 原中文**：无法实例化"{type}"

**当前文案**：“{type}”才不是可实例化的类型…行啦，接下来交给你自己呐

**C++ 原句〔数组下标 485〕**：%nf 才不是可实例化的实体…行啦，接下来交给你自己呐

英文依据："{type}" cannot be instantiated

---

### 074 · typeNotSupportBinaryOperator

方式：语义适配

**Pylance 原中文**：类型“{leftType}”和“{rightType}”不支持运算符“{operator}”

**当前文案**：和“{leftType}”“{rightType}”匹配的“{operator}”运算符？没有哦，一片空白啦

**C++ 原句〔数组下标 349〕**：和这些操作数匹配的 %sq 运算符？没有哦，一片空白啦

英文依据：Operator "{operator}" not supported for types "{leftType}" and "{rightType}"

---

### 075 · typeNotSupportUnaryOperator

方式：语义适配

**Pylance 原中文**：类型“{type}”不支持运算符“{operator}”

**当前文案**：和“{type}”匹配的“{operator}”一元运算符？没有哦，一片空白啦

**C++ 原句〔数组下标 349〕**：和这些操作数匹配的 %sq 运算符？没有哦，一片空白啦

英文依据：Operator "{operator}" not supported for type "{type}"

---

### 076 · typeUnknown

方式：Python 专有改写

**Pylance 原中文**："{name}"类型未知

**当前文案**：呜…人家还不知道“{name}”是什么类型呢

英文依据：Type of "{name}" is unknown

---

### 077 · typePartiallyUnknown

方式：Python 专有改写

**Pylance 原中文**：“{name}”的类型部分未知

**当前文案**：“{name}”的类型还有一部分不清楚呢，帮人家补全嘛

英文依据：Type of "{name}" is partially unknown

---

### 078 · tupleIndexOutOfRange

方式：语义适配

**Pylance 原中文**：类型 {type} 的索引 {index} 超出范围

**当前文案**：“{type}”的索引 {index} 把范围撑爆了啦，自己去裁一点啦

**C++ 原句〔数组下标 175〕**：下标把范围撑爆了啦，自己去裁一点啦

英文依据：Index {index} is out of range for type {type}

---

### 079 · duplicateParam

方式：语义适配

**Pylance 原中文**：参数“{name}”重复

**当前文案**：参数名“{name}”重样啦，两个一模一样的名字，人家喊谁好？

**C++ 原句〔数组下标 100〕**：参数名重样啦，两个一模一样的名字，人家喊谁好？

英文依据：Duplicate parameter "{name}"

---

### 080 · duplicateBaseClass

方式：原句沿用

**Pylance 原中文**：不允许重复的基类

**当前文案**：让我看看，「基类名重复」，人家看到了呀

**C++ 原句〔数组下标 263〕**：让我看看，「基类名重复」，人家看到了呀

英文依据：Duplicate base class not allowed

---

### 081 · constantRedefinition

方式：语义适配

**Pylance 原中文**：“{name}”是常量 (因为它是大写)且无法重新定义

**当前文案**：“{name}”因为名字全大写被视作常量啦，重定义这种小把戏，人家看都不看

**C++ 原句〔数组下标 46〕**：%no 早就被预定义过了啦，重定义这种小把戏，人家看都不看

英文依据："{name}" is constant (because it is uppercase) and cannot be redefined

---

### 082 · finalReassigned

方式：语义适配

**Pylance 原中文**："{name}"声明为 Final，无法重新分配

**当前文案**：“{name}”早就声明为 Final 了啦，重新赋值这种小把戏，人家看都不看

**C++ 原句〔数组下标 46〕**：%no 早就被预定义过了啦，重定义这种小把戏，人家看都不看

英文依据："{name}" is declared as Final and cannot be reassigned

---

### 083 · finalUnassigned

方式：语义适配

**Pylance 原中文**："{name}" 被声明为 Final，但未分配值

**当前文案**：Final 变量“{name}”少了初始值，人家也帮不了你呀

**C++ 原句〔数组下标 257〕**：常量 %n 少了初始值设定项，人家也帮不了你呀

英文依据："{name}" is declared Final, but value is not assigned

---

### 084 · classMethodClsParam

方式：Python 专有改写

**Pylance 原中文**：类方法应采用“cls”参数

**当前文案**：类方法要带上“cls”参数啦，别把它落下嘛

英文依据：Class methods should take a "cls" parameter

---

### 085 · staticClsSelfParam

方式：Python 专有改写

**Pylance 原中文**：静态方法不应采用“self”或“cls”参数

**当前文案**：静态方法的参数不该叫“self”或“cls”啦，小笨蛋再看看嘛

英文依据：Static methods should not take a "self" or "cls" parameter

---

### 086 · baseClassCircular

方式：语义适配

**Pylance 原中文**：类不能从自身派生

**当前文案**：唔…类？才不可以继承它自己啦，这一点没得商量咯

**C++ 原句〔数组下标 3272〕**：唔…模块？才不可以和自身有接口依赖关系啦，这一点没得商量咯

英文依据：Class cannot derive from itself

---

### 087 · recursiveDefinition

方式：语义适配

**Pylance 原中文**：无法确定“{name}”的类型，因为它引用其自身

**当前文案**：哼！“{name}”的类型推导依赖于它自己，人家没办法确定类型啦，这种小问题自己注意一下嘛

**C++ 原句〔数组下标 2421〕**：哼！%n 的初始值设定项的实例化依赖于其自身的值，这种小问题自己注意一下嘛

英文依据：Type of "{name}" could not be determined because it refers to itself

---

### 088 · tryWithoutExcept

方式：语义适配

**Pylance 原中文**：Try 语句必须至少有一个 except 或 finally 子句

**当前文案**：except 或 finally 子句呢？try 块至少要有一个，人家左看右看都没看到哦，你要是早听人家的，哪会走到这一步

**C++ 原句〔数组下标 2179〕**：一个 handler 或 finally 子句呢？try 块至少这边人家左看右看都没看到哦，你要是早听人家的，哪会走到这一步

英文依据：Try statement must have at least one except or finally clause

---

### 089 · zeroCaseStatementsFound

方式：Python 专有改写

**Pylance 原中文**：Match 语句必须至少包含一个 case 语句

**当前文案**：“match”里至少要有一个 case 啦，给人家一条可走的路嘛

英文依据：Match statement must include at least one case statement

---

### 090 · dictKeyValuePairs

方式：Python 专有改写

**Pylance 原中文**：字典条目必须包含键/值对

**当前文案**：字典条目要成对写好键和值啦，别让它们落单嘛

英文依据：Dictionary entries must contain key/value pairs

---

### 091 · formatStringUnterminated

方式：语义适配

**Pylance 原中文**：f 字符串中未终止的表达式；应为 "}"

**当前文案**：笨蛋！还要人家告诉你 f 字符串的表达式这里要写“}”吗？

**C++ 原句〔数组下标 67〕**：笨蛋！还要人家告诉你这里要写“}”吗？

英文依据：Unterminated expression in f-string; expecting "}"

---

### 092 · formatStringBrace

方式：句式套用

**Pylance 原中文**：f 字符串文本中不允许使用单个右大括号；使用双右大括号

**当前文案**：杂鱼~f 字符串里不允许单独写“}”，要写普通右大括号就用“}}”啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Single close brace not allowed within f-string literal; use double close brace

---

### 093 · stringUnsupportedEscape

方式：原句沿用

**Pylance 原中文**：字符串文本中不受支持的转义序列

**当前文案**：这个字符转义序列，人家翻遍了手册也没认出来

**C++ 原句〔数组下标 192〕**：这个字符转义序列，人家翻遍了手册也没认出来

英文依据：Unsupported escape sequence in string literal

---

### 094 · futureImportLocationNotAllowed

方式：语义适配

**Pylance 原中文**：从__future__导入必须位于文件的开头

**当前文案**：from __future__ 导入这边的要求是位于文件开头，别想蒙混过关嘛

**C++ 原句〔数组下标 3263〕**：全局模块片段声明这边的要求是位于任何其他声明以前，别想蒙混过关嘛

英文依据：Imports from __future__ must be at the beginning of the file

---

### 095 · codeTooComplexToAnalyze

方式：语义适配

**Pylance 原中文**：代码太复杂，无法分析；通过重构为子例程或减少条件代码路径来降低复杂性

**当前文案**：代码实在太复杂，没办法分析，拆成小函数或减少条件分支，下次先问过人家呐

**C++ 原句〔数组下标 143〕**：程序大得过分或实在太复杂，没办法编译，下次先问过人家呐

英文依据：Code is too complex to analyze; reduce complexity by refactoring into subroutines or reducing conditional code paths

---

### 096 · unreachableCodeStructure

方式：原句沿用

**Pylance 原中文**：代码在结构上无法访问

**当前文案**：这行语句被挡在路那头了啦，人家都走不过去

**C++ 原句〔数组下标 111〕**：这行语句被挡在路那头了啦，人家都走不过去

英文依据：Code is structurally unreachable

---

### 097 · unreachableCodeType

方式：语义适配

**Pylance 原中文**：类型分析指示代码不可访问

**当前文案**：类型分析确认这段代码被挡在路那头了啦，人家都走不过去

**C++ 原句〔数组下标 111〕**：这行语句被挡在路那头了啦，人家都走不过去

英文依据：Type analysis indicates code is unreachable

---

### 098 · unnecessaryTypeIgnore

方式：Python 专有改写

**Pylance 原中文**：不必要的 "# type: ignore" 注释

**当前文案**：这个“# type: ignore”用不上啦，人家已经确认过了哦

英文依据：Unnecessary "# type: ignore" comment

---

### 099 · unnecessaryPyrightIgnore

方式：Python 专有改写

**Pylance 原中文**：不必要的 "# pyright: ignore" 注释

**当前文案**：这个“# pyright: ignore”用不上啦，别多遮一层嘛

英文依据：Unnecessary "# pyright: ignore" comment

---

### 100 · importResolveNoEnvironment

方式：语义适配

**Pylance 原中文**：对于所选解释器，找不到导入“{importName}”。

**当前文案**：唉，真是的…当前选中的解释器里，模块“{importName}”在哪里呀？人家找不到哦

**C++ 原句〔数组下标 3275〕**：唉，真是的…模块 %sq 的模块文件在哪里呀？人家找不到哦

---

### 101 · importResolveRedirect

方式：语义适配

**Pylance 原中文**：在“{venv}”环境中找不到导入“{importName}”。

**当前文案**：唉，真是的…“{venv}”环境里，模块“{importName}”在哪里呀？人家找不到哦

**C++ 原句〔数组下标 3275〕**：唉，真是的…模块 %sq 的模块文件在哪里呀？人家找不到哦

---

### 102 · abstractMethodInvocation

方式：语义适配

**Pylance 原中文**：无法调用方法“{method}”，因为它是抽象的且未实施

**当前文案**：哼，笨蛋，抽象方法“{method}”还没实现，不允许调用啦

**C++ 原句〔数组下标 322〕**：哼，笨蛋，不允许使用抽象类类型 %t 的对象:

英文依据：Method "{method}" cannot be called because it is abstract and unimplemented

---

### 103 · annotatedMetadataInconsistent

方式：语义适配

**Pylance 原中文**：带批注的元数据类型“{metadataType}”与类型“{type}”不兼容

**当前文案**：额…元数据类型“{metadataType}”与类型“{type}”不兼容哦

**C++ 原句〔数组下标 42〕**：额…操作数类型不兼容哦(%t1 和 %t2)

英文依据：Annotated metadata type "{metadataType}" is not compatible with type "{type}"

---

### 113 · argPositional

方式：语义适配

**Pylance 原中文**：应为位置参数

**当前文案**：这里要的是位置参数哦，你以为谁都像你这么随手写咯

**C++ 原句〔数组下标 1266〕**：位置参数这边不、可以位于特性中的命名参数以后哦，你以为谁都像你这么随手写咯

英文依据：Expected positional argument

---

### 114 · assertAlwaysTrue

方式：语义适配

**Pylance 原中文**：断言表达式的计算结果始终为 true

**当前文案**：欸…情况是这样：断言表达式的计算结果始终为 True。不服气的话，把这行代码念三遍再说…

**C++ 原句〔数组下标 1573〕**：欸…情况是这样：数组的条件声明始终为 true。不服气的话，把这行代码念三遍再说…

英文依据：Assert expression always evaluates to true

---

### 122 · awaitIllegal

方式：句式套用

**Pylance 原中文**：使用 “await” 需要 Python 3.5 或更高版本

**当前文案**：欸？使用 “await” 要 Python 3.5 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Use of "await" requires Python 3.5 or newer

---

### 125 · baseClassFinal

方式：语义适配

**Pylance 原中文**：基类 "{type}" 被标记为 final 类，无法子类化

**当前文案**：不可以将标记为 final 的“{type}”用作基类，这一点没得商量哦

**C++ 原句〔数组下标 1904〕**：不可以将“final”类类型用作基类，这一点没得商量哦

英文依据：Base class "{type}" is marked final and cannot be subclassed

---

### 126 · baseClassIncompatible

方式：语义适配

**Pylance 原中文**：{type} 的基类相互不兼容

**当前文案**：额…“{type}”的基类类型互不兼容哦

**C++ 原句〔数组下标 42〕**：额…操作数类型不兼容哦(%t1 和 %t2)

英文依据：Base classes of {type} are mutually incompatible

---

### 128 · baseClassMethodTypeIncompatible

方式：语义适配

**Pylance 原中文**：类“{classType}”的基类以不兼容的方式定义方法“{name}”

**当前文案**：类“{classType}”的基类对“{name}”方法的定义？差得远呢，类型完全对不上嘛

**C++ 原句〔数组下标 147〕**：声明与 %nfd？差得远呢，完全对不上嘛。记住哦，这可是人家的独家提醒！

英文依据：Base classes for class "{classType}" define method "{name}" in incompatible way

---

### 130 · baseClassVariableTypeIncompatible

方式：语义适配

**Pylance 原中文**：类“{classType}”的基类以不兼容的方式定义变量“{name}”

**当前文案**：类“{classType}”的基类对“{name}”变量的定义？差得远呢，类型完全对不上嘛

**C++ 原句〔数组下标 147〕**：声明与 %nfd？差得远呢，完全对不上嘛。记住哦，这可是人家的独家提醒！

英文依据：Base classes for class "{classType}" define variable "{name}" in incompatible way

---

### 131 · binaryOperationNotAllowed

方式：句式套用

**Pylance 原中文**：类型表达式中不允许使用二元运算符

**当前文案**：杂鱼~类型表达式里不允许使用二元运算符的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Binary operator not allowed in type expression

---

### 134 · breakInExceptionGroup

方式：语义适配

**Pylance 原中文**："except*" 块中不允许 "break"

**当前文案**：“except*”块里不可以用 break 语句啦，别想蒙混过关呐

**C++ 原句〔数组下标 2182〕**：不可以在 finally 块中用 break 语句…行啦，接下来交给你自己呐

英文依据："break" is not allowed in an "except*" block

---

### 135 · bytesUnsupportedEscape

方式：语义适配

**Pylance 原中文**：bytes 文本中不受支持的转义序列

**当前文案**：这个 bytes 字符转义序列，人家翻遍了手册也没认出来

**C++ 原句〔数组下标 192〕**：这个字符转义序列，人家翻遍了手册也没认出来

英文依据：Unsupported escape sequence in bytes literal

---

### 136 · callableExtraArgs

方式：语义适配

**Pylance 原中文**："Callable"应只有两个类型参数

**当前文案**：Callable 的类型参数数目不合规矩，应该是两个，人家说一不二哦

**C++ 原句〔数组下标 1817〕**：“main”的参数数目不合规矩，应该是零个或两个参数，人家说一不二哦

英文依据：Expected only two type arguments to "Callable"

---

### 138 · callableNotInstantiable

方式：语义适配

**Pylance 原中文**：无法实例化类型“{type}”

**当前文案**：“{type}”才不是可实例化的类型…行啦，接下来交给你自己呐

**C++ 原句〔数组下标 485〕**：%nf 才不是可实例化的实体…行啦，接下来交给你自己呐

英文依据：Cannot instantiate type "{type}"

---

### 143 · classDefinitionCycle

方式：语义适配

**Pylance 原中文**：“{name}”的类定义取决于自身

**当前文案**：欸…情况是这样：类“{name}”的定义直接或间接依赖于它自己

**C++ 原句〔数组下标 2446〕**：欸…情况是这样：构造函数直接或间接委托给其自身

英文依据：Class definition for "{name}" depends on itself

---

### 148 · classPatternPositionalArgCount

方式：语义适配

**Pylance 原中文**：类“{type}”的位置模式太多; 应为 {expected}，但收到了 {received}

**当前文案**：哈、哈啊？类“{type}”的位置模式太多了啦，应该是 {expected} 个，你却给了 {received} 个，个数要给人家对上嘛

**C++ 原句〔数组下标 2154〕**：哈、哈啊？%nf 的参数多得离谱了啦，你个呆子，个数要给人家对上嘛。别、别误会了，人家才不是特意帮你检查的！

英文依据：Too many positional patterns for class "{type}"; expected {expected} but received {received}

---

### 151 · classTypeParametersIllegal

方式：句式套用

**Pylance 原中文**：类类型参数语法需要 Python 3.12 或更高版本

**当前文案**：欸？类类型参数语法要 Python 3.12 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Class type parameter syntax requires Python 3.12 or newer

---

### 153 · classVarNotAllowed

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用“ClassVar”

**当前文案**：杂鱼~这里不允许使用“ClassVar”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据："ClassVar" is not allowed in this context

---

### 155 · classVarTooManyArgs

方式：句式套用

**Pylance 原中文**：“ClassVar”后应只有一个类型参数

**当前文案**：ClassVar 后应只有一个类型参数，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

**C++ 原句〔数组下标 2218〕**：此强制转换应只有一个操作数表达式，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

英文依据：Expected only one type argument after "ClassVar"

---

### 158 · collectionAliasInstantiation

方式：语义适配

**Pylance 原中文**：无法实例化类型“{type}”，请改用“{alias}”

**当前文案**：“{type}”才不是可实例化的类型，改用“{alias}”嘛…行啦，接下来交给你自己呐

**C++ 原句〔数组下标 485〕**：%nf 才不是可实例化的实体…行啦，接下来交给你自己呐

英文依据：Type "{type}" cannot be instantiated, use "{alias}" instead

---

### 159 · comparisonAlwaysFalse

方式：语义适配

**Pylance 原中文**：条件的计算结果始终为 False，因为类型“{leftType}”和“{rightType}”没有重叠

**当前文案**：欸…情况是这样：“{leftType}”和“{rightType}”没有重叠，条件的计算结果始终为 False。不服气的话，把这行代码念三遍再说…

**C++ 原句〔数组下标 3243〕**：情况是这样：原子约束的计算结果为 false。这种程度就慌了？杂鱼！

英文依据：Condition will always evaluate to False since the types "{leftType}" and "{rightType}" have no overlap

---

### 160 · comparisonAlwaysTrue

方式：语义适配

**Pylance 原中文**：条件的计算结果始终为 True，因为类型“{leftType}”和“{rightType}”没有重叠

**当前文案**：欸…情况是这样：“{leftType}”和“{rightType}”没有重叠，条件的计算结果始终为 True。不服气的话，把这行代码念三遍再说…

**C++ 原句〔数组下标 1573〕**：欸…情况是这样：数组的条件声明始终为 true。不服气的话，把这行代码念三遍再说…

英文依据：Condition will always evaluate to True since the types "{leftType}" and "{rightType}" have no overlap

---

### 163 · concatenateContext

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用“Concatenate”

**当前文案**：杂鱼~这里不允许使用“Concatenate”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据："Concatenate" is not allowed in this context

---

### 167 · constructorParametersMismatch

方式：语义适配

**Pylance 原中文**：类“{classType}”中__new__和__init__的签名不匹配

**当前文案**：类“{classType}”中 __new__ 和 __init__ 的签名？差得远呢，完全对不上嘛。记住哦，这可是人家的独家提醒！

**C++ 原句〔数组下标 147〕**：声明与 %nfd？差得远呢，完全对不上嘛。记住哦，这可是人家的独家提醒！

英文依据：Mismatch between signature of __new__ and __init__ in class "{classType}"

---

### 168 · containmentAlwaysFalse

方式：语义适配

**Pylance 原中文**：表达式的计算结果始终为 False，因为类型“{leftType}”和“{rightType}”没有重叠

**当前文案**：欸…情况是这样：“{leftType}”和“{rightType}”没有重叠，表达式的计算结果始终为 False。不服气的话，把这行代码念三遍再说…

**C++ 原句〔数组下标 3243〕**：情况是这样：原子约束的计算结果为 false。这种程度就慌了？杂鱼！

英文依据：Expression will always evaluate to False since the types "{leftType}" and "{rightType}" have no overlap

---

### 169 · containmentAlwaysTrue

方式：语义适配

**Pylance 原中文**：表达式的计算结果始终为 True，因为类型“{leftType}”和“{rightType}”没有重叠

**当前文案**：欸…情况是这样：“{leftType}”和“{rightType}”没有重叠，表达式的计算结果始终为 True。不服气的话，把这行代码念三遍再说…

**C++ 原句〔数组下标 1573〕**：欸…情况是这样：数组的条件声明始终为 true。不服气的话，把这行代码念三遍再说…

英文依据：Expression will always evaluate to True since the types "{leftType}" and "{rightType}" have no overlap

---

### 170 · continueInExceptionGroup

方式：语义适配

**Pylance 原中文**："except*" 块中不允许 "continue"

**当前文案**：“except*”块里不可以用 continue 语句啦，别想蒙混过关呐

**C++ 原句〔数组下标 2183〕**：不可以在 finally 块中用 continue 语句…你说你，气不气人呐

英文依据："continue" is not allowed in an "except*" block

---

### 171 · coroutineInConditionalExpression

方式：语义适配

**Pylance 原中文**：始终计算结果为 True 的条件表达式引用协同例程

**当前文案**：欸…情况是这样：条件表达式引用了协程，计算结果始终为 True。不服气的话，把这行代码念三遍再说…

**C++ 原句〔数组下标 1573〕**：欸…情况是这样：数组的条件声明始终为 true。不服气的话，把这行代码念三遍再说…

英文依据：Conditional expression references coroutine which always evaluates to True

---

### 188 · dataProtocolInSubclassCheck

方式：句式套用

**Pylance 原中文**：issubclass 调用中不允许使用数据协议(包括非方法属性)

**当前文案**：杂鱼~issubclass 调用里不允许使用数据协议(包括非方法属性)的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Data protocols (which include non-method attributes) are not allowed in issubclass calls

---

### 192 · defaultValueNotAllowed

方式：语义适配

**Pylance 原中文**：“*”或“**”的参数不能有默认值

**当前文案**：喂——不许！“*”或“**”参数不可以带有默认值呐

**C++ 原句〔数组下标 1914〕**：喂——不许！参数包不可以里头有默认值呐

英文依据：Parameter with "*" or "**" cannot have default value

---

### 194 · deprecatedClass

方式：占位符替换

**Pylance 原中文**：类"{name}"已弃用

**当前文案**：对了，「类“{name}” 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The class "{name}" is deprecated

---

### 195 · deprecatedConstructor

方式：占位符替换

**Pylance 原中文**：类"{name}"的构造函数已弃用

**当前文案**：对了，「类“{name}”的构造函数 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The constructor for class "{name}" is deprecated

---

### 196 · deprecatedDescriptorDeleter

方式：占位符替换

**Pylance 原中文**：已弃用描述符“{name}”的“__delete__”方法

**当前文案**：对了，「描述符“{name}”的 __delete__ 方法 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The "__delete__" method for descriptor "{name}" is deprecated

---

### 197 · deprecatedDescriptorGetter

方式：占位符替换

**Pylance 原中文**：已弃用描述符“{name}”的“__get__”方法

**当前文案**：对了，「描述符“{name}”的 __get__ 方法 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The "__get__" method  for descriptor "{name}" is deprecated

---

### 198 · deprecatedDescriptorSetter

方式：占位符替换

**Pylance 原中文**：已弃用描述符“{name}”的“__set__”方法

**当前文案**：对了，「描述符“{name}”的 __set__ 方法 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The "__set__" method  for descriptor "{name}" is deprecated

---

### 199 · deprecatedFunction

方式：占位符替换

**Pylance 原中文**：函数“{name}”已弃用

**当前文案**：对了，「函数“{name}” 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The function "{name}" is deprecated

---

### 200 · deprecatedMethod

方式：占位符替换

**Pylance 原中文**：类“{className}”中的“{name}”方法已弃用

**当前文案**：对了，「类“{className}”中的方法“{name}” 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The method "{name}" in class "{className}" is deprecated

---

### 201 · deprecatedPropertyDeleter

方式：占位符替换

**Pylance 原中文**：已弃用 property "{name}" 的 deleter

**当前文案**：对了，「property“{name}”的 deleter 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The deleter for property "{name}" is deprecated

---

### 202 · deprecatedPropertyGetter

方式：占位符替换

**Pylance 原中文**：已弃用 property "{name}" 的 getter

**当前文案**：对了，「property“{name}”的 getter 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The getter for property "{name}" is deprecated

---

### 203 · deprecatedPropertySetter

方式：占位符替换

**Pylance 原中文**：已弃用 property "{name}" 的 setter

**当前文案**：对了，「property“{name}”的 setter 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

**C++ 原句〔数组下标 1215〕**：对了，「%n 已声明为弃用」，人家看到了啦。人家才不稀罕帮你，只是看不下去而已

英文依据：The setter for property "{name}" is deprecated

---

### 204 · deprecatedType

方式：语义适配

**Pylance 原中文**：自 Python {version} 起，此类型已弃用；请改用“{replacement}”

**当前文案**：又怎么了啦，此类型自 Python {version} 起已弃用 -- 改用“{replacement}”哦

**C++ 原句〔数组下标 2221〕**：又怎么了啦，访问说明符 %s1 已弃用 -- 改用 %s2 哦

英文依据：This type is deprecated as of Python {version}; use "{replacement}" instead

---

### 205 · dictExpandIllegalInComprehension

方式：句式套用

**Pylance 原中文**：推导式中不允许使用字典扩展

**当前文案**：杂鱼~推导式里不允许使用字典扩展的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Dictionary expansion not allowed in comprehension

---

### 206 · dictInAnnotation

方式：句式套用

**Pylance 原中文**：类型表达式中不允许使用字典表达式

**当前文案**：杂鱼~类型表达式里不允许使用字典表达式的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Dictionary expression not allowed in type expression

---

### 213 · duplicateArgsParam

方式：句式套用

**Pylance 原中文**：只允许一个 "*" 参数

**当前文案**：不可以写一个以上的“*”参数，人家可不讲情面呢

**C++ 原句〔数组下标 3267〕**：不可以声明一个以上的模块，人家可不讲情面呢

英文依据：Only one "*" parameter allowed

---

### 214 · duplicateCapturePatternTarget

方式：语义适配

**Pylance 原中文**：捕获目标“{name}”不能在同一模式中出现多次

**当前文案**：捕获目标“{name}”在同一模式里写了好几遍啦，名字一模一样，人家喊谁好？

**C++ 原句〔数组下标 100〕**：参数名重样啦，两个一模一样的名字，人家喊谁好？

英文依据：Capture target "{name}" cannot appear more than once within the same pattern

---

### 215 · duplicateCatchAll

方式：句式套用

**Pylance 原中文**：仅允许一个 catch-all except 子句

**当前文案**：不可以写一个以上的兜底 except 子句，人家可不讲情面呢

**C++ 原句〔数组下标 3267〕**：不可以声明一个以上的模块，人家可不讲情面呢

英文依据：Only one catch-all except clause allowed

---

### 216 · duplicateEnumMember

方式：语义适配

**Pylance 原中文**：Enum 成员 "{name}" 已声明

**当前文案**：“{name}”在这个 Enum 里早就登记过了啦，同名的人家可不再收

**C++ 原句〔数组下标 101〕**：%sq 在这个范围里早就登记过了啦，同名的人家可不再收

英文依据：Enum member "{name}" is already declared

---

### 217 · duplicateGenericAndProtocolBase

方式：句式套用

**Pylance 原中文**：只允许一个 Generic[...] 或 Protocol[...] 基类

**当前文案**：不可以写一个以上的Generic[...] 或 Protocol[...] 基类，人家可不讲情面呢

**C++ 原句〔数组下标 3267〕**：不可以声明一个以上的模块，人家可不讲情面呢

英文依据：Only one Generic[...] or Protocol[...] base class allowed

---

### 218 · duplicateKeywordOnly

方式：句式套用

**Pylance 原中文**：只允许一个“*”分隔符

**当前文案**：不可以写一个以上的“*”分隔符，人家可不讲情面呢

**C++ 原句〔数组下标 3267〕**：不可以声明一个以上的模块，人家可不讲情面呢

英文依据：Only one "*" separator allowed

---

### 219 · duplicateKwargsParam

方式：句式套用

**Pylance 原中文**：仅允许一个 “**” 参数

**当前文案**：不可以写一个以上的“**”参数，人家可不讲情面呢

**C++ 原句〔数组下标 3267〕**：不可以声明一个以上的模块，人家可不讲情面呢

英文依据：Only one "**" parameter allowed

---

### 220 · duplicatePositionOnly

方式：句式套用

**Pylance 原中文**：只允许一个“/”参数

**当前文案**：不可以写一个以上的“/”分隔符，人家可不讲情面呢

**C++ 原句〔数组下标 3267〕**：不可以声明一个以上的模块，人家可不讲情面呢

英文依据：Only one "/" parameter allowed

---

### 221 · duplicateStarPattern

方式：句式套用

**Pylance 原中文**：模式序列中只允许一个“*”模式

**当前文案**：不可以写一个以上的序列里的“*”模式，人家可不讲情面呢

**C++ 原句〔数组下标 3267〕**：不可以声明一个以上的模块，人家可不讲情面呢

英文依据：Only one "*" pattern allowed in a pattern sequence

---

### 222 · duplicateStarStarPattern

方式：句式套用

**Pylance 原中文**：只允许一个“**”条目

**当前文案**：不可以写一个以上的“**”条目，人家可不讲情面呢

**C++ 原句〔数组下标 3267〕**：不可以声明一个以上的模块，人家可不讲情面呢

英文依据：Only one "**" entry allowed

---

### 223 · duplicateUnpack

方式：句式套用

**Pylance 原中文**：list 中仅允许一个解包操作

**当前文案**：不可以写一个以上的list 里的解包操作，人家可不讲情面呢

**C++ 原句〔数组下标 3267〕**：不可以声明一个以上的模块，人家可不讲情面呢

英文依据：Only one unpack operation allowed in list

---

### 227 · enumClassOverride

方式：语义适配

**Pylance 原中文**：Enum 类 "{name}" 是 final 类，无法子类化

**当前文案**：不可以将 final 的 Enum 类“{name}”用作基类，这一点没得商量哦

**C++ 原句〔数组下标 1904〕**：不可以将“final”类类型用作基类，这一点没得商量哦

英文依据：Enum class "{name}" is final and cannot be subclassed

---

### 235 · exceptionGroupIncompatible

方式：句式套用

**Pylance 原中文**：异常组语法 ("except*") 需要 Python 3.11 或更高版本

**当前文案**：欸？异常组语法 ("except*") 要 Python 3.11 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Exception group syntax ("except*") requires Python 3.11 or newer

---

### 240 · expectedArrow

方式：句式套用

**Pylance 原中文**：应为“->”，后跟返回类型批注

**当前文案**：笨蛋！还要人家告诉你这里要写“->”和后面的返回类型批注吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected "->" followed by return type annotation

---

### 241 · expectedAsAfterException

方式：句式套用

**Pylance 原中文**：异常类型后应为“as”

**当前文案**：笨蛋！还要人家告诉你这里要写异常类型后面的“as”吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected "as" after exception type

---

### 242 · expectedBoolLiteral

方式：语义适配

**Pylance 原中文**：应为 True 或 False

**当前文案**：应该是“True”或“False”，这里人家说了算嘛

**C++ 原句〔数组下标 1040〕**：应该是“ON”、“OFF”或“DEFAULT”，这里人家说了算嘛

英文依据：Expected True or False

---

### 243 · expectedCase

方式：句式套用

**Pylance 原中文**：应为 “case” 语句

**当前文案**：笨蛋！还要人家告诉你这里要写“case”语句吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected "case" statement

---

### 244 · expectedComplexNumberLiteral

方式：句式套用

**Pylance 原中文**：模式匹配的预期复数文本

**当前文案**：笨蛋！还要人家告诉你这里要写模式匹配中的复数字面量吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected complex number literal for pattern matching

---

### 246 · expectedDecoratorName

方式：句式套用

**Pylance 原中文**：预期的修饰器名称

**当前文案**：笨蛋！还要人家告诉你这里要写装饰器名吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected decorator name

---

### 247 · expectedDelExpr

方式：句式套用

**Pylance 原中文**："del"后应为表达式

**当前文案**：笨蛋！还要人家告诉你这里要写“del”后面的表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected expression after "del"

---

### 248 · expectedExceptionClass

方式：语义适配

**Pylance 原中文**：异常类或对象无效

**当前文案**：异常类或对象不管用的哦，白费劲呐

**C++ 原句〔数组下标 264〕**：基类才不管用的哦，白费劲呐

英文依据：Invalid exception class or object

---

### 249 · expectedExceptionObj

方式：语义适配

**Pylance 原中文**：应为异常对象、异常类或 None

**当前文案**：欸？应该是异常对象、异常类或 None，自己承认一下吧

**C++ 原句〔数组下标 1423〕**：欸？应该是类、结构或联合类型，自己承认一下吧

英文依据：Expected exception object, exception class or None

---

### 250 · expectedImportAlias

方式：句式套用

**Pylance 原中文**：应为 “as” 后面的符号

**当前文案**：笨蛋！还要人家告诉你这里要写“as”后面的符号吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected symbol after "as"

---

### 251 · expectedInExpr

方式：句式套用

**Pylance 原中文**："in"后应为表达式

**当前文案**：笨蛋！还要人家告诉你这里要写“in”后面的表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected expression after "in"

---

### 252 · expectedNameAfterAs

方式：句式套用

**Pylance 原中文**："as" 后应有符号名

**当前文案**：笨蛋！还要人家告诉你这里要写“as”后面的符号名吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected symbol name after "as"

---

### 254 · expectedPatternExpr

方式：句式套用

**Pylance 原中文**：预期的模式表达式

**当前文案**：笨蛋！还要人家告诉你这里要写模式表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected pattern expression

---

### 255 · expectedPatternSubjectExpr

方式：句式套用

**Pylance 原中文**：预期的模式主题表达式

**当前文案**：笨蛋！还要人家告诉你这里要写模式的主体表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected pattern subject expression

---

### 256 · expectedPatternValue

方式：句式套用

**Pylance 原中文**：应为 “a.b”形式的模式值表达式

**当前文案**：笨蛋！还要人家告诉你这里要写“a.b”形式的模式值表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected pattern value expression of the form "a.b"

---

### 257 · expectedSliceIndex

方式：句式套用

**Pylance 原中文**：预期索引或切片表达式

**当前文案**：笨蛋！还要人家告诉你这里要写索引或切片表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected index or slice expression

---

### 258 · expectedTypeNotString

方式：语义适配

**Pylance 原中文**：应为类型，但收到字符串文本

**当前文案**：哈？这里应该是类型，你却写了字符串字面量啦，你写成什么了哟

**C++ 原句〔数组下标 3754〕**：哈？参数类型不对(这里应该是 %t)啦，你写成什么了哟

英文依据：Expected type but received a string literal

---

### 259 · expectedTypeParameterName

方式：句式套用

**Pylance 原中文**：应为类型参数名称

**当前文案**：笨蛋！还要人家告诉你这里要写类型参数名吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected type parameter name

---

### 260 · expectedYieldExpr

方式：句式套用

**Pylance 原中文**：yield 语句中的预期表达式

**当前文案**：笨蛋！还要人家告诉你这里要写yield 语句里的表达式吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

适配说明：沿用原项目“还要人家告诉你这里要写…”句式，保留 Python 所缺成分。

英文依据：Expected expression in yield statement

---

### 261 · finalClassIsAbstract

方式：语义适配

**Pylance 原中文**：类“{type}”被标记为 final，并且必须实现所有抽象符号

**当前文案**：哼，笨蛋，类“{type}”都标记为 final 了，还得实现所有抽象成员啦

**C++ 原句〔数组下标 322〕**：哼，笨蛋，不允许使用抽象类类型 %t 的对象:

英文依据：Class "{type}" is marked final and must implement all abstract symbols

---

### 264 · finalMethodOverride

方式：语义适配

**Pylance 原中文**：方法 "{name}" 无法替代在类 "{className}" 中定义的 final 方法

**当前文案**：哈？重写类“{className}”中标记为 final 的方法“{name}”这种事，人家现在做不到哦

**C++ 原句〔数组下标 1850〕**：哈？重写“final”%nd 这种事，人家现在做不到哦

英文依据：Method "{name}" cannot override final method defined in class "{className}"

---

### 265 · finalNonMethod

方式：语义适配

**Pylance 原中文**：不能将函数“{name}”标记为 @final，因为它不是方法

**当前文案**：不可以用 @final 修饰器标记函数“{name}”，它不是方法，人家可不讲情面呢

**C++ 原句〔数组下标 2614〕**：不可以用 "final" 修饰符声明非虚函数，人家可不讲情面呢

英文依据：Function "{name}" cannot be marked @final because it is not a method

---

### 268 · finalTooManyArgs

方式：句式套用

**Pylance 原中文**：“Final”后应为单个类型参数

**当前文案**：Final 后应只有一个类型参数，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

**C++ 原句〔数组下标 2218〕**：此强制转换应只有一个操作数表达式，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

英文依据：Expected a single type argument after "Final"

---

### 269 · finallyBreak

方式：语义适配

**Pylance 原中文**：“break” 不能用于退出 “finally” 块

**当前文案**：不可以用 break 语句退出 finally 块…行啦，接下来交给你自己呐

**C++ 原句〔数组下标 2182〕**：不可以在 finally 块中用 break 语句…行啦，接下来交给你自己呐

适配说明：只禁止退出 finally；不把 finally 内部嵌套循环中的合法 break/continue 一并禁止。

英文依据：A "break" cannot be used to exit a "finally" block

---

### 270 · finallyContinue

方式：语义适配

**Pylance 原中文**：“continue” 不能用于退出 “finally” 块

**当前文案**：不可以用 continue 语句退出 finally 块…你说你，气不气人呐

**C++ 原句〔数组下标 2183〕**：不可以在 finally 块中用 continue 语句…你说你，气不气人呐

适配说明：只禁止退出 finally；不把 finally 内部嵌套循环中的合法 break/continue 一并禁止。

英文依据：A "continue" cannot be used to exit a "finally" block

---

### 271 · finallyReturn

方式：语义适配

**Pylance 原中文**：“return” 不能用于退出 “finally” 块

**当前文案**：不可以用 return 语句退出 finally 块啦，你还想装没看见吗

**C++ 原句〔数组下标 2178〕**：不准 finally 块内有 return 语句啦，你还想装没看见吗

适配说明：只禁止退出 finally；不把 finally 内部嵌套循环中的合法 break/continue 一并禁止。

英文依据：A "return" cannot be used to exit a "finally" block

---

### 273 · formatStringDebuggingIllegal

方式：句式套用

**Pylance 原中文**：F 字符串调试说明符“=”需要 Python 3.8 或更高版本

**当前文案**：欸？F 字符串调试说明符“=”要 Python 3.8 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：F-string debugging specifier "=" requires Python 3.8 or newer

---

### 274 · formatStringEscape

方式：句式套用

**Pylance 原中文**：Python 3.12 之前 f 字符串的表达式部分中不允许使用转义序列(反斜杠)

**当前文案**：杂鱼~Python 3.12 之前 f 字符串的表达式部分里不允许使用转义序列(反斜杠)的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Escape sequence (backslash) not allowed in expression portion of f-string prior to Python 3.12

---

### 276 · formatStringIllegal

方式：句式套用

**Pylance 原中文**：格式化字符串文本(f 字符串)需要 Python 3.6 或更高版本

**当前文案**：欸？格式化字符串文本(f 字符串)要 Python 3.6 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Format string literals (f-strings) require Python 3.6 or newer

---

### 277 · formatStringInPattern

方式：句式套用

**Pylance 原中文**：模式中不允许使用格式字符串

**当前文案**：杂鱼~模式里不允许使用格式字符串的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Format string not allowed in pattern

---

### 283 · functionInConditionalExpression

方式：语义适配

**Pylance 原中文**：始终计算结果为 True 的条件表达式引用函数

**当前文案**：欸…情况是这样：条件表达式引用了函数，计算结果始终为 True。不服气的话，把这行代码念三遍再说…

**C++ 原句〔数组下标 1573〕**：欸…情况是这样：数组的条件声明始终为 true。不服气的话，把这行代码念三遍再说…

英文依据：Conditional expression references function which always evaluates to True

---

### 284 · functionTypeParametersIllegal

方式：句式套用

**Pylance 原中文**：函数类型参数语法需要 Python 3.12 或更高版本

**当前文案**：欸？函数类型参数语法要 Python 3.12 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Function type parameter syntax requires Python 3.12 or newer

---

### 294 · genericTypeArgMissing

方式：句式套用

**Pylance 原中文**：“Generic”至少需要一个类型参数

**当前文案**：笨蛋！还要人家告诉你 Generic 后面至少要写一个类型参数吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

英文依据："Generic" requires at least one type argument

---

### 295 · genericTypeArgTypeVar

方式：语义适配

**Pylance 原中文**：“Generic”的类型参数必须是类型变量

**当前文案**：Generic 的类型参数只能是类型变量，下次先问过人家哦

**C++ 原句〔数组下标 2107〕**：泛型只能有类型参数，下次先问过人家哦

英文依据：Type argument for "Generic" must be a type variable

---

### 296 · genericTypeArgUnique

方式：语义适配

**Pylance 原中文**：“Generic”的类型参数必须是唯一

**当前文案**：Generic 的类型参数重样啦，一模一样的名字，人家喊谁好？

**C++ 原句〔数组下标 100〕**：参数名重样啦，两个一模一样的名字，人家喊谁好？

英文依据：Type arguments for "Generic" must be unique

---

### 302 · incompatibleMethodOverride

方式：语义适配

**Pylance 原中文**：方法“{name}”以不兼容的方式替代类“{className}”

**当前文案**：方法“{name}”对类“{className}”中同名方法的重写？差得远呢，类型完全对不上嘛。记住哦，这可是人家的独家提醒！

**C++ 原句〔数组下标 147〕**：声明与 %nfd？差得远呢，完全对不上嘛。记住哦，这可是人家的独家提醒！

英文依据：Method "{name}" overrides class "{className}" in an incompatible manner

---

### 305 · initMustReturnNone

方式：语义适配

**Pylance 原中文**：“__init__”的返回类型必须为 None

**当前文案**：等等！“__init__”的返回类型要是写成 None 以外的类型，人家可要先炸给你看啦

**C++ 原句〔数组下标 278〕**：等等！构造函数或析构函数要是返回值，人家可要先炸给你看啦

英文依据：Return type of "__init__" must be None

---

### 308 · initVarNotAllowed

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用“InitVar”

**当前文案**：杂鱼~这里不允许使用“InitVar”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据："InitVar" is not allowed in this context

---

### 311 · instantiateAbstract

方式：语义适配

**Pylance 原中文**：无法实例化抽象类“{type}”

**当前文案**：哼，笨蛋，不允许实例化抽象类“{type}”啦

**C++ 原句〔数组下标 322〕**：哼，笨蛋，不允许使用抽象类类型 %t 的对象:

英文依据：Cannot instantiate abstract class "{type}"

---

### 328 · lazyImportIllegal

方式：句式套用

**Pylance 原中文**：延迟导入语句需要 Python 3.15 或更高版本

**当前文案**：欸？延迟导入语句要 Python 3.15 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Lazy import statement requires Python 3.15 or newer

---

### 331 · listInAnnotation

方式：句式套用

**Pylance 原中文**：类型表达式中不允许使用 List 表达式

**当前文案**：杂鱼~类型表达式里不允许使用 List 表达式的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：List expression not allowed in type expression

---

### 335 · literalNotCallable

方式：语义适配

**Pylance 原中文**：无法实例化 Literal 类型

**当前文案**：Literal 才不是可实例化的类型…行啦，接下来交给你自己呐

**C++ 原句〔数组下标 485〕**：%nf 才不是可实例化的实体…行啦，接下来交给你自己呐

英文依据：Literal type cannot be instantiated

---

### 337 · matchIncompatible

方式：句式套用

**Pylance 原中文**：Match 语句需要 Python 3.10 或更高版本

**当前文案**：欸？Match 语句要 Python 3.10 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Match statements require Python 3.10 or newer

---

### 339 · maxParseDepthExceeded

方式：语义适配

**Pylance 原中文**：超出最大分析深度;将表达式分解为较小的子表达式

**当前文案**：表达式嵌套太深太复杂，超过最大分析深度啦，人家没办法分析了，拆成小一点的子表达式再来见人家呐

**C++ 原句〔数组下标 143〕**：程序大得过分或实在太复杂，没办法编译，下次先问过人家呐

英文依据：Maximum parse depth exceeded; break expression into smaller sub-expressions

---

### 340 · memberAccess

方式：语义适配

**Pylance 原中文**：无法访问类“{type}”的属性“{name}”

**当前文案**：类型“{type}”的属性“{name}”不可访问，你要干嘛

**C++ 原句〔数组下标 330〕**：%nfd 不可访问，你要干嘛

适配说明：只说不可访问，不擅自断言属性不存在。

英文依据：Cannot access attribute "{name}" for class "{type}"

---

### 346 · methodNotDefined

方式：语义适配

**Pylance 原中文**：未定义“{name}”方法

**当前文案**：笨蛋！“{name}”方法不定义就想用？你以为别的女孩子也会像我一样提醒你吗？

**C++ 原句〔数组下标 20〕**：笨蛋！%sq 不声明就想用？你以为别的女孩子也会像我一样提醒你吗？

英文依据："{name}" method not defined

---

### 347 · methodNotDefinedOnType

方式：语义适配

**Pylance 原中文**：未在类型"{type}"上定义"{name}"方法

**当前文案**：杂鱼~类型“{type}”都没有“{name}”方法的啦

**C++ 原句〔数组下标 135〕**：杂鱼~%n 都没有成员 %sq 的啦

英文依据："{name}" method not defined on type "{type}"

---

### 358 · namedTupleEmptyName

方式：语义适配

**Pylance 原中文**：命名 tuple 中的名称不能为空

**当前文案**：一定要用非空名称声明 NamedTuple，别想蒙混过关啦

**C++ 原句〔数组下标 3269〕**：一定要用非空名称声明模块，别想蒙混过关啦

英文依据：Names within a named tuple cannot be empty

---

### 365 · namedTupleNameUnique

方式：语义适配

**Pylance 原中文**：命名的 tuple 中的名称必须唯一

**当前文案**：命名 tuple 里的名称重样啦，两个一模一样的名字，人家喊谁好？

**C++ 原句〔数组下标 100〕**：参数名重样啦，两个一模一样的名字，人家喊谁好？

英文依据：Names within a named tuple must be unique

---

### 374 · newTypeParamCount

方式：语义适配

**Pylance 原中文**：NewType 需要两个位置参数

**当前文案**：NewType 的参数数目不合规矩，应该是两个位置参数，人家说一不二哦

**C++ 原句〔数组下标 1817〕**：“main”的参数数目不合规矩，应该是零个或两个参数，人家说一不二哦

英文依据：NewType requires two positional arguments

---

### 380 · nonDefaultAfterDefault

方式：语义适配

**Pylance 原中文**：非默认参数遵循默认参数

**当前文案**：没有默认值的位置参数要排在有默认值的位置参数前面哦，你插在后面算怎么回事

**C++ 原句〔数组下标 306〕**：默认实参要待在形参列表的最后哦，你插在中间算怎么回事

适配说明：保留 Python 位置参数的默认值顺序约束，不推广到可自由排列默认值的仅关键字参数。

英文依据：Non-default argument follows default argument

---

### 381 · nonLocalInModule

方式：语义适配

**Pylance 原中文**：模块级不允许使用 nonlocal 声明

**当前文案**：不准在模块级用 nonlocal 声明，这里人家说了算哦！自己乖乖改掉，改完再来见人家…

**C++ 原句〔数组下标 394〕**：不准引用封闭函数的局部变量，这里人家说了算哦！自己乖乖改掉，改完再来见人家…

英文依据：Nonlocal declaration not allowed at module level

---

### 393 · notRequiredArgCount

方式：句式套用

**Pylance 原中文**：“NotRequired” 之后应为单个类型参数

**当前文案**：NotRequired 后应只有一个类型参数，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

**C++ 原句〔数组下标 2218〕**：此强制转换应只有一个操作数表达式，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

英文依据：Expected a single type argument after "NotRequired"

---

### 394 · notRequiredNotInTypedDict

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用“NotRequired”

**当前文案**：杂鱼~这里不允许使用“NotRequired”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据："NotRequired" is not allowed in this context

---

### 421 · paramAfterKwargsParam

方式：语义适配

**Pylance 原中文**：参数不能跟随“**”参数

**当前文案**：欸？“**”参数一定要是最后一个参数啦，这点常识还要人家教嘛

**C++ 原句〔数组下标 2191〕**：欸？%[C++/CLI] 参数数组一定要是最后一个参数啦，这点常识还要人家教嘛

英文依据：Parameter cannot follow "**" parameter

---

### 422 · paramAlreadyAssigned

方式：语义适配

**Pylance 原中文**：已分配参数“{name}”

**当前文案**：欸…情况是这样：参数“{name}”早就赋过值了

**C++ 原句〔数组下标 148〕**：欸…情况是这样：%n 早就初始化过了

英文依据：Parameter "{name}" is already assigned

---

### 424 · paramAssignmentMismatch

方式：占位符替换

**Pylance 原中文**：无法将"{sourceType}"类型的表达式分配给"{paramType}"类型的参数

**当前文案**：“{sourceType}” 类型的实参与 “{paramType}” 类型的形参？差得远呢，完全对不上嘛

**C++ 原句〔数组下标 167〕**：%t1 类型的实参与 %t2 类型的形参？差得远呢，完全对不上嘛

英文依据：Expression of type "{sourceType}" cannot be assigned to parameter of type "{paramType}"

---

### 425 · paramNameMissing

方式：语义适配

**Pylance 原中文**：没有名为“{name}”的参数

**当前文案**：名为“{name}”的参数？这儿可没有哦，人家替你确认过了呐

**C++ 原句〔数组下标 1267〕**：名为 %sq2 的参数？特性 %sq1 那儿可没有哦，人家替你确认过了呐

英文依据：No parameter named "{name}"

---

### 431 · paramSpecContext

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用 ParamSpec

**当前文案**：杂鱼~这里不允许使用“ ParamSpec”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据：ParamSpec is not allowed in this context

---

### 444 · positionArgAfterNamedArg

方式：语义适配

**Pylance 原中文**：位置参数不能出现在关键字参数之后

**当前文案**：位置参数这边不、可以位于关键字参数以后哦，你以为谁都像你这么随手写咯

**C++ 原句〔数组下标 1266〕**：位置参数这边不、可以位于特性中的命名参数以后哦，你以为谁都像你这么随手写咯

英文依据：Positional argument cannot appear after keyword arguments

---

### 445 · positionArgAfterUnpackedDictArg

方式：语义适配

**Pylance 原中文**：位置参数不能出现在关键字参数解压缩之后

**当前文案**：位置参数这边不、可以位于关键字参数解包以后哦，你以为谁都像你这么随手写咯

**C++ 原句〔数组下标 1266〕**：位置参数这边不、可以位于特性中的命名参数以后哦，你以为谁都像你这么随手写咯

英文依据：Positional argument cannot appear after keyword argument unpacking

---

### 450 · positionOnlyIncompatible

方式：句式套用

**Pylance 原中文**：仅位置参数分隔符需要 Python 3.8 或更高版本

**当前文案**：欸？仅位置参数分隔符要 Python 3.8 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Position-only parameter separator requires Python 3.8 or newer

---

### 459 · protocolIllegal

方式：句式套用

**Pylance 原中文**：使用 "Protocol" 需要 Python 3.7 或更高版本

**当前文案**：欸？使用 "Protocol" 要 Python 3.7 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Use of "Protocol" requires Python 3.7 or newer

---

### 473 · readOnlyArgCount

方式：句式套用

**Pylance 原中文**：“ReadOnly”后应为单个类型参数

**当前文案**：ReadOnly 后应只有一个类型参数，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

**C++ 原句〔数组下标 2218〕**：此强制转换应只有一个操作数表达式，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

英文依据：Expected a single type argument after "ReadOnly"

---

### 474 · readOnlyNotInTypedDict

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用“ReadOnly”

**当前文案**：杂鱼~这里不允许使用“ReadOnly”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据："ReadOnly" is not allowed in this context

---

### 476 · requiredArgCount

方式：句式套用

**Pylance 原中文**："Required"后应为单个类型参数

**当前文案**：Required 后应只有一个类型参数，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

**C++ 原句〔数组下标 2218〕**：此强制转换应只有一个操作数表达式，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

英文依据：Expected a single type argument after "Required"

---

### 477 · requiredNotInTypedDict

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用"Required"

**当前文案**：杂鱼~这里不允许使用“Required”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据："Required" is not allowed in this context

---

### 478 · returnInAsyncGenerator

方式：语义适配

**Pylance 原中文**：async 生成器中不允许使用具有值的 return 语句

**当前文案**：在 async 生成器里要用 return 返回值？先问过人家同不同意咯

**C++ 原句〔数组下标 2740〕**：在协同例程要写 "return" (乖乖改用 "co_return")？先问过人家同不同意咯

英文依据：Return statement with value is not allowed in async generator

---

### 479 · returnInExceptionGroup

方式：语义适配

**Pylance 原中文**："except*" 块中不允许 "return"

**当前文案**：“except*”块里不可以用 return 语句啦，别想蒙混过关呐

**C++ 原句〔数组下标 2178〕**：不准 finally 块内有 return 语句啦，你还想装没看见吗

英文依据："return" is not allowed in an "except*" block

---

### 494 · sentinelParamCount

方式：语义适配

**Pylance 原中文**：Sentinel 需要一个位置参数

**当前文案**：Sentinel 的参数数目不合规矩，应该是一个位置参数，人家说一不二哦

**C++ 原句〔数组下标 1817〕**：“main”的参数数目不合规矩，应该是零个或两个参数，人家说一不二哦

英文依据：Sentinel requires one positional argument

---

### 513 · templateStringIllegal

方式：句式套用

**Pylance 原中文**：模板字符串字面量(t-strings)需要 Python 3.14 或更高版本

**当前文案**：欸？模板字符串字面量(t-strings)要 Python 3.14 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Template string literals (t-strings) require Python 3.14 or newer

---

### 515 · ternaryNotAllowed

方式：句式套用

**Pylance 原中文**：类型表达式中不允许使用三元表达式

**当前文案**：杂鱼~类型表达式里不允许使用三元表达式的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Ternary expression not allowed in type expression

---

### 519 · tupleInAnnotation

方式：句式套用

**Pylance 原中文**：类型表达式中不允许使用 tuple 表达式

**当前文案**：杂鱼~类型表达式里不允许使用 tuple 表达式的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Tuple expression not allowed in type expression

---

### 521 · typeAliasIsRecursiveDirect

方式：语义适配

**Pylance 原中文**：类型别名“{name}”不能在其定义中使用自身

**当前文案**：类型别名“{name}”这边不可以在它自己的定义中出现哦，你以为谁都像你这么随手写啦

**C++ 原句〔数组下标 1586〕**：用 auto 类型说明符声明的变量这边不可以冒出来在其自身的初始值设定项中哦，你以为谁都像你这么随手写啦

英文依据：Type alias "{name}" cannot use itself in its definition

---

### 525 · typeAliasStatementIllegal

方式：句式套用

**Pylance 原中文**：类型别名语句需要 Python 3.12 或更高版本

**当前文案**：欸？类型别名语句要 Python 3.12 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Type alias statement requires Python 3.12 or newer

---

### 532 · typeAnnotationCall

方式：句式套用

**Pylance 原中文**：类型表达式中不允许使用调用表达式

**当前文案**：杂鱼~类型表达式里不允许使用调用表达式的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Call expression not allowed in type expression

---

### 533 · typeAnnotationVariable

方式：句式套用

**Pylance 原中文**：类型表达式中不允许使用变量

**当前文案**：杂鱼~类型表达式里不允许使用变量的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Variable not allowed in type expression

---

### 538 · typeArgsMismatchOne

方式：语义适配

**Pylance 原中文**：应为一个类型参数，但收到 {received}

**当前文案**：类型参数的个数不对啦，应该是 1 个，但收到 {received}，个数要给人家对上哟

**C++ 原句〔数组下标 1941〕**：哈、哈啊？访问器函数的参数多得离谱了啦，个数要给人家对上哟

英文依据：Expected one type argument but received {received}

---

### 539 · typeArgsMissingForAlias

方式：句式套用

**Pylance 原中文**：泛型类型别名“{name}”的预期类型参数

**当前文案**：笨蛋！还要人家告诉你泛型类型别名“{name}”需要类型参数吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

英文依据：Expected type arguments for generic type alias "{name}"

---

### 540 · typeArgsMissingForClass

方式：句式套用

**Pylance 原中文**：泛型类“{name}”的预期类型参数

**当前文案**：笨蛋！还要人家告诉你泛型类“{name}”需要类型参数吗？

**C++ 原句〔数组下标 79〕**：笨蛋！还要人家告诉你这里要写类型说明符吗？

英文依据：Expected type arguments for generic class "{name}"

---

### 541 · typeArgsTooFew

方式：语义适配

**Pylance 原中文**：为“{name}”提供的类型参数太少；应为 {expected}，但收到 {received}

**当前文案**：小杂鱼~“{name}”的类型参数太少了啦，应为 {expected}，但收到 {received}

**C++ 原句〔数组下标 442〕**：小杂鱼~%nf 的参数太少了啦

英文依据：Too few type arguments provided for "{name}"; expected {expected} but received {received}

---

### 542 · typeArgsTooMany

方式：语义适配

**Pylance 原中文**：为“{name}”提供的类型参数太多；应为 {expected}，但收到 {received}

**当前文案**：小杂鱼~“{name}”的类型参数太多了啦，应为 {expected}，但收到 {received}

**C++ 原句〔数组下标 443〕**：小杂鱼~%nf 的参数太多了啦

英文依据：Too many type arguments provided for "{name}"; expected {expected} but received {received}

---

### 543 · typeAssignmentMismatchWildcard

方式：语义适配

**Pylance 原中文**：导入符号“{name}”的类型为“{sourceType}”，该类型不可分配给声明的类型“{destType}”

**当前文案**：导入的“{name}”是“{sourceType}”类型，不可以分配到声明为“{destType}”的变量…你说你，气不气人呐

**C++ 原句〔数组下标 513〕**：不可以将 %t1 类型的值分配到 %t2 类型的实体…你说你，气不气人呐

英文依据：Import symbol "{name}" has type "{sourceType}", which is not assignable to declared type "{destType}"

---

### 546 · typeCommentDeprecated

方式：语义适配

**Pylance 原中文**：已弃用 type 注释; 请改用 type 批注

**当前文案**：又怎么了啦，type 注释已弃用 -- 改用类型批注哦

**C++ 原句〔数组下标 2221〕**：又怎么了啦，访问说明符 %s1 已弃用 -- 改用 %s2 哦

英文依据：Use of type comments is deprecated; use type annotation instead

---

### 547 · typeExpectedClass

方式：语义适配

**Pylance 原中文**：应为类，但收到“{type}”

**当前文案**：欸？应该是类类型，可你给的是“{type}”，自己承认一下吧

**C++ 原句〔数组下标 1423〕**：欸？应该是类、结构或联合类型，自己承认一下吧

英文依据：Expected class but received "{type}"

---

### 549 · typeGuardArgCount

方式：句式套用

**Pylance 原中文**：“TypeGuard”或“TypeIs”后应为单个类型参数

**当前文案**：TypeGuard 或 TypeIs 后应只有一个类型参数，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

**C++ 原句〔数组下标 2218〕**：此强制转换应只有一个操作数表达式，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

英文依据：Expected a single type argument after "TypeGuard" or "TypeIs"

---

### 551 · typeIsReturnType

方式：语义适配

**Pylance 原中文**：TypeIs 的返回类型(“{returnType}”)与值参数类型(“{type}”)不一致

**当前文案**：额…TypeIs 的返回类型“{returnType}”与值参数类型“{type}”不一致哦

**C++ 原句〔数组下标 42〕**：额…操作数类型不兼容哦(%t1 和 %t2)

英文依据：Return type of TypeIs ("{returnType}") is not consistent with value parameter type ("{type}")

---

### 553 · typeNotSupportBinaryOperatorBidirectional

方式：语义适配

**Pylance 原中文**：预期类型为“{expectedType}”时，类型“{leftType}”和“{rightType}”不支持运算符“{operator}”

**当前文案**：预期类型为“{expectedType}”时，和“{leftType}”“{rightType}”匹配的“{operator}”运算符？没有哦，一片空白啦

**C++ 原句〔数组下标 349〕**：和这些操作数匹配的 %sq 运算符？没有哦，一片空白啦

英文依据：Operator "{operator}" not supported for types "{leftType}" and "{rightType}" when expected type is "{expectedType}"

---

### 554 · typeNotSupportUnaryOperatorBidirectional

方式：语义适配

**Pylance 原中文**：预期类型为 "{expectedType}"时，类型"{type}"不支持运算符"{operator}"

**当前文案**：预期类型为“{expectedType}”时，和“{type}”匹配的“{operator}”一元运算符？没有哦，一片空白啦

**C++ 原句〔数组下标 349〕**：和这些操作数匹配的 %sq 运算符？没有哦，一片空白啦

英文依据：Operator "{operator}" not supported for type "{type}" when expected type is "{expectedType}"

---

### 569 · typeVarDefaultIllegal

方式：句式套用

**Pylance 原中文**：类型变量默认类型需要 Python 3.13 或更高版本

**当前文案**：欸？类型变量默认类型要 Python 3.13 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Type variable default types require Python 3.13 or newer

---

### 579 · typeVarTupleContext

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用 TypeVarTuple

**当前文案**：杂鱼~这里不允许使用“ TypeVarTuple”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据：TypeVarTuple is not allowed in this context

---

### 599 · typedDictEmptyName

方式：语义适配

**Pylance 原中文**：TypedDict 中的名称不能为空

**当前文案**：TypedDict 里的名称一定要非空，别想蒙混过关啦

**C++ 原句〔数组下标 3269〕**：一定要用非空名称声明模块，别想蒙混过关啦

英文依据：Names within a TypedDict cannot be empty

---

### 600 · typedDictEntryName

方式：语义适配

**Pylance 原中文**：字典条目名称的预期字符串文本

**当前文案**：笨蛋！还要人家告诉你字典条目的名字要写字符串字面量吗？

**C++ 原句〔数组下标 1038〕**：笨蛋！还要人家告诉你这里要写字符串文本吗？

英文依据：Expected string literal for dictionary entry name

---

### 601 · typedDictEntryUnique

方式：语义适配

**Pylance 原中文**：字典中的名称必须唯一

**当前文案**：字典里的名称重样啦，两个一模一样的名字，人家喊谁好？

**C++ 原句〔数组下标 100〕**：参数名重样啦，两个一模一样的名字，人家喊谁好？

英文依据：Names within a dictionary must be unique

---

### 608 · typedDictInClassPattern

方式：句式套用

**Pylance 原中文**：类模式中不允许使用 TypedDict 类

**当前文案**：杂鱼~类模式里不允许使用 TypedDict 类的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：TypedDict class not allowed in class pattern

---

### 615 · unaryOperationNotAllowed

方式：句式套用

**Pylance 原中文**：类型表达式中不允许使用一元运算符

**当前文案**：杂鱼~类型表达式里不允许使用一元运算符的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Unary operator not allowed in type expression

---

### 619 · uninitializedAbstractVariables

方式：语义适配

**Pylance 原中文**：抽象基类中定义的变量未在 final 类 "{classType}" 中初始化

**当前文案**：final 类“{classType}”里头有从抽象基类继承、却压根没初始化的变量，这里人家说了算呢

**C++ 原句〔数组下标 517〕**：对象里头有压根没初始化的常量或引用成员，这里人家说了算呢

英文依据：Variables defined in abstract base class are not initialized in final class "{classType}"

---

### 620 · uninitializedInstanceVariable

方式：语义适配

**Pylance 原中文**：未在类体或__init__方法中初始化实例变量“{name}”

**当前文案**：哎呀，实例变量“{name}”还没在类体或 __init__ 方法中初始化呢，人家也帮不了你呀

**C++ 原句〔数组下标 809〕**：还没初始化的 %n 里头有常量成员，这里人家说了算嘛

英文依据：Instance variable "{name}" is not initialized in the class body or __init__ method

---

### 622 · unionSyntaxIllegal

方式：句式套用

**Pylance 原中文**：联合的替代语法需要 Python 3.10 或更高版本

**当前文案**：欸？联合的替代语法要 Python 3.10 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Alternative syntax for unions requires Python 3.10 or newer

---

### 632 · unpackArgCount

方式：句式套用

**Pylance 原中文**："Unpack"后应为单个类型参数

**当前文案**：Unpack 后应只有一个类型参数，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

**C++ 原句〔数组下标 2218〕**：此强制转换应只有一个操作数表达式，人家给你三秒钟改好啦。别、别误会了，人家才不是特意帮你检查的…

英文依据：Expected a single type argument after "Unpack"

---

### 635 · unpackIllegalInComprehension

方式：句式套用

**Pylance 原中文**：在推导式中不允许使用解包操作

**当前文案**：杂鱼~在推导式里不允许使用解包操作的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Unpack operation not allowed in comprehension

---

### 636 · unpackInAnnotation

方式：句式套用

**Pylance 原中文**：类型表达式中不允许使用解包运算符

**当前文案**：杂鱼~类型表达式里不允许使用解包运算符的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Unpack operator not allowed in type expression

---

### 646 · unpackedSubscriptIllegal

方式：句式套用

**Pylance 原中文**：下标中的解包运算符需要 Python 3.11 或更高版本

**当前文案**：欸？下标中的解包运算符要 Python 3.11 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Unpack operator in subscript requires Python 3.11 or newer

---

### 649 · unreachableCodeCondition

方式：语义适配

**Pylance 原中文**：由于条件静态评估结果为 false，因此未对代码进行分析

**当前文案**：情况是这样：条件静态计算结果为 False，这段代码就不分析啦。这种程度就慌了？杂鱼！

**C++ 原句〔数组下标 3243〕**：情况是这样：原子约束的计算结果为 false。这种程度就慌了？杂鱼！

英文依据：Code is not analyzed because condition is statically evaluated as false

---

### 650 · unreachableExcept

方式：语义适配

**Pylance 原中文**：无法访问 Except 子句，因为已处理异常

**当前文案**：异常早就处理过了，这个 except 被挡在路那头了啦，人家都走不过去

**C++ 原句〔数组下标 111〕**：这行语句被挡在路那头了啦，人家都走不过去

英文依据：Except clause is unreachable because exception is already handled

---

### 652 · varAnnotationIllegal

方式：句式套用

**Pylance 原中文**：变量的 Type 批注需要 Python 3.6 或更高版本; 请使用 type 注释以与以前的版本兼容

**当前文案**：欸？变量的 Type 批注要 Python 3.6 或更高版本才玩得起啦，先把版本切过去再来见人家咯; 请使用 type 注释以与以前的版本兼容

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Type annotations for variables requires Python 3.6 or newer; use type comment for compatibility with previous versions

---

### 657 · walrusIllegal

方式：句式套用

**Pylance 原中文**：运算符 ":=" 需要 Python 3.8 或更高版本

**当前文案**：欸？运算符 ":=" 要 Python 3.8 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Operator ":=" requires Python 3.8 or newer

---

### 658 · walrusNotAllowed

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用运算符 ":="，且不带括号

**当前文案**：杂鱼~这里不允许使用“运算符 ":="，且不带括号”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据：Operator ":=" is not allowed in this context without surrounding parentheses

---

### 659 · walrusNotAllowedInComprehension

方式：句式套用

**Pylance 原中文**：在推导可迭代表达式中不允许使用操作符 ":="

**当前文案**：杂鱼~在推导可迭代表达式里不允许使用操作符 ":="的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Operator ":=" is not allowed within a comprehension iterable expression

---

### 660 · wildcardInFunction

方式：句式套用

**Pylance 原中文**：类或函数中不允许使用通配符 import

**当前文案**：杂鱼~类或函数里不允许使用通配符 import的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

英文依据：Wildcard import not allowed within a class or function

---

### 664 · yieldFromIllegal

方式：句式套用

**Pylance 原中文**：使用“yield from”需要 Python 3.3 或更高版本

**当前文案**：欸？使用“yield from”要 Python 3.3 或更高版本才玩得起啦，先把版本切过去再来见人家咯

**C++ 原句〔数组下标 2730〕**：欸？推导出的返回类型要 C++14 才玩得起啦，先把标准切过去再来见人家咯

适配说明：C++ 标准版本门槛句式改为 Python 版本门槛，原版本号和额外建议不变。

英文依据：Use of "yield from" requires Python 3.3 or newer

---

### 665 · yieldFromOutsideAsync

方式：语义适配

**Pylance 原中文**：async 函数中不允许使用 "yield from"

**当前文案**：async 函数里，yield from 表达式？人家可不答应呐

**C++ 原句〔数组下标 2669〕**：catch 子句那边，co_yield 表达式？人家可不答应呐

英文依据："yield from" not allowed in an async function

---

### 666 · yieldWithinComprehension

方式：句式套用

**Pylance 原中文**：允许在推导式中使用 "yield"

**当前文案**：杂鱼~推导式里不允许使用 yield 的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：修正上游中文漏“不”字的问题，按英文 not allowed 保持禁止含义。

英文依据："yield" not allowed inside a comprehension

---

### 667 · zeroLengthTupleNotAllowed

方式：句式套用

**Pylance 原中文**：此上下文中不允许使用零长度 tuple

**当前文案**：杂鱼~这里不允许使用“零长度 tuple”的啦

**C++ 原句〔数组下标 655〕**：杂鱼~你的声明中不允许使用 %sq 修饰符

适配说明：只套用禁止使用某语法的句式，限制的 Python 上下文和名称不变。

英文依据：Zero-length tuple is not allowed in this context
