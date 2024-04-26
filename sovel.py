import cv2 as cv
import numpy as np
import sys

img = cv.imread('test.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

def sobel_edge_detection(image):
    # 이미지를 그레이스케일로 변환
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # x 방향으로의 소벨 필터 적용
    sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)
    # y 방향으로의 소벨 필터 적용
    sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)
    # 소벨 필터 적용 결과의 절댓값 계산
    abs_sobelx = cv.convertScaleAbs(sobelx)
    abs_sobely = cv.convertScaleAbs(sobely)
    # x 방향 및 y 방향으로의 에지 강도 결합
    edges = cv.addWeighted(abs_sobelx, 0.5, abs_sobely, 0.5, 0)
    return edges

edges = sobel_edge_detection(img)
cv.imshow('Edges', edges)

cv.waitKey(0)
cv.destroyAllWindows()