# -*- coding: utf-8 -*-
import os
import sys
import openpyxl
from os import listdir
from os.path import isfile, join

# 두께 비례식
def thickness():
    stand = float(input('기준 단위 : '))
    stand_cm = float(input('기준 단위 측정 cm : '))
    mat_cm = float(input('구해야 할 소재 cm :'))
    mat = (stand * mat_cm) / stand_cm
    return str(mat)

def curve(paper_name, image_number, DIR):
    print('IV curve 그래프')
    wb = openpyxl.load_workbook(DIR + '/image.xlsx')
    s_curve = wb['s_curve']

    info = ['figure_name', 'x-axis', 'y-axis', 'device',
                    'on_current (A)', 'off_current (A)', 'set voltage (V)',
                    'off voltage (V)', 'unipolar/bipolar']
    for i in range(1,len(info)):
        s_curve.cell(i,1).value = info[i]

    i_number = image_number
    image_name = f'{paper_name}.I.V-curve{i_number}_1'

    curve_info = ['NAN'] * 10
    curve_info[0] = image_name
    curve_info[1] = 'Figure_' + input('Figure 이름 : ')

    x_first = input('x-axis first : ')
    x_last = input('x-axis last : ')
    curve_info[2] = f'[{x_first}:{x_last}]'

    y_first = input('y-axis first : ')
    y_last = input('y-axis last : ')
    curve_info[3] = f'[{y_first}:{y_last}]'

    # device
    curve_info[4] = input('device : ')

    # current
    curve_info[5] = input('on current : ')
    curve_info[6] = input('off current : ')

    # voltage
    curve_info[7] = input('set voltage : ')
    curve_info[8] = input('reset voltage : ')

    curve_info[9] = input('unipolar / bipolar?(1 / 2) : ')
    if curve_info[9] == '1' : curve_info[8] = 'unipolar'
    else: curve_info[9] = 'bipolar'

    # 얻은 값들 엑셀 쓰기
    max_col = s_curve.max_column
    for row in range(0, len(curve_info)):
        s_curve.cell(row+1, max_col+1).value = curve_info[row]

    wb.save(DIR + '/image.xlsx')
    wb.close()

    return print(f'{image_number}번째 이미지 done')

# element 개수마다 element_info 추가됨
def device(paper_name, image_number, DIR):
    print('device 그래프')

    wb = openpyxl.load_workbook(DIR + '/image.xlsx')
    s_device = wb['s_device']

    i_number = image_number
    image_name = f'{paper_name}.device{i_number}_1'
    element_cnt = int(input('element 총 몇 개? : '))

    # element 개수만큼 생
    # 0 : figure_name / 1 : device / [2: element / 3: thickness]
    device_info = ['NAN'] * 2
    device_info[0] = 'Figure_' + input('Figure 이름 : ')
    device_info[1] = input('Device 구성 : ')

    for i in range(element_cnt):
        element_info = ['NAN'] * 2
        element_info[0] = input(f'{i} 번째 소재 element : ')
        if input('두께 계산해야함? (y/n) : ') == 'y':
            element_info[1] = thickness()
        else: element_info[1] = input('두께 : ')
        device_info.extend(element_info)
    device_info.insert(0, image_name)

    # 얻은 값들 엑셀 쓰기
    max_col = s_device.max_column
    for row in range(0, len(device_info)):
        s_device.cell(row+1, max_col+1).value = device_info[row]

    # info = ['figure_name', 'device']
    # for i in range(1,len(info)):
    #     s_device.cell(i,1).value = info[i]

    wb.save(DIR + '/image.xlsx')
    wb.close()

    return print(f'{image_number}번째 이미지 done')

def endurance(paper_name, image_number, DIR):
    print('Endurance 그래프')

    wb = openpyxl.load_workbook(DIR + '/image.xlsx')
    s_endurance = wb['s_endurance']

    i_number = image_number
    line_cnt = int(input('선 총 몇개? : '))

    # 0 : file name / 1 : figure_name / [2: x-axis / 3: y-axis]
    # 4 : Device / 5: Cycle / 6 : temperature
    # 7 : high resistance / 8 : high gradient
    # 9 : low resistance / 10 : low gradient

    # 선 개수만큼 반복
    for i in range(line_cnt):
        print(f'{i}번째 선')

        endurance_info = ['NAN'] * 11
        endurance_info[0] = f'{paper_name}.retention{i_number}_{i}'
        endurance_info[1] = 'Figure_' + input('Figure 이름 : ')

        x_first = input('x-axis first : ')
        x_last = input('x-axis last : ')
        endurance_info[2] = f'[{x_first}:{x_last}]'

        y_first = input('y-axis first : ')
        y_last = input('y-axis last : ')
        endurance_info[3] = f'[{y_first}:{y_last}]'

        endurance_info[4] = input('Device : ')
        endurance_info[5] = float(eval(input('Cycle : ').replace('^','**')))

        endurance_info[6] = float(input(('Temperature(K) : ')))
        temp_check = input('절대 온도인가요? (y / n / r) : ')
        if temp_check == 'n': endurance_info[6] += 273
        elif temp_check == 'r': endurance_info[6] = 300

        # high resistance
        high_res_high = eval(input('위 그래프에 제일 높은 y값 : ').replace('^','**'))
        high_res_low = eval(input('위 그래프에서 제일 낮은 y값 : ').replace('^','**'))
        endurance_info[7] = (high_res_high + high_res_low) / 2

        # high restance gradient
        endurance_info[8] = (high_res_high - high_res_low) / endurance_info[6]

        # low resistance
        low_res_high = eval(input('아래 그래프에서 제일 높은 y값 : ').replace('^','**'))
        low_res_low = eval(input('아래 그래프에서 제일 낮은 y값 : ').replace('^','**'))
        endurance_info[9] = (low_res_high + low_res_low) / 2

        # low resistance gradient
        endurance_info[10] = (low_res_high - low_res_low) / endurance_info[6]

        # 얻은 값들 엑셀 쓰기
        max_col = s_endurance.max_column

        for row in range(1, len(endurance_info)+1):
            s_endurance.cell(row, max_col + 1).value = endurance_info[row-1]

        wb.save(DIR + '/image.xlsx')
    wb.close()

    return print(f'{image_number}번째 이미지 done')

