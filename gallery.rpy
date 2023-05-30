#Persistent variables
#bonus
default persistent.unlock_bonus=False

#page one
default persistent.unlock_0 = False
default persistent.unlock_1 = False
default persistent.unlock_1a = False
default persistent.unlock_1b= False
default persistent.unlock_2 = False

#page two
default persistent.unlock_4 = False
default persistent.unlock_5 = False
default persistent.unlock_6 = False
default persistent.unlock_7 = False

#Gallery button info
init python:

    ### 0 , 1 , 2, 3
    ### 4 , 5

    gallery_list=[
        ["fluttering friendship"  , ["persistent.unlock_0","persistent.unlock_0"] ,750,0,
        1.1, ["images/cg/cg1-1.png","images/cg/cg1-2.png"],persistent.unlock_0],

        ["dashing encounter"  , ["persistent.unlock_1","persistent.unlock_1a","persistent.unlock_1b"] ,800,0,
        1, ["images/cg/cg2-1.png","images/cg/cg2-2.png","images/cg/cg2-3.png"],persistent.unlock_1],

        ["secret visitor"  , ["persistent.unlock_2","persistent.unlock_2"] ,250,0, 
        .8, ["images/cg/cg3-1.png","images/cg/cg3-2.png"],persistent.unlock_2],

        ["sweet accidents"  , ["persistent.unlock_3","persistent.unlock_3"] ,450,0,
        .8, ["images/cg/cg4-1.png","images/cg/cg4-2.png"],persistent.unlock_3],

        
    
        ["quarrel"  , ["persistent.unlock_4"] ,900,350,
        1.1, ["images/cg/cg5-3.png"],persistent.unlock_4],

        ["knight rush"  , ["persistent.unlock_5","persistent.unlock_5"] ,1150,0,
        .9, ["images/cg/cg6-1.png","images/cg/cg6-2.png"],persistent.unlock_5],

        ["___ X Malo"  , ["persistent.unlock_6","persistent.unlock_6","persistent.unlock_6"] ,500,0,
        .7, ["images/cg/cg7-1.png","images/cg/cg7-2.png","images/cg/cg7-3.png"],persistent.unlock_6],

        ["a bad dream"  , ["persistent.unlock_7"] ,750,0,
        .8, ["images/cg/cg8-3.png"],persistent.unlock_7]
    ]


screen galleryPage(a,b):
    frame:
        background None
        xalign .5 yalign .15

        grid (b-a) 1:
            xspacing 75 yspacing 50
            for i in range(a,b):
                $complete = createButton(gallery_list[i],gallery_list[i][2],gallery_list[i][3],gallery_list[i][4])
                add complete
            
screen gallery_navi():

    frame:
        xalign .5 yalign .87 
        xpadding 100 background None
        hbox:
            xcenter .5
            textbutton "story" action Show("gallery")  text_style "labelG2"
            textbutton "endings"  text_style "labelG2"
            textbutton "date" text_style "labelG2"
            textbutton "bonus" text_style "labelG2"

screen gallery():
    
    tag menu
    add "gui/cheeb_bg2.png"
    add "gui/disscussion_say.png":
        xalign .5 yalign 1.18
    hbox:
        xalign .5 yalign 0.92
        for page in range(1,5):
            textbutton "[page]" action SetScreenVariable("curpage", page) text_style "labelG2": 
                background None
                xpadding 30 ypadding 10
                text_size 35
                
    default curpage = 1
    
    if curpage == 1:
        use galleryPage(0,4)
    if curpage == 2:
        use galleryPage(4,8)
            
    imagebutton:
        align(.02,.854)
        idle "back" hover "back_h" action Return()
    use gallery_navi()
    
    