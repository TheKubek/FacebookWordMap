def common_words(no=1000):
    inp = "sie=2844816 longer=1 available=1 jest=1 i=2658222 w=2477368 nie=2209859 na=1928331 z=1725331 do=1239463 to=1202756 że=1129684 ze=1 " \
          "a=789895 o=634485 jak=613079 ale=531765 po=517714 co=515817 tak=479696 za=417406 od=351621 go=344692 " \
          "już=338548 juz=1 jego=333067 jej=315650 czy=285055 przez=284923 tylko=284848 tego=260588 sobie=229783 " \
          "jeszcze=225946 może=220962 moze=1 ze=212740 kiedy=212490 pan=205405 ich=198351 dla=192767 by=184651 " \
          "gdy=178802 teraz=176778 ja=176486 ten=173877 który=163522 ktory=1 nawet=162128 bardzo=158126 przed=155100 " \
          "tu=151295 jednak=148713 pod=147479 coś=145800 cos=1 tam=142414 wszystko=139642 przy=138531 więc=136276 " \
          "wiec=1 nic=135638 bo=135411 nim=132294 żeby=129800 zeby=1 miał=128414 mial=1 on=128249 być=127488 byc=1 " \
          "potem=122764 też=122396 tez=1 jeśli=119586 jesli=1 bez=118907 nad=110436 gdzie=106779 lecz=101111 " \
          "siebie=96422 nigdy=94150 ani=91781 właśnie=90607 sam=90060 u=85592 dobrze=84323 niż=84252 niz=1 " \
          "jakby=83531 aby=82860 ty=82207 oczy=81675 zawsze=80261 raz=79108 były=78151 byly=1 no=77040 albo=73129 " \
          "gdyby=72223 aż=71588 az=1 wtedy=71207 przecież=71048 przeciez=1 ona=67344 drzwi=67342 jako=66512 " \
          "chyba=65973 nagle=65842 wszyscy=65522 jeden=64319 czym=64061 kto=63630 sposób=60974 sposob=1 czas=60358 " \
          "kilka=59516 dlaczego=59118 razem=58853 także=58746 mój=57119 nikt=56094 choć=55515 wiele=54702 dwa=54015 " \
          "ktoś=53945 lub=53492 trzeba=53425 niech=52639 ku=51003 twarz=50948 którego=50446 we=50311 znowu=49773 " \
          "człowiek=48776 jakiś=48319 tutaj=47964 szybko=47079 tyle=46320 głos=46025 między=45854 wreszcie=45462 " \
          "również=45115 życie=45007 oczywiście=44478 znów=44082 swoje=43746 dlatego=43643 zbyt=43308 ciebie=43154 " \
          "zupełnie=42774 taki=42715 czego=42574 iż=42492 dopiero=41582 powiedzieć=41260 obok=41162 prawie=41153 " \
          "poza=40676 zaś=40331 wciąż=40299 jeżeli=40011 moje=39602 prawda=39214 trzy=39067 dzień=37545 miejsce=37244 " \
          "mimo=36896 ponieważ=36725 zaraz=36471 długo=36301 coraz=36263 podczas=36022 natychmiast=35407 zanim=34422 " \
          "cóż=34270 każdy=34256 zrobić=34054 ojciec=33735 my=33147 dość=32580 oraz=32333 jaki=32287 stanie=32035 " \
          "wcale=31810 wśród=31620 mieć=31476 zresztą=31261 dziś=31181 ile=31112 chociaż=31020 gdyż=30982 " \
          "kiedyś=30387 swój=30116 jedynie=29687 pewno=29267 nieco=28038 niemal=27191 gdzieś=26630 jedno=26510 " \
          "wokół=26003 powoli=25941 wrażenie=25717 matka=25697 świat=25484 kobieta=25435 skąd=25389 myśl=25351 " \
          "stary=25296 dużo=25233 drogi=25166 nadal=25072 drugi=24997 bowiem=24985 przynajmniej=24409 pewnie=24388 " \
          "często=23997 razy=23809 mężczyzna=23751 dokładnie=23361 niczego=23189 mówić=22961 dzięki=22953 " \
          "pewien=22782 widać=22638 cicho=22468 właściwie=22321 rzecz=22235 wolno=22068 oto=21811 ciało=21807 " \
          "czasem=21661 wiedzieć=21616 stąd=21582 wkrótce=21494 dół=21384 pół=21378 noc=20979 całkiem=20848 " \
          "wówczas=20706 dom=20554 wzrok=20509 mocno=20476 trudno=20389 dziewczyna=20301 dziecko=20261 skoro=20223 " \
          "wobec=20199 śmierć=20176 rzeczywiście=20070 koniec=19917 tuż=19804 daleko=19691 pięć=19605 serce=19518 " \
          "spokojnie=19353 czegoś=19333 wielki=19227 dłoń=19063 część=19014 najpierw=19002 mało=18868 temat=18797 " \
          "włosy=18707 wraz=18688 usta=18662 widok=18658 równie=18612 ponad=18414 robić=18365 cztery=18048 " \
          "ciągle=18028 inny=17972 znaleźć=17882 dobry=17786 wyraźnie=17701 ponownie=17679 pytanie=17632 " \
          "dzisiaj=17543 kogoś=17475 zwykle=17439 słowo=17371 jakoś=17185 nasz=17107 szczęście=17058 prawo=17005 " \
          "zapewne=16937 światło=16801 bóg=16780 tymczasem=16752 przykład=16750 przede=16715 nikogo=16505 " \
          "dzieje=16488 lekko=16450 żaden=16337 zobaczyć=16192 ramię=16113 twój=15910 wy=15887 czymś=15875 " \
          "znacznie=15861 powietrze=15719 rano=15675 doktor=15644 sprawa=15504 młody=15439 dziesięć=15208 " \
          "następnie=15195 och=15175 dwadzieścia=15172 jutro=15138 zatem=14977 list=14946 jednocześnie=14944 " \
          "ach=14796 zamiast=14788 iść=14766 dawno=14698 czemu=14648 natomiast=14516 wiadomo=14500 możliwe=14452 " \
          "słońce=14409 kapitan=14335 wiatr=14318 głośno=14250 ostatni=14201 podobnie=14152 dać=14122 ego=14018 " \
          "całkowicie=13911 zostać=13891 prosto=13889 niewiele=13859 krew=13803 broń=13797 zwłaszcza=13792 spod=13790 " \
          "większość=13740 miłość=13722 koło=13716 pomiędzy=13592 mąż=13569 wprost=13218 dopóki=13213 wieczorem=13206 " \
          "doskonale=13173 niby=13161 łatwo=13109 blisko=13041 dotąd=13023 kogo=12889 droga=12876 głęboko=12812 " \
          "żona=12749 przedtem=12726 niebo=12687 panna=12678 źle=12656 ów=12568 obaj=12553 niestety=12546 " \
          "według=12472 zewnątrz=12430 prawdopodobnie=12415 bądź=12397 miasto=12390 choćby=12342 król=12333 " \
          "ostrożnie=12301 czyli=12220 spojrzenie=12209 około=12173 zaledwie=12113 spokój=12108 moment=12064 " \
          "wczoraj=12057 gwałtownie=11911 pokój=11883 chłopiec=11769 wzdłuż=11729 przeciwko=11689 bok=11676 " \
          "pomocy=11658 cisza=11599 nowy=11570 stać=11518 ależ=11447 ból=11405 okno=11350 ciężko=11272 syn=11198 " \
          "myśleć=11072 czasami=11037 wszędzie=10946 odpowiedź=10940 obraz=10925 sto=10916 krok=10893 rok=10862 " \
          "statek=10817 żyć=10813 ledwie=10807 postać=10639 owszem=10616 dokąd=10551 szczególnie=10546 sześć=10504 " \
          "znak=10364 brat=10341 ruch=10327 los=10233 jakże=10223 brak=10105 wieczór=10019 uśmiech=9999 sen=9986 " \
          "pomysł=9985 długi=9915 chwila=9840 woda=9839 zza=9824 fakt=9799 wyraz=9796 ogień=9733 uważnie=9713 " \
          "chłopak=9710 wyłącznie=9706 cokolwiek=9664 zrozumieć=9644 akurat=9614 samochód=9605 wiadomość=9596 " \
          "naprzód=9548 numer=9523 wrócić=9448 nazwisko=9384 ni=9303 wprawdzie=9252 krótko=9251 zgodnie=9248 " \
          "czoło=9206 wysoko=9179 widzieć=9098 wina=9093 pomoc=9056 kiedykolwiek=9033 oboje=9032 rozdział=9017 " \
          "strach=8991 spotkanie=8969 dosyć=8966 szeroko=8957 dwaj=8954 oko=8885 zapach=8837 wziąć=8762 zabić=8689 " \
          "tłum=8657 toteż=8616 czekać=8487 stan=8459 brew=8442 trzydzieści=8440 jednakże=8380 oddech=8367 późno=8366 " \
          "przeciw=8324 głowa=8303 oprócz=8294 dźwięk=8291 cień=8282 zarówno=8276 czyż=8269 chętnie=8268 mama=8246 " \
          "szukać=8230 dostać=8195 niezbyt=8128 dowiedzieć=8122 mnóstwo=8030 obecnie=7983 niezwykle=7952 uczucie=7882 " \
          "południe=7846 poważnie=7825 podobno=7805 stamtąd=7795 morze=7789 dziwnie=7786 wyjść=7756 kawałek=7727 " \
          "naturalnie=7714 telefon=7700 wewnątrz=7700 problem=7677 język=7606 czarny=7602 stół=7572 wręcz=7566 " \
          "gotów=7565 słychać=7547 ksiądz=7542 poznać=7512 wypadek=7512 profesor=7485 spać=7443 ostatnio=7421 " \
          "siostra=7399 póki=7393 starannie=7377 szczerze=7362 zamiar=7350 ziemia=7344 tamten=7326 pójść=7322 " \
          "plan=7267 zabrać=7251 wysoki=7228 pies=7220 szkoda=7215 las=7206 trzeci=7194 widocznie=7181 rzadko=7173 " \
          "sporo=7172 pełen=7157 przyznać=7155 byle=7153 ono=7116 umysł=7109 historia=7104 rozkaz=7098 tydzień=7091 " \
          "patrzeć=7086 reszta=7082 nos=7058 przyjaciel=7054 cel=7008 sprawdzić=6962 poprzez=6946 podróż=6939 " \
          "miecz=6924 działo=6891 strasznie=6887 generał=6881 osobiście=6878 przykro=6840 zarazem=6787 pomimo=6778 " \
          "kamień=6689 lewo=6684 deszcz=6649 potrzeba=6646 znać=6628 moc=6626 zły=6620 wejść=6579 pamięć=6542 " \
          "nareszcie=6538 przekonać=6534 udział=6527 kolejny=6518 świetnie=6514 ostatecznie=6495 tom=6491 zdanie=6476 " \
          "wojna=6458 rozmawiać=6441 istotnie=6437 otóż=6436 ręka=6432 niedawno=6428 plecy=6409 duży=6397 rana=6364 " \
          "córka=6358 ślad=6358 pięćdziesiąt=6329 ostro=6327 dookoła=6312 nigdzie=6245 siedem=6241 nóż=6234 " \
          "jechać=6223 ciotka=6215 nowo=6199 mary=6191 nieraz=6187 spotkać=6181 czyżby=6174 wpół=6114 sytuacja=6106 " \
          "wyobrazić=6101 delikatnie=6100 zazwyczaj=6098 powstrzymać=6057 pozwolić=6054 dotychczas=6040 krzyk=6020 " \
          "zadanie=6009 kształt=6007 wierzyć=6000 pośród=5999 facet=5994 zachód=5981 uwierzyć=5979 koń=5976 " \
          "lekarz=5969 pułkownik=5946 porozmawiać=5943 poczucie=5917 niegdyś=5902 dokoła=5889 północ=5881 osiem=5869 " \
          "powrót=5866 ton=5859 znaczenie=5852 rodzina=5830 klucz=5824 ukryć=5821 żal=5821 oficer=5793 zatrzymać=5793 " \
          "liczyć=5760 przejść=5745 zimno=5743 głąb=5740 łagodnie=5739 tysiąc=5736 zmienić=5735 praca=5733 bob=5731 " \
          "jedyny=5710 obecność=5710 ciemność=5704 przyszłość=5694 słyszeć=5687 odpowiedzieć=5678 uczynić=5672 " \
          "dziewczynka=5640 piękny=5624 podobny=5599 głównie=5588 prócz=5577 stale=5576 siła=5525 niekiedy=5511 " \
          "absolutnie=5508 radość=5507 brzeg=5496 centrum=5492 zdobyć=5492 świadomość=5489 zachować=5455 " \
          "względem=5447 państwo=5445 niedługo=5423 zegarek=5422 punkt=5421 śnieg=5399 niedaleko=5395 prawdziwy=5378 " \
          "równocześnie=5375 gra=5359 pewny=5353 rozmowa=5343 pole=5337 wóz=5329 trzymać=5314 ledwo=5286 aha=5283 " \
          "własny=5273 stanowczo=5269 cześć=5266 pokazać=5247 czterdzieści=5245 wschód=5244 pisać=5242 " \
          "specjalnie=5229 obcy=5224 obiad=5210 dziwny=5203 księżyc=5202 zająć=5177 pracować=5172 przestrzeń=5167 " \
          "milczenie=5165 głupi=5158 czytać=5147 dane=5144 dotrzeć=5112 ucha=5097 niewątpliwie=5094 możliwość=5089 " \
          "słuchać=5083 spojrzeć=5074 płaszcz=5071 ubranie=5053 kraj=5048 piętnaście=5032 prędko=5029 doprawdy=5024 " \
          "śmiech=5016 jasno=4979 odejść=4979 błąd=4975 niebezpieczeństwo=4972 ciepło=4968 wcześnie=4964 pewność=4960 " \
          "pistolet=4948 gniew=4942 korytarz=4935 związek=4935 blask=4922 wracać=4917 wyjaśnić=4909 pora=4908 " \
          "silny=4904 nazajutrz=4898 utrzymać=4898 pokład=4891 walczyć=4879 następny=4869 dziadek=4853 pas=4840 " \
          "przeciwnie=4840 żołnierz=4824 szef=4820 kochanie=4793 pięknie=4791 chodzić=4790 osoba=4786 środek=4770 " \
          "dwoje=4769 atak=4765 wuj=4754 system=4752 naprzeciw=4750 zapytać=4744 uczuć=4731 drzewo=4726 grupa=4719 " \
          "hrabia=4718 pośrodku=4709 zacząć=4708 rodzaj=4707 palec=4705 duch=4684 wbrew=4671 odgłos=4668 " \
          "zapomnieć=4668 major=4647 przypomnieć=4643 łeb=4636 teren=4635 wystarczająco=4626 przyjąć=4617 miło=4616 " \
          "codziennie=4603 początkowo=4602 zamek=4600 przyjemność=4598 nerwowo=4592 spośród=4567 usłyszeć=4559 " \
          "nieźle=4558 gardło=4556 jeść=4554 pomyśleć=4546 zostawić=4535 wyjątkowo=4529 początek=4525 miesiąc=4524 " \
          "rząd=4524 hej=4520 łódź=4520 otworzyć=4506 niepokój=4501 cholera=4499 szczęśliwy=4490 spodnie=4489 " \
          "umrzeć=4464 niepewnie=4456 wiek=4441 naraz=4430 złapał=4426 czerwony=4407 kupić=4406 pociąg=4395 " \
          "kontakt=4394 porucznik=4391 gorąco=4388 tył=4355 niechętnie=4352 powód=4351 oddać=4336 łóżko=4316 " \
          "dowód=4300 nieruchomo=4289 opuścić=4289 ażeby=4283 niespodziewanie=4280 wesoło=4264 godzina=4263 " \
          "odkąd=4262 któryś=4259 okazać=4257 krzesło=4240 któż=4228 zdecydowanie=4215 odległość=4201 mieszkanie=4193 " \
          "oba=4193 policja=4170 cios=4151 odnaleźć=4149 spokojny=4132 starzec=4131 przyjść=4130 muzyka=4129 " \
          "nieustannie=4116 ogromny=4115 potrzebny=4093 słusznie=4087 działać=4083 sens=4082 okropnie=4081 fala=4064 " \
          "ciemno=4062 wolność=4062 dusza=4061 ktokolwiek=4054 wspomnienie=4052 błyskawicznie=4051 dzieło=4050 " \
          "pozostać=4041 bynajmniej=4030 wysokość=4028 dym=4026 kapelusz=4024 cichy=4023 walka=3995 charakter=3993 " \
          "brać=3990 czuć=3978 uprzejmie=3971 stopniowo=3968 śniadanie=3966 pierś=3956 schody=3955 gość=3948 " \
          "oddział=3944 ponadto=3943 omal=3936 lada=3933 chory=3931 miły=3917 ponuro=3906 głęboki=3903 owo=3891 " \
          "wszakże=3891 dyrektor=3883 wino=3882 dowódca=3879 serdecznie=3867 nisko=3865 komuś=3860 kilkanaście=3858 " \
          "lud=3855 wspaniale=3850 frank=3842 babcia=3834 opowieść=3827 zachowanie=3824 wedle=3818 robota=3816 " \
          "nazwać=3811 pusty=3789 grać=3787 częściowo=3783 niebawem=3783 bezpośrednio=3773 stanowisko=3764 lęk=3763 " \
          "udać=3763 imperium=3761 sygnał=3756 wygląd=3750 krótki=3743 wolny=3736 pat=3734 przypadek=3732 ciężki=3724 " \
          "spróbować=3718 nauczyć=3708 rzucić=3702 rozumieć=3700 wejście=3693 trzej=3684 pospiesznie=3683 ostry=3681 " \
          "strażnik=3681 mistrz=3676 prosić=3676 drobne=3675 spodziewać=3660 towarzystwo=3652 opowiedzieć=3650 " \
          "rad=3650 podnieść=3641 okres=3636 swobodnie=3631 dokonać=3630 mózg=3630 jedzenie=3625 chleb=3624 " \
          "zwłoki=3621 sierżant=3617 dach=3614 uciekać=3609 wszelki=3609 koniecznie=3607 radio=3601 biedny=3598 " \
          "para=3595 siedzieć=3583 proces=3575 dostatecznie=3569 znad=3569 nieszczęście=3563 kot=3562 potężny=3557 " \
          "dosłownie=3554 młodzieniec=3553 ciężar=3550 okrzyk=3550 pragnienie=3545 zdrowie=3545 niezależnie=3537 " \
          "istota=3536 skóra=3532 zauważyć=3528 dwanaście=3525 wódz=3511 służyć=3509 przeważnie=3505 gospodarz=3504 " \
          "złapać=3501 uważać=3485 mowa=3484 mur=3484 nawzajem=3480 gest=3474 ogromnie=3470 mianowicie=3463 " \
          "zwrócić=3462 ucho=3457 wykorzystać=3451 brzuch=3449 mrok=3416 prowadzić=3412 gruby=3402 sędzia=3399 " \
          "zimny=3398 pozbyć się=3394 przedmiot=3393 przeżyć=3386 sprzed=3384 okręt=3375 dziewięć=3372 kochać=3372 " \
          "dojść=3366 poradzić=3364 obejrzeć=3361 święty=3344 otwarcie=3342 papier=3342 bronić=3333 dwór=3329 " \
          "piwo=3323 kula=3320 słabo=3319 skończyć=3316 wszak=3312 tato=3311 wytłumaczyć=3305 święta=3286 silnik=3276 " \
          "samolot=3275 uwolnić=3271 ptak=3270 ba=3258 niecierpliwie=3258 autor=3255 zniszczyć=3243 mgła=3241 " \
          "sztuka=3241 poeta=3240 nastrój=3231 wygodnie=3231 budynek=3230 niezmiernie=3230 dno=3229 ruszyć=3229 " \
          "skutek=3225 wpływ=3224 szum=3220 wasz=3216 winien=3209 świeżo=3207 napisać=3206 tytuł=3203 adres=3200 " \
          "pamiętać=3199 "
    spl = inp.split()
    return [w.split("=")[0] for w in spl][:no]


if __name__ == '__main__':
    print(common_words(20))
