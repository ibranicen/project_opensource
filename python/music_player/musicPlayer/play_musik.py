import pygame
import os
import pandas as pd
from tabulate import tabulate

os.system("cls")

pygame.init()
pygame.mixer.init()

font = pygame.font.Font(None, 24)
font_kecil = pygame.font.Font(None, 20)

list_lagu = [
    "1. dry flower",                #bila anda ingin menambahkan lagu wajib menuliskan judul lagu anda disini
    "2. spiral",            
]

no_list = []
judul_lagu = []

for item in list_lagu:
    part = item.split(".")
    if len(part) == 2:
        no_list.append(part[0].strip())
        judul_lagu.append(part[1].strip())

df = pd.DataFrame({
    'No': no_list,
    'Judul Lagu': judul_lagu
})

def music_sys(input_music:str) -> str:
    screen = pygame.display.set_mode((300,100))
    current_music = input_music

    SONG_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(SONG_END)

    is_paused = False

    def putar_lagu(lagu):
        screen.fill((0,0,0))

        if lagu == "dry flower" or lagu == "1":                 #saya berikan 1 contoh lagu dan juga filenya, file lagu harus dari directory yang sama dengan directory program ini
            pygame.mixer.music.load(f"{lagu}.mp3")              #disaranakn menggunakan directory berbeda dari codingan lain bila anda ingin menggunakan program ini
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(0)
            pygame.display.set_caption(f"{lagu}")
            judul_lagu = font.render(f"MEMUTAR LAGU {lagu.upper()}", True, (255, 255, 0))
            screen.blit(judul_lagu,(50, 45))
            print(f"musik {lagu}.mp3 diputar")

        # if lagu == "golden" or lagu == "2":                 #kalau and ingin menambah lagu pakai ini, ganti saja golden dengan judul lagu anda yang berada di direktory
        #     pygame.mixer.music.load(f"{lagu}.mp3")
        #     pygame.mixer.music.set_volume(1)
        #     pygame.mixer.music.play(0)
        #     pygame.display.set_caption(f"{lagu}")
        #     judul_lagu = font_kecil.render(f"MEMUTAR LAGU {lagu.upper()}", True, (255, 255, 0))
        #     screen.blit(judul_lagu,(33, 45))
        #     print(f"musik {lagu}.mp3 diputar")

        pygame.event.clear(SONG_END)    
    putar_lagu(current_music)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == SONG_END:
                idx = df.index[df['Judul Lagu'].str.lower() == current_music][0]
                idx_next = (idx + 1) % len(df)
                current_music = df.iloc[idx_next]['Judul Lagu']
                putar_lagu(current_music)
                is_paused = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if is_paused:
                        pygame.mixer.music.unpause()
                        is_paused = False
                        print("▶ Musik dilanjutkan")

                    else:
                        pygame.mixer.music.pause()
                        is_paused = True
                        print("⏸ Musik di-pause")

                elif event.key == pygame.K_n:
                    idx = df.index[df['Judul Lagu'].str.lower() == current_music][0]
                    idx_next = (idx + 1) % len(df)
                    current_music = df.iloc[idx_next]['Judul Lagu']
                    putar_lagu(current_music)
                    is_paused = False

        pygame.display.update()

def play_music():
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=False),"\n")
    while True:
        try:
            user_input = input("masukan judul lagu >> ").strip().lower()
            
            nomor_matching = user_input in df['No'].astype(str).values
            judul_matching = user_input in df['Judul Lagu'].str.lower().values

            if not (nomor_matching or judul_matching):
                raise Exception("Lagu tidak tersedia")

            else:
                if nomor_matching:
                    playMusic = df.loc[df['No'].astype(str) == user_input, 'Judul Lagu'].values[0]
                else:
                    playMusic = df.loc[df['Judul Lagu'].str.lower() == user_input, 'Judul Lagu'].values[0]

                print("\n[!] Tekan SPASI untuk Pause/Play. Tekan N untuk Next.")
                music_sys(playMusic)
        except Exception:
            print("error")
            continue

if __name__ == "__main__":
    play_music()