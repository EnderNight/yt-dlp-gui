all:
	gcc -o yt-dlp-gui `pkg-config --cflags --libs gtk4` main.c

.PHONY: clean

clean:
	rm -f yt-dlp-gui
