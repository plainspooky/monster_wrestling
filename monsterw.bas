100 ' SAVE "MONSTERW.BAS"
105 '
110 ' MONSTER WRESTLING for MSX-BASIC
115 ' v1.0
120 '
125 ' (c)2017 Giovanni Nunes
130 '
135 ' My version for the game of same
140 ' name inclued in the book WEIRD
145 ' COMPUTER GAMES from Usborne Publ.
150 '
155 I%=RND(-TIME):KEY OFF:COLOR 15,0,0:SCREEN 0:WIDTH 40:LOCATE ,,0:T%=60
160 MP%=4:MR%=12:MW%=2*T%:WT%=1*T%
165 DI!=3!:MA!=6!:MI!=1!
170 PC%=0:RC%=0:P$="FALSE":A$="TRUE"
175 'Main Loop
180 IF RC%>=MR% THEN 200 ELSE RC%=RC%+1
185 IF P$="TRUE" THEN GOSUB 310 ELSE GOSUB 250
190 TIME=0
195 IF TIME<WT% THEN 195 ELSE 175
200 'End of Game
205 TI$="End of Game":FG%=15:BG%=0:GOSUB 365:LI%=2
210 IF A$="TRUE" THEN RESTORE 235 ELSE IF A$="FALSE" THEN RESTORE 240 ELSE RESTORE 245
215 READ M$:IF M$="*" THEN 230
220 LOCATE 2,LI%:LI%=LI%+1:M%=INSTR(M$,"#"):IF M%>0 THEN PRINT LEFT$(M$,M%-1);RC%;RIGHT$(M$,LEN(M$)-M%) ELSE PRINT M$
225 GOTO 215
230 LOCATE 2,CSRLIN+1:PRINT "Press any key to exit... ";:K$=INPUT$(1):END
235 DATA "Phew!!!","The monster is tired and has gone", "to look for another victim.", "You survive to tell the tale!", "*"
240 DATA "You have been crushed to a pulp in","the monster's huge arms.","You survived # round(s)","*"
245 DATA "You blacked out!","*"
250 'the MONSTER mode
255 DA%=INT(RND(1)*DI!+1)+DI!:MO%=INT(RND(1)*MA!+1)+MI!
260 DI!=DI!+.5:MA!=MA!+.5:MI!=MI!+.5
265 TI$="Monster Wrestling":FG%=15:BG%=4:GOSUB 365
270 LOCATE 2,2:PRINT "Size of monster :";MO%
275 LOCATE 2,4:PRINT "Distance away :";DA%
280 LOCATE 2,6:PRINT "Muscular Effort?"
285 CO%=2:LI%=7:TIME=0:GOSUB 385
290 IF VL$="PANIC" THEN P$="TRUE":RETURN
295 IF VL$="FALSE" THEN A$="FALSE":RETURN 200
300 IF MO%*DA%<>VAL(VL$) THEN A$="FALSE":RETURN 200
305 RETURN
310 'the PANIC mode
315 PC%=PC%+1: IF PC%>3 THEN A$="NONE":RETURN 200
320 OS%=RND(1)*9+1:HI%=INT(RND(1)*9+1)*OS%
325 TI$="PANIC ON!":FG%=15:BG%=6:GOSUB 365
330 IF PC%=3 THEN LOCATE 2,10:PRINT "*** You are seeing stars ***"
335 LOCATE 2,2:PRINT "Heartbeat increase :";HI%
340 LOCATE 2,4:PRINT "Oxygen supply :";OS%
345 LOCATE 2,6:PRINT "Amount of adrenalin?"
350 CO%=2:LI%=7:TIME=MW%\2:GOSUB 385
355 IF VL$<>"PANIC" THEN IF OS%*VAL(VL$)=HI% THEN P$="FALSE" ELSE A$="FALSE":RETURN 200
360 RETURN
365 'redraw screen
370 CLS:COLOR FG%,BG%
375 LOCATE 0,0:PRINT"[ ";TI$;" ]"
380 RETURN
385 'get input
390 VL$=""
395 LOCATE CO%,LI%:PRINT"> ";VL$;" "
400 K$=INKEY$
405 IF K$="P" OR K$="p" THEN VL$="PANIC":RETURN
410 IF K$>="0" AND K$<="9" THEN VL$=VL$+K$
415 IF K$=CHR$(8) THEN IF LEN(VL$)>1 THEN VL$=LEFT$(VL$,LEN(VL$)-1) ELSE VL$=""
420 IF K$=CHR$(13) THEN RETURN
425 IF TIME>MW% THEN VL$="FALSE":RETURN
430 GOTO 395
435 ' https://usborne.com/browse-books/features/computer-and-coding-books/
