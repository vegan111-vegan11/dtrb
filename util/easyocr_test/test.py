import torch

# Check if CUDA (GPU) is available
cuda_available = torch.cuda.is_available()

print("CUDA (GPU) is available:", cuda_available)


import torch

# CUDA가 사용 가능한지 확인
if torch.cuda.is_available():
    # CUDA 장치 개수 확인
    print(torch.cuda.device_count())

    # 현재 사용 가능한 CUDA 장치의 인덱스 확인
    print(torch.cuda.current_device())

    # 모든 CUDA 장치의 이름 확인
    print(torch.cuda.get_device_name(0))

    # 텐서를 CUDA로 이동
    x = torch.tensor([1, 2, 3]).cuda()

    # GPU에서 연산 수행
    y = x * 2
else:
    print("CUDA is not available.")
