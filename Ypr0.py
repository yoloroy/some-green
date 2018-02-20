import pygame
import os
import comp

class GUI:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self, surface):
        for element in self.elements:
            render = getattr(element, "render", None)
            if callable(render):
                element.render(surface)

    def update(self):
        for element in self.elements:
            update = getattr(element, "update", None)
            if callable(update):
                element.update()

    def get_event(self, event):
        for element in self.elements:
            get_event = getattr(element, "get_event", None)
            if callable(get_event):
                element.get_event(event)

class Label:
    def __init__(self, rect, text, minus = 20):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.bgcolor = pygame.Color("white")
        self.font_color = pygame.Color("white")
        # Рассчитываем размер шрифта в зависимости от высоты
        self.font = pygame.font.Font('Boomboom.otf', self.rect.height - minus)
        self.rendered_text = None
        self.rendered_rect = None


    def render(self, surface):
   #     surface.fill(self.bgcolor, self.rect)
        self.rendered_text = self.font.render(self.text, 1, self.font_color)
        self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 2, centery=self.rect.centery)
        # выводим текст
        surface.blit(self.rendered_text, self.rendered_rect)


class Button(Label):
    def __init__(self, rect, text, minus = 20, key = None):
        super().__init__(rect, text, minus)
        self.bgcolor = (177, 224, 242)
        # при создании кнопка не нажата
        self.r = rect
        self.pressed = False
        self.key = key
        if key:
            self.img = pygame.image.load(str(key))
            self.nameofpict = key

    def render(self, surface):
        if self.key:
            self.key = pygame.transform.scale(self.img, (self.r[2], self.r[3]))
            screen.blit(self.key, (self.rect.x, self.rect.y))
            self.rendered_text = self.font.render(self.text, 1, self.font_color)
            if not self.pressed:
                color1 = pygame.Color("white")
                color2 = pygame.Color("black")
                self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 5, centery=self.rect.centery)
            else:
                color1 = pygame.Color("black")
                color2 = pygame.Color("white")
                self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 10, centery=self.rect.centery + 5)

            pygame.draw.rect(surface, color1, self.rect, 2)
            pygame.draw.line(surface, color2, (self.rect.right - 1, self.rect.top),
                             (self.rect.right - 1, self.rect.bottom), 2)
            pygame.draw.line(surface, color2, (self.rect.left, self.rect.bottom - 1),
                             (self.rect.right, self.rect.bottom - 1), 2)

        else:
            self.rendered_text = self.font.render(self.text, 1, self.font_color)
            if not self.pressed:
                color1 = pygame.Color("white")
                color2 = pygame.Color("black")
                self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 5, centery=self.rect.centery)
            else:
                color1 = pygame.Color("black")
                color2 = pygame.Color("white")
                self.rendered_rect = self.rendered_text.get_rect(x=self.rect.x + 10, centery=self.rect.centery + 5)

            pygame.draw.rect(surface, color1, self.rect, 2)
            pygame.draw.line(surface, color2, (self.rect.right - 1, self.rect.top), (self.rect.right - 1, self.rect.bottom), 2)
            pygame.draw.line(surface, color2, (self.rect.left, self.rect.bottom - 1),
                             (self.rect.right, self.rect.bottom - 1), 2)
            # выводим текст
            surface.blit(self.rendered_text, self.rendered_rect)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.pressed = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.pressed = False

