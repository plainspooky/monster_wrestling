20 LET P=0
30 LET K=3
40 CLS
50 LET X=1
60 LET Y=6
70 LET N=-1
75 LET N=N+1
80 LET G=INT(RND(0)*Y+X)
90 LET I=INT(RND(0)*K+K)
100 LET Y=Y+0.5
110 LET X=X+0.5
120 LET K=K+0.5
130 PRINT
140 PRINT
150 PRINT "SIZE OF MONSTER: ";
160 PRINT G
170 PRINT
180 PRINT "DISTANCE AWAY: ";
190 PRINT I
200 PRINT
210 PRINT "MUSCULAR EFFORT?";
220 GOSUB 570
230 IF Z<>G*I THEN GOTO 320
240 CLS
250 PRINT "MONSTER KEPT AT BAY"
260 IF N<11 THEN GOTO 75
270 PRINT "PHEW!!!!-THE MONSTER"
280 PRINT "IS TIRED AND HAS GONE TO"
290 PRINT "LOOK FOR ANOTHER VICTIM."
300 PRINT "YOU SURVIVE TO TELL THE TALE!"
310 STOP
320 CLS
330 PRINT "YOU HAVE BEEN CRUSHED"
340 PRINT "TO A PULP IN THE"
350 PRINT "MONSTER'S HUGE ARMS"
360 PRINT
370 PRINT "YOU SURVIVED ";N;" ROUNDS"
380 STOP
390 CLS
400 LET WX=INT(RND(0)*9+1)
410 LET WY=INT(RND(0)*9+1)
420 LET W=WX*WY
430 LET P=P+1
440 IF P=4 THEN GOTO 700
450 IF P=3 THEN PRINT "YOU ARE SEEING STARS"
460 PRINT "PANIC ON!!"
470 PRINT
480 PRINT "HEARTBEAT INCREASE: ";W
490 PRINT "OXYGEN SUPPLY=";WX
500 PRINT
510 PRINT "AMOUNT OF ADRENALIN? ";
520 LET Q=100
530 GOSUB 580
540 IF Z<>WY THEN GOTO 320
550 CLS: IF N<11 THEN GOTO 75
560 GOTO 270
570 LET Q=0
580 LET Z$=""
590 LET A$=INKEY$
600 IF A$=CHR$(13) THEN GOTO 680
610 IF A$="P" THEN GOTO 390
620 IF VAL(A$)=0 AND A$<>"0" THEN GOTO 650
630 PRINT A$;
640 LET Z$=Z$+A$
650 LET Q=Q+1
660 IF Q=500 THEN GOTO 320
670 GOTO 590
680 LET Z=VAL(Z$)
690 RETURN
700 CLS
710 PRINT "YOU BLACKED OUT"
730 STOP
