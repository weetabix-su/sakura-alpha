init:
    #WEETABIX NOTE: Insert weetabix credit images here
    #CGs
    image stat blank "e\b.jpg"
    image stat c001a "e\c001a.jpg"
    image stat c001b "e\c001b.jpg"
    image stat c001 "e\c001.jpg"
    image stat c002 "e\c002.jpg"
    image stat c003 "e\c003.jpg"
    image stat c004 "e\c004.jpg"
    image sora s01 "e\sora01.jpg"
    image sora s02 "e\sora02.jpg"
    image sora s03 "e\sora03.jpg"
    image sora s06 "e\sora06.jpg"
    image sora s07 "e\sora07.jpg"
    image sora ame01 "e\sora_ame01.jpg"
    image sora ame01b "e\sora_ame01b.jpg"
    image sora ame02 "e\sora_ame02.jpg"
    image sora ame03 "e\sora_ame03.jpg"
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
    scene stat blank
    $renpy.pause(2)
    scene stat c003
    $renpy.pause (1)
    scene stat c004
    $renpy.pause(0.8)
    
    jump quit
label quit:
    $renpy.quit()