past_qrcode = ""

def make(pos,qrcode):

    if qrcode == "kode1":
        past_qrcode = 'kode1'
        if past_qrcode == "kode1" and pos == 1:
            if pos == 1:
                pass
        elif past_qrcode != "kode1" and pos == 1:
            song = "song1-1"
            picture = "picture1-1"
        elif pos == 2:
            song = "song1-2"
            picture = "picture1-2"
        elif pos == 3:
            song = "song1-3"
            picture = "picture1-3"


    if qrcode == "kode2":
        past_qrcode = 'kode2'
        if pos == 1:
            song = "song2-1"
            picture = "picture2-1"
        elif pos == 2:
            song = "song2-2"
            picture = "picture2-2"
        elif pos == 3:
            song = "song2-3"
            picture = "picture2-3"

    if qrcode == "kode3":
        past_qrcode = 'kode3'
        if pos == 1:
            song = "song3-1"
            picture = "picture3-1"
        elif pos == 2:
            song = "song3-2"
            picture = "picture3-2"
        elif pos == 3:
            song = "song3-3"
            picture = "picture3-3"

    if qrcode == "kode4":
        past_qrcode = 'kode4'
        if pos == 1:
            song = "song4-1"
            picture = "picture4-1"
        elif pos == 2:
            song = "song4-2"
            picture = "picture4-2"
        elif pos == 3:
            song = "song4-3"
            picture = "picture4-3"

    past_qrcode = qrcode
    return song, picture
