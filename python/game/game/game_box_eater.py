import pygame
import random

pygame.init()
pygame.font.init()

DISPLAY_PANJANG = 750
DISPLAY_LEBAR = 750

window = pygame.display.set_mode((DISPLAY_PANJANG,DISPLAY_LEBAR))
clock = pygame.time.Clock()

pygame.mixer.music.load("lagu_game.mp3")
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

font_kecil = pygame.font.Font(None, 24)
font_besar = pygame.font.Font(None, 74)

speed = 8
ukuran_block = 50
WARNA_TEMBOK = (150,150,150)

peta = [
    "XXXX XXXXXX XXX",
    "X     X       X",
    "  XXX X XXXXX  ",
    "X X   X X   X X",
    "X   XXX X X X X",
    "X X       X X X",
    "X X XXXXX X X X",
    "  X         X  ", 
    "X X XXXXX X X X",
    "X X   X   X   X",
    "X X X XXXXXXX X",
    "X   X         X",
    "X XXXXXX XXXX X",
    "X             X",
    "XXXX XXXXXX XXX"
]

walls = []
for baris_idx, baris in enumerate(peta):
    for kolom_idx, karakter in enumerate(baris):
        if karakter == 'X':
            kotak = pygame.Rect(kolom_idx * ukuran_block, baris_idx*ukuran_block, ukuran_block, ukuran_block)
            walls.append(kotak)

def reset_game():
    global x, y, run_x, run_y, belok_x, belok_y, skor, game_over, game_win, points, enemies, pilihan_arah
    
    x = 375
    y = 375
    run_x = 0
    run_y = 0
    belok_x = 0
    belok_y = 0
    skor = 0
    game_over = False
    game_win = False
    
    points = []
    for baris_idx, baris in enumerate(peta):
        for kolom_idx, karakter in enumerate(baris):
            if karakter == " ":
                pt_x = kolom_idx * ukuran_block + 21
                pt_y = baris_idx * ukuran_block + 21
                points.append(pygame.Rect(pt_x, pt_y, 8, 8))
                    
    enemies = [
        {"x": 65, "y": 665, "run_x": 9, "run_y": 0, "warna": (255, 0, 0)},   
        {"x": 665, "y": 665, "run_x": -9, "run_y": 0, "warna": (250, 0, 0)} 
    ]
    pilihan_arah = [(9, 0), (-9, 0), (0, 9), (0, -9)]

reset_game()

panjang = 25
lebar = 25

isRun = True
while isRun:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT]:
        isRun = False
        
    if (game_over or game_win) and keys[pygame.K_r]:
        reset_game()

    if not game_over and not game_win:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            belok_x = -speed
            belok_y = 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            belok_x = speed
            belok_y = 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            belok_x = 0
            belok_y = speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            belok_x = 0
            belok_y = -speed

    if not game_over and not game_win:
        kotak_tes = pygame.Rect(x + belok_x, y + belok_y, panjang, lebar)
        bisaBelok = True

        for wall in walls:
            if kotak_tes.colliderect(wall):
                bisaBelok = False
                break

        if bisaBelok:
            run_x = belok_x
            run_y = belok_y    

        x += run_x
        y += run_y

        player_rect = pygame.Rect(x ,y, panjang, lebar)

        for wall in walls:
            if player_rect.colliderect(wall):
                x -= run_x
                y -= run_y
                run_x = 0
                run_y = 0
                belok_x = 0
                belok_y = 0
                break

        if x < 0 : x = DISPLAY_LEBAR - lebar
        if x > DISPLAY_LEBAR-lebar: x = 0
        if y < 0: y = DISPLAY_PANJANG - panjang
        if y > DISPLAY_PANJANG: y = 0 

        for pt in points[:]:
            if player_rect.colliderect(pt):
                points.remove(pt)
                skor += 1
                if skor >= 100:
                    game_win = True

        for enemy in enemies:
            enemy["x"] += enemy["run_x"]
            enemy["y"] += enemy["run_y"]

            enemy_rect = pygame.Rect(enemy["x"], enemy["y"], 20, 20)
            nabrak_tembok = False

            for wall in walls:
                if enemy_rect.colliderect(wall):
                    nabrak_tembok = True
                    break

            if nabrak_tembok:
                enemy["x"] -= enemy["run_x"]
                enemy["y"] -= enemy["run_y"]
                enemy["run_x"], enemy["run_y"] = random.choice(pilihan_arah)

            if enemy["x"] < 0 : enemy["x"] = DISPLAY_LEBAR - 20
            if enemy["x"] > DISPLAY_LEBAR - 20: enemy["x"] = 0
            if enemy["y"] < 0: enemy["y"] = DISPLAY_PANJANG - 20
            if enemy["y"] > DISPLAY_PANJANG: enemy["y"] = 0    

            if player_rect.colliderect(enemy_rect):
                game_over = True

    window.fill((0,0,0))

    for wall in walls:
        pygame.draw.rect(window, WARNA_TEMBOK, wall)

    for pt in points:
        pygame.draw.rect(window, (255,255,0), pt)

    if not game_over:
        pygame.draw.rect(window, (0,255,0), (x,y,panjang,lebar))

    for enemy in enemies:
        pygame.draw.rect(window, enemy['warna'], (enemy["x"], enemy["y"], 20, 20))

    point_skor = font_kecil.render(f"SKOR: {skor} / 100", True, (255, 255, 255))
    window.blit(point_skor, (620, 5))

    game_close = font_kecil.render("PRESS (LEFT SHIFT) TO CLOSE", True, (255, 255, 255))
    window.blit(game_close, (5, 5))

    if game_over:
        surface_lose = font_besar.render("GAME OVER", True, (255, 0, 0))
        window.blit(surface_lose, (220, 320))
        surface_restart = font_kecil.render("PRESS 'R' TO PLAY AGAIN", True, (255, 255, 255))
        window.blit(surface_restart, (270, 400))

    if game_win:
        surface_win = font_besar.render("YOU WIN!", True, (0, 250, 0))
        window.blit(surface_win, (250, 320))    
        surface_restart = font_kecil.render("PRESS 'R' TO PLAY AGAIN", True, (255, 255, 255))
        window.blit(surface_restart, (270, 400))

    pygame.display.update()

pygame.quit()