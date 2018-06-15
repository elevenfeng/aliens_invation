import pygame
import sys
from classes.bullet import Bullet
from classes.alien import Alien
from time import sleep

#飞船开火
def fire_bullet(bullets,setting,screen,ship):
    # 创建新子弹，限制最大子弹数
    if len(bullets) < setting.bullet_allow:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)

#监听键盘keydown事件
def check_keydown_events(event,setting,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        # 飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 飞船向左移
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
        #发射子弹
        fire_bullet(bullets,setting,screen,ship)

##监听键盘事件
def check_events(setting,screen,ship,bullets,aliens,states,play_bt,score_board):
    # 监视鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        #Q键退出游戏
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,setting,screen,ship,bullets)
            if event.key==pygame.K_q:
                sys.exit()
        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                ship.moving_left = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            m_x,m_y=pygame.mouse.get_pos()
            check_play_button(states,play_bt,m_x,m_y,aliens,bullets,ship,setting,screen,score_board)

#玩家单击play开始游戏
def check_play_button(states,play_bt,mouse_x,mouse_y,aliens,bullets,ship,setting,screen,score_board):
    bt_click=play_bt.rect.collidepoint(mouse_x,mouse_y)
    if bt_click and not states.game_active:
        states.reset_states()
        states.game_active=True
        setting.init_dynamic_pra()

        aliens.empty()
        bullets.empty()

        create_fleet(setting,screen,ship,aliens)
        ship.center_ship()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #积分板绘制
        score_board.pre_score()
        score_board.pre_ship()

#更新屏幕
def update_screen(setting, screen, ship,bullets,aliens,states,play_bt,score_board):
    # 让最近的屏幕绘制可见
    screen.fill(setting.bg_color)
    ship.blitme()

    #重绘所有子弹
    for bullet in bullets:
        bullet.draw_bullet()

    #重绘所有外星人
    # for alien in aliens:
    #     alien.blitme()
    aliens.draw(screen)

    #绘制play按钮
    if not states.game_active:
        play_bt.draw_bt()

    #绘制记分板
    score_board.show_score()

    pygame.display.flip()

#更新子弹位置
def update_bullets(setting,screen,ship,aliens,bullets,states,score_board):
    # 子弹更新
    bullets.update()
    # 消除屏幕外子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        check_alien_bullet_collision(aliens, bullets, setting, screen, ship,states,score_board)

#计算每行多少个外星人
def get_num_aliens_x(setting,screen,alien_width):
    alien = Alien(setting, screen)
    alien_width=alien.rect.width
    alien_space_x = setting.screen_width - 2 * alien_width
    alien_num_x = int(alien_space_x / (2 * alien_width))
    return alien_num_x

#计算屏幕可容纳多少行外星人
def get_aliens_row_num(setting,ship_height,alien_height):
    available_space_y=setting.screen_height-3*alien_height-ship_height
    num_rows=int(available_space_y/(2*alien_height))-3
    return num_rows


#创建外星人
def create_alien(setting,screen,aliens,alien_num,row_num,ship):
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_num+ship.rect.height
    aliens.add(alien)
#创建外星人群
def create_fleet(setting,screen,ship,aliens):
    alien=Alien(setting,screen)
    alien_width=alien.rect.width
    alien_num_x=get_num_aliens_x(setting,screen,alien_width)
    num_rows=get_aliens_row_num(setting,ship.rect.height,alien.rect.height)
    for row_num in range(num_rows):
        for alien_num in range(alien_num_x):
            create_alien(setting,screen,aliens,alien_num,row_num,ship)
#外星人到达屏幕边缘时采取措施
def check_fleet_edge(aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            alien.change_direct(aliens)
            break
#更新外星人位置
def update_aliens(ship,aliens,bullets,setting,screen,states,score_board):
    check_fleet_edge(aliens)
    aliens.update()
    #外星人与飞船碰撞
    if pygame.sprite.spritecollide(ship,aliens,True):
        ship_hit(ship, aliens, bullets, setting, screen, states,score_board)
    #检测外星人是否到底部并处理
    check_aliens_bottom(setting, states, screen, ship, aliens, bullets,score_board)

def check_alien_bullet_collision(aliens,bullets,setting,screen,ship,states,score_board):
    collision = pygame.sprite.groupcollide(aliens, bullets, True, False)
    if collision:
        for aliens in collision.values():
            states.score+=setting.alien_points*len(aliens)
            score_board.pre_score()

    # 外星人全部被消灭后，再重新生成外星人
    if len(aliens) == 0:
        bullets.empty()
        setting.increase_speed()
        create_fleet(setting, screen, ship, aliens)


#飞船与外星人碰撞后的动作
def ship_hit(ship,aliens,bullets,setting,screen,states,score_board):
    if states.ship_left>0:
        states.ship_left-=1
        score_board.pre_ship()
        sleep(0.5)
    else:
        states.game_active=False
        pygame.mouse.set_visible(True)

    aliens.empty()
    bullets.empty()


    ship.center_ship()

    create_fleet(setting,screen,ship,aliens)

#检测外星人是否到屏幕底部
def check_aliens_bottom(setting,states,screen,ship,aliens,bullets,score_board):
    screen_rect=screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ship,aliens,bullets,setting,screen,states,score_board)
            break;


