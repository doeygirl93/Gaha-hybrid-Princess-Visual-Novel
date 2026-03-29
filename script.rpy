# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("You", color="#ff69b4") # MC
define a = Character("Alpha", color="#000000") # Alpha
define b = Character("Britany", color="#ff00ff") #

# The game starts here.
image alpha angry:
    "images/alpha_angry.png"
    zoom 3.5
    yalign 1.1

image alpha annoyed:
    "images/alpha_annoyed.png"
    zoom 3.5
    yalign 1.1

image alpha blush:
    "images/alpha_blush.png"
    zoom 3.5
    yalign 1.1

image alpha cold:
    "images/alpha_cold.png"
    zoom 3.5
    yalign 1.1

image alpha flirt:
    "images/alpha_flirt.png"
    zoom 3.5
    yalign 1.1

image alpha neutral:
    "images/alpha_neutral.png"
    zoom 3.5
    yalign 1.1

image alpha shocked:
    "images/alpha_shocked.png"
    zoom 3.5
    yalign 1.1

image alpha smirk:
    "images/alpha_smirk.png"
    zoom 3.5
    yalign 1.1

image alpha walk:
    "images/alpha_walk.png"
    zoom 3.5
    yalign 1.1


image britany angry:
    "images/bully_angry.png"
    zoom 3.5
    yalign 1.1

image britany crash_out: 
    "images/bully_crash_out.png"
    zoom 3.5
    yalign 1.1

image britany crine: 
    "images/bully_crine.png"
    zoom 3.5
    yalign 1.1

image britany gum: 
    "images/bully_gum.png"
    zoom 3.5
    yalign 1.1

image britany kawaii:
    "images/bully_kawaii.png"
    zoom 3.5
    yalign 1.1

image britany laugh:
    "images/bully_laugh.png"
    zoom 3.5
    yalign 1.1

image britany neutral:
    "images/bully_neutral.png"
    zoom 3.5
    yalign 1.1

image britany scared:
    "images/bully_scared.png"
    zoom 3.5
    yalign 1.1


image mc happy:
    "images/mc_happy.png"
    zoom 4.5
    yalign 1.1

image mc hybrid:
    "images/mc_hybrid.png"
    zoom 4.5
    yalign 1.1

image mc locked: 
    "images/mc_locked.png"
    zoom 4.5
    yalign 1.1

image mc lonely:
    "images/mc_lonely.png"
    zoom 4.5
    yalign 1.1

image mc neutral:
    "images/mc_neutral.png"
    zoom 4.5
    yalign 1.1

image mc sad:
    "images/mc_sad.png"
    zoom 4.5
    yalign 1.1

image mc scared:
    "images/mc_scared.png"
    zoom 4.5
    yalign 1.1

image mc toast:
    "images/mc_toast.png"
    zoom 4.5
    yalign 1.1

image mc walk:
    "images/mc_walk.png"
    zoom 4.5
    yalign 1.1

image bg hallway = "images/bg_hallway.png"
image bg yard = "images/bg_yard.png"
image bg roof = "images/bg_roof.png"

default rep = 0






label start:

    scene bg hallway with dissolve

    show mc walk:
        xalign 0.9
        yalign 0.4
    with moveinleft

    
    show mc toast with dissolve
    m "(Thinking) Hi, I'm the main character of this game."

    show mc scared with dissolve
    m "I'm so scared its the first day of school and I don't know anyone."

    show alpha walk:
        xalign 0.0
        yalign 0.5
        xzoom -1.0
    with moveinright

    a "Hey, new kid! Watch where you're going! You know here or something?!"

    menu:
        "Stand your ground":
            jump stand_ground
            
        "Apologize and run":
            jump apologize_run
            


label stand_ground:
    show mc locked with dissolve
    m "Yo what the hell?! I do know where I'm going, you just bumped into me!"
    show alpha angry with dissolve
    a "Huh? You don't know how to talk to people? What are you, some kind of idiot?!"
    show mc scared with dissolve
    m "No, I'm not an idiot! I just don't want to fight you!"
    show alpha annoyed with dissolve
    a "Ughh girls these days! Whatever, just stay out of my way, got it?!"
    $ rep += 1
    jump cafeteria_scene

label apologize_run:
    show mc scared with dissolve
    m "Oh, I'm sorry! I didn't see you there!"
    show alpha annoyed with dissolve
    a "Whatever, just stay out of my way, got it?!"
    $ rep -= 1
    jump cafeteria_scene

label cafeteria_scene:
    scene bg yard with dissolve

    show mc walk:
        xalign 0.9
        yalign 0.4
    with moveinleft
    
    show britany neutral:
        xalign 0.0
        yalign 0.5
        xzoom -1.0
    with moveinright
    b "Hey, new kid! You're sitting alone, huh? That's so sad!"

    show britany crash_out with hpunch
    "CLANG!"
    show mc toast # Or whatever pose shows you got hit/surprised
    with vpunch

    return
