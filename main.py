import time
import sys

def print_lyrics():
    # Icons added to match the energy of the song
    song_data = [
        ("🎵 Ada dawasama mata awula...", 1.6),
        ("🎵 Gini gaththa maha mage rewula...", 1.8),
        ("🎵 Anemanda me siththewula....... ✨", 2.2),
        (" ", 0.6), 
        ("🔥 Hey!", 0.5),
        ("💃 18 Wannam ", 1.2),
        ("🌀 Kerakennam", 1.2),
        ("💖 Dennam hitha man gane", 1.5),
        ("🕒 Hawasata ehenam", 0.7),
        ("🚶 Mama ennam", 1.5),
        ("✨ Kelle uba enawaneeee... 🎶", 1.7),
        (" ", 0.2),
        ("💃 18 Wannam ", 1.0),
        ("🌀 Kerakennam", 1.3),
        ("💖 Dennam hitha man gane", 1.2),
        ("🕒 Hawasata ehenam", 0.7),
        ("🚶 Mama ennam", 1.5),
        ("✨ Kelle uba enawaneeee! 🎶", 2.5),
    ]

    print("\n" + "="*45)
    print("  🎧 PLAYING: 18 Wannam - Yuki & Ravi Jay 🎧")
    print("="*45 + "\n")

    try:
        for line, delay in song_data:
            # Different speeds for different lines
            # 'Hey!' and 'Wannam' print slightly faster
            speed = 0.02 if "Hey" in line or "Wannam" in line else 0.04
            
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(speed) 
            
            print() 
            time.sleep(delay)
        
        print("\n🎶 Papapapapapa  papapapapapap  apappa  aaaa 🎶")
        print("\n" + "="*45)
        print("           ✅ SONG FINISHED ✅")
        print("="*45)

    except KeyboardInterrupt:
        print("\n\n🛑 Music stopped. See you next time!")
        sys.exit()

if __name__ == "__main__":
    print_lyrics()