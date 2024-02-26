import pandas as pd

# 주어진 데이터
data = {
    'result': [0.61, 0.52],
    'batch_ratio': [1, 1],
    'total_data_uwage_ratio': [0.5, 0.5],
    'number_of_training_images': [16832, 16832],
    'lan_of_training_images': ['th', 'th'],
    'model': ['None-VGG-BiLSTM-CTC-Seed1111', 'TPS-ResNet-BiLSTM-Attn-Seed1111']
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model.xlsx'
file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\model_1.xlsx'
df.to_excel(file_path, index=False)

print("파일이 저장되었습니다:", file_path)
