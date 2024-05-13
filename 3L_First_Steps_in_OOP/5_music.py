class Music:

    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):         # self === song
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("Angel", "Rammstein", "....")
song1 = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
#This is "Angel" from "Rammstein"
#....
song = Music("Angel", "Rammstein", "....")
song = Music("Title", "Artist", "Lyrics")
#This is "Title" from "Artist"
#Lyrics