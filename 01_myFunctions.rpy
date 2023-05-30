

init python:

    def createButton(picture,cord_x,cord_y,zoomp):
    #make the gallery
        g = Gallery()
        g.transition = dissolve
        g.locked_button ="gui/g_frame.png"
        
        g.button(picture[0])
        
        for i in range(len(picture[5])):
            g.image(picture[5][i])
            g.condition(picture[1][i])
            
        
        #picture = index of list containing images for the button
        # [title , unlock condition ,[picture1,picture2]]
        #cord = index of list containing x and y cordinates to show image

        img_mask = AlphaMask(im.Crop(im.FactorScale(picture[5][0],zoomp), (cord_x, cord_y, 312, 715)), "gui/g_framep.png")
        img_comp = Composite( (312, 715), (0, 0), "gui/g_frame.png", (0, 0), img_mask)
        img_button= g.make_button(picture[0], img_comp)

        return img_button


            
    def createcredButton(picture):

        img_mask = AlphaMask( im.Crop(picture , (300, 0, 312, 715)), "gui/g_framep.png")
        img_comp = Composite( (312, 715), (0, 0), "gui/g_frame.png", (0, 0), img_mask)

        return img_comp
    

    

    #///

init python:
    import pygame
    import math


    class TrackCursor(renpy.Displayable):

        def __init__(self, child, paramod, **kwargs):

            super(TrackCursor, self).__init__()

            self.child = renpy.displayable(child)
            self.x = 0
            self.y = 0
            self.actual_x = 0
            self.actual_y = 0

            self.paramod = paramod
            self.last_st = 0



        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)
            minimum_speed = 0.5
            maximum_speed = 3
            speed = 1 + minimum_speed
            mouse_distance_x = min(maximum_speed, max(minimum_speed, (self.x - self.actual_x)))
            mouse_distance_y = (self.y - self.actual_y)
            if self.x is not None:
                st_change = st - self.last_st

                self.last_st = st
                self.actual_x = math.floor(self.actual_x + ((self.x - self.actual_x) * speed * (st_change )) * self.paramod)
                self.actual_y = math.floor(self.actual_y + ((self.y - self.actual_y) * speed * (st_change)) * self.paramod)


                if mouse_distance_y <= minimum_speed:
                    mouse_distance_y = minimum_speed
                elif mouse_distance_y >= maximum_speed:
                    mouse_distance_y = maximum_speed

                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.actual_x, self.actual_y))



            renpy.redraw(self, 0)
            return rv

        def event(self, ev, x, y, st):
            hover = ev.type == pygame.MOUSEMOTION
            click = ev.type == pygame.MOUSEBUTTONDOWN
            mousefocus = pygame.mouse.get_focused()
            if hover:

                if (x != self.x) or (y != self.y) or click:
                    self.x = -x /self.paramod
                    self.y = -y /self.paramod