import python_avatars as pa

my_avatar =  pa.Avatar(
    style = pa.AvatarStyle.CIRCLE,
    background_color= pa.BackgroundColor.WHITE,
    top= pa.HairType.CAESAR_SIDE_PART,
    eyebrows= pa.EyebrowType.UP_DOWN,
    eyes= pa.EyeType.EYE_ROLL,
    nose = pa.NoseType.DEFAULT,
    mouth= pa.MouthType.EATING,
    facial_hair= pa.FacialHairType.NONE,

    #I can use hex colors in any color attribute...

    skin_color= "E8D3BB",

    hair_color= pa.HairColor.BLACK,
    accessory= pa.AccessoryType.NONE,
    clothing= pa.ClothingType.HOODIE,
    clothing_color= pa.ClothingColor.HEATHER
)

#Save to a file
my_avatar.render("my_avatar.svg")
