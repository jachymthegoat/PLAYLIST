from playlist import Playlist
from track import Track
"""
    Jáchym Nácovský
    13.12.2024
    """
def inputTrack()->Track|None:
    """Zadání skladby"""
    try:
        name = input("Zadejte název stopy: ").strip()
        if not name:
            return None
        
        length = int(input("Zadejte délku stopy (v sekundách): ").strip())
        rating = float(input("Zadejte hodnocení stopy: ").strip())

        return Track(name,length,rating)
    except ValueError:
        print("Chyba: Číselné údaje nebyly zadány správně.")
        return None
    
def inputPlaylist()-> Playlist:
    """Zadání playlistu"""
    tracks = []
    while True:
        track = inputTrack()
        if track is None:
            break
        tracks.append(track)
    
    return Playlist(tracks)

def preparePlaylist(playlist:Playlist, minLength:int) -> Playlist:
    """Příprava playlistu"""
    playlist.sortByRating()
    playlist.shuffle()
    return playlist.selectTotalLength(minLength)

def main():
    try:
        minLength = int(input("Zadejte minimální délku playlistu (v sekundách): ").strip())
    except ValueError:
        print("Chyba")
        return
    
    print("Načítání playlistu:")
    playlist = inputPlaylist()

    if not playlist._tracks:
        print("Je prázdný.")
        return
    
    preparedPlaylist = preparePlaylist(playlist,minLength)

    print("\nPlaylist:")
    print(preparedPlaylist)

    if preparedPlaylist.totalLength<minLength:
        print("Pozor, je moc krátky.")

if __name__ == "__main__":
    main()