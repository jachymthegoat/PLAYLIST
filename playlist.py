from __future__ import annotations
from track import Track
import random
class Playlist:
    """
    Reprezentuje playlist skladeb
    Jáchym Nácovský
    13.12.2024
    """
    def __init__(self, tracks:list[Track]):
        self._tracks = tracks.copy()
    @property
    def totalLength(self)->int:
        """Vrací délku všech skladeb"""
        return sum(track.length for track in self._tracks)
    
    def sortByRating(self):
        """Seřadí skladby"""
        for i in range(0, len(self._tracks)-1):
            for j in range (0, len(self._tracks)-1):
                if self._tracks[j].rating < self._tracks[j+1].rating:
                    self._tracks[j], self._tracks[j+1] = self._tracks[j+1], self._tracks[j]

    def shuffle(self):
        """Zamíchá skladby"""
        n = len(self._tracks)
        for i in range(n):
            j = random.randint(0,n-1)
            self._tracks[i], self._tracks[j] = self._tracks[j], self._tracks[i]

    def selectTotalLength(self,minLength:int)-> Playlist:
        """Vybere skladby a vytvoří playlist"""
        selected_tracks = []
        current_length = 0

        for track in self._tracks:
            if current_length >= minLength:
                break
            selected_tracks.append(track)
            current_length += track.length
        return Playlist(selected_tracks)
    
    def __str__(self):
        """Vrací playlist v daném formátu"""
        track_str = "\n".join(str(track) for track in self._tracks)
        total_minutes = int(self.totalLength) // 60
        total_seconds = int(self.totalLength) % 60
        return f"{track_str}\n[{total_minutes}:{total_seconds:02}]"