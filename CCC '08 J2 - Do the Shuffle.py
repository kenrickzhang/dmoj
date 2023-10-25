button = 0
songs = ["A", "B", "C", "D", "E"]

while button != 4:
    button = int(input())
    count = int(input())

    for i in range(0, count):
        if button == 1:
            first_song = songs[0]
            songs.pop(0)
            songs.append(first_song)
        elif button == 2:
            last_song = songs[-1]
            songs.pop(-1)
            new_songs = [last_song]
            for song in songs:
                new_songs.append(song)
            songs = new_songs
        elif button == 3:
            first_song = songs[0]
            songs[0] = songs[1]
            songs[1] = first_song

final_str = ""
for song in songs:
    final_str += song + " "
print(final_str.strip())