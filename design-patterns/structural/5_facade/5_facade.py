# Complex subsystems
class TV:
    def on(self):
        return "TV is ON"

    def off(self):
        return "TV is OFF"

    def set_input(self, input_source):
        return f"TV input set to {input_source}"


class SoundSystem:
    def on(self):
        return "Sound system ON"

    def off(self):
        return "Sound system OFF"

    def set_volume(self, level):
        return f"Volume set to {level}"


class DVDPlayer:
    def on(self):
        return "DVD player ON"

    def off(self):
        return "DVD player OFF"

    def play(self, movie):
        return f"Playing {movie}"


class Lights:
    def dim(self, level):
        return f"Lights dimmed to {level}%"

    def on(self):
        return "Lights ON"


class HomeTheaterFacade:
    def __init__(self):
        self.tv = TV()
        self.sound = SoundSystem()
        self.dvd = DVDPlayer()
        self.lights = Lights()

    def watch_movie(self, movie):
        print("Getting ready to watch a movie...")
        print(self.lights.dim(10))
        print(self.tv.on())
        print(self.tv.set_input("DVD"))
        print(self.sound.on())
        print(self.sound.set_volume(5))
        print(self.dvd.on())
        print(self.dvd.play(movie))
        print("Enjoy your movie! 🍿")

    def end_movie(self):
        print("\nShutting down movie theater...")
        print(self.dvd.off())
        print(self.sound.off())
        print(self.tv.off())
        print(self.lights.on())
        print("Done! ✓")


# A simplified wrapper that hides complex stuff behind an easy-to-use interface
theater = HomeTheaterFacade()
theater.watch_movie("The Matrix")
theater.end_movie()
