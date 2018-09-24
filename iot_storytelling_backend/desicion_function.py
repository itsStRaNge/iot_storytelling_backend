def desfu(pos,qrcode):

    if qrcode == "kode1":
        if pos == 1:
            song = "song1-1"
            picture = "picture1-1"
        elif pos == 2:
            song = "song1-2"
            picture = "picture1-2"
        elif pos == 3:
            song = "song1-3"
            picture = "picture1-3"
        elif pos == 4:
            song = "song1-4"
            picture = "picture1-4"

    if qrcode == "kode2":
        if pos == 1:
            song = "song2-1"
            picture = "picture2-1"
        elif pos == 2:
            song = "song2-2"
            picture = "picture2-1"
        elif pos == 3:
            song = "song2-3"
            picture = "picture2-3"
        elif pos == 4:
            song = "song2-4"
            picture = "picture2-4"

    return song, picture
