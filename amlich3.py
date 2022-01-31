# Imports
from amlich_data import *
from amlich_functions import *

'''
Le calendrier chinois est la combinaison de deux calendriers, un calendrier solaire
(agricole) et un calendrier luni-solaire (civil). Ils peuvent se résumer par les définitions
suivantes :
• Le mois lunaire commence le jour de la nouvelle Lune (shuò : 朔) calculée en temps
légal chinois pour le méridien 120° est (UTC + 8h). Avant 1929 on utilisait le
méridien de Beijing (Pékin) 116° 25′ est.
• L’année solaire (suì : 歲 岁) est une année tropique vraie, calculée également pour le
méridien 120° est et qui s'étend d'un solstice d'hiver (dōng zhì : 冬至) au suivant.
• L’année lunaire (nián : 年) débute au nouvel an chinois et comporte 12 ou 13 mois
lunaires de 29 ou 30 jours. Elle peut avoir 353, 354, 355, 383, 384 ou 385 jours.
• Le jour commence à minuit et est divisé en 96 quartiers, cette division du jour en 96
quarts d’heure, introduite par A. Schall, bouleverse les habitudes des chinois, en effet
avant la réforme le jour était divisé en 100 parties appelées kè (刻) ou en 12 doubles
heures (shí chén : 時辰 [时辰]) et la première de ces doubles heures commençait à
23h.

Construction du calendrier solaire :  
L'écliptique est découpé en 24 sections de saison de 15° chacune appelées termes
solaires (jié qì : 節氣 [节气]) le mot « jié » signifiant le nœud et le mot « qì » signifiant le
souffle. Les termes solaires principaux, ceux multiples de 30°, sont appelés zhōng qì (中氣 [
中气]). Le tableau I donne successivement, les noms des jié qì chinois, le jour où le Soleil
entre dans chaque terme solaire pour l’année grégorienne 2006, la longitude céleste écliptique
vraie du début du terme solaire, la signification du nom chinois correspondant à la section et
enfin le numéro classique que l’on donne aux termes solaires ainsi que des remarques. Les 12
termes principaux sont numérotés de Z1 à Z12 et les 12 termes secondaires sont numérotés de
J1 à J12. Les termes principaux correspondent à des mois solaires vrais et les termes
secondaires correspondent à des demi-mois solaires vrais.

Nom chinois          En 2006        Long.      Signification           Numéro / Remarques (Z principal, Z secondaire)
lì chūn 立春         4 février       315°      début du printemps             J1
yǔ shuǐ 雨水         19 février      330°      eau et pluies              Z1 : plus d’eau que de neige
jīng zhé驚蟄 [惊蛰]   6 mars          345°      réveil des insectes       J2 : fin de l’hibernation
chūn fēn 春分        21 mars         0°        équinoxe de printemps     Z2 : milieu du printemps
qīng míng 清明       5 avril.        15°       complète clarté           J3 : s’occupe des tombes
gǔ yǔ 穀雨 [谷雨]     20 avril        30°       pluie des grains          Z3 : la pluie fait germer les grains
lì xià 立夏          5 mai           45°       début de l’été                 J4
xiǎo mǎn小滿 [小满]   21 mai          60°       petite abondance           Z4 : grosseurs des grains
máng zhòng芒種 [芒种] 6 juin          75°       grains en épi                 J5
xià zhì 夏至         21 juin         90°       solstice d’été             Z5 : milieu de l’été
xiǎo shǔ 小暑        7 juillet       105°      petites chaleurs               J6
dà shǔ 大暑          23 juillet      120°      grandes chaleurs               Z6
lì qiū 立秋          7 août          135°      début de l’automne             J7
chǔ shǔ 處暑 [处暑]  23 août         150°       fin des chaleurs               Z7
bái lù 白露          8 sept.        165°       rosée blanche                  J8
qiū fēn 秋分         23 sept.       180°       équinoxe d’automne       Z8 : milieu de l’automne
hán lù 寒露          8 oct.         195°       rosée froide                   J9
shuāng jiàng 霜降    23 oct.        210°       arrivée du givre               Z9
lì dōng 立冬         7 nov.         225°       début de l’hiver              J10
xiǎo xuě 小雪        22 nov.        240°       petites neiges                 Z10
dà xuě 大雪          7 déc.         255°       grandes neiges                J11
dōng zhì 冬至        22 déc.        270°       solstice d’hiver        Z11 : début de l’année solaire
xiǎo hán 小寒        5 janv.        285°       petits froids                 J12
dà hán 大寒          20 janv.       300°       grands froids                 Z12

Le calendrier lunaire est basé sur la lunaison vraie (dìng shuò : 定朔) calculée pour le
méridien 120° est (UTC + 8h). Le premier jour du mois est le jour qui contient l’instant de la
nouvelle Lune (shuò : 朔). Les mois lunaires ne portent pas de nom, mais sont numérotés de 1
à 12. Une année lunaire peut comporter douze mois lunaires, dans ce cas on l’appellera
« année lunaire commune » ou treize mois lunaires dans ce cas on l’appellera « année lunaire
embolismique » (rùn nián : 閏年 [闰年]). En fonction de la durée des lunaisons, les années
lunaires communes peuvent avoir 353, 354 ou 355 jours et les années lunaires embolismiques
peuvent alors avoir 383, 384 ou 385 jours. Dans les années lunaires embolismiques, le mois
supplémentaire (rùn yuè : 閏月 [闰月]) porte le même numéro que le mois le précédant. Dans
la suite de cet article le mois supplémentaire aura donc le même numéro que le mois
précédent suivi de « bis ».
Certaines années lunaires peuvent contenir deux fois le jié qì : lìchūn 立春, début du
printemps, ces années sont dites double printemps (shuāng chūn : 雙春 [双春]). De même
certaines contiennent également deux fois le zhōng qì : yǔshuǐ 雨水, pluie, ces années sont
dites double printemps double pluie (shuāng chūn shuāng yŭ : 雙春雙雨 [双春双雨]).
Pour calculer le calendrier lunaire, il suffit de définir deux règles : une règle permettant
de calculer le début de l’année lunaire et une règle permettant de savoir quand un mois lunaire
supplémentaire doit être introduit.
Règle pour le calcul du début de l’année.
Cette règle est très ancienne, elle date de l’an 104 avant J.-C., elle est la suivante : Le
solstice d’hiver tombe toujours le onzième mois lunaire. Il suffit donc de remonter de 10 ou
parfois 11 lunaisons (dans le cas d’une année lunaire embolismique) pour connaître le nouvel
an chinois. Ce calcul dépend donc de la seconde règle : quand introduit-on un mois
supplémentaire ?
Règle pour introduire le mois supplémentaire.
Le mois lunaire supplémentaire est celui qui ne contient pas de terme solaire
principal zhōng qì. Avec la précision suivante : si la nouvelle Lune tombe le même jour qu’un
terme principal, le mois lunaire contient le zhōng qì même si l’entrée dans ce zhōng qì est
antérieure à la nouvelle Lune.
Avant la réforme de 1645 les chinois utilisaient le Soleil moyen. La durée moyenne du
mois solaire est le douzième de l’année tropique (365,24219052 jours) soit 30,43684921 jours
et le mois solaire est donc de 30 ou 31 jours, or la lunaison vraie est toujours inférieure à 30
jours, le mois lunaire est donc égal à 29 ou 30 jours, le calcul du mois supplémentaire ne
posait aucun problème car le mois lunaire pouvait contenir au plus une seule entrée dans un
zhōng qì. L’introduction du mouvement vrai du Soleil en 1645 fait apparaître une
complication importante. En effet lorsque la Terre est proche de son périhélie et lorsque la
nouvelle Lune est proche de son apogée, le mois solaire vrai peut être plus court que la
lunaison vraie, dans ce cas le mois lunaire peut contenir deux entrées dans un zhōng qì. Dans
ce cas peu de temps après (ou avant) on voit toujours apparaître un mois lunaire sans zhōng
qì. Mais ce mois lunaire est un faux mois supplémentaire qui vient compenser la lunaison
contenant les deux zhōng qì.
Le premier jour de l’année lunaire est donc relativement facile à trouver si l’on analyse
la répartition des nouvelles Lunes par rapport aux termes solaires principaux, mais cette
analyse est beaucoup plus délicate à programmer en raison de l’apparition de ces faux mois
supplémentaires.

La seule vraie règle est la suivante :
Le onzième mois lunaire contient toujours le solstice d’hiver et le mois supplémentaire
est celui qui ne contient pas de zhōng qì. 



# astrologie chinoise
Theo niên lịch cổ, người Á Đông phân chia một năm thành 12 tháng. Ứng theo 12 con giáp. Trong đó, các tháng Thìn – Tuất – Sửu – Mùi được tính như sau: Tháng giêng âm lịch luôn luôn là tháng Dần, tháng hai là Mão, cứ tuân theo thứ tự đó đến tháng 11 là Tý, tháng chạp là Sửu (12 tháng ứng với 12 chi). Theo thứ tự lần lượt là:

Tháng 1 (Tháng Giêng) là Dần
Tháng 2 là Mão
Tháng 3 là Thìn
Tháng 4 là Tỵ
Tháng 5 là Ngọ
Tháng 6 là Mùi
Tháng 7 là Thân
Tháng 8 là Dậu
Tháng 9 là Tuất
Tháng 10 là Hợi
Tháng 11 là Tý
Tháp 12 (Tháng Chạp) là Sửu
Bạn có thể kết hợp với các can trong năm để chi tiết hơn về can chi:

Tháng giêng của năm có hàng can Giáp, Kỷ (ví dụ năm giáp tý, kỷ tỵ) là tháng Bính Dần
Tháng giêng của năm có hàng can Ất, Canh là tháng Mậu Dần
Tháng giêng của năm có hàng can Bính, Tân là tháng Canh Dần
Tháng giêng của năm có hàng can Đinh, Nhâm là tháng Nhâm Dần
Tháng giêng của năm có hàng can Mậu, Quý là tháng Giáp Dần
Trường hợp năm có tháng nhuận thì cứ theo tháng chính (không đổi).

Trong đó 4 tam giác cân được tượng trưng cho 4 bộ Tam-Hạp: các tuổi cách nhau 4, 8, 12, 16, 20, … tuổi

* Tỵ – Dậu – Sửu (tạo thành Kim cuộc)
* Thân – Tý – Thìn (tạo thành Thủy cuộc)
* Dần – Ngọ – Tuất
* Hợi – Mẹo – Mùi (tạo thành Mộc cuộc)

Và 3 hình chữ thập tượng trưng cho 3 bộ Tứ-Hành-Xung: các tuổi cách nhau 3, 6, 9, 12, 15, 18, 21 …. tuổi

* Dần – Thân – Tỵ – Hợi
* Thìn – Tuất – Sửu – Mùi
* Tý – Ngọ – Mẹo – Dậu

'''


# ==================== main program
today = datetime.datetime.today()
currentLunarDate = getLunarDate(today.day, today.month, today.year)
print('Current Lunar Date : ', currentLunarDate)
print()
month = today.month
year = today.year
#year calendar
#print(calendar(year))
#lunar month calendar
s = lunar_month(month, year)
#print(s)
#alert('Month', s)
print(s)
tk_show(s)
print()
print('Today info:')
today_info()
#alertAbout()
# ========================create html page on desktop (big, normal or small)
setOutputSize('small')
res = printYear(2021, 4)   # 6 months by row
write2file('/home/pi/Desktop/year.html', res)