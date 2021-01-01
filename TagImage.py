import sys
import openpyxl
from os import listdir
from os.path import isfile, join

# 논문 개수마다 폴더 생성
# 폴더 안 데이터 개수마다 col 수 증가

def curve():
    # 절대 경로 / 상대 경로
    AB_DIR = '/Users/SBJ/Desktop/kriss/Data/Curve'
    DIR = 'Data/Image/Curve'

    row_info = ['figure_name','x-axis','y-axis','device','on current (A)','off current (A)','set voltage (A)','reset voltage (V)','unipolar/bipolar']
    file_list = [f for f in listdir(AB_DIR) if isfile(join(AB_DIR, f))]
    print(file_list)

# 단위는 logarithmic scale 로 계산되어야함