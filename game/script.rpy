init:
    #WEETABIX NOTE: Insert weetabix credit images here
    #CGs
    image yobi car_byoin_chusyajo_yu "yobi/car_byoin_chusyajo_yu.jpg"
	image yobi cat02 "yobi/cat02.jpg"
	image yobi cat02_h "yobi/cat02_h.jpg"
	image yobi cat03 "yobi/cat03.jpg"
	image yobi cat03_h "yobi/cat03_h.jpg"
	image yobi cat05 "yobi/cat05.jpg
	image yobi cat05_h "yobi/cat05_h.jpg"
	image yobi cat06 "yobi/cat06.jpg"
	image yobi cat07 "yobi/cat07.jpg"
	image yobi cat09 "yobi/cat09.jpg"
	image yobi cat09_h "yobi/cat09_h.jpg"
label start:
    "Note: The English Version of 'Narcissu' contains two different translations: One from the voiced version (by Seung Park, a.k.a. gp32); One from the unvoiced version (by Peter Jolly, a.k.a. Haeleth).
    "Select a version which you most prefer."
    menu:
        "gp32":
            $renpy.block_rollback()
            "DISCLAIMER: This port WILL NOT feature character vocals as it may interfere with the performance of the RenPSP Visual Novel engine.""Press X to Continue"
            jump GPstart
        "Haeleth":
            $renpy.block_rollback()
            jump HAEstart
label GPstart:
    jump quit
label HAEstart:
*introduction

;�T�E���h���[�h�E�X�y�b�N


bg "sys\spec_sample_bg2.bmp",3

wait 500

~

bg "sys\spec_sample_bg.bmp",5
btndef "sys\spec_sample_on.bmp"
;�{�^���摜�t�@�C�������������ɌĂяo���Ă���



btn 1,285,192,424,24,285,192
btn 2,285,233,424,24,285,233
btn 3,285,274,424,24,285,274
btn 4,285,314,424,24,285,314
btn 5,685,561,100,22,685,561

;�{�^���ʒu�w��

btnwait %11
;btnwait

if %11<1 jumpb
;

if %11==1 bgm "bgm\nar_inst.mp3"
;
if %11==2 bgm "bgm\n01.mp3"
;
if %11==3 bgm "bgm\koko.mp3"
;
if %11==4 bgm "bgm\n04.mp3"
;
if %11==5 bgmstop : goto *start
;

jumpb



*image
;mov $sys_midasi,"�v�����[�O"
mov $sys_midasi,"`Prologue"

bg "e\b.jpg",5
stop
dwavestop 1
mp3fadeout 1500


dwavestop 0

bg "e\c001a.jpg",1

bg "e\c001b.jpg",3

bg "e\c001.jpg",3

bg "e\c002.jpg",3

bg "e\c003.jpg",3

wait 700

bg "e\c004.jpg",5

wait 800


dwavestop 1



dwave 1,"se\rain_1.wav"

bg "e\sora_ame03.jpg",3

bg "e\c02.jpg",3

setwindow 100,358,35,17,17,17,0,3,1,1,5,#ffffff,0,0,799,599
!sd
erasetextwindow 0

;�@���@�P�X�X�U�N�@�t�@�Z�c�~�@��\
`- Spring 1996 : Setsumi -\

mp3loop "bgm\n04.mp3"

bg "e\sora_ame01.jpg",3



;�w�c�m���ɁA�c�����������v�ȕ������Ȃ������c�x\
`"My health was never particularly good, sure..."\

dwavestop 0


;�����ł����w�Z�͕��ʂɒʂ������A
;�ċx�݂ɂ͐^�����ɓ��Ă������قǗV�񂾂��Ƃ��������B\
`But I was able to attend primary school like anyone else.
`In the summer holidays I was able to play till the sun burnt me black.\


bg "e\byoin_heya_yu2.jpg",5

;�U���B���w�ɓ����Ă����̍��B@
;���������n�܂��A���j�p�̐����𒍕����������B\
`It was June, just after I entered middle school.@
` 
`It was just before the midterm tests.\

;���̎��A���߂ē��@���Ă̂��o�������B\
`It was the day after I ordered a swimming costume for the summer.
`That was the first day I was admitted to hospital.\

;���w���̒��ԃe�X�g�̏����O�A
;�~���n�߂��J���A�₯�ɗ₽�����������B\
`It was a cold, unpleasant, drizzly day.\

dwave 1,"se\rain_1.wav"

bg "e\sora_ame03.jpg",5

;�^�����Ȕ~�J���̒��B\
`Shrouded by the rainy sky, murky, white, and damp.\

;�����Ⴀ�A�ŏ��̍��́A
;�N���X�̊F���Ȃ������̂悤�Ɍ������ɗ��Ă��ꂽ�B\
`At first my classmates came to see me every day.\

;�މ@�������ɂ́A
;�T���̓x�ɁA�Ƃɂ��V�тɗ��Ă��ꂽ�B\
`When I was out of hospital, they'd come over to play at the weekend.\

;�c�ł��A�����Ȃ͍̂ŏ������B\
`But that was only at first.\


dwavestop 1


bg "e\sora_ame01.jpg",3

;�H���}���A�~���z���A
;���@�A�މ@�A�ʉ@�c�����Ă܂����@���J���Ԃ��c\
`Autumn came, and passed into winter.
`I was admitted, and discharged; went in for tests, and was readmitted...\

;���āA�F�B�ƌĂ��ł����N���X���C�g�B\
`There were people in my class that I'd called my friends.\

;�������A�m�荇���ւƕς������B\
`Before I'd really realised what was happening, they were merely acquaintances.\

;�����āA���l�ւƕς������B\
`Then strangers.\

;�G�߂��d�˂閈�ɁA
;�ޓ��̋L�������킽���͏������悤�������B\
`With each change of the seasons, I faded from more memories.\

bg "e\chara_k01.jpg",5


;�u�c�ǂ������A�h�ǂ��C�����Ȃ��h�炵���v\
`"I suppose they... don't like seeing me."\

dwavestop 0

wait 300


;�u���ʂɐ����Ă����l�ɂƂ��āA�킽���̑��݂��Ă̂́v\
`"If you've got a normal life, you don't want someone like me in it..."\

dwavestop 0

bg "e\chara_k01.jpg",3


!s80

;�u�������c�����ꂽ�悤�������c�v\
`"So they blank me out..."\

dwavestop 0

dwave 1,"se\rain_1.wav"

bg "e\w.jpg",3

bg "e\sora_ame03.jpg",5


!sd

;�u�����̋G�߂��A�����~�J�����c
;�@�N�Ƃ����t�����킷�K�v���Ȃ��߂������c�v\
`"I've passed all these seasons, under that white overcast sky, without needing to speak to anyone..."\

dwavestop 0

;�u�킽���̉p���̋��ȏ��́A
;�@�P�N���̒��ԃe�X�g�ȍ~�A�܂������ȏ��Ԃ������v\
`"My English textbook is untouched from the first-year midterms onwards..."\

dwavestop 0

bg "e\chara_0012.jpg",5

;�u�c�����Łc@�킽���̎��Ԃ��~�܂����炵���v\
`"As though...@
` even time stopped for me there..."\

dwavestop 0

bg "e\chara_0013b.jpg",3

bg "e\c005.jpg",5

bg "e\c0052.jpg",3



!w800

dwave 1,"se\z42r.wav"

bg "e\w.jpg",1

bg "e\sora01.jpg",5

bg "e\c00.jpg",5
    jump quit
label quit:
    $renpy.quit()