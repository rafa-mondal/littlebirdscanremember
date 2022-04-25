# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("???")

# The game starts here.

label start:

    define flash = Fade(.25, 0.0, .75, color="#fff")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    "..."

    "You can hear something."

    "What is it?"

    with flash

    "You feel a spark blooming from your chest."

    with flash
    with flash

    "\"Neurons\" rush, twining together like a path that has found itself again."

    "Suddenly, you remember how to speak."

    r "My..."

    r "My name."

    "The words sound robotic to your ears, your voice clanging like rusty metal."

    show robot neutral

    r "What was my name?"

    r "!?"

    "Searing heat flashes at the base of your head."

    "Scenes collide, visions shift."

    "Suddenly, you remember how to see."

    with flash

    #insert POV background

    r "Where...?"

    r "Where is this place?"

    "You can't seem to remember anything."

    "Not even who you are, or how you got here."

    "With shaky form you try to stand, but to no avail."

    #clutter

    r "What was that?"

    "Your gaze turns towards the ground, where a small rusted object lay."

    "It must have fallen out of your hands. That’s weird, you didn’t
    realize you were holding anything before."

    "Picking it up, you inspect the object."

    r "This is...a music box."

    #select: open it
    menu:
        "Open it":
            jump next

label next:

    "You open the music box."

    play music "audio/music_box.mp3"

    #plays song

    "..."

    "You've heard this song before."

    "You feel \"pain\" in your chest, but you don't know why."

    r "..."

    r "I want to know who I am."

    r "I want to know why I am here."

    "With renewed confidence, you pick yourself up a second time."

    "Your metal limbs creak and groan."

    "Your robotic frame buckles and twists in agony."

    "And you look over the horizon."

    stop music fadeout 1.0

    play music "audio/when_there_was_earth.mp3"

    #cue music
    #cue scene

    "The lonely robot walks, with no memories, no stories to tell
    to those who might listen."

    "Left with nothing but the melody of a memory, it
    rings softly from deep within you."

    #with flash

    "Yet, you feel that familiar spark in your chest."

    "That somewhere in this desolate world you were born into…"

    "Someone is out there waiting for you."

    # This ends the game.

    return
