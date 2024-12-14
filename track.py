class Track:
    """
    Reprezentuje skladbu
    Jáchym Nácovský
    13.12.2024
    """
    @property
    def title(self)->str:
        """Vrací název skladby"""
        return self.__title
    @property
    def length(self)->int:
        """Vrací délku skladby"""
        return self.__length
    @property
    def rating(self)->float:
        """Vrací hodnocení skladby"""
        return self.__rating
    
    def __init__(self, title:str, length:int, rating:float):
        self.__title = title
        self.__length = length
        self.__rating = rating

    def __str__(self):
        """Vrací string v zadaném formátu"""
        minutes = self.__length // 60
        seconds = self.__length % 60
        time_str = f"{minutes}:{seconds:02d}"

        full_stars = int(self.__rating)
        decimal_part = self.__rating - full_stars

        if decimal_part >=0.75:
            star_repr = "*" * full_stars + "*"
        elif decimal_part >=0.25:
            star_repr = "*" * full_stars + "."
        else:
            star_repr = "*" * full_stars

        return f"{self.__title} [{time_str}] ({star_repr})"
