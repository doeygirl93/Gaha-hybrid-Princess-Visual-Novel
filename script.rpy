define m = Character("MC", color="#5bc0de")
define a = Character("Alpha", color="#d9534f")
define b = Character("Britany", color="#f0ad4e")
define k = Character("King", color="#5cb85c")

image bg_school_entrance = "images/bg_school_entrance.png"
image bg_bunk_bed = "images/bg_bunk_bed.png"
image bg_duegon = "images/bg_duegon.png"
image bg_roof_top = "images/bg_roof_top.png"


image mc tired:
    "images/mc_tired.png"
    zoom 4.0
image mc pained:
    "images/mc_pained.png"
    zoom 4.0
image mc determined:
    "images/mc_determined.png"
    zoom 4.0
image mc hybrid:
    "images/mc_hybrid.png"
    zoom 4.0
image mc scared:
    "images/mc_scared.png"
    zoom 4.0
image mc suprised:
    "images/mc_suprised.png"
    zoom 4.0

image alpha proctor:
    "images/alpha_proctor.png"
    zoom 4.0
image alpha suspicious:
    "images/alpha_suspicious.png"
    zoom 4.0
image alpha shocked:
    "images/alpha_shocked.png"
    zoom 4.0
image alpha hero:
    "images/alpha_hero.png"
    zoom 4.0
image alpha angy:
    "images/alpha_angy.png"
    zoom 4.0

image britany smug:
    "images/britany_smug.png"
    zoom 4.0
image britany taunt:
    "images/britany_taunt.png"
    zoom 4.0
image britany fear:
    "images/britany_fear.png"
    zoom 4.0
image britany broken:
    "images/britany_broken.png"
    zoom 4.0
image king stone:
    "images/king_stone.png"
    zoom 4.0
image king shattered:
    "images/king_shattered.png"
    zoom 4.0


default rizz_score = 0

label start:
    scene bg_school_entrance with fade
    play music "Where We Started.mp3" fadein 1.0

    "(Thinking) I've always hated this school. The endless lectures and the pointless assignments."
    "(Thinking) My mom told me this year school could be different. That it would be a place where I could find my potential."
    "(Thinking) But ever since the war started, the school has been... different."
    "(Thinking) The tension is so thck here you can cut it with a knife."
    "(Thinking) It all seems like this new anoucement is the ultimate finalee. Gradution is coming. "
    "(Thinking) And this 'new' anouncement seems to be the thing that were all waiting for."


    show king stone:
        xalign 0.5
        yalign 0.5
    with dissolve
    m "(Thinking) Is that? The king?.. Why is he here? I thought he was locked away in the castle. Why is he here to talk to us?"
    "The king is the most powerful hybrid in the world. He is the one who creat the school and society itself."
    k "Welcome, Draftees. You are here to serve the King and the Kingdom. "
    k "You've all been called here to be molded into the perfect citizens."
    k "Since they day you were born, you've been tested and measured in every way possible. "
    k" Your potentail has been calculated and sorted. You're all here because you have potentail to be heros, leaders, and legends. "
    k "And now you are here to be forged into the future of our world."

    hide king stone

    show mc tired:
        xalign 0.5
        yalign 0.5 
    with dissolve

    m "(Thinking) The king's voice is like a hammer constantly pound in my head." 
    m " I can't belive this is why I'm here. Nobody beileved me when I said I was different."
    m "(muttering) I thought me getting in here was a glitch. I thought I was a mistake. But now... " 

    show mc suprised:
        xalign 0.5
        yalign 0.5 
    with dissolve
    m "now it ALL makes sense. I can finally see the truth. I've always had potential. I've ALAWYS been different."
    m " I just needed to be in the right place to see it"
    show alpha proctor:
        xalign 0.8
        yalign 0.5
    with moveinleft

    a "hey watch it noobie, you might be new here but you better know your place."
    show mc tired:
        xzoom -1.0
        xalign 0.2
        yalign 0.5 
    with dissolve
    m "(Thinking) His voice is like a whip. I can feel the laser focus of his gaze ethicing me all over my skin."
    show mc scared:
        xzoom -1.0
        xalign 0.2
        yalign 0.5 
    with dissolve

    m "(muttering) OH umm... sorry mr alpha sir. I didn't mean to step out of line. But I just..."
    show alpha angy:
        xalign 0.8
        yalign 0.5
    a "(Interrupting) Save it chud. You’re lucky you're lucky im not in a bad moood today."
    show alpha proctor:
        xalign 0.8
        yalign 0.5
    m "(whispering quickly) Oh well then I guess i better be on my best behavior huh. well ima go to the dorms now. . ."

    hide alpha proctor with moveoutright

    m "(thinking) I guess even if I do have potental . . . WHat ever that means? . . I stil can't get through the day without being yelled at"
    hide mc tired with dissolve
    m "(Thinking) I guess I'll never be good enough for anyone. I guess I'll still be irrevelent and a mistake no matter how much potentail i have "
    
label dorm:
    scene black with fade
    scene bg_bunk_bed with fade

    show mc tired:
        xalign 0.1
        yalign 0.5
        xzoom -1.0 
    with dissolve

    show britany smug:
        xalign 0.9 
        yalign 0.5
    with moveinleft

    b "(Laughing) Is this a joke? You look like a war refugee that hopped out of a dumpter"   
return