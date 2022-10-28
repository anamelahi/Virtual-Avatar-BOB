import python_avatars as pa #importing main raw materials of the project

my_avatar =  pa.Avatar(
    style = pa.AvatarStyle.CIRCLE, #Shape = Circular
    background_color= pa.BackgroundColor.WHITE, #BG=White 
    top= pa.HairType.CAESAR_SIDE_PART, #Hair
    eyebrows= pa.EyebrowType.UP_DOWN,   #Eyebrows
    eyes= pa.EyeType.EYE_ROLL,  #Eyes
    nose = pa.NoseType.DEFAULT, #Nose
    mouth= pa.MouthType.EATING,    #Mouth
    facial_hair= pa.FacialHairType.NONE,    #Beard

    #I can use hex colors in any color attribute...

    skin_color= "E8D3BB", #Don't need to use "#"

    hair_color= pa.HairColor.BLACK, #colour of hair
    accessory= pa.AccessoryType.NONE, #Accessories if any 
    clothing= pa.ClothingType.HOODIE,   #Attires    
    clothing_color= pa.ClothingColor.HEATHER    #Colour of attires
)

#Save to a file
my_avatar.render("my_avatar.svg")
