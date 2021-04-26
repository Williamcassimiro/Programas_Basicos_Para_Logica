from time import sleep
import emoji

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print(emoji.emojize("FELIZ ANO NOVO  :fireworks:", use_aliases=True))
