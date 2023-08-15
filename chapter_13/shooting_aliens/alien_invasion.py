import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from background import Background
import random

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("外星入侵地球，强强快来拯救世界吧 :)")

        # 在游戏顶部增加提示
        font = pygame.font.SysFont('SimHei', 48)  # Change None to 'Arial'
        self.play_info = font.render("使用方向键控制飞船，按下空格键发射子弹", True, (255, 255, 255))
        self.play_info_rect = self.play_info.get_rect()
        self.play_info_rect.centerx = self.screen.get_rect().centerx
        self.play_info_rect.top = 10

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.background = Background(ai_game=self)
        self._create_fleet_rande()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()            

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions2()
        

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        #TODO 修改逻辑，如果子弹击中的是cool外星人，那么需要两发子弹的碰撞，可以在alien.py中增加子弹碰撞的次数，如果击中的是普通外星人，那么就消失
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _check_bullet_alien_collisions2(self):
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, False)  # 仅移除子弹，而不移除外星人

        for bullet, aliens in collisions.items():
            for alien in aliens:
                if alien.iscool:
                    alien.hits += 1
                    if alien.hits >= 2:  # 子弹击中cool外星人两次
                        self.aliens.remove(alien)
                else:
                    self.aliens.remove(alien)  # 普通外星人直接消失

        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

    #1.打印一行cool外星人，一行普通外星人，以此类推
    #2.第1，3，5...行第一个外新人是cool, 其余都是普通外星人
    def _create_fleet(self):
        alien = Alien(self,True)
        alien_width, alien_height = alien.rect.size
        rows=5
        columns=9
        for hang in range(rows):
            for lie in range(columns):
                self._create_alien(lie * (2 * alien_width) + alien_width, hang * (2 * alien_height) + alien_height,False)



    def _create_fleet_rande(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        #1.只显示偶数位置上的外星人，
        #2.每行显示的外星人逐行递减一个，
        #3.每行显示的外星人逐行递增一个，此时应该忽略列数，
        #4.偶数位置显示cool版本外星人，奇数位置显示普通外星人
        alien = Alien(self,False)
        alien_width, alien_height = alien.rect.size
        rows=5
        columns=8
        for hang in range(rows):
            for lie in range(columns):
                    # 生成随机整数
                    random_number = random.randint(1, 100)  # 生成1到100之间的随机整数
                    iscool=False
                    if random_number % 2 == 0:
                        iscool=True
                    self._create_alien(lie * (2 * alien_width) + alien_width, hang * (2 * alien_height) + alien_height,iscool)


    def _create_alien(self, x_position, y_position, is_cool=False):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self,is_cool)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    #改变飞船整体移动方向 用边界是否触碰到窗口来的判断方向的改变
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        #绘制背景图片
        self.background.update()
        self.background.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # 显示游戏顶部的提示信息
        self.screen.blit(self.play_info, self.play_info_rect)
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()