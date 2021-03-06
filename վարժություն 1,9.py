"""Վարժություն 1.9
Ունենք inc և dec ֆունկցիաները։ inc-ը վերադարձնում է արգումենտին
գումարած 1 արժեքը, իսկ dec-ը արգումենտից հանած 1 արժեքը


 def inc(a):
    return a + 1


 def dec(a):
    return a - 1


Կիրառելով պարամետրերի փոխարինման մոդելը, պարզաբանեք հետևյալ
ֆունկցիաներից յուրաքանչյուրից առաջացող գործընթացները, դրանցից որն է
ռեկուրսիվ, որը պոչավոր ռեկուրսիվ, պատասխանը հիմնավորեք


 def add1(a, b):
    if a == 0:
        return b
    else:
        return inc(add1(dec(a), b))


def add2(a, b):
    if a == 0:
        return b
    else:
        return add2(dec(a), inc(b))

Օրինակի համար դիտարկեք add1(4, 5) և add2(4, 5) կանչերը"""


#Պատսղան

"""add1() - Ֆունկցիան ռեկուրսիվ է։
քանի որ add1() - ֆունկցիան իր մարմնի մեջ կանչոմ է իրեն , դա անվանում են ռեկուրսիվ ֆունկցիա, 
add1() - առաջացող գործնդացները - կանչելով add1()- ֆունկցիան ժամանակ ստեղցվում ե լոկալ միջավայր,  ստուգվում է պայմանը,
եթե a = 0 -ի վերադարձնում է b - ի արժեքը, հակարակ դեպքում հետ է վերադարձնում  inc(add1(dec(a), b)) - ի արժեքը
inc(add1(dec(a), b)) - արտահայտությունից հետո ստեղծվում ե լոկալ միջավայր inc() - ֆունկցիայի համար, իր մեջ կանչվում է 
add1() - ֆն․ վորի մեջ վորպես արգումենտ տրվում է dec(a) և b -ն , որից հետո կանչվում է dec(a) - ֆն․ և ստեղծվում է լոկալ
միջավայր dec() - ի համար։
dec() - կանչի ժամանակ a - ի արժեքը փոքրացվում է 1 - ով
որից հետո return է արվում 3 - ը add1() - ին եվ նորից ե կանչվում  add1(3, 5)  - ֆն․ մինչև  a - հավասար է լինում 0 -ի
դրանից հետո հետ է վորադարցնում b - արժեքը, որը հավասար է 5 - ի հետո ռեկւրսիվ կերպ 4 անգամ inc() - ֆունկցիան է աշխատում 
և պատասխանը ստանում ենք 9։


add2() - ի դեպքում պոչավոր ռեկուրսիվ ե քանի վոր ամեն ֆունկցիաի կանչից հետո նոր լոկալ տարածկ չի ստեղցվում,
քանի որ գործողություններն կատարվում են ռեկուրսիայի ամեն մի քայլի ժամանակ, որվեսզի դա տեղի ունենա անհրաժեշտ է 
2 -րդ փոփոխական , որի հետ վոր կատաչվելու է գուրցողությունները , որից հետո վերջնական պատասխան վերադառցնելու է b - ի 
արժեքը։

add2() - ի կանչի ժամանակ նույնպես ստուգվում է պայմանը, եթե ճիշտ է վերադարցնում է b - ի արժեքը,
եթե ոչ կանչվելու է add2(dec(a), inc(b)) - ն ,
կանչվելու է dec(a)- ն վորը փոքրացնոլու է a - ի արժեքը 1 -ով, եվ կանչվելու ե inc(b) - րոը ավելացնելու է b - ի 
արժեքը 1 - ով։
հետո կանչվելու է  add2(3,6)։
ես գործողությունը կատարվելու է մինչև a հավասար լինի 0 -ի, որից հետո վերադարցնելու b - ի արժեքը որը հավասար ե 9 -ի։

"""