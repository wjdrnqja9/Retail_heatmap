# ⭐ Head_heatmap

- Object Detection을 사여하여 매장 내 동선 히트맵 생성

- 직원이 카메라에 나오는 경우 직원 동선 제외 기능

# :cloud: 개요

- 기존 CCTV 혹은 추가로 설치된 카메라를 활용하여 소비자들의 동선을 Heat map으로 표현한다.

- 소비자 트래픽이 높은 지역과 낮은 지역을 파악하여 여러가지 방안을 통해 판매율을 높일 수 있다.

- 개개인을 추적하는 용도가 아닌 전체적인 동선 분포를 파악하기 위함이기 때문에 약간의 오탐률은 감수 가능하다.

- 머리만 추적하기 때문에 물체에 몸이 가려질 확률이 높은 Retail 분야에서 사용하기 적합하다.

- 하나의 단안 카메라로 작동하기 때문에 범용적이고 경제적이다.

- 좌표값을 기록할 때 시간(프레임)을 함께 기록하여 시간별 분석도 가능하다.

# :snowflake: 사용 모델 : YOLOv5

처리 속도가 매우 빠르고 용량이 낮아 실시간 영상이나 장시간 녹화된 영상에 적합하다.

# :zap: 사용 방법

### 1. requirements.txt 설치

```bash
pip install -r requirements.txt
```

### 2. Videos 폴더에 영상을 넣고 다음을 실행한다.

```bash
python3 detect.py --weights crowdhuman_yolov5m.pt --source Videos/ --view-img  --heads
```

### 3. 상황에 맞게 다음 파일의 videopath, labelpath를 설정한 후 실행한다. 
labelpath는 detect.py 실행 후 runs\detect\exp에 저장된 txt 파일 경로


#### - 직원이 카메라에 나오지 않을 때
```bash
python3 heatmap.py
```

#### - 직원이 카메라에 나올 때
```bash
python3 heatmap_remove.py
```
창이 실행되면 아래 사진과 같 직원의 위치에 마우스를 드래그한 후 Enter or space bar를 누른다.

![xywh](https://user-images.githubusercontent.com/75363285/206894532-78a7b4f8-5c7d-461a-99a6-89020c3d2a9e.png)


### 3. heatmap.png 파일로 저장된다.


# 🌟 결과 

## heatmap.py
![heatmap](https://user-images.githubusercontent.com/75363285/206843855-339b2816-62c0-41b1-9390-fe2c816dc43c.png)

## heatmap_remove.py
![heatmap_remove](https://user-images.githubusercontent.com/75363285/206894664-371db902-dc09-426b-bdd5-e422024bc4db.png)


# 참조
- https://github.com/ultralytics/yolov5
- https://github.com/deepakcrk/yolov5-crowdhuman
