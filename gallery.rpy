#persistant variables 
default persistent.unlock_0 = False
default persistent.unlock_1 = False
default persistent.unlock_2= False
default persistent.unlock_3 = False

init python:
    #gallery button info
    ### 0[title] ,  1[unlock params] ,  2[x-cord in frame], 3[y-cord in frame]
    ### 4[zoom] ,   5[images],          6[unlock params]

    gallery_list=[
        ["title"  , ["persistent.unlock_0"] ,500,0,
        1.5, ["image.png"], persistent.unlock_0],
        
        ["title"  , ["persistent.unlock_1"] ,500,0,
        1.5, ["image.png"], persistent.unlock_1],
        
        ["title"  , ["persistent.unlock_2"] ,500,0,
        1.5, ["image.png"], persistent.unlock_2],
        
        ["title"  , ["persistent.unlock_3"] ,500,0,
        1.5, ["image.png"], persistent.unlock_3]

]

screen galleryPage(a,b):
    frame:
        background None
        xalign .5 yalign .15
        grid (b-a) 1:
            xspacing 50 yspacing 50
            for i in range(a,b):
                $complete = createButton(gallery_list[i],gallery_list[i][2],gallery_list[i][3],gallery_list[i][4])
                add complete
            
screen gallery():
    tag menu
        xalign .5 yalign 1.15
        use galleryPage(0,4)


    
