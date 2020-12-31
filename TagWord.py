# -*- coding: utf-8 -*-

# tag_word : after extract word data from paper, taging all of the data
# requirement :
# 1. 포맷에 맞춘 엑셀파일( 2개의 row로 쪼개야함 )
# 2. 단락 넘어갈 때 '-' 로 된 단어 미리 수정해놔야함
# 3. 확장자 csv
# date : 2020/12/30

import pandas as pd
import csv
# from Data/chart_data import *

# have to format specific excel style (sentences -> words)
# read data and make the list
# with open('word.csv', 'r', encoding='UTF8') as csv_file:
#     reader = csv.reader(csvfile, delimiter=',')
#     pc = ([j.replace('\t', "") for i in reader for j in i])

mp = ['property', 'properties', 'conduction', 'driving', 'frequencies', 'absorbance', 'space_charge_limited', 'scattering', 'phase', 'valence', 'electronic', 'doping', 'force', 'vibrational', 'opacity', 'mass', 'holes', 'solid-state', 'thermochemical', 'doped', 'endothermic', 'energy', 'electric', 'excited', 'barrier', 'physical', 'electrochemical', 'intrinsic', 'transmittance', 'field', 'chemical', 'semiconductor', 'HOMO', 'metallic', 'charge', 'electrons', 'bands', 'electron', 'atomic', 'transport', 'LUMO', 'insulator', 'electrically', 'trapping', 'detrapping', 'stretching', 'electromagnetic', 'metal', 'carbon-rich', 'chemically']
sp_dev = ['/']
ds = ['structure', 'TE', 'BE', 'electrode', 'conventional', 'electrolyte', 'dielectric', 'buffer', 'active', 'top', 'bottom', 'layer', 'substrate', 'thickness', 'thick', 'tox', 'multistack', 'vertical', 'channel', 'Cluster', 'cluster', 'MIM', 'cross-point', 'nanowire', 'nanodot', 'nanomesh', 'X-point', 'oxram', 'CBRAM', 'terminal', 'surface', 'PMC', 'ReRAM', 'width', 'pitch', 'film']
da = ['application', 'selector', 'memristors', 'memristive', 'Memory', 'neuromorphic', 'switch', 'mulit-level', 'MLC', 'memories', 'Neural', 'NVM', 'storage', 'floating_gate', 'nonvolatile', 'transistors']

p = ["performance"]
pp = ["power", "consumption"]
pc = ['current', 'Ion', 'Iset', 'Ioff', 'leakage', 'Ileak', 'Ireset', 'compliance', 'Iprog', 'Ierase', 'Icc', 'IHRS', 'ILRS']
pv = ['voltage', 'Vset', 'Vreset', 'Vforming', 'Vread', 'Verase', 'Vprogram']
pr = ['resistance', 'resistive', 'conductivity', 'high_resistance', 'low-resistance', 'HRS', 'LRS', 'RH', 'RL', 'Roff', 'Ron', 'resistance-state']
po = ['operating', 'Forming-free', 'semi-forming', 'unipolar', 'bipolar', 'complementary', 'ON', 'OFF', 'operation', 'Program', 'erase', 'read', 'write', 'rupture', 'fast', 'slow', 'forming', 'current–voltage', 'I–V','formation', 'Electroforming', 'switching', 'breakdown', 'high', 'low', 'set', 'reset', 'positive', 'negative', 'threshold', 'sweep', 'dissolution', 'polarity']
ps = ['speed']
pe = ['endurance', 'cycles', 'cycling', 'cyclability']
pt = ['retention', 'lifetime']
pab = ['reliability', 'stability', 'variability', 'disturbance', 'uniformity', 'dispersion', 'distributions', 'cumulative', 'Fluctuation', 'deviation', 'window', 'non-uniformity', 'uniform', 'reproducible', 'probabilities']
plec = ['selectivity', 'ratio', 'Non-linearity']

mc = ['mechanism', 'VCM', 'ECM', 'interface-switching', 'filament', 'thermal-chemical', 'mechanism', 'URS', 'BRS', 'CRS', 'frenkel', 'electrochemical', 'path', 'TCM', 'Schottky', 'ohmic', 'Poole', 'precipitation', 'SCLC', 'oxidized', 'reduction']
e = ['environment', 'humidity', 'temperature', 'pressure', 'time', 'heat', 'air', 'dry']
s = ['synthesis', 'RF-sputtering', 'sputtering', 'e-beam', 'evaporator', 'spin-coated', 'sputtering', 'annealing', 'laser', 'lithography', 'photolithography', 'etching', 'etched', 'patterning', 'ALD', 'CVD', 'PVD', 'PLD', 'plasma', 'deposition', 'process', 'solution', 'self-assembly', 'drying', 'thermal', 'angled', 'beam', 'vapor', 'printing']

u = ["kg", "nm", "mm", "mA", "Ω", "lm","µm", "µ", "ppm", "L", "C"]

chemi = ['H', 'He', 'Li', 'Be', 'B', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'Ca', 'Sc', 'Ti', 'Cr', 'Fe', 'Co', 'Ni', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'Xe', 'Cs', 'Ba', 'Hf', 'Ta', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn']

data_set = {'mp': mp, 'sp_dev': sp_dev, 'ds': ds, 'da': da,
            'p' : p, 'pp': pp, 'pc': pc,
            'pv': pv, 'pr': pr, 'po': po, 'ps': ps, 'pe': pe, 'pt': pt,
            'pab': pab, 'plec': plec, 'mc': plec, 'e': e, 's': s, 'u': u, 'chemi': chemi}

# with open('word.csv', 'r', encoding='UTF8') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('word_step_1.csv','w') as new_file:
#         csv_writer = csv.writer(new_file)
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

reader = ["9", "10", "ECM", "Ω", "evaporator"]

def word_check(reader,data_set):
    checked = ['o'] * len(reader)
    print(reader)
    for i in range(len(reader)):
        for tag, checked_list in data_set.items():
            if reader[i] in checked_list :
                checked[i] = tag
                break
    print(checked)

# to do list : 숫자 찾기, list 대문자로 만들기

word_check(reader,data_set)
