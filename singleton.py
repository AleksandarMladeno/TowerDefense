import pygame
import os

# enemy path
PATH1_1 = [(91, 348), (110, 330), (135, 322), (158, 329), (184, 340), (195, 364), (195, 392), (191, 420), 
            (200, 448), (203, 473), (228, 485), (254, 490), (294, 488), (327, 483), (365, 473), (386, 452),
            (400, 429), (401, 400), (381, 372), (354, 355), (323, 339), (308, 320), (325, 295), (352, 273),
            (392, 256), (439, 263), (462, 287), (482, 313), (502, 328), (528, 343), (556, 323), (561, 287), 
            (564, 247), (569, 195)]
PATH1_2=[(614, 586), (621, 554), (637, 523), (667, 510), (706, 498), (743, 506), (782, 511), (830, 506), 
            (866, 496), (889, 470), (886, 437), (847, 422), (810, 403), (780, 378), (798, 342), (829, 323), 
            (853, 299), (856, 256), (813, 250), (768, 256), (725, 264), (692, 288), (649, 311), (609, 327), 
            (564, 331), (560, 298), (568, 239), (579, 198)]

PATH2_1 = [(87, 269), (97, 276), (108, 282), (119, 287), (130, 292), (141, 297), (153, 302), (164, 306),
        (175, 311), (186, 315), (198, 319), (211, 322), (223, 326), (237, 330), (249, 332), (262, 335), (276, 338),
        (290, 339), (302, 342), (315, 346), (326, 348), (339, 349), (354, 350), (371, 352), (381, 355), (392, 357),
        (403, 359), (417, 361), (430, 364), (446, 365), (459, 367), (472, 369), (488, 369), (500, 369), (513, 369),
        (529, 366), (543, 365), (556, 363), (571, 360), (586, 356), (600, 353), (611, 349), (625, 345), (638, 339),
        (651, 335), (665, 331), (679, 326), (693, 320), (704, 315), (715, 311), (727, 307), (740, 302), (753, 299),
        (766, 295), (777, 289), (789, 281), (803, 277), (816, 273), (828, 270), (840, 263), (856, 262), (869, 257),
        (881, 255), (894, 252), (907, 248), (918, 244), (933, 240), (950, 237), (964, 235), (979, 233), (991, 232),
        (1001, 232), (1013, 232)]
PATH2_2 = [(302, 595), (310, 588), (320, 583), (330, 578), (339, 573), (349, 568), (359, 561), (369, 554),
        (378, 548), (387, 540), (396, 532), (405, 523), (413, 515), (421, 506), (428, 495), (433, 486), (438, 475),
        (442, 465), (445, 454), (447, 441), (450, 427), (453, 412), (456, 401), (461, 390), (470, 384), (479, 380),
        (489, 379), (502, 379), (512, 378), (524, 375), (538, 373), (547, 371), (558, 369), (571, 366), (581, 362),
        (590, 359), (600, 355), (611, 350), (622, 346), (633, 343), (645, 341), (658, 337), (668, 333), (681, 329),
        (694, 326), (704, 322), (715, 318), (726, 313), (736, 308), (748, 303), (758, 297), (767, 295), (781, 290),
        (793, 286), (806, 281), (817, 276), (830, 272), (841, 268), (851, 263), (861, 260), (871, 258), (882, 255),
        (893, 253), (903, 251), (916, 250), (932, 249), (944, 247), (957, 246), (971, 242), (985, 242), (1003, 240),
        (1015, 239)]

