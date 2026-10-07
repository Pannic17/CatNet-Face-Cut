# CatNet-Face-Cut

CatNet 的 Python 猫脸检测与裁剪实验，用于为分类模型准备猫脸图像。使用 OpenCV Haar 级联检测正面猫脸，并扩大检测区域以包含耳朵。

主项目与其他模块入口：[CatNet-Unity](https://github.com/Pannic17/CatNet-Unity)。后续分类训练见 [CatNet-Tensorflow](https://github.com/Pannic17/CatNet-Tensorflow) 和 [CatNet-Test-Pytorch](https://github.com/Pannic17/CatNet-Test-Pytorch)。

## 文件说明

| 文件 | 用途 |
| --- | --- |
| `detection.py` | `detect()` 返回裁剪坐标，`cut()` 返回裁剪图像，`load()` 批量处理一个输入类别 |
| `test.py` | 单图检测和裁剪的窗口展示实验 |
| `haarcascade_frontalcatface*.xml` | 猫脸级联分类器 |
| `haarcascade_frontalface*.xml` | 仓库附带的人脸级联分类器 |
| `cat_test_*.jpg`、`person_test.png` | 示例图片 |

## 环境与使用

代码使用 Python、`opencv-python`；`os` 和 `math` 是标准库。可在独立环境中安装：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install opencv-python
```

运行前先修改 `detection.py` 中的路径：

1. 将 `detect()` 的级联 XML 路径改为本地 `haarcascade_frontalcatface_extended.xml`。
2. 设置 `load()` 中的 `path`（输入根目录）和 `loca`（输出根目录）。输入类别目录为 `<根目录>/<类别>/original/`，预先创建 `<输出根目录>/<类别>/faces/`。
3. 修正输出拼接：当前 `loca = loca + breed + '/faces'` 缺少末尾分隔符，后续 `loca + new_name` 不会写入预期目录；可改用 `os.path.join(loca, new_name)`。
4. 从仓库根目录执行：

```powershell
python detection.py
```

按提示输入类别名。成功裁剪的图片以 `<类别>_<序号>.jpg` 命名；无法检测、负坐标或检测宽度小于 30 的图片会跳过。`detection.py` 还会将检测框调试图写入 `cxks.png`。

单图实验需要先修改 `test.py` 中的图片与 XML 路径，再执行 `python test.py`，在 OpenCV 窗口中按键继续。

## 当前限制

路径仍是原作者的 `H:` 盘路径，脚本没有命令行路径参数。`detection.py` 在文件末尾直接调用 `load()`，导入该模块也会进入交互流程。代码主要处理首个检测结果，未完整检查右侧／底部边界；`test.py` 在没有检测结果时可能使用未赋值坐标。两份脚本都保留 `cv2.waitKey(0)`，批处理时应按需要调整等待逻辑。训练数据集未随仓库提供。

本文依据源码整理；未执行图像批处理或验证检测效果。
