#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 16:12:05 2021

@author: student
"""
import pygame
import random
from pygame.locals import *


pygame.init()

(width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Clash_of_Brothers')

font_main = pygame.font.SysFont('Constantia', 30)

class Screen():
    
    def __init__(self, image_link):
        self.img = pygame.image.load(image_link).convert()
        self.img = pygame.transform.scale(self.img, (width, height))
        
        self.sprite_img = pygame.sprite.Sprite()
        self.sprite_img.image = self.img
        self.sprite_img.rect = self.img.get_rect
    
    def add_scenario(self, rect, punto, text, loc, font_color = (139, 0, 0)):
        font = pygame.font.SysFont('Constantia', punto)
        pygame.draw.rect(self.img, (211, 211, 211), rect)
        blit_text(self.sprite_img.image, text, loc, font, font_color)

clicked = False 

class Button():
    
    button_col = (0, 0, 0)
    hover_col = (70, 70, 70)
    click_col = (35, 35, 35)
    text_col = (34, 139, 234)
    
    def __init__(self, posx, posy, w, h, img, punto, text):
        self.x = posx
        self.y = posy
        self.width = w
        self.height = h
        self.screen = img
        self.font = pygame.font.SysFont('Constantia', punto)
        self.text = text
    
    def draw_button(self):
        
        global clicked
        action = False
        
        pos = pygame.mouse.get_pos()
        button_rect = Rect(self.x, self.y, self.width, self.height)
        
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(self.screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(self.screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(self.screen, self.button_col, button_rect)
            
        pygame.draw.line(self.screen, (0, 0, 139), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(self.screen, (0, 0, 139), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(self.screen, (0, 0, 139), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(self.screen, (0, 0, 139), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        
        text_img = self.font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        self.screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 12))
        return action

class Text_Box():
    
    text_color = (34, 139, 234)
    
    def __init__(self, posx, posy, w, h, img, font, text = ''):
        self.x = posx
        self.y = posy
        self.width = w
        self.height = h
        self.rect = Rect(posx, posy, w, h)
        self.screen = img
        self.font = font
        self.text = text
        self.text_surface = self.font.render(text, True, self.text_color)
        self.active = False
        
    def handle_event(self, event):
        text_rectangle = Rect(self.x, self.y, self.width, self.height)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_rectangle.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    final_text = self.text
                    self.text = ''
                    return final_text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.text_surface = self.font.render(self.text, True, self.text_color)
    
    def draw_text_box(self):
        text_box_rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, (0, 0, 0), text_box_rect)
        
        pygame.draw.line(self.screen, (0, 0, 139), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(self.screen, (0, 0, 139), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(self.screen, (0, 0, 139), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(self.screen, (0, 0, 139), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        
        text_len = self.text_surface.get_width()
        self.screen.blit(self.text_surface, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 10))
        
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = width,height
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
        
upper_pos = (0, 300, 600, 50)
lower_pos = (0, 350, 600, 50)

#topkapi 1 (check)
topkapi1 = Screen(r'topkapı_palace.jpg')
topkapi1_text = "Welcome to Clash of Brothers!"
start = Button(50, 280, 150, 44, topkapi1.sprite_img.image, 30, "Start")
leave = Button(400, 280, 150, 44, topkapi1.sprite_img.image, 30,  "Leave") 
#-----------------------------------------------------------------------------------------------------------------------------------   

#topkapi 2 (check())
topkapi2 = Screen(r'topkapı_palace_2.jpg') 
topkapi2_text = "You are an heir of the Ottoman Empire! Please pick a name for your character."
topkapi2_box = Text_Box(50, 300, 500, 30, topkapi2.sprite_img.image, pygame.font.SysFont('Constantia', 25))
#-----------------------------------------------------------------------------------------------------------------------------------   

#karaman (check)
karaman = Screen(r'karaman.jpg')
continue_button = Button(225, 280, 120, 40, karaman.sprite_img.image, 30, "Continue")    
def gen_karaman_text(name):
    return  "Hello, Shahzade " +  name + ". You are ruling the province of Karaman which is close to the capital, Constantinople. " \
            "Your father has always wanted you to rule the empire after his death. The governor of Konya, your older brother, is " \
            "your political rival. He is jealous of you because of your close relationship with the emperor."    
#-----------------------------------------------------------------------------------------------------------------------------------   
       
#letter (check)
letter = Screen(r'letter.jpg')
letter_text = "Here is a letter from Constantinople my Shahzade! Our great emperor has passed away. We should take off " \
              "as soon as possible to arrive at the court before your brother. If your brother reaches to the capital before us, " \
              "he might take over the throne."            
letter_humane = Button(0, 300, 600, 50, letter.sprite_img.image, 22, "What a lamentable day! We can take off later. I am in mourning.")
letter_pragmatic = Button(0, 350, 600, 50, letter.sprite_img.image, 22,  "You are right, we should leave soon. I will be the emperor!")
#-----------------------------------------------------------------------------------------------------------------------------------   

#bursa and room (check)
bursa = Screen(r'bursa.jpg')
bursa_hum_text = "You are near the Bursa province which is very close the capital Constantinople. You learned that your brother's men " \
                 "had managed to delay the arrival of the letter that informed you of the emperor's death. Hence, your brother is the emperor now. " \
                 "He wants your head! What will you do now?"
bursa_humane = Button(0, 300, 600, 50, bursa.sprite_img.image, 22, "Let's retreat to my province, Karaman. Maybe, we can negotiate with him.")
bursa_pragmatic = Button(0, 350, 600, 50, bursa.sprite_img.image, 22,  "Attack Bursa and start a revolt!")


karaman_room = Screen(r'karaman_room.jpg')
kr_text = "Your brother has taken over the throne my Shahzade! He has ordered your execution! What should we do now?"
kr_humane = Button(0, 300, 300, 50, karaman_room.sprite_img.image, 19, "We should consider seeking help Egypt.")
kr_pragmatic = Button(300, 300, 300, 50, karaman_room.sprite_img.image, 22, "Lets form alliances in Italy.")
kr_braveheart = Button(0, 350, 600, 50, karaman_room.sprite_img.image, 22, "Prepare the army! We will fight")
#----------------------------------------------------------------------------------------------------------------------------------- 

#karaman_2 (check)

karaman_room2 = Screen(r'karaman_room.jpg')
kr2_text = "The new emperor, your brother, liked your retreat move. He called you to Constantinople and promised that he will " \
            "not order your execution."
            
kr2_humane = Button(0, 300, 600, 50, karaman_room2.sprite_img.image, 22, "He is my brother. I believe him. Pack up my stuff. We will go to Constantinople.")
kr2_pragmatic = Button(0, 350, 600, 50, karaman_room2.sprite_img.image, 22, "I don't believe him. He is a filthy liar. I will raise a strong army against him!")

karaman_room2_2 = Screen(r'karaman_room.jpg')
kr2_2_text = "Whom should we seek help from?"
kr2_2_humane = Button(0, 300, 600, 50, karaman_room2_2.sprite_img.image, 22, "Our Muslim brother in Egypt can help us.")
kr2_2_pragmatic = Button(0, 350, 600, 50, karaman_room2_2.sprite_img.image, 22, "Lets form alliances in Italy.")
#----------------------------------------------------------------------------------------------------------------------------------- 

#Constantinople_hum (check)

constantinople_hum = Screen(r'constantinople_hum.jpg')
constantinople_hum2 = Screen(r'constantinople_bad.jpg')
const_text_good = "Your brother has kept his promise and declared you as his second man. You lived a happy life." \
                  "Your brothership and loyalty towards each other will always be remembered in the history of the Ottoman Empire!"
const_text_bad = "You noticed that something is going wrong. Suddenly, 8 to 10 executioners entered your room. They will strangle you!"
const_hum_good = Button(0, 350, 600, 50, constantinople_hum.sprite_img.image, 22, "What a beautiful life I have! My brother and I will never betray each other.")
const_hum_bad =  Button(0, 350, 600, 50, constantinople_hum2.sprite_img.image, 22, "I will beat them with my bare hands!")
#-----------------------------------------------------------------------------------------------------------------------------------

#Strangle (check)
topkapi_escape = Screen(r'topkapi_escape.jpg')
topkapi_esc_text = "You are a strong warrior. You managed to beat all of the executioners and ran away from the palace. What will you do" \
                    "now my Shahzade?"
escape_hum = Button(0, 300, 600, 50, topkapi_escape.sprite_img.image, 22, "I will seek help from our Muslims brothers in Egypt")
escape_prag = Button(0, 350, 600, 50, topkapi_escape.sprite_img.image, 22, "I can secure support from European states. Let's go to Italy")

topkapi_early_dead = Screen(r'executioners.jpg')
topkapi_early_dead_text = "You have been brutally killed by your brother's executioners. You will always be remembered as a loyal and honorable " \
                          "shahzade. You have counted on your brother but he betrayed you. He will always be remembered as a " \
                          "cruel and wicked leader."

main_men = Button(0, 350, 600, 50, topkapi_early_dead.sprite_img.image, 22, "Return to main menu")
#-----------------------------------------------------------------------------------------------------------------------------------

#Attack Bursa (check)
bursa_fail = Screen(r'bursa_lost.jpg')
bursa_fail_text= "Our army is losing my Shahzade! The capital army is very strong. We should retreat, but where?  What should we do?"

bursa_egypt = Button(0, 300, 600, 50, bursa_fail.sprite_img.image, 22, "Let's go to Egypt. One day, we shall return to home!")
bursa_italy = Button(0, 350, 600, 50, bursa_fail.sprite_img.image, 22, "Let's seek help from the Pope. We can beat my brother with the help of the Pope.")

bursa_after_istanbul_text = "Which country should we seek help from my Shahzade?"
bursa_success = Screen(r'bursa_capture.jpg')
def bursa_success_text(name):
    return "You have defeated the emperor's army! People of Bursa are cheering and celebrating the victory of TRUE emperor! Hail emperor " + name + "!"
bursa_direct= Button(0, 300, 600, 50, bursa_success.sprite_img.image, 22, "Either Constantinople will conquer me or I will conquer Constantinople!")
bursa_direct2 = Button(0, 350, 600, 50, bursa_success.sprite_img.image, 22, "Time to attack Constantinople!")
#-----------------------------------------------------------------------------------------------------------------------------------

#Istanbul Siege One Army (check)
istanbul_siege_1 = Screen(r'istanbul_walls.jpg')
istanbul_siege_1_text = "It is very difficult to conquer Constantinople my Shahzade! There are huge walls, professional guards, and the capital, " \
                        "army. Are you sure you want to attack the city without any support from other nations?"
istanbul_siege1_support_egypt = Button(300, 300, 300,50, istanbul_siege_1.sprite_img.image, 22, "Let's go to Egypt to form an alliance.")
istanbul_siege1_support_italy = Button(0, 300, 300, 50, istanbul_siege_1.sprite_img.image, 22, "Let's seek support from Europe")
istanbul_siege1_direct = Button(0, 350,600, 50, istanbul_siege_1.sprite_img.image, 22, "I have defeated my brother once. I can defeat him again!")
#-----------------------------------------------------------------------------------------------------------------------------------

#Istanbul Siege Result (check)
istanbul_siege_loss_1 = Screen(r'istanbul_siege.jpg')
istanbul_win = Screen(r'istanbul_win.jpg')

istanbul_siege_loss_text1 = "Our army has been defeated my Shahzade! We should consider running away."
siege_loss_1_egypt = Button(0, 300, 600, 50, istanbul_siege_loss_1.sprite_img.image, 22, "Let's head to Egypt.")
siege_loss_1_italy = Button(0, 350, 600, 50, istanbul_siege_loss_1.sprite_img.image, 22, "Let's head to Italy.")


istanbul_siege_win = "With your mighty army you have managed to take over the throne my emperor! Will you forgive your brother?"
siege_win_brutal = Button(0, 300, 600, 50, istanbul_win.sprite_img.image, 22, "Send the executioners! He deserved it.")
siege_win_humane = Button(0, 350, 600, 50, istanbul_win.sprite_img.image, 22, "He is my brother. I won't be like him.")
#-----------------------------------------------------------------------------------------------------------------------------------

#Letter_runaway
letter_run_away = Screen(r'large_army.jpg')
letter_run_away_text= "Your brother has raised a very large army. He is coming at us! We can't win this battle. We should take off soon. " \
                      "Where should we go sir?"
#escape_hum
#escape_prag
#-----------------------------------------------------------------------------------------------------------------------------------
                      
#Karaman Room Braveheart (check)
braveheart_dead = Screen(r'braveheart_dead.jpg')
braveheart_dead_text = "We lost my shahzade. You are killed by an archer during the combat. You will always be remembered as a brave " \
                       "and benevolent historical figure. Your loyalty, charisma, and courage will never be forgotten." 
#main_men button
                       
braveheart_alive = Screen(r'sivas_province.jpg')
braveheart_alive_text = "You managed to escape from the siege my shahzade! We should go to Egypt as the emperor's army is very powerful in " \
                        "the West."
alive_hum = Button(0, 300, 600, 50, braveheart_alive.sprite_img.image, 22, "Will I be able to return to my home again?")
alive_prag = Button(0, 350, 600, 50, braveheart_alive.sprite_img.image, 22, "Let's head to Cairo and return with a more powerful army!")
#-----------------------------------------------------------------------------------------------------------------------------------

#Egypt road (check)
brigands = Screen(r'medieval_brigand.jpg')
brigand_text = "Oh no! Brigands cut off your escape. They want you to drop your weapon and give them money. Be careful my Shahzade. " \
               "They might be your brother's men. "

kill_brigands = Button(0, 300, 600, 50, brigands.sprite_img.image, 22, "We must fight them!")
pay_brigands = Button(0, 350, 600, 50, brigands.sprite_img.image, 22, "Pay them")
#-------------------------------------------------------------------------------------------------------------------------------

#Brigand Fight (check)
brigand_win = Screen(r'brigand_win.jpg')
brigand_win_text = "You beated them my Shahzade. You are a skilled warrior! Let's continue our journey to Egypt'"
#continue_button

brigand_lose = Screen(r'brigand_lose.jpg')
brigand_lose_text = "Your are killed by brigands. No news will be heard from you. No one knows where your corpse is. You will always known " \
                     "as a traitor who sought help from Mamluks (Egypt)" 
                  
#return to main menu
#-------------------------------------------------------------------------------------------------------------------------------

#Pay Brigand (check)
pay_brigand_win = Screen(r'brigand_win.jpg')
pay_brigand_win_text = "After taking all of your money, brigands allowed you to travel as you wish."
#continue_button

pay_brigand_lose = Screen(r'brigand_captive.jpg')
pay_brigand_lose_text = "Turns out that these men are your brother's spies. They handcuffed you and took you as a captive. They will deliver you over " \
                        "to your brother in Constantinople!"
escape = Button(0, 350, 600, 50, pay_brigand_lose.sprite_img.image, 22, "I will escape!")
#-------------------------------------------------------------------------------------------------------------------------------

#Escape Result (check)
executioner = Screen(r'executioners.jpg')
brigand_ending = "You could not escape. Executioners have been sent to your prison. You are dead and will always be remember as a traitor " \
                 "who sought help from Mamluks. (Egypt)"
escaped_text = "You have managed to escape and met Mamluk Sultan. He welcomes you with great hospitality. How will you convince him for a military alliance against " \
               "your brother."
#-------------------------------------------------------------------------------------------------------------------------------
                 
#Mamluks (check)
mamluks = Screen(r'mamluks.jpg')
mamluks_text = "You have met Mamluk Sultan! He welcomes you with great hospitality. How will you convince him for a military alliance against " \
               "your brother."
mamluk_traitor = Button(0, 300, 600, 50, mamluks.sprite_img.image, 22, "I might give you some province if you support me.")
mamluk_hum = Button(0, 350, 600, 50, mamluks.sprite_img.image, 22, "I will guarantee the friendship between the Mamluks and Ottomans if you help me.")
#-------------------------------------------------------------------------------------------------------------------------------

# (check)
mamluks_result = Screen(r'egypt.jpg')
#Mamluk Good
mamluk_gtraitor_text = "Your offer sounded very interesting to Mamluk Sultan. He will provide military support. Time to conquer Constantinople!"
mamluk_ghum_text = "Mamluk Sultan values the friendship between the Ottomans and Mamluks. He will provide military support. Prepare for the siege!"
#continue button

#Mamluk Bad
mamluk_prisoner = Screen(r'prisoner.jpg')
mamluk_bad_hum_text = "Delivering you over to your brother sounded like a more profitable business for the Mamluk Sultan. Executioners have been sent " \
                      "to you and you are dead."
                 
#main menu
#-------------------------------------------------------------------------------------------------------------------------------

#Way to Italy Direct and Pirates (check)
way_to_italy = Screen(r'way_to_italy.jpg')
way_to_italy_text = "The trade ship is ready to take off to Italy. You are hiding your identity from other people."
#continue_button

pirates = Screen(r'pirate.jpg')
pirate_text = "Uh oh! Pirates have taken all the ship crew as captives. We should escape! What will you do now my Shahzade?"
pay_pirates = Button(0, 300, 600, 50, pirates.sprite_img.image, 22, "I will reveal my identity and offer them treasure in return for leaving me.")
revolt = Button(0, 350, 600, 50, pirates.sprite_img.image, 22, "Start a revolt against pirates!")
#-------------------------------------------------------------------------------------------------------------------------------

#Pirate Success (check)
#if pay 
italy_coast = Screen(r'italy_coast.jpg')
italy_coast_text = "Pirates have decided to release you. The pope paid the pirates for your release. You arrived at Italy!"
pay_good_news = Button(0, 350, 600, 50, italy_coast.sprite_img.image, 22, "The Pope is the best host I can ever ask for.")
#if revolt
pirate_revolt_win = Screen(r'pirate_revolt_win.jpg')
pirate_revolt_win_text = "You are a true leader and warrior! You and the ship crew managed to beat pirates."
revolt_good_news = Button(0, 350,600, 50, pirate_revolt_win.sprite_img.image, 22, "Time to meet the Pope!")
#-------------------------------------------------------------------------------------------------------------------------------

#Pirate Failure (check)
#if pay
sold_to_brother = Screen(r'pirate_captive.jpg')
sold_to_brother_text = "Bad news! Pirates have decided to deliver you over your brother."
executioner2 = Screen(r'executioners.jpg')

#Executioner screen
sold_to_brother_dead = "You have been executed by your brother's men."
#Return to main menu

#if revolt
pirate_dead = Screen(r'pirate_dead.jpg')
pirate_dead_text = "You have been killed by pirates. No news will be heard of you ever again. Your corpse will be in the bottom of the sea."
#Return to main menu 
#-------------------------------------------------------------------------------------------------------------------------------

#Pope (check)
pope = Screen(r'Pope.jpg')
pope_text = "Pope: Welcome sir! We know that the Ottoman throne should be yours. We believe that such a mighty empire as the Ottomans should " \
            "serve Jesus and Lord. If you follow the path of Jesus, we can raise an army for you."
christian_button = Button(0, 350, 600, 50, pope.sprite_img.image, 22, "I will fight for Jesus and take over the Ottoman throne!")
muslim = Button(0, 300, 600, 50, pope.sprite_img.image, 22, "This is treason against my home country. I shall not accept this offer!")
old_man = Screen(r'old_man.jpg')
pope_text2 = "Pope refused to offer you an army. Nor did he allow you to travel as you wished. You died of old age in Italy"
#Return to main menu
#-------------------------------------------------------------------------------------------------------------------------------

#Pope Army (check)
christian_army = Screen(r'christian_army.jpg')
#if christian
christian_army_prag = "You are ruling the papal army as a Christian general. You are known as a traitor within the borders of the Ottoman empire. " \
                      "Time to take over the throne my lord!"
#if muslim
christian_army_hum = "The Pope admired your boldness and principled attitude. He decided to give you an army in return for a truce agreement" \
                     "between the Christian states and the Ottoman empire if you take the lead of the country."
#-------------------------------------------------------------------------------------------------------------------------------

#istanbul Siege Only One Army
siege_only_egypt = Screen(r'istanbul_siege_2.jpg')
siege_only_egypt_text = "We have support from the Egyptian army! However, Constantinople's defense is very powerful. What should we do " \
                        "my Shahzade?"
to_italy = Button(0, 350, 600, 50, siege_only_egypt.sprite_img.image, 22, "We should ask the Pope for help. Let's go to Rome.")
attack_one_army_egypt = Button(0, 300, 600, 50, siege_only_egypt.sprite_img.image, 22, "Our army is strong enough. Let's attack the city!")

siege_only_italy = Screen(r'istanbul_siege_2.jpg')
siege_only_italy_text = "The Pope is supporting us my Shahzade! However, Constantinople's defense is very powerful. What should we do?"
to_egypt = Button(0, 350, 600, 50, siege_only_italy.sprite_img.image, 22, "Let's seek help from Mamluks.")
attack_one_army_italy = Button(0, 300, 600, 50, siege_only_italy.sprite_img.image, 22, "Our army is strong enough. Let's attack the city!")
#-------------------------------------------------------------------------------------------------------------------------------

#Istanbul Siege Two Armies
two_army_siege = Screen(r'large_army.jpg')
two_army_siege_text = "We have a powerful army now! Let's attack my Shahzade."
two_army_siege_button = Button(0, 350, 600, 50, two_army_siege.sprite_img.image, 22, "Prepare for the siege!")
#-------------------------------------------------------------------------------------------------------------------------------

#if istanbul win brutal 
tyrant_king = Screen(r'tyrant_king.jpg')
tyrant_king_text_christ = "You are not only a traitor who have been converted to Christianity but also a ruthless leader who executed " \
                          "his brother. You will not be known as a virtuous leader."
tyrant_king_text = "You become a tyrant after the execution of your brother. You will always be known as a sibling slayer."
tyrant_king_button = Button(0 , 350, 600, 50, tyrant_king.sprite_img.image, 22, "I have no toleration for disobedience!")

#if Istanbul win 
good_king_christ = Screen(r'good_king.jpg')
good_king_christ_text = "You will always known as a sinful emperor who have received help from the Pope to take over the Ottoman throne. " \
                       "However, your affection towards your brother will always be remembered."
                   
good_king_screen = Screen(r'benevolent_king.jpg')
def good_king_gen(name):
    return "You become the emperor! Shall I call you emperor " + name + "? You affection towards your family will always be remembered. " \
           "You are not only a benevolent leader but also a true military commander who succesfully managed to take over the throne." 
good_king = Button(0, 350, 600, 50, good_king_screen.sprite_img.image, 22, "Wise leaders should rule their countries with benevolence!")
good_king_christian = Button(0, 350, 600, 50, good_king_christ.sprite_img.image, 22, "I am a benevolent leader at least.")
#-------------------------------------------------------------------------------------------------------------------------------

#if istanbul loss brutal 
final_loss_only_egypt = Screen(r'final_loss.jpg')
final_loss_egypt_text = "Our army has been destroyed. Mamluk's support was not enough. You have been captured during the siege and executed."

final_loss_only_italy = Screen(r'traitor.jpg')
final_loss_italy_text = "People of the Ottoman empire are happy about your execution. You are a traitor who has converted to Christianity " \
                        "to receive help from the Pope."

final_loss_only_italy_2 = Screen(r'medieval_execution.jpg')
final_loss_italy_text2 = "Our army has been destroyed. The Pope's support did not help us conquer Constantinople. You have been captured during " \
                         "the siege and exectued."

both_loss =  Screen(r'heroic_execution.jpg')
final_loss_both_army = "Your brother has won the historical battle. Even though you had support from two nations, the capital army fought really well. " \
                       "Your brother has ordered your execution."
#return to main menu
#-------------------------------------------------------------------------------------------------------------------------------


current_screen = "topkapi1"

while True:
    
    if current_screen == "topkapi1":
        army = 1
        dice = None
        egypt_army = False
        pope_army = False
        brother_kill = False
        christian = False
        bursa_direct_clicked = False
        escaped = False
        ambition_point = 0 
    
        screen.blit(topkapi1.img, (0,0))
        topkapi1.add_scenario(Rect(105, 40, 400, 30), 30, topkapi1_text, (160, 48))
        if start.draw_button():
            current_screen = "topkapi2"
   
    if current_screen == "topkapi2":
        screen.blit(topkapi2.img, (0,0))
        topkapi2.add_scenario(Rect(0, 40, 600, 50), 25, topkapi2_text, (60,48))        
           
    if current_screen == "karaman":
        screen.blit(karaman.img, (0,0))
        karaman_text = gen_karaman_text(char_name)
        karaman.add_scenario(Rect(0, 0, 600, 100), 25, karaman_text, (15, 10))
        if continue_button.draw_button():
            current_screen = "letter"
    
    if current_screen == "letter":
        screen.blit(letter.img, (0,0))
        letter.add_scenario(Rect(0, 0, 600, 90), 25, letter_text, (15, 10))
        if letter_humane.draw_button():
            current_screen = "karaman_room"
        if letter_pragmatic.draw_button():
            current_screen = "bursa"
            
    if current_screen == "karaman_room":
        screen.blit(karaman_room.img, (0,0))
        karaman_room.add_scenario(Rect(0, 0, 600, 70), 25, kr_text, (15, 10))
        if kr_humane.draw_button():
            current_screen = "brigand"
        if kr_pragmatic.draw_button():
            current_screen = "pre-pirate"
        if kr_braveheart.draw_button():
            
            if dice == None:
                dice = random.random()
            if dice <= 0.35:
                current_screen = "braveheart_dead"
            else:
                current_screen = "braveheart_alive"
            dice = None
    
    if current_screen == "braveheart_dead": 
        screen.blit(braveheart_dead.img, (0,0))
        braveheart_dead.add_scenario(Rect(0, 0, 600, 70), 25, braveheart_dead_text, (15, 10))
        mainmen2 = Button(0, 350, 600, 50, braveheart_dead.sprite_img.image, 22, "Return to main menu")
        if mainmen2.draw_button():
            current_screen = "topkapi1"
           
    if current_screen == "braveheart_alive":
        screen.blit(braveheart_alive.img, (0,0))
        braveheart_alive.add_scenario(Rect(0, 0, 600, 60), 25, braveheart_alive_text, (15, 10))
        if alive_hum.draw_button():
            current_screen = "brigand"
        if alive_prag.draw_button():
            ambition_point = 0.1
            current_screen = "brigand"
            
    if current_screen == "bursa":
        screen.blit(bursa.img, (0,0))
        bursa.add_scenario(Rect(0, 0, 600, 100), 25, bursa_hum_text, (15, 10))
        if bursa_humane.draw_button():
            current_screen = "karaman_room2"
        if bursa_pragmatic.draw_button():
            if dice == None:
                dice = random.random()
            if dice <= 0.5:
                current_screen = "bursa_success"
            else:
                army -= 1
                current_screen = "bursa_fail"
            dice = None
            
    if current_screen == "bursa_success":
        screen.blit(bursa_success.img, (0,0))
        bursa_text_success = bursa_success_text(char_name)
        bursa_success.add_scenario(Rect(0, 0, 600, 60), 25, bursa_text_success, (15, 10))
        if bursa_direct.draw_button():
            ambition_pont = 0.1
            current_screen = "istanbul_walls"
            bursa_direct_clicked = True
        if bursa_direct2.draw_button():
            current_screen = "istanbul_walls"
   
    if current_screen == "istanbul_walls":
        screen.blit(istanbul_siege_1.img, (0,0))
        istanbul_siege_1.add_scenario(Rect(0, 0, 600, 70), 25, istanbul_siege_1_text, (15,10))
        if istanbul_siege1_support_egypt.draw_button():
            current_screen = "brigand"
        if istanbul_siege1_support_italy.draw_button():
            current_screen = "pre-pirate"
        if istanbul_siege1_direct.draw_button():
            if dice == None:
                dice = random.random()
            if dice <= 0.05 + ambition_point:
                current_screen = "istanbul_win"
            else:
                army -= 1
                current_screen = "istanbul_loss_early"
            dice = None
    
    if current_screen == "istanbul_win":
        screen.blit(istanbul_win.img, (0,0))
        istanbul_win.add_scenario(Rect(0, 0, 600, 60), 25, istanbul_siege_win, (15, 10))
        if siege_win_brutal.draw_button():
            current_screen = "tyrant_king"
        if siege_win_humane.draw_button():
            current_screen = "good_king"
    
    if current_screen == "istanbul_loss_early":
        screen.blit(istanbul_siege_loss_1.img, (0,0))
        istanbul_siege_loss_1.add_scenario(Rect(0, 0, 600, 60), 25, istanbul_siege_loss_text1, (15, 10))
        if siege_loss_1_egypt.draw_button():
            current_screen = "brigand"
        if siege_loss_1_italy.draw_button():
            current_screen = "pre-pirate"
        
    if current_screen == "bursa_fail":
        screen.blit(bursa_fail.img, (0,0))
        bursa_fail.add_scenario(Rect(0, 0, 600, 60), 25, bursa_fail_text, (15, 10))
        if bursa_egypt.draw_button():
            current_screen = "brigand"
        if bursa_italy.draw_button():
            current_screen = "pre-pirate"
        
    if current_screen == "karaman_room2":
        screen.blit(karaman_room2.img, (0,0))
        karaman_room2.add_scenario(Rect(0, 0, 600, 60), 25, kr2_text, (15, 10))
        if kr2_humane.draw_button():
            army -= 1
            current_screen = "constantinople_early"
        if kr2_pragmatic.draw_button():
            current_screen = "karaman_room2_2"
    
    if current_screen == "karaman_room2_2":
        screen.blit(karaman_room2_2.img, (0,0))
        karaman_room2_2.add_scenario(Rect(0, 0, 600, 40), 25, kr2_2_text, (15, 10))
        if kr2_2_humane.draw_button():
            current_screen = "brigand"
        if kr2_2_pragmatic.draw_button():
            current_screen = "pre-pirate"
            
    if current_screen == "constantinople_early":
        if dice == None:
            dice = random.random()
        if dice <= 0.1:    
            screen.blit(constantinople_hum.img, (0,0))
            constantinople_hum.add_scenario(Rect(0, 0, 600, 80), 25, const_text_good, (15, 10))
            if const_hum_good.draw_button():
                current_screen = "topkapi1"
        
        else:
            screen.blit(constantinople_hum2.img, (0,0))
            constantinople_hum2.add_scenario(Rect(0, 0, 600, 60), 25, const_text_bad, (15, 10))
            if const_hum_bad.draw_button():
                dice = random.random()
                if dice <= 0.05:
                    current_screen = "topkapi_escape"
                else:
                    current_screen = "topkapi_early_death"
    
    if current_screen == "topkapi_escape":
        screen.blit(topkapi_escape.img, (0,0))
        topkapi_escape.add_scenario(Rect(0, 0, 600, 60), 25, topkapi_esc_text, (15, 10))
        if escape_hum.draw_button():
            current_screen = "brigand"
        if escape_prag.draw_button():
            current_screen = "pre-pirate"
    
    if current_screen == "topkapi_early_death":
        screen.blit(topkapi_early_dead.img, (0,0))
        topkapi_early_dead.add_scenario(Rect(0, 0, 600, 90), 25, topkapi_early_dead_text, (15, 10))
        if main_men.draw_button():
            current_screen = "topkapi1"
            
    if current_screen == "brigand":
        screen.blit(brigands.img, (0,0))
        brigands.add_scenario(Rect(0, 0, 600, 60), 25, brigand_text, (15, 10))
        if kill_brigands.draw_button():
            dice = random.random()
            if dice <= 0.4:
                current_screen = "brigand_win"
            else:
                current_screen = "brigand_lose"
        if pay_brigands.draw_button():
            dice = random.random()
            if dice <= 0.6:
                current_screen = "pay_brigand_win"
            else:
                current_screen = "pay_brigand_lose"
    
    if current_screen == "brigand_win":
        screen.blit(brigand_win.img, (0,0))
        brigand_win.add_scenario(Rect(0, 0, 600, 60), 25, brigand_win_text, (15, 10))
        continue2 = Button(0, 350, 600, 50, brigand_win.sprite_img.image, 22, "Continue") 
        if continue2.draw_button():
            current_screen = "egypt"
    
    if current_screen == "brigand_lose":
        screen.blit(brigand_lose.img, (0,0))
        brigand_lose.add_scenario(Rect(0, 0, 600, 80), 25, brigand_lose_text, (15, 10))
        mainmen3 = Button(0, 350, 600, 50, brigand_lose.sprite_img.image, 22, "Return to main menu")
        if mainmen3.draw_button():
            current_screen = "topkapi1"
          
            
    if current_screen == "pay_brigand_win":
        screen.blit(pay_brigand_win.img, (0,0))
        pay_brigand_win.add_scenario(Rect(0, 0, 600, 60), 25, pay_brigand_win_text, (15, 10))
        continue3 = Button(0, 350, 600, 50, pay_brigand_win.sprite_img.image, 30, "Continue") 
        if continue3.draw_button():
            current_screen = "egypt"
    
    if current_screen == "pay_brigand_lose":
        screen.blit(pay_brigand_lose.img, (0,0))
        pay_brigand_lose.add_scenario(Rect(0, 0, 600, 60), 25, pay_brigand_lose_text, (15, 10))
        if escape.draw_button():
            if dice == None:
                dice = random.random()
            if dice <= 0.3:
                escaped = True
                current_screen = "egypt"
            else:
                current_screen = "executed"
            dice = None
    
    if current_screen == "executed":
        screen.blit(executioner.img, (0,0))
        executioner.add_scenario(Rect(0, 0, 600, 80), 25, brigand_ending, (15, 10))
        mainmen4 = Button(0, 350, 600, 50, executioner.sprite_img.image, 22, "Return to main menu")
        if mainmen4.draw_button():
            current_screen = "topkapi1"
          
            
    if current_screen == "egypt":
        screen.blit(mamluks.img, (0,0))
        
        if not escaped:
            mamluks.add_scenario(Rect(0, 0, 600, 60), 25, mamluks_text, (15, 10))
        else:
            mamluks.add_scenario(Rect(0, 0, 600, 60), 25, escaped_text, (15, 10))
            
        if mamluk_traitor.draw_button():
            traitor = True
            if dice == None:
                dice = random.random()
            if dice <= 0.9:
                current_screen = "egypt_positive"
                army += 1
                egypt_army = True
            else:
                current_screen = "egypt_negative"
            dice = None
        if mamluk_hum.draw_button():
            traitor = False
            if dice == None:
                dice = random.random()
            if dice <= 0.2:
                current_screen = "egypt_positive"
                army += 1
                egypt_army = True
            else:
                current_screen = "egypt_negative"
            dice = None
    
    if current_screen == "egypt_positive":
        screen.blit(mamluks_result.img, (0,0))
        if traitor:
            mamluks_result.add_scenario(Rect(0, 0, 600, 60), 25, mamluk_gtraitor_text, (15, 10))
        else:
            mamluks_result.add_scenario((Rect(0, 0, 600, 60)), 25, mamluk_ghum_text, (15, 10))     
        continue4 = Button(0, 350, 600, 50, mamluks_result.sprite_img.image, 22, "Great news from Mamluks!")
        if continue4.draw_button():
            if not pope_army:
                current_screen = "istanbul_siege_one_army"
            else:
                current_screen = "istanbul_siege_two_army"

    if current_screen == "egypt_negative":
        screen.blit(mamluk_prisoner.img, (0,0))
        mamluk_prisoner.add_scenario(Rect(0, 0, 600, 70), 25, mamluk_bad_hum_text, (15, 10))
        mainmen5 = Button(0, 350, 600, 50, mamluk_prisoner.sprite_img.image, 22, "Return to main menu")
        if mainmen5.draw_button():
            current_screen = "topkapi1"
           
    if current_screen == "pre-pirate":
        screen.blit(way_to_italy.img, (0,0))
        way_to_italy.add_scenario(Rect(0, 0, 600, 60), 25, way_to_italy_text, (15, 10))
        continue5 = Button(0, 350, 600, 50, way_to_italy.sprite_img.image, 22, "I am so excited to meet the Pope!")
        if continue5.draw_button():
            current_screen = "pirates"
    
    if current_screen == "pirates":
        screen.blit(pirates.img, (0,0))
        pirates.add_scenario(Rect(0, 0, 600, 60), 25, pirate_text, (15, 10))
        if pay_pirates.draw_button():
            dice = random.random()
            if dice <= 0.5:
                current_screen = "pay_pirate_success"
            else:
                current_screen = "pay_pirate_fail"
        if revolt.draw_button():
            dice = random.random()
            if dice <= 0.5:
                current_screen = "pirate_revolt_success"
            else:
                current_screen = "pirate_revolt_fail"
    
    if current_screen == "pay_pirate_success":
        screen.blit(italy_coast.img, (0,0))
        italy_coast.add_scenario(Rect(0, 0, 600, 60), 25, italy_coast_text, (15, 10))
        if pay_good_news.draw_button():
            current_screen = "italy"
    
    if current_screen == "pay_pirate_fail":
        screen.blit(sold_to_brother.img, (0,0))
        sold_to_brother.add_scenario(Rect(0, 0, 600, 60), 25, sold_to_brother_text, (15, 10))
        continue6 = Button(0, 350, 600, 50, sold_to_brother.sprite_img.image, 22, "I don't want to die in a ship!")
        if continue6.draw_button():
            current_screen = "executioner2"
                
    if current_screen == "executioner2":
         screen.blit(executioner2.img, (0,0))
         executioner2.add_scenario(Rect(0, 0, 600, 60), 25, sold_to_brother_dead, (15, 10))
         mainmen6 = Button(0, 350, 600, 50, executioner2.sprite_img.image, 22, "What a tragic ending!")
         if mainmen6.draw_button():
             current_screen = "topkapi1"
    
    if current_screen == "pirate_revolt_success":
        screen.blit(pirate_revolt_win.img, (0,0))
        pirate_revolt_win.add_scenario(Rect(0, 0, 600, 60), 25, pirate_revolt_win_text, (15, 10))
        if revolt_good_news.draw_button():
            current_screen = "italy"
    
    if current_screen == "pirate_revolt_fail":
        screen.blit(pirate_dead.img, (0,0))
        pirate_dead.add_scenario(Rect(0, 0, 600, 60), 25, pirate_dead_text, (15, 10))
        mainmen7 = Button(0, 350, 600, 50, pirate_dead.sprite_img.image, 22, "Hope I will go to heaven at least!")
        if mainmen7.draw_button():
            current_screen = "topkapi1"
           
    if current_screen == "italy":
        screen.blit(pope.img, (0,0))
        pope.add_scenario(Rect(0, 0, 600, 80), 25, pope_text, (15, 10))
        if christian_button.draw_button():
           current_screen = "christian_army"
           christian = True
           pope_army = True
           army += 1
        if muslim.draw_button():
            dice = random.random()
            if dice <= 0.5:
                current_screen = "muslim_good"
                army += 1
                pope_army = True
            else:
                current_screen = "muslim_bad"
    
    if current_screen == "christian_army":
        screen.blit(christian_army.img, (0, 0))
        christian_army.add_scenario(Rect(0, 0, 600, 70), 25, christian_army_prag, (15, 10))
        continue7 = Button(0, 350, 600, 50, christian_army.sprite_img.image, 22, "I will be the next Ottoman emperor!")
        if continue7.draw_button():
            if egypt_army:
                current_screen = "istanbul_siege_two_army"
            else:
                current_screen = "istanbul_siege_one_army"
    
    if current_screen == "muslim_good":
        screen.blit(christian_army_hum.img, (0,0))
        christian_army_hum.add_scenario(Rect(0, 0, 600, 60), 25, christian_army_hum, (15, 10))
        continue8 = Button(0, 350, 600, 50, christian_army.sprite_img.image, 22, "I will conquer Constantinople!")
        if continue8.draw_button():
            if egypt_army:
                current_screen = "istanbul_siege_two_army"
            else:
                current_screen = "istanbul_siege_one_army"
    
    if current_screen == "muslim_bad":
        screen.blit(old_man.img, (0,0))
        old_man.add_scenario(Rect(0, 0, 600, 60), 25, pope_text2, (15, 10))
        mainmen8 = Button(0, 350, 600, 50, old_man.sprite_img.image, 22, "I lived a decent and honorable life at least.")
        if mainmen8.draw_button():
            current_screen = "topkapi1"
            
    
    if current_screen == "istanbul_siege_one_army":
        if egypt_army:
            screen.blit(siege_only_egypt.img, (0,0))
            siege_only_egypt.add_scenario(Rect(0, 0, 600, 60), 25, siege_only_egypt_text, (15, 10))
            if to_italy.draw_button():
                current_screen = "pre-pirate"
            if attack_one_army_egypt.draw_button():
                dice = random.random()
                if army == 2:
                    ambition_point = 0.1
                else:
                    ambition_point = 0
                if dice <= 0.35 + ambition_point:
                    current_screen = "istanbul_win"
                else:
                    current_screen = "istanbul_loss"
        if pope_army:
            screen.blit(siege_only_italy.img, (0,0))
            siege_only_italy.add_scenario(Rect(0, 0, 600, 60), 25, siege_only_italy_text, (15, 10))
            if to_egypt.draw_button():
                current_screen = "brigand"
            if attack_one_army_italy.draw_button():
                dice = random.random()
                if army == 2:
                    ambition_point = 0.1
                else:
                    ambition_point = 0
                if dice <= 0.35 + ambition_point:
                    current_screen = "istanbul_win"
                else:
                    current_screen = "istanbul_loss"
    
    if current_screen == "istanbul_siege_two_army":
        screen.blit(two_army_siege.img, (0,0))
        two_army_siege.add_scenario(Rect(0, 0, 600, 60), 25, two_army_siege_text, (15, 10))
        if two_army_siege_button.draw_button():
            print(army)
            if army == 3:
                dice = random.random()
                if dice <= 0.9:
                    current_screen = "istanbul_win"
                else:
                    current_screen = "istanbul_loss"
            if army == 2:
                dice = random.random()
                if dice <= 0.8:
                    current_screen = "istanbul_win"
                else:
                    current_screen = "istanbul_loss"
    
    if current_screen == "istanbul_loss":
        if egypt_army and pope_army:
            screen.blit(both_loss.img, (0,0))
            both_loss.add_scenario(Rect(0, 0, 600, 60), 25, final_loss_both_army, (15, 10))
            mainmenfinal = Button(0, 350, 600, 50, both_loss.sprite_img.image, 22, "I did my best to take over the thone.")
        elif egypt_army:
            screen.blit(final_loss_only_egypt.img, (0,0))
            final_loss_only_egypt.add_scenario(Rect(0, 0, 600, 60), 25, final_loss_egypt_text, (15, 10))
            mainmenfinal = Button(0, 350, 600, 50, final_loss_only_egypt.sprite_img.image, 22, "I didn't bend the knee at least.")
        else:
            if christian:
                screen.blit(final_loss_only_italy.img, (0,0))
                final_loss_only_italy.add_scenario(Rect(0, 0, 600, 60), 25, final_loss_italy_text, (15, 10))
                mainmenfinal = Button(0, 350, 600, 50, final_loss_only_italy.sprite_img.image, 22, "I will pray to Jesus and the Lord.")
            else:
                screen.blit(final_loss_only_italy_2.img, (0,0))
                final_loss_only_italy_2.add_scenario(Rect(0, 0, 600, 60), 25, final_loss_italy_text2, (15, 10))
                mainmenfinal = Button(0, 350, 600, 50, final_loss_only_italy_2.sprite_img.image, 22, "I will pray to Allah for the last time.")               
        if mainmenfinal.draw_button():
            current_screen = "topkapi1"
            
    if current_screen == "tyrant_king":
        screen.blit(tyrant_king.img, (0,0))
        if christian:
            tyrant_king.add_scenario(Rect(0, 0, 600, 70), 25, tyrant_king_text_christ, (15, 10))
        else:
             tyrant_king.add_scenario(Rect(0, 0, 600, 75), 25, tyrant_king_text, (15, 10))
        if tyrant_king_button.draw_button():
            current_screen = "topkapi1"
    
    if current_screen == "good_king":
        if christian:
            screen.blit(good_king_christ.img, (0, 0))
            good_king_christ.add_scenario(Rect(0, 0, 600, 70), 25, good_king_christ_text, (15, 10))
            if good_king_christian.draw_button():
                current_screen = "topkapi1"
        else:
            screen.blit(good_king_screen.img, (0, 0))
            good_king_text = good_king_gen(char_name)
            good_king_screen.add_scenario(Rect(0, 0, 600, 70), 25, good_king_text, (15, 10))
            if good_king.draw_button():
                current_screen = "topkapi1"
            
    if leave.draw_button():
        pygame.quit()
        quit()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()   
        if current_screen == "topkapi2":
            final_text = topkapi2_box.handle_event(event)
            topkapi2_box.draw_text_box()
            if final_text != None:
                current_screen = "karaman"
                char_name = final_text
                print(char_name)
    
    pygame.display.flip()
    pygame.display.update()