PATH3 = [(128, 509), (127, 519), (134, 529), (139, 536), (150, 539), (161, 537), (173, 535), (185, 530), (195, 526),
        (205, 523), (216, 520), (227, 515), (238, 514), (248, 511), (259, 507), (270, 502), (280, 496), (289, 490), (301, 486),
        (310, 481), (320, 475), (334, 469), (343, 464), (353, 458), (362, 452), (374, 449), (384, 442), (393, 436), (396, 425),
        (392, 415), (387, 404), (381, 391), (372, 378), (378, 371), (387, 364), (399, 357), (410, 352), (422, 348), (435, 345),
        (446, 342), (452, 332), (459, 321), (469, 312), (480, 304), (489, 299), (500, 297), (512, 294), (522, 292), (537, 292),
        (550, 294), (564, 297), (578, 299), (591, 305), (601, 310), (611, 315), (621, 321), (632, 330), (646, 334), (657, 340),
        (669, 346), (685, 353), (694, 357), (705, 360), (719, 361), (734, 361), (746, 359), (756, 353), (770, 342), (777, 329),
        (772, 317), (764, 306), (751, 297), (737, 287), (722, 280), (709, 266), (707, 250), (703, 235), (710, 222), (722, 214),
        (735, 209), (744, 204), (755, 199), (765, 193), (773, 190), (784, 185), (796, 180), (808, 175), (820, 170), (833, 166),
        (844, 161), (858, 157), (867, 155), (881, 152), (894, 152), (901, 160), (908, 170)]

PATH4 = [(116, 321), (123, 326), (130, 330), (137, 334), (146, 338), (154, 339), (164, 340), (174, 340), (184, 339), (195, 338),
        (204, 334), (213, 330), (224, 324), (235, 318), (240, 309), (242, 298), (241, 287), (241, 274), (244, 265), (253, 260), (262, 256),
        (271, 252), (283, 247), (293, 244), (304, 241), (315, 237), (324, 235), (335, 234), (345, 234), (357, 233), (368, 231), (376, 231),
        (389, 228), (397, 225), (406, 222), (415, 219), (423, 216), (430, 213), (439, 210), (447, 207), (455, 204), (463, 200), (471, 196),
        (480, 193), (489, 192), (498, 192), (509, 191), (515, 191), (522, 195), (530, 198), (539, 203), (545, 207), (552, 211), (558, 216),
        (562, 223), (567, 227), (572, 234), (576, 240), (581, 245), (588, 251), (596, 255), (602, 259), (608, 264), (614, 271), (614, 276),
        (611, 281), (610, 286), (606, 290), (601, 294), (592, 301), (586, 306), (578, 311), (565, 317), (556, 322), (548, 327), (536, 332),
        (526, 333), (515, 335), (505, 334), (494, 337), (487, 344), (481, 349), (478, 359), (478, 366), (481, 373), (486, 382), (492, 390),
        (497, 398), (505, 404), (512, 410), (519, 416), (524, 422), (530, 428), (537, 435), (543, 441), (552, 446), (556, 450), (562, 458),
        (570, 468), (579, 475), (585, 482), (596, 483), (606, 477), (614, 474), (623, 472), (633, 470), (642, 468), (650, 462), (661, 456),
        (671, 452), (683, 446), (693, 441), (702, 438), (712, 436), (724, 431), (732, 430), (745, 428), (757, 426), (769, 425), (783, 421),
        (795, 417), (806, 412), (815, 408), (823, 405), (833, 401), (844, 396), (853, 390), (861, 382), (867, 374), (869, 361), (873, 349),
        (878, 343), (885, 334), (890, 324), (897, 318), (905, 310), (912, 303), (918, 298), (925, 289), (933, 283), (941, 279), (950, 278),
        (962, 274), (973, 273), (985, 269), (998, 267), (1006, 265), (1015, 265)]

PATH5 = [(136, 448), (148, 448), (163, 449), (177, 449), (191, 449), (202, 449), (218, 449), (232, 447), (242, 445),
        (255, 443), (267, 441), (279, 441), (294, 440), (307, 440), (321, 438), (332, 437), (347, 436), (363, 435), (378, 432),
        (394, 429), (406, 427), (417, 425), (427, 421), (440, 413), (452, 408), (462, 402), (474, 395), (483, 386), (471, 380),
        (461, 372), (453, 360), (452, 346), (457, 337), (463, 332), (470, 326), (479, 320), (491, 312), (500, 306), (509, 302),
        (520, 296), (531, 292), (545, 289), (557, 288), (574, 288), (585, 288), (596, 289), (611, 290), (620, 291), (631, 291),
        (644, 291), (655, 292), (660, 283), (661, 270), (667, 260), (677, 256), (689, 252), (700, 252), (714, 250), (727, 249),
        (740, 249), (755, 249), (769, 250), (783, 250), (799, 250), (811, 251), (825, 251), (838, 250), (851, 250), (862, 250),
        (873, 249), (885, 245), (896, 241), (912, 238), (925, 237)]

PATH_DICT:dict={
    1:{
        1:PATH1_1,
        2:PATH1_2
    },
    2:{
        1:PATH2_1,
        2:PATH2_2
    },
    3:{
        1:PATH3
    },
    4:{
        1:PATH4
    },
    5:{
        1:PATH5
    }
}
# base
BASE = pygame.Rect(485, 115, 160,170)
BASE2=pygame.Rect(850, 100, 160,170)
BASE3 = pygame.Rect(855, 5, 160, 170)
BASE4 = pygame.Rect(890, 106, 160, 170)
BASE5 = pygame.Rect(770, 95, 160, 170)
BASE_RECT_DICT:dict={
    1:BASE,
    2:BASE2,
    3:BASE3,
    4:BASE4,
    5:BASE5
}


class VolController:
    music_volume = 0.2
    sound_volume = 0.2

    @classmethod
    def minusVol(cls,voice:pygame.mixer.Sound or pygame.mixer.music,vol:float):
        res=voice.get_volume()-vol
        if(0.0<=res<=1.0):
            voice.set_volume(res)
        elif 0.0>res:
            voice.set_volume(0.0)
        else:
            voice.set_volume(1.0)
        
        if isinstance(voice,pygame.mixer.Sound):
            cls.sound_volume=voice.get_volume()
        else:
            cls.music_volume=voice.get_volume()

    @classmethod
    def addVol(cls,voice:pygame.mixer.Sound or pygame.mixer.music,vol:float):
        res=voice.get_volume()+vol
        if(0.0<=res<=1.0):
            voice.set_volume(res)
        elif 0.0>res:
            voice.set_volume(0.0)
        else:
            voice.set_volume(1.0)
        
        if isinstance(voice,pygame.mixer.Sound):
            cls.sound_volume=voice.get_volume()
        else:
            cls.music_volume=voice.get_volume()
    
class MapController:
    __max_map_index=5
    def __init__(self,WIN_WIDTH:int, WIN_HEIGHT:int):
        self.__WIN_WIDTH=WIN_WIDTH
        self.__WIN_HEIGHT=WIN_HEIGHT

        self.__map_index=1
        with open('map.txt', 'r') as f:
            self.__map_index=int(f.read())
        self.__map_index=self.__map_index if 1<=self.__map_index<=self.__max_map_index else 1
        
        self.__curMap= pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(self.__map_index)+".png")),(self.__WIN_WIDTH,self.__WIN_HEIGHT))

        self.__curPathPage=PATH_DICT[self.__map_index]

        self.__curBaseRect=BASE_RECT_DICT[self.__map_index]

    def change_map(self):
        with open('map.txt', 'w') as f:
            f.write(str(self.__map_index))
        self.__curMap= pygame.transform.scale(pygame.image.load(os.path.join("images", "Map"+str(self.__map_index)+".png")),(self.__WIN_WIDTH,self.__WIN_HEIGHT))
        self.__curPathPage=PATH_DICT[self.__map_index]
        self.__curBaseRect=BASE_RECT_DICT[self.__map_index]
    @property
    def map_index(self)->int:
        return self.__map_index
    
    @map_index.setter
    def map_index(self, value:int):
        self.__map_index=value if 1<=value<=self.__max_map_index else self.__map_index
        # self.curMap= pygame.image.load(os.path.join("images", "Map"+self.__map_index+".png"))

    @property
    def curMap(self)->pygame.Surface:
        return self.__curMap
    
    @property
    def curBaseRect(self)->pygame.Rect:
        return self.__curBaseRect
    
    @property
    def curPathPage(self)->dict:
        return self.__curPathPage