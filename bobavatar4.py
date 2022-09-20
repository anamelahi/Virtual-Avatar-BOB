import python_avatars as pa
from python_avatars import install_part
#from python_avatars import install_part

# Install the new part
#install_part("suit.svg", pa.ClothingType)

my_avatar =  pa.Avatar(
    style = pa.AvatarStyle.CIRCLE,
    background_color= pa.BackgroundColor.WHITE,
    top= pa.HairType.FRO_BAND,
    eyebrows= pa.EyebrowType.UP_DOWN_NATURAL,
    eyes= pa.EyeType.HAPPY,
    nose = pa.NoseType.DEFAULT,
    mouth= pa.MouthType.SMILE,
    facial_hair= pa.FacialHairType.MOUSTACHE_FANCY,




    #skin_color= "000000",

    hair_color= pa.HairColor.BLACK,
    accessory= pa.AccessoryType.WAYFARERS,
    clothing= pa.ClothingType.BLAZER_SWEATER,
    clothing_color= pa.ClothingColor.BLACK
)

my_avatar.render("bob_avatar4.svg")