class SongNode:
    def __init__(self, song_id):
        self.song_id = song_id
        self.next = None

class MusicPlayer:
    def __init__(self):
        self.head = None

    def add_song(self, song_id):
        """Add  a song to the playlist"""
        new_song = SongNode(song_id)
        new_song.next = self.head
        self.head = new_song

    def reverse_playlist(self):
        """Reverse the order of songs in the playlist"""
        prev = None
        current = self.head
        while current is not None:
            next_song = current.next
            current.next = prev
            prev = current
            current = next_song
        self.head = prev

    def display_playlist(self):
        """Display the songs in the playlist"""
        current = self.head
        if not current:
            print("The playlist is empty")
            return
        while current is not None:
            print(f"Sond ID: {current.song_id}")
            current = current.next

player = MusicPlayer()

player.add_song(1)
player.add_song(2)
player.add_song(3)
player.add_song(4)

print("Original Playlist")
player.display_playlist()

player.reverse_playlist()

print("\nReversed Playlist:")
player.display_playlist()
