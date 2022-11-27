"""Band class"""
class Band:
    """Band class to comply with requirements """

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musicians playing their first (or no) instrument."""
        if not self.musicians:
            return f"{self.name} needs a musician!"
        return f"{self.name} is playing: {self.musicians[ 0 ]}"


if __name__ == '__main__':
    from musician import Musician

    band = Band()
    assert not band.name
    assert not band.musicians

    band.name = "Extreme"
    band.musicians.append(Musician("Nuno Bettencourt"))
    band.musicians.append(Musician("Gary Cherone"))
    band.musicians.append(Musician("Pat Badger"))
    band.musicians.append(Musician("Kevin Figueiredo"))
    print(band)
    print(band.play())