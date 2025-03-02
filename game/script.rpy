# Declare the game
define joelle = Character("Joelle", color="#ffcc99")
define mrs_peterson = Character("Mrs. Peterson", color="#cc99ff")

# Declare Backgrounds
image black = "#000000" # Simple black screen
image suburban_street_dusk = "images/suburban_street_dusk.png"
image joelle_house = "images/joelle_house.png"
image joelle_bedroom = "images/joelle_bedroom.png"
image joelle_backyard = "images/joelle_backyard.png"
image joelle_house_night = "images/joelle_house_night.png"

# Declare Character Sprites
image joelle = "images/characters/joelle.png"
image mrs_peterson = "images/characters/mrs_peterson.png"

# Start the game
label start:

    # Play ambient hum in a loop
    play audio "audio/ambient_hum.ogg" loop 

    # Scene: Black screen with ambient sound
    scene black with fade
    
    # Opening Text
    show text "There’s nothing like a fresh start. That’s what I told myself." with fade
    pause 2.0
    hide text with fade

    # Scene: Joelle arrives at Logan Ridge
    scene suburban_street_dusk with dissolve
    play sound "audio/car_engine_off.ogg" 

    joelle "Logan Ridge. Quaint, quiet, affordable. Perfect for starting over."

    joelle "Perfect for forgetting."

    # Scene: Joelle steps out of her car
    scene joelle_house with fade
    joelle "A fresh start. A quiet town. That’s all I need."

    # Scene: Joelle’s House
    scene joelle_house with dissolve
    joelle "Alright, home sweet home. Time to settle in."

    # Gameplay starts (Exploring the house)
    scene joelle_bedroom with dissolve
    menu:
        "Look at the photo of Matt":
            joelle "Matt... you’d hate this town. Too clean, too perfect."
        "Unpack moving boxes":
            joelle "So much stuff..."

    # Scene: Mrs. Peterson arrives
    scene joelle_backyard with dissolve
    show mrs_peterson with fade
    mrs_peterson "You’re going to love being here. So many great people, especially Ronnie haha."

    menu:
        "Thanks, I'm sure I will.":
            mrs_peterson "Everyone loves Ronnie. He’s quite the charming man."
        "I'm just settling in.":
            mrs_peterson "Oh, take your time! But you'll meet Ronnie soon enough."
        "I'm not really into making new friends.":
            mrs_peterson "Oh... well, I hope Logan Ridge still feels like home for you."

    # Scene: Nighttime
    scene joelle_house_night with fade
    joelle "New places are always weird at first. Empty spaces, unfamiliar sounds…"

    # End of prototype
    return
