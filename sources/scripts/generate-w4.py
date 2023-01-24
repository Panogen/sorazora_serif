import fontforge
# After opening the FontForge project, this script does three things:
#   1. Merges features.fea
#   2. Generates the font as OpenType (CFF)
#   3. Increments the patch number (x.x.(x))
# It then closes FontForge without saving. The purpose of this is to allow changes to be made
# to the OpenType features without having to delete everything in FontForge.
#
# The PostScript version string must be in the format major.minor.patch, otherwise an exception
# will be thrown (the font will still export, but the version number will fail to increment).
#
# Incrementing the major or minor version should be done manually. This script is only for the
# patch number.
#
# Please close FontForge before running.

current_font = fontforge.open("C:/Users/anpanpano/Documents/Lettering, Calligraphy, Type, etc/type projects"
                              "/Xymyric/Xymyric 9/Sorazora Serif/sorazora_serif/sources/w4_regular.sfd")

current_font.mergeFeature("C:/Users/anpanpano/Documents/Lettering, Calligraphy, Type, etc/type projects"
                          "/Xymyric/Xymyric 9/Sorazora Serif/sorazora_serif/sources/feature/pyfeatures.fea")
current_font.generate(
    "C:/Users/anpanpano/Documents/Lettering, Calligraphy, Type, etc/type projects"
    "/Xymyric/Xymyric 9/Sorazora Serif/sorazora_serif/sources/builds/w4_v"
    + font.version
    + ".otf"
)
current_font.close()  # Don't save the imported features
current_font = fontforge.open("C:/Users/anpanpano/Documents/Lettering, Calligraphy, Type, etc/type projects"
                              "/Xymyric/Xymyric 9/Sorazora Serif/sorazora_serif/sources/w4_regular.sfd")
prev_version = current_font.version
split_around_dots = prev_version.split('.')
major_vers = split_around_dots[0]
minor_vers = split_around_dots[1]
patch = int(split_around_dots[2])
new_patch = patch + 1
new_vers = major_vers + '.' + minor_vers + '.' + str(new_patch)
current_font.version = new_vers

current_font.save()
current_font.close()

input("Finished, press enter to exit."); exit()