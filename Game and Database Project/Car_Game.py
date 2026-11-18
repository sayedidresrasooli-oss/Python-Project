
import random
import sys
import pygame

# راه‌اندازی پای‌گیم
pygame.init()

# تنظیمات صفحه نمایش
WIDTH, HEIGHT = 300, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodge Game")

# رنگ‌ها
GRAY = (51, 51, 51)
WHITE = (255, 255, 255)
RED = (255, 69, 0)
GREEN = (0, 255, 127)
YELLOW = (255, 215, 0)
PINK = (255, 20, 147)

# فونت‌ها
font = pygame.font.Font(None, 28)
game_over_font = pygame.font.Font(None, 36)

# لاین‌های جاده
LANES = [50, 150, 250]
player_lane = 1
player_width, player_height = 40, 70
player_target_x = LANES[player_lane] - player_width // 2
player_x = player_target_x  # موقعیت فعلی برای حرکت نرم
player_y = 410

score = 0
speed = 5
obstacles = []
clock = pygame.time.Clock()
game_over = False

# تایمر برای ساخت موانع
SPAWN_OBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_OBSTACLE, 1200)


def draw_car(surface, x, y, color):
  pygame.draw.rect(surface, color, (x - 20, y - 35, 40, 70), border_radius=8)
  pygame.draw.rect(surface, (0, 0, 0), (x - 14, y - 20, 28, 15))
  pygame.draw.rect(surface, (0, 0, 0), (x - 14, y + 10, 28, 15))


# حلقه اصلی بازی
running = True
while running:
  screen.fill(GRAY)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if game_over:
        if event.key == pygame.K_r:  # ریست بازی با کلید R
          game_over = False
          obstacles.clear()
          score = 0
          speed = 5
          player_lane = 1
          player_target_x = LANES[player_lane] - player_width // 2
          player_x = player_target_x
        elif event.key == pygame.K_ESCAPE:
          running = False
      else:
        if event.key == pygame.K_LEFT and player_lane > 0:
          player_lane -= 1
          player_target_x = LANES[player_lane] - player_width // 2
        elif event.key == pygame.K_RIGHT and player_lane < 2:
          player_lane += 1
          player_target_x = LANES[player_lane] - player_width // 2

    if event.type == SPAWN_OBSTACLE and not game_over:
      lane = random.choice(LANES)
      color = random.choice([RED, YELLOW, PINK])
      obstacles.append({"x": lane, "y": -50, "color": color})

  # حرکت نرم و انیمیشنی ماشین به سمت لاین انتخاب شده
  if player_x < player_target_x:
    player_x += min(12, player_target_x - player_x)
  elif player_x > player_target_x:
    player_x -= min(12, player_x - player_target_x)

  if not game_over:
    # رسم خطوط جاده
    for y_pos in range(0, HEIGHT, 60):
      pygame.draw.line(screen, WHITE, (100, y_pos), (100, y_pos + 30), 4)
      pygame.draw.line(screen, WHITE, (200, y_pos), (200, y_pos + 30), 4)

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    for obs in obstacles[:]:
      obs["y"] += speed
      obs_rect = pygame.Rect(obs["x"] - 20, obs["y"] - 35, 40, 70)

      if player_rect.colliderect(obs_rect):
        game_over = True

      draw_car(screen, obs["x"], obs["y"], obs["color"])

      if obs["y"] > HEIGHT + 50:
        obstacles.remove(obs)
        score += 10
        if score % 50 == 0:
          speed += 1

    draw_car(screen, player_x + player_width // 2, player_y + 35, GREEN)

    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

  else:
    # صفحه باخت
    game_over_surf = game_over_font.render("GAME OVER", True, RED)
    final_score_surf = font.render(f"Final Score: {score}", True, WHITE)
    restart_surf = font.render("Press 'R' to Restart", True, WHITE)

    screen.blit(
        game_over_surf,
        (WIDTH // 2 - game_over_surf.get_width() // 2, HEIGHT // 2 - 40),
    )
    screen.blit(
        final_score_surf,
        (WIDTH // 2 - final_score_surf.get_width() // 2, HEIGHT // 2),
    )
    screen.blit(
        restart_surf,
        (WIDTH // 2 - restart_surf.get_width() // 2, HEIGHT // 2 + 40),
    )

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
sys.exit()