def load_image(name, colorkey = None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

class PaletteButtons:  # for missions
    def __init__(self, left, top, buttons):
        self.left = left
        self.top = top
        self.button_size = board.cell_size
        self.buttons = buttons

    # отрисовка

    def render(self):
        for y in range(3):
            for x in range(5):
                try:
                    pygame.draw.rect(screen, self.buttons[5*y + x]['color'],
                                     (self.left + x * self.button_size, self.top + y * self.button_size,
                                      self.button_size, self.button_size))
                    font_w = 25
                    font = pygame.font.Font(None, font_w)
                    screen.blit(font.render(self.buttons[5*y + x]['str'], 1,
                                            (255 - self.buttons[5*y + x]['color'][0],
                                             255 - self.buttons[5*y + x]['color'][1],
                                             255 - self.buttons[5*y + x]['color'][2])),
                                (self.left + x * self.button_size, self.top + y * self.button_size,
                                 self.button_size, self.button_size))
                except Exception:
                    print(5*y + x, len(keyboard_alphavet))

    # выдача цвета

    def get_color(self, pos, key):
        for y in range(3):
            for x in range(5):
                rect = [self.left + x * self.button_size, self.top + y * self.button_size, self.button_size,
                        self.button_size]
                if pygame.Rect(rect).collidepoint(pos):
                    board.mouse_color[key] = list(self.buttons[5*y + x]['color']).copy()


class Palette:  # for SandBox
    def __init__(self, left, top):
        self.left = left
        self.top = top

    # отрисовка

    def render(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.left, self.top, 109, 300))
        pygame.draw.rect(screen, (215, 215, 255), (self.left, self.top, 109, 300), 1)
        self.left += 10  # костыль, нужно исправить
        self.top += 10

        font_w = 25
        font = pygame.font.Font(None, font_w)
        screen.blit(font.render('R', 1, (255, 0, 0)), (self.left, self.top))
        pygame.draw.rect(screen, (215, 215, 255), (self.left - 1, font_w + self.top, 11, 257), 1)

        for i in range(255, 0, -1):
            pygame.draw.rect(screen, (i, 0, 0), (self.left, i + font_w + self.top, 9, 1))
        screen.blit(font.render('G', 1, (0, 255, 0)), (self.left + 14, self.top))
        pygame.draw.rect(screen, (215, 215, 255), (self.left + 13, font_w + self.top, 11, 257), 1)

        for i in range(255, 0, -1):
            pygame.draw.rect(screen, (0, i, 0), (self.left + 14, i + font_w + self.top, 9, 1))

        screen.blit(font.render('B', 1, (0, 0, 255)), (self.left + 28, self.top))
        pygame.draw.rect(screen, (215, 215, 255), (self.left + 27, font_w + self.top, 11, 257), 1)

        for i in range(255, 0, -1):
            pygame.draw.rect(screen, (0, 0, i), (self.left + 28, i + font_w + self.top, 9, 1))

        screen.blit(font.render('Color', 1, ((board.mouse_color[0][0] + board.mouse_color[1][0]) // 2,
                                             (board.mouse_color[0][1] + board.mouse_color[1][1]) // 2,
                                             (board.mouse_color[0][2] + board.mouse_color[1][2]) // 2)),
                    (self.left + 42, self.top))

        pygame.draw.rect(screen, (215, 215, 255), (self.left + 42, font_w + self.top - 1, 15, 16), 1)
        pygame.draw.rect(screen, board.mouse_color[0], (self.left + 43, font_w + self.top, 7, 14))
        pygame.draw.rect(screen, board.mouse_color[1], (self.left + 49, font_w + self.top, 7, 14))
        self.left -= 10  # костыль, нужно исправить
        self.top -= 10

    # показ, где сейчас выставлены какие цвета

    def draw_colors(self):
        pass

    # выдача цвета

    def get_color(self, pos, key):
        rects = [pygame.Rect(self.left + 10, self.top + 35, 9, 265), 
                 pygame.Rect(self.left + 24, self.top + 35, 9, 265),
                 pygame.Rect(self.left + 38, self.top + 35, 9, 265)]
        if rects[0].collidepoint(pos):
            board.mouse_color[key][0] = screen.get_at(pos)[0]
        elif rects[1].collidepoint(pos):
            board.mouse_color[key][1] = screen.get_at(pos)[1]
        elif rects[2].collidepoint(pos):
            board.mouse_color[key][2] = screen.get_at(pos)[2]


class Board:
    def __init__(self, width=1, height=1, board=[[['q', (255, 255, 255)]]]):
        self.width = width
        self.height = height
        self.cell_size = min((size[0] - 129) // width, (size[1] - 129) // height)
        self.top = 10
        self.font = pygame.font.Font(None, self.cell_size * 6 // 7)
        self.left = 10
        self.board = board
        self.color = (215, 215, 255)
        self.grid = False
        self.mouse_color = [[255, 255, 255], [0, 0, 0]]

    # вид

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # проверка клетки на существование

    def check_cell(self, cell):
        return bool(cell)

    # отрисовка картинки какая она есть

    def render_picture(self):
        pygame.draw.rect(screen, (215, 215, 255), (self.left - 1, self.top - 1, self.cell_size * self.width + 2,
                                                   self.cell_size * self.height + 2), 1)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]:
                    pygame.draw.rect(screen, self.board[i][j][1], (j * self.cell_size + self.left,
                                                                   i * self.cell_size + self.top, self.cell_size,
                                                                   self.cell_size), 0)
                if self.grid:
                    pygame.draw.rect(screen, self.color, (j * self.cell_size + self.left - 1,
                                                          i * self.cell_size + self.top - 1, self.cell_size + 2,
                                                          self.cell_size + 2), 1)
        self.draw_focus()

    # отрисовка задания

    def render_mission(self):
        pygame.draw.rect(screen, (215, 215, 255), (self.left - 1, self.top - 1, self.cell_size * self.width + 2,
                                                   self.cell_size * self.height + 2), 1)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]:
                    try:
                        col = 255
                        color = [col, col, col]
                        if self.board[i][j][1] != board1[i][j][1]:
                            color[0] = (self.board[i][j][1][0] + color[0]) // 2
                            color[1] = (self.board[i][j][1][1] + color[1]) // 2
                            color[2] = (self.board[i][j][1][2] + color[2]) // 2
                        else:
                            raise ValueError
                    except ValueError:
                        color = self.board[i][j][1]
                    pygame.draw.rect(screen, color, (j * self.cell_size + self.left, i * self.cell_size + self.top,
                                                     self.cell_size, self.cell_size), 0)
                    if self.board[i][j][1] != board1[i][j][1] or board.grid:
                        number = str(self.board[i][j][0]) 
                        screen.blit(self.font.render(number, 1, (255 - self.board[i][j][1][0], 255 - self.board[i][j][1][1],
                                                            255 - self.board[i][j][1][2])), (j * self.cell_size + self.left,
                                                                                             i * self.cell_size + self.top))
                if self.grid:
                    pygame.draw.rect(screen, self.color, (j * self.cell_size + self.left - 1,
                                                          i * self.cell_size + self.top - 1, self.cell_size + 2,
                                                          self.cell_size + 2), 1)
        self.draw_focus()

    # нужно знать над какой клеткой мышь? идите сюда!

    def get_focus(self, pos):
        x = (pos[0] - self.left) // self.cell_size
        y = (pos[1] - self.top) // self.cell_size
        if x < 0 or x > len(self.board[0]) - 1 or y < 0 or y > len(self.board) - 1:
            self.focus = 0
        else:
            self.focus = (x, y)

    # отрисовка фокусировки

    def draw_focus(self):
        if self.focus and self.board[self.focus[1]][self.focus[0]]:
            pygame.draw.rect(screen, (255, 215, 0), (self.focus[0] * self.cell_size + self.left,
                                                     self.focus[1] * self.cell_size + self.top, self.cell_size,
                                                     self.cell_size), 1)

    # закраска клетки

    def cell_fill(self, key):
        if self.focus and self.board[self.focus[1]][self.focus[0]] and (self.board[self.focus[1]][self.focus[0]] != board_orig.board[self.focus[1]][self.focus[0]] or mode == 'sandbox'):
            if key == 1:
                self.board[self.focus[1]][self.focus[0]][1] = list(self.mouse_color[0].copy())
            elif key == 3:
                self.board[self.focus[1]][self.focus[0]][1] = list(self.mouse_color[1].copy())

    # обнуление

    def null(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]:
                    self.board[i][j][1] = (255, 255, 255)

# конвертирование картинки в формат для доски


def convert_map(board):
    a = board.copy()
    for j in range(len(board)):
        for i in range(len(board[0])):
            try:
                a[j][i] = [colors_for_cell[a[j][i]], list(a[j][i]).copy()]
                a[j][i] = a[j][i].copy()
            except TypeError:
                pass
            except KeyError:
                pass
            except AttributeError:
                pass
    return a


def full_copy(l):
    return [full_copy(i) if type(i) is list else i for i in list(l)]


def linerisator(a):
    if not a:
        return []
    else:
        if type(a[0]) == list:
            return linerisator(a[0])+linerisator(a[1:])
        else:
            return [a[0]]+linerisator(a[1:])

mus_flag = True
pygame.init()
size = 1280, 720
screen = pygame.display.set_mode(size)
pygame.mixer.pre_init()
music_list = os.listdir('music')
for i in music_list:
    music = pygame.mixer.Sound('music/' + i)
    music.play()



map_name = 'pict' #input('Enter map name: ')
mode = None
running = False
man_menue = False
main = True

keyboard_alphavet = ['q', 'w', 'e', 'r', 't',
                     'a', 's', 'd', 'f', 'g',
                     'z', 'x', 'c', 'v', 'b']

short_keys = {'113': 'q', '119': 'w', '101': 'e', '114': 'r', '116': 't',
              '97': 'a', '115': 's', '100': 'd', '102': 'f', '103': 'g',
              '122': 'z', '120': 'x', '99': 'c', '118': 'v', '98': 'b'}

gui = GUI()
b1 = Button((390, 350, 230, 80), "sandbox")
b2 = Button((640, 350, 210, 80), "manual")
b3 = Button((390, 450, 460, 80), 'settings')
b4 = Button((390, 550, 460, 100), 'Exit')
gui.add_element(b1)
gui.add_element(b2)
gui.add_element(b3)
gui.add_element(b4)

maps = GUI()
new_map = Button((300, 350, 200, 200), 'new map', 150)
maps.add_element(new_map)
nm1= Button((300 + 210, 350, 200, 200), '', 1, 'maps/'+os.listdir('maps')[0])
nm2= Button((300 + 210*2, 350, 200, 200), '', 1, 'maps/'+os.listdir('maps')[1])
selfm1 = Button((300, 560, 114, 114), '', 1, 'mymaps/land.png')
selfm2 = Button((300 + 124, 560, 114, 114),'', 1,  'mymaps/pch.jpg')
selfm3 = Button((300 + 124*2, 560, 114, 114),'',  1, 'mymaps/pyth.png')
selfm4 = Button((300 + 124*3, 560, 114, 114),'',1,   'mymaps/sng.jpg')
selfm5 = Button((300 + 124*4, 560, 114, 114),'',1, 'mymaps/yan.jpg')
maps.add_element(nm1)
maps.add_element(nm2)
maps.add_element(selfm1)
maps.add_element(selfm2)
maps.add_element(selfm3)
maps.add_element(selfm4)
maps.add_element(selfm5)
latest = Label((50, 350, 200, 80), 'lates photos:', 40)
default = Label((50, 560, 200, 80), 'default maps:', 40)
maps.add_element(latest)
maps.add_element(default)
settings = False

sets = GUI()
stopmus = Button((390, 450, 460, 80), 'stop music')
sets.add_element(stopmus)
sb1 = Button((390, 350, 230, 80), "sandbox")
sb2 = Button((640, 350, 210, 80), "manual")
sb3 = Button((390, 550, 460, 100), 'Exit')
sets.add_element(sb1)
sets.add_element(sb2)
sets.add_element(sb3)

bg = pygame.image.load('data/ppx.jpg')

while main:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False
        if b4.pressed:
            main = False
        if b1.pressed:
            mode = 'sandbox'
            running = True
            main = False
        if b2.pressed:
            mode = ''
            main = False
            man_menue = True
        if b3.pressed:
            main = False
            settings = True
        gui.get_event(event)
    gui.render(screen)
    gui.update()

    pygame.display.flip()

while settings:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            settings = False
        if stopmus.pressed:
            pygame.mixer.quit()
        if sb3.pressed:
            settings = False
        if sb1.pressed:
            mode = 'sandbox'
            running = True
            settings = False
        if sb2.pressed:
            mode = ''
            settings = False
            man_menue = True

        sets.get_event(event)
    sets.render(screen)
    sets.update()

    pygame.display.flip()
    
while man_menue:
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            man_menue = False
        for elem in maps.elements[1:3]:
            if elem.pressed:
                map_name = elem.nameofpict.split('/')[1].split('.')[0]
                running = True
                man_menue = False
        for elem in maps.elements[3:-2]:
            if elem.pressed:
                map_name = elem.nameofpict.split('/')[1].split('.')[0]
                running = True
                man_menue = False

        maps.get_event(event)
    maps.render(screen)
    maps.update()

    pygame.display.flip()



exec('import ' + map_name)
board_ = eval(map_name).grid
colors_ = list(set(linerisator(board_)) - {0})
colors = dict([(keyboard_alphavet[i], colors_[i]) for i in range(len(colors_))])
colors_for_cell = dict([(colors_[i], keyboard_alphavet[i]) for i in range(len(colors_))])
board1 = convert_map(full_copy(board_))
board = Board(len(board_[0]), len(board_), convert_map(full_copy(board_)))
board_orig = Board(len(board_[0]), len(board_), convert_map(full_copy(board_)))
if mode == 'sandbox':
    board.null()
else:
    board.null()
palette_buttons = PaletteButtons(board.left, board.top + board.cell_size * board.height + 10,
                                 [{'color': colors[i], 'str': i} if i in colors else {'color': [133, 133, 133],
                                                                                      'str': 'None'}
                                  for i in keyboard_alphavet])
palette = Palette(board.left + board.cell_size * board.width + 10, board.top)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        board.get_focus(pygame.mouse.get_pos())
        if not board.grid:
            board.grid = event.type == pygame.KEYDOWN and event.key == 306
        elif event.type == pygame.KEYUP and event.key == 306:
            board.grid = False
        
        if event.type == pygame.KEYDOWN:
            try:
                board.mouse_color[0] = list(colors[short_keys[str(event.key)]])
            except Exception:
                pass
        try:
            if event.__dict__['unicode'] in keyboard_alphavet:
                pass
        except Exception: 
            pass
        screen.fill((245, 245, 255))
        if mode == 'sandbox':
            board.render_picture()
            palette.render()
        else:
            board.render_mission()
            palette_buttons.render()
        if pygame.mouse.get_pressed()[0]:
            if mode != 'sandbox':
                palette_buttons.get_color(pygame.mouse.get_pos(), 0)
            else:
                palette.get_color(pygame.mouse.get_pos(), 0)
            board.cell_fill(1)
        elif pygame.mouse.get_pressed()[2]:
            if mode != 'sandbox':
                palette_buttons.get_color(pygame.mouse.get_pos(), 1)
            else:
                palette.get_color(pygame.mouse.get_pos(), 1)
            board.cell_fill(3)

    pygame.display.flip()
        

pygame.quit()
