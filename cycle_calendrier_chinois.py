#!/usr/bin/python
# -*- coding: utf-8 -*-

# https://www.imcce.fr/newsletter/docs/article_chinois.pdf
# am-duong-ngu-hanh-cua-thien-can.jpg

'''
Le calendrier civil chinois est lunisolaire (yīn yáng lì : 陰陽曆 [阴阳历])

Tronc         Nom           Élément
céleste     chinois
 
1 甲          jiǎ          Bois : mù 木
2 乙           yǐ
3 丙          bǐng          Feu : huŏ火
4 丁          dīng
5 戊           wù          Terre : tŭ 土
6 己           jǐ
7 庚          gēng         Métal : jīn 金
8 辛          xīn
9 壬          rén          Eau : shuǐ 水
10 癸         guǐ

Rameau          Signe          Direction     Saison     Mois
terrestre                                   lunaire

1 zǐ 子       Rat : shǔ鼠        0° (nord)     Hiver    11e mois
2 chǒu 丑     Bœuf : niú 牛      30°                    12e mois
3 yín 寅     Tigre : hǔ 虎       60°         Printemps  1er mois
4 mǎo 卯     Lapin : tù 兔       90° (est)              2emois
5 chén 辰    Dragon : lóng 龍    120°                   3e mois
6 sì 巳      Serpent : shé蛇     150°          Été      4e mois
7 wǔ 午      Cheval : mǎ 馬      180°(sud)              5e mois
8 wèi 未     Mouton : yáng 羊    210°                   6e mois
9 shēn 申    Singe : hóu 猴      240°        Automne    7e mois
10 yǒu 酉     Coq : jī 鷄        270°(ouest)            8e mois
11 xū 戌      Chien : gǒu 狗     300°                   9e mois
12 hài 亥      Porc : zhū 猪     330°          Hiver    10e mois

'''
elements = ['Bois:mù 木', 'Feu:huŏ火', 'Terre:tŭ 土', 'Métal:jīn 金', 'Eau:shuǐ 水']
# troncs célestes
# gia'p, â't, bi'nh, ding, mâu, ky, canh, tân, nhâm, quy' 
tronc =['jiǎ 甲', 'yǐ 乙', 'bǐng 丙', 'dīng 丁', 'wù 戊', 'jǐ 己', 'gēng 庚', 'xīn 辛', 'rén 壬', 'guǐ 癸']

# rameaux terrestres
# Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi
# ty', suu, dâ`n, meo, thi`n, ty, ngo, mui`, thân, dâu, tuât, hoi
rameaux = ['zǐ 子', 'chǒu 丑', 'yín 寅', 'mǎo 卯', 'chén 辰', 'sì 巳',
           'wǔ 午', 'wèi 未', 'shēn 申', 'yǒu 酉', 'xū 戌', 'hài 亥']

signes = ['Rat:shǔ鼠', 'Bœuf:niú 牛', 'Tigre:hǔ 虎', 'Lapin:tù 兔', 'Dragon:lóng 龍', 'Serpent:shé蛇',
          'Cheval:mǎ 馬', 'Mouton:yáng 羊','Singe:hóu 猴','Coq:jī 鷄','Chien:gǒu 狗', 'Porc:zhū 猪']

start = 1954  # 1914: giap dan, 1954: Giap ngo, 1968: mau than

dif = 2021 - start  # année courante
# 2014 jiǎ 甲 Cheval : mǎ 馬
ref = 2014
y_off = start - ref
offset = 6  # difference index entre tronc et rameau/signe

# start
print('Année =>','Tronc céleste [', 'Rameau terrestre/', 'Signe', '](Polarité,Element)')
for k in range(61):
    ky = k + y_off
    kof = ky + offset
    print('\n------------------------------------------------------>>>>>   ' if k==dif else '',
          start+k,'=>',tronc[(ky)%10],'[', rameaux[kof%12],'/', signes[kof%12],
          '](', '+' if ky%2==0 else '-',elements[(ky//2%5)],')',
          ' \n' if k==dif else '')