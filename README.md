# Face Ratio Analyzer – Minimalist 3-Section & 5-Eye Auto-Measurer (dlib-based)

This project uses dlib’s 68-face-landmark model to measure any portrait automatically and outputs:

- 3-section ratios (upper : middle : lower face)
- 5-eye ratios (R1/5, Re-eye, M1/5, L-eye, L1/5)
- Comparison with standard aesthetic values (±10 % tolerance)
- One-click Excel summary

Perfect for beauty analysis, AI retouching reference, facial-proportion research, or thesis data processing.

---

## ✨ Key Features

✔ Batch-process an entire folder – drop any `.jpg / .jpeg / .png` into `images/`.  
✔ Auto-detect faces & 68 landmarks.  
✔ Export the above ratios plus “long / short / standard” verdicts.  
✔ Auto-generate Excel report.

## Required packages
numpy==1.21.6  
opencv-python==4.5.5.64  
pandas==1.3.5  
openpyxl  
tabulate  

📫 Contact: caoyi3@stu.scu.edu.cn

# Face Ratio Analyzer — 基于 dlib 的极简三庭五眼自动测量工具

本项目使用 **dlib** 的 68 点人脸关键点模型，对人脸照片进行自动测量，输出：

- 三庭比例（上庭：中庭：下庭）
- 五眼比例（R1/5、Re-eye、M1/5、L-eye、L1/5）
- 与标准美学数据比较（允许 ±10% 浮动）
- 自动生成 Excel 汇总结果

适合：美学分析、AI 修图参考、人脸比例研究、论文数据处理。

---

## ✨ 功能特点

### ✔ 支持批量处理整文件夹图片  
将所有 `.jpg / .jpeg / .png` 放入 `images/`，脚本自动处理。
### ✔ 自动检测人脸与 68 点关键点  
### ✔ 输出三庭与五眼比例  
包括：
- **上庭、中庭、下庭比例**
- **R1/5 (右侧 1/5)**
- **Re-eye (右眼宽度)**
- **M1/5 (双眼距离)**
- **L-eye (左眼宽度)**
- **L1/5 (左侧 1/5)**

### ✔ 与标准值比较（±10% 容差）  
输出 “偏长 / 偏短 / 标准”。

### ✔ 自动导出 Excel  

## 你需要的依赖
numpy==1.21.6
opencv-python==4.5.5.64 
pandas==1.3.5
openpyxl
tabulate

📫我的邮箱
caoyi3@stu.scu.edu.cn



