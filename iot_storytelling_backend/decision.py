def make(pos, qr_code):
    song = "none.mp3"
    picture = "none.mp3"

    if qr_code == "code1":
        if pos == 1:
            song = "song1-1.mp3"
            picture = "picture1-1.png"
        elif pos == 2:
            song = "song1-2.mp3"
            picture = "picture1-2.png"
        elif pos == 3:
            song = "song1-3.mp3"
            picture = "picture1-3.png"
        elif pos == 4:
            song = "song1-4.mp3"
            picture = "picture1-4.png"

    if qr_code == "code2":
        if pos == 1:
            song = "song2-1.mp3"
            picture = "picture2-1.png"
        elif pos == 2:
            song = "song2-2.mp3"
            picture = "picture2-1.png"
        elif pos == 3:
            song = "song2-3.mp3"
            picture = "picture2-3.png"
        elif pos == 4:
            song = "song2-4.mp3"
            picture = "picture2-4.png"

    return song, picture
