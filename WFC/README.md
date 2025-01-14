# Generowanie obrazów metodą Wave Function Collapse
Wave Function Collapse (WFC) to algorytm stosowany do generowania obrazów, map lub wzorów. Został stworzony przez Maxa Gumin i cieszy się popularnością w generatywnej sztuce, grach komputerowych oraz grafice generowanej proceduralnie Jego działanie opiera się na obliczaniu entropii elementów w tabelii i ich kolapsie do jednego elementu ze zbioru możliwych.

## Wersja pythona i zależności
- Python 3.10.12 lub  nowszy
- Pygame 2.6.0 lub nowszy

## Uruchomienie programu
Program uruchamiamy poleceniem python3 main.py  [DIM] [TILESET], gdzie DIM i TILESET to argumenty opcjonalne.
- DIM oznacza wymiar siatki (będzie ona wymiaru DIMxDIM)
- TILESET to nazwa zestawu płytek które będą wyświetlane.

Domyślnie DIM=20, a TILESET='basic_set'.

## Działanie programu
Pseudokod wygląda następująco:
1. Wgranie płytek(poniżej wyjaśnie ich strukturę)
2. Stworzenie siatki 
3. Obliczenie entropii każdego elementu w siatce który jeszcze nie uległ kolapsowi.
4. Kolaps elementu o najmniejszej entropii.
5. Jeśli nie wszystkie elementy siatki uległy kolapsowi, idź do punktu 3.

### Płytki:
Są one zdefiniowane w plikach .json w katalogu tile_sets/\<wybrany zestaw\>/tiles.json. Przykładowa definicja:
{
"id":  0,
"path":  "basic_set/images/tile-0.png",
"north":  [0,  2],
"east":  [0,  1],
"south":  [0,  2],
"west":  [0,  1]
}
Klucze north, east, south oraz west określają id płytek które moga sąsiadować z nasza płytką od danej strony.



### Entropia
Entropią jest liczba możliwych płytek jakie 'pasują' w danym miejscu siatki.

### Kolaps:
Kolaps odbywa się poprzez znalezienie elementu w siatce o najmniejszej entropii (jeśli jest to niejednoznaczne to element wybierany jest losowo ze zbioru elementów o najmniejszej entropii)
, a następnie wybierany jest losowo element z możliwych na dane miejsce.

## Przykładowy przebieg programu

 

## Źródła i pomocne linki
- https://github.com/mxgmn/WaveFunctionCollapse
- https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/
- https://www.youtube.com/watch?v=rI_y2GAlQFM

