import pandas as pd

# 주어진 데이터
data = {
    'train_loss': [1.4, 0.05, 0.03, 0.02],
    'epoch': [100, 3000, 4000, 6000],
    'batch_ratio': [0.5, 0.5, 0.5, 0.5],
    'total_data_uwage_ratio': [0.5, 0.5, 0.5, 0.5],
    'number_of_training_images': [767799, 767799, 767799, 767799],
    'lan_of_training_images': ['th', 'th', 'th', 'th'],
    'model': ['None-VGG-BiLSTM-Attn-Seed1111', 'None-VGG-BiLSTM-Attn-Seed1111', 'None-VGG-BiLSTM-Attn-Seed1111', 'None-VGG-BiLSTM-Attn-Seed1111']
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model.xlsx'
file_path = r'C:\Users\TAMSystech\yjh\ipynb\deep-text-recognition-benchmark\연구노트\ocr\model\model_3.xlsx'
df.to_excel(file_path, index=False)

print("파일이 저장되었습니다:", file_path)
