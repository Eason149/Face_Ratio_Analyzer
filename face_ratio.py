"""
Eason149 2025-11-14
安装的依赖都在文件夹中，如果不能使用请联系我，确保你的虚拟环境是python3.7，太高了用不了。
"""
import cv2
import dlib
import numpy as np
import os
import pandas as pd

# 路径
IMAGE_DIR = r"C:\Users\cy184\Desktop\face_ratio\images"  # 这里放待处理图片
LANDMARK_MODEL = "shape_predictor_68_face_landmarks.dat"

# 标准值
standards = {
    "R1/5": 0.93,
    "Re-eye": 1.00,
    "M1/5": 1.03,
    "L-eye": 1.00,
    "L1/5": 0.96
}

# 偏差判断函数
def compare(value, standard):
    tolerance = standard * 0.10  # 允许误差为标准值的10%
    if value > standard + tolerance:
        return "偏长"
    elif value < standard - tolerance:
        return "偏短"
    else:
        return "标准"

# 初始化 dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(LANDMARK_MODEL)

# 用于存储结果
results = []

# 遍历图片
for filename in os.listdir(IMAGE_DIR):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue
    img_path = os.path.join(IMAGE_DIR, filename)
    img = cv2.imread(img_path)
    if img is None:
        print(f"{filename} 无法读取，跳过")
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    if len(faces) == 0:
        print(f"{filename} 未检测到人脸")
        continue

    for face in faces:
        landmarks = predictor(gray, face)
        pts = np.array([[p.x, p.y] for p in landmarks.parts()])

        # 三庭
        upper = np.linalg.norm(pts[19]-pts[27])#这个没有上庭监测点，这里代替了
        mid = np.linalg.norm(pts[27]-pts[33])
        lower = np.linalg.norm(pts[33]-pts[8])
        total = upper + mid + lower
        upper_ratio = upper/total
        mid_ratio = mid/total
        lower_ratio = lower/total

        # 五眼
        r1_5 = np.linalg.norm(pts[0]-pts[16])/total
        re_eye = np.linalg.norm(pts[16]-pts[45])/total
        m1_5 = np.linalg.norm(pts[39]-pts[42])/total
        l_eye = np.linalg.norm(pts[39]-pts[0])/total
        l1_5 = np.linalg.norm(pts[1]-pts[0])/total

        # 存入字典
        row = {
            "文件名": filename,
            "上庭比例": round(upper_ratio, 2),
            "中庭比例": round(mid_ratio, 2),
            "下庭比例": round(lower_ratio, 2),
            "R1/5": round(r1_5, 2),
            "R1/5判定": compare(r1_5, standards["R1/5"]),
            "Re-eye": round(re_eye, 2),
            "Re-eye判定": compare(re_eye, standards["Re-eye"]),
            "M1/5": round(m1_5, 2),
            "M1/5判定": compare(m1_5, standards["M1/5"]),
            "L-eye": round(l_eye, 2),
            "L-eye判定": compare(l_eye, standards["L-eye"]),
            "L1/5": round(l1_5, 2),
            "L1/5判定": compare(l1_5, standards["L1/5"])
        }
        results.append(row)

# 保存 Excel 文件
df = pd.DataFrame(results)
output_path = os.path.join(IMAGE_DIR, "face_ratios_outcome.xlsx")
df.to_excel(output_path, index=False)
print(f"已保存分析结果到：{output_path}")
