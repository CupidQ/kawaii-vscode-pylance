# 仅供查看 Pylance 静态诊断，请勿把它当作正常程序运行。
# 在 VS Code 中打开此目录，选择 Python 解释器，查看波浪线/悬浮提示。
import kawaii_missing_package

print(kawaii_undefined_name)

age: int = "十七岁"


def add(a: int, b: int) -> int:
    return a + b


add("一", 2)
add(1)


def greeting() -> int:
    return "你好呀"