def retention(paper_name, image_number, DIR):
    print('Retention 그래프')

    wb = openpyxl.load_workbook(DIR + '/image.xlsx')
    s_retention = wb['s_retention']

    i_number = image_number
    line_cnt = int(input('선 총 몇개? : '))

    # 0 : file name / 1 : figure_name / [2: x-axis / 3: y-axis]
    # 4 : Device / 5: time / 6 : temperature
    # 7 : high resistance / 8 : high gradient
    # 9 : low resistance / 10 : low gradient

    # 선 개수만큼 반복
    for i in range(line_cnt):
        print(f'{i}번째 선')

        retention_info = ['NAN'] * 11
        retention_info[0] = f'{paper_name}.retention{i_number}_{i}'
        retention_info[1] = 'Figure_' + input('Figure 이름 : ')

        x_first = input('x-axis first : ')
        x_last = input('x-axis last : ')
        retention_info[2] = f'[{x_first}:{x_last}]'

        y_first = input('y-axis first : ')
        y_last = input('y-axis last : ')
        retention_info[3] = f'[{y_first}:{y_last}]'

        retention_info[4] = input('device : ')
        retention_info[5] = float(eval(input('time : ').replace('^','**')))

        retention_info[6] = float(input('Temperature(K) : '))
        temp_check = input('절대 온도인가요? (y / n / r) : ')
        if temp_check == 'n': retention_info[6] += 273
        elif temp_check == 'r': retention_info[6] = 300

        # high resistance
        high_res_high = eval(input('위 그래프에 제일 높은 y값 : ').replace('^','**'))
        high_res_low = eval(input('위 그래프에서 제일 낮은 y값 : ').replace('^','**'))
        retention_info[7] = (high_res_high + high_res_low) / 2

        # high restance gradient
        retention_info[8] = (high_res_high - high_res_low) / retention_info[6]

        # low resistance
        low_res_high = eval(input('아래 그래프에서 제일 높은 y값 : ').replace('^','**'))
        low_res_low = eval(input('아래 그래프에서 제일 낮은 y값 : ').replace('^','**'))
        retention_info[9] = (low_res_high + low_res_low) / 2

        # low resistance gradient
        retention_info[10] = (low_res_high - low_res_low) / retention_info[6]

        # 얻은 값들 엑셀 쓰기
        max_col = s_retention.max_column

        for row in range(1, len(retention_info)+1):
            s_retention.cell(row, max_col + 1).value = retention_info[row-1]

        wb.save(DIR + '/image.xlsx')
    wb.close()

    return print(f'{image_number}번째 이미지 done')

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

    paper_name = name
    image_number = 0

    # 임시로 DIR[0]으로 했는데 폴더 개수만큼 반복하도록 바꿔야함
    image_list = (os.listdir(DIR[0]))
    # func_list = {'0': 'curve', '1': 'device', '2': 'endurance', '3': 'retention'}

    for image in range(len(image_list) + 1):
        print('0 : I-V curve / 1 : device / 2 : endurance / 3 : retention')
        image_type = input("Image 타입 입력해주세요 : ")
        image_number += 1

        if image_type == '0': curve(paper_name, str(image_number), DIR)
        elif image_type == '1': device(paper_name, str(image_number), DIR)
        elif image_type == '2': endurance(paper_name, str(image_number), DIR)
        elif image_type == '3': retention(paper_name, str(image_number), DIR)

    # for i in range(len(func_list)):
        #     if image_type == str(i):
        #         image_number += 1
        #         eval(func_list[str(i)] + '(' + paper_name + ',' + str(image_number) + ',' + DIR + ')')
    # 임시로 DIR[0]으로 했는데 폴더 개수만큼 반복하도록 바꿔야함

AB_DIR = '/Users/SBJ/Desktop/kriss/thesis'

# 총 3개의 논문, [0,1] 번째는 이미지, QA / 마지막 논문은 text라 해당 안됨
file_list = (os.listdir(AB_DIR))
if file_list[0] or file_list[-1] == '.DS_Store': file_list.remove('.DS_Store')
file_list.sort(key=float)

DIR = [AB_DIR + '/' + file_list[0], AB_DIR + '/' + file_list[1]]

for i in range(2):
    print(file_list[i], DIR[i])
    process(file_list[i], DIR[i])