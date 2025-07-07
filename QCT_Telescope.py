import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import hsv_to_rgb
from scipy.special import sph_harm
from mpl_toolkits.mplot3d import Axes3D
from fastecdsa.curve import Curve
import pygame
from pygame.locals import *
import sys

# Инициализация PyGame
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Квантовый Криптотопологический Телескоп")

# Параметры кривой
_67 = Curve(name="_67", p=67, a=0, b=7, q=79, gx=2, gy=22)
G = _67.G
n = _67.q
d = 27  # Приватный ключ

# Шрифты
font_large = pygame.font.SysFont('Arial', 36, bold=True)
font_medium = pygame.font.SysFont('Arial', 24)
font_small = pygame.font.SysFont('Arial', 18)

class QuantumCryptoTopologicalTelescope:
    def __init__(self, d, n):
        self.d = d
        self.n = n
        self.focus_level = 0
        self.quantum_fluctuations = []
        self.collision_points = []
        self.singularities = []
        self.hawking_radiation = []
        self.initialize_data()
    
    def initialize_data(self):
        """Инициализация данных для визуализации"""
        # Генерация точек гиперкуба
        self.hypercube_points = []
        for ur in range(n):
            for uz in range(n):
                T = (ur * self.d + uz) % n
                Rx = T
                s = (ur + uz) % n
                self.hypercube_points.append((ur, uz, Rx, s))
        
        # Обнаружение коллизий
        collision_map = {}
        for i, point in enumerate(self.hypercube_points):
            key = (point[2], point[3])  # (Rx, s)
            if key in collision_map:
                collision_map[key].append(i)
            else:
                collision_map[key] = [i]
        
        self.collision_points = [points for points in collision_map.values() if len(points) > 1]
        
        # Инициализация квантовых флуктуаций
        self.quantum_fluctuations = np.random.rand(100, 3) * 2 - 1
        
        # Инициализация сингулярностей
        self.singularities = []
        for _ in range(5):
            self.singularities.append({
                'pos': np.random.rand(3) * 2 - 1,
                'size': np.random.uniform(0.1, 0.5),
                'energy': np.random.uniform(0.5, 2.0),
                'type': np.random.choice(['vortex', 'monopole', 'scalar'])
            })
    
    def update(self, focus_level):
        """Обновление состояния телескопа"""
        self.focus_level = focus_level
        
        # Обновление квантовых флуктуаций
        self.quantum_fluctuations += np.random.normal(0, 0.05 * focus_level, self.quantum_fluctuations.shape)
        self.quantum_fluctuations = np.clip(self.quantum_fluctuations, -1, 1)
        
        # Обновление сингулярностей
        for s in self.singularities:
            s['pos'] += np.random.normal(0, 0.01 * focus_level, 3)
            s['pos'] = np.clip(s['pos'], -1, 1)
            s['energy'] = np.clip(s['energy'] + np.random.normal(0, 0.1 * focus_level), 0.1, 3.0)
        
        # Генерация излучения Хокинга
        if np.random.rand() < 0.05 * focus_level:
            self.hawking_radiation.append({
                'pos': np.random.rand(3) * 2 - 1,
                'dir': np.random.randn(3),
                'energy': np.random.uniform(0.5, 1.5),
                'life': 100
            })
        
        # Обновление излучения Хокинга
        for rad in self.hawking_radiation[:]:
            rad['pos'] += 0.02 * focus_level * rad['dir']
            rad['life'] -= 1
            if rad['life'] <= 0:
                self.hawking_radiation.remove(rad)
    
    def render(self, surface):
        """Рендеринг телескопа на поверхность PyGame"""
        # Очистка экрана
        surface.fill((10, 5, 30))  # Темно-синий фон
        
        # Рендеринг основного дисплея телескопа
        scope_rect = pygame.Rect(50, 50, 700, 700)
        pygame.draw.rect(surface, (20, 15, 40), scope_rect)
        pygame.draw.rect(surface, (80, 60, 150), scope_rect, 3)
        
        # Рендеринг квантовых флуктуаций
        for point in self.quantum_fluctuations:
            x = int(scope_rect.x + scope_rect.width * (0.5 + 0.4 * point[0]))
            y = int(scope_rect.y + scope_rect.height * (0.5 + 0.4 * point[1]))
            size = int(2 + 3 * abs(point[2]))
            pygame.draw.circle(surface, (0, 200, 255), (x, y), size)
        
        # Рендеринг сингулярностей
        for s in self.singularities:
            x = int(scope_rect.x + scope_rect.width * (0.5 + 0.4 * s['pos'][0]))
            y = int(scope_rect.y + scope_rect.height * (0.5 + 0.4 * s['pos'][1]))
            size = int(20 * s['size'] * (1 + 0.5 * np.sin(pygame.time.get_ticks() * 0.001 * s['energy'])))
            
            # Цвет в зависимости от типа сингулярности
            if s['type'] == 'vortex':
                color = (255, 100, 100)  # Красный
            elif s['type'] == 'monopole':
                color = (100, 255, 100)  # Зеленый
            else:  # scalar
                color = (100, 100, 255)  # Синий
            
            pygame.draw.circle(surface, color, (x, y), size, 2)
            
            # Аура
            aura_size = size + int(10 * (1 + np.sin(pygame.time.get_ticks() * 0.001 * s['energy'])))
            pygame.draw.circle(surface, (*color, 100), (x, y), aura_size, 1)
        
        # Рендеринг излучения Хокинга
        for rad in self.hawking_radiation:
            x = int(scope_rect.x + scope_rect.width * (0.5 + 0.4 * rad['pos'][0]))
            y = int(scope_rect.y + scope_rect.height * (0.5 + 0.4 * rad['pos'][1]))
            size = int(5 * rad['energy'])
            pygame.draw.circle(surface, (255, 255, 200), (x, y), size)
        
        # Рендеринг коллизий
        for collision in self.collision_points[:20]:  # Ограничим количество для производительности
            points = [self.hypercube_points[i] for i in collision]
            for i, point in enumerate(points):
                x = int(scope_rect.x + scope_rect.width * (0.5 + 0.3 * (point[0]/n - 0.5)))
                y = int(scope_rect.y + scope_rect.height * (0.5 + 0.3 * (point[1]/n - 0.5)))
                size = int(3 + 5 * (point[3]/n))
                color_val = int(255 * point[2]/n)
                pygame.draw.circle(surface, (color_val, 200, 255 - color_val), (x, y), size)
                
                # Соединение точек коллизии
                if i > 0:
                    prev_point = points[i-1]
                    prev_x = int(scope_rect.x + scope_rect.width * (0.5 + 0.3 * (prev_point[0]/n - 0.5)))
                    prev_y = int(scope_rect.y + scope_rect.height * (0.5 + 0.3 * (prev_point[1]/n - 0.5)))
                    pygame.draw.line(surface, (255, 255, 0), (prev_x, prev_y), (x, y), 2)
        
        # Рендеринг информации
        info_x = 770
        title = font_large.render("Квантовый Криптотопологический Телескоп", True, (220, 180, 255))
        surface.blit(title, (info_x, 50))
        
        key_info = font_medium.render(f"Анализ ключа: d={self.d} mod {self.n}", True, (180, 220, 255))
        surface.blit(key_info, (info_x, 120))
        
        focus_info = font_medium.render(f"Фокус: {self.focus_level:.2f}", True, (255, 200, 100))
        surface.blit(focus_info, (info_x, 160))
        
        # Информация о сингулярностях
        y_pos = 220
        singularity_title = font_medium.render("Обнаруженные сингулярности:", True, (255, 150, 150))
        surface.blit(singularity_title, (info_x, y_pos))
        
        y_pos += 40
        for i, s in enumerate(self.singularities[:3]):  # Покажем только первые 3
            text = f"Сингулярность {i+1}: {s['type']}"
            text += f" | Энергия: {s['energy']:.2f}"
            singularity_text = font_small.render(text, True, (255, 200, 200))
            surface.blit(singularity_text, (info_x, y_pos))
            y_pos += 30
        
        # Информация о коллизиях
        y_pos += 20
        collisions_title = font_medium.render(f"Коллизии: {len(self.collision_points)}", True, (150, 255, 150))
        surface.blit(collisions_title, (info_x, y_pos))
        
        # Управление
        y_pos = HEIGHT - 150
        controls_title = font_medium.render("Управление телескопом:", True, (200, 200, 255))
        surface.blit(controls_title, (info_x, y_pos))
        
        controls = [
            "W/S: Увеличить/Уменьшить фокус",
            "A/D: Увеличить/Уменьшить масштаб",
            "R: Переключить ключ",
            "C: Переключить режим коллизий",
            "ESC: Выход"
        ]
        
        for i, control in enumerate(controls):
            control_text = font_small.render(control, True, (180, 220, 255))
            surface.blit(control_text, (info_x, y_pos + 40 + i * 30))
        
        # Легенда
        legend_rect = pygame.Rect(info_x, HEIGHT - 300, 400, 180)
        pygame.draw.rect(surface, (30, 20, 60), legend_rect)
        pygame.draw.rect(surface, (80, 60, 150), legend_rect, 2)
        
        legend_title = font_medium.render("Легенда:", True, (220, 180, 255))
        surface.blit(legend_title, (info_x + 10, HEIGHT - 290))
        
        legend_items = [
            ("Квантовые флуктуации", (0, 200, 255)),
            ("Вихревые сингулярности", (255, 100, 100)),
            ("Монопольные сингулярности", (100, 255, 100)),
            ("Скалярные сингулярности", (100, 100, 255)),
            ("Излучение Хокинга", (255, 255, 200)),
            ("Коллизии", (255, 255, 0))
        ]
        
        for i, (text, color) in enumerate(legend_items):
            pygame.draw.circle(surface, color, (info_x + 20, HEIGHT - 240 + i * 30), 8)
            item_text = font_small.render(text, True, (200, 200, 200))
            surface.blit(item_text, (info_x + 40, HEIGHT - 245 + i * 30))

# Создание телескопа
telescope = QuantumCryptoTopologicalTelescope(d, n)
focus = 1.0
scale = 1.0
show_collisions = True

# Главный цикл
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_r:
                # Случайный ключ
                d = np.random.randint(1, n)
                telescope = QuantumCryptoTopologicalTelescope(d, n)
            elif event.key == K_c:
                show_collisions = not show_collisions
    
    # Обработка непрерывного ввода
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        focus = min(focus + 0.05, 5.0)
    if keys[K_s]:
        focus = max(focus - 0.05, 0.1)
    
    # Обновление телескопа
    telescope.update(focus)
    
    # Рендеринг
    telescope.render(screen)
    
    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
