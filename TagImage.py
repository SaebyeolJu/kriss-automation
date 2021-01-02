# -*- coding: utf-8 -*-
import os
import sys
import openpyxl
from os import listdir
from os.path import isfile, join

# 기울기 구하기
def gradient(start_v, first_v):
    start_v, first_v = 0, 0

# 두께 비례식
def thickness():
    stand = input('기준 단위 : ')
    stand_cm = input('기준 단위 측정 cm : ')
    mat_cm = input('구해야 할 소재 cm :')
    mat = (stand * mat_cm) / stand_cm
    return mat

def curve(name, image_number):
    curve_info = ['figure_name','unipolar/bipolar', 'device',
                'x-first', 'x-last', 'y-first', 'y-last',
                'on current (A)', 'off current (A)',
                'set voltage (A)', 'reset voltage (V)']
    x_axis = []
    y_axis = []
    return print('curve')

# element 개수마다 element_info 추가됨
def device(paper_name, image_number, wb):
    image_name = f'{paper_name}.device{image_number}_1'
    element_cnt = int(input('element 총 몇 개? : '))

    # element 개수만큼 생
    # 0 : figure_name / 1 : device / [2: element / 3: thickness]
    device_info = ['NAN'] * 2
    device_info[0] = 'Figure_' + input('Figure 이름 : ')
    device_info[1] = input('Device 구성 : ')

    for i in range(element_cnt):
        element_info = ['NAN'] * 2
        element_info[0] = input(f'{i} 번째 소재 element : ')
        if input('두께 계산해야함? : (y/n)') == 'y':
            element_info[1] = thickness()
        else: element_info[1] = input('두께 : ')
        device_info.extend(element_info)
        wb.s_endurance['A'] = device_info
    return wb.save(DIR + '/image.xlsx')

def endurance(name, image_number):
    figure_name = 'Figure_'
    print('add more line?')

    return print('endurance')

def retention(name, image_number):
    finure_name = 'Figure_'
    print('add more line?')
    return print('retention')

def process(name, DIR):
    # 이미지 데이터 엑셀 생성
    wb = openpyxl.Workbook()

    # 엑셀 시트 총 4개
    s_curve = wb.active
    s_curve.title = 's_curve'
    wb.create_sheet('s_device')
    wb.create_sheet('s_endurance')
    wb.create_sheet('s_retention')

    wb.save(DIR + '/image.xlsx')
    print(str(wb))

    paper_name = name
    image_list = (os.listdir(DIR[0]))
    func_list = {'0': 'curve', '1': 'device', '2': 'endurance', '3': 'retention'}

    for image in range(len(image_list) + 1):
        image_number = 0
        image_type = input("Image 타입 입력해주세요 : ")
        for i in range(len(func_list)):
            if image_type == str(i):
                image_number += 1
                eval(func_list[str(i)] + '(' + paper_name + ',' + str(image_number) + ',' + str(wb) + ')')

# 내가 다 타이핑 해야 함
# 계산하는 것 없음

# 단위는 logarithmic scale 로 계산되어야함

# 폴더 안 데이터 개수마다 col 수 증가

AB_DIR = '/Users/SBJ/Desktop/kriss/thesis'

# 총 3개의 논문, [0,1] 번째는 이미지, QA / 마지막 논문은 text라 해당 안됨
file_list = (os.listdir(AB_DIR))
if file_list[0] or file_list[-1] == '.DS_Store': file_list.remove('.DS_Store')
file_list.sort(key=float)
print(file_list)

DIR = [AB_DIR + '/' + file_list[0], AB_DIR + '/' + file_list[1]]

for i in range(2):
    print(file_list[i],DIR[i])
    process(file_list[i], DIR[i])