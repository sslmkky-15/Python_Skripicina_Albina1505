print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")
camel = r"""
The camel habitat...
  /--
 / @
' :;
! ;
| !
| |
| !
| :;
| !
:; :;
!!
!!
!!
!!
!!
!!
!,!
!,!
! !
! /_I
LI
LI
/_I
Look at that!"""

lion = r"""
The lion habitat...
w.
,YWMMW M
'MMMMMW, WMWMW,
YP"WMMMммммммь,
MMMMWWMMMM;
:MMM[==MWMW^;
,mM^"
,MM:.
;
MMMMb WMW" @\
MMMMMMMW "=./
WMMm
"AMP
/
F
dMMMMMMMM,_/ =_}
;
;;MMMMMMMMMMW^^;
) ) { `"^W^
\ ( /
Ww.
/ Y,
;
MMMP"1
(--,)
/ `) \"")
Al
`-, -;"\:
The lion is roaring!"""

deer = """
The deer habitat...
/1

//
11
11
1.1
//_
---
\:
:/
  ..@ 
 .-./\
;; -'
;;;
\\
1
;
/
IN
....../
Pretty good!"""

goose = r"""
The goose habitat...
(.
 (-.
 (.
 <_
 <_
 <_
 <_
 <_
 <_
 <<
 <<
 (_<_<
Beautiful!"""

bat = r"""
The bat habitat...
  /\   "~"  |
  Y
 / |\;-"~    |
/ |\,,-"~   /
\/ /\     .-'
 Y       /
 |      I
 ]\     I
 (" ~~~~~---( ~  Y. )
It's doing fine."""

rabbit = r"""
The rabbit habitat...
  /1    /1
  /1    /1
 Y :|  ///
 | jj/(.^
 >-"~"-"p"
  /     Y
 jo  o  |
 (~T~   j
 >. -'  ./
 / \/
/ |   "~"  |
 Y
/ |\;-"~    |
/ |\,,-"~   /
\/ /\     .-'
 Y       /
 |      I
 ]\     I
 (" ~~~~~---( ~  Y. )
It looks fine!"""
animals = [camel, lion, deer, goose, bat, rabbit]
while True:
    user_input = input("Please enter the number of the habitat you would like to view: > ")
    if user_input.lower() == "exit":
        animal_index = int(user_input)
        if 0 <= animal_index < len(animals):
          print("animals[animal_index]")
        else:
            print("Invalid number. Please enter a number between 0 and " + str(len(animals) - 1) + ".")
        print("Invalid input. Please enter a number or 'exit'.")
        print("See you later!")