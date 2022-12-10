# Head_heatmap
- Object Detection을 사용하여 매장 내 히트맵 생성 

# Summary
기존 CCTV 혹은 추가로 설치된 카메라를 활용하여 소비자들의 동선을 Heat map으로 표현한다.
소비자 트래픽이 높은 지역과 그렇지 못한 콜드스폿 을 파악하여 판매율 을 높이기 위한 플래노그램을 설정할수 있다. 

# Object Detection Model : YOLOv5
처리 속도가 빨라 장시간 녹화된 영상에 적합하다.
개개인을 추적하는 용도가 아닌 전체적인 동선 분포를 파악하기 위함이기 때문에 약간의 오탐률은 감수 가능하다.

# 구현 방법
영상의 일정 프레임마다 사람 머리의 좌표값을 기록하고, 좌표값을 바탕으로 히트맵을 작성한다.
좌표값을 기록할 때 시간(프레임)을 함께 기록하여 시간별 분석도 가능하다.

#
- 머리를 추적하기 때문에 물체에 가려진 사람의 이동도 탐지할 수 있음.
- 하나의 단안 카메라로 작동하기 때문에 범용적이고 경제적이지만, 정확한 좌표를 출력하는 것은 어려움. 

## 사용 방법

1. Videos에 영상을 넣고 다음을 실행한다.

```bash
python3 detect.py --weights crowdhuman_yolov5m.pt --source Videos/ --view-img  --heads
```

2.  실행 후 runs\detect\exp에 저장된 파일의 경로로 heatmap.py 파일의 videopath, labelpath를 설정한다.


3. 터미널에서 heatmap.py파일을 실행한다.

```bash
python3 heatmap.py
```




# 결과 

![heatmap](https://user-images.githubusercontent.com/75363285/206843855-339b2816-62c0-41b1-9390-fe2c816dc43c.png)

# 참조
- https://github.com/ultralytics/yolov5
- https://github.com/deepakcrk/yolov5-crowdhuman
