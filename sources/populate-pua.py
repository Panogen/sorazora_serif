import fontforge
# !! Must be run through FFPython.exe. Using the inbuilt Python interpreter will crash FontForge.


def create_char(font, uni, glyph_name):
    # Because the placeholder is copied over to all the new glyphs,
    # it must be present in the FF file PRIOR to running this script.
    font.selection.select("placeholder")
    font.copy()
    font.selection.select(font.createChar(uni, glyph_name))
    font.paste()


current_font = fontforge.open("C:\\Users\\anpanpano\\Documents\\Lettering, Calligraphy, Type, etc\\type projects"
                              "\\Xymyric\\Xymyric 9\\Sorazora Serif\\sorazora_serif\\sources\\w4_regular.sfd")
unusedValues = (
    0xe001, 0xe01b, 0xe01C, 0xe027,
    0xe028, 0xe02d, 0xe02e, 0xe030,
    0xe031, 0xe03c, 0xe03d, 0xe03f,
    0xe040, 0xe042, 0xe043, 0xe04b,
    0xe04c, 0xe08a, 0xe08b, 0xe08c,
    0xe08d, -1  # -1 added to prevent out-of-bounds error
)
unusedValueInd = 0
rangeA = (0xe000, 0xe050)   # Ranges do not include the second number.
rangeB = (0xe080, 0xe09e)
rangeC = (0xe110, 0xe114)
rangeD = (0xe150, 0xe15d)


print('Add Section A ("Connected Forms")')
unicode = rangeA[0]
letter_unicode = 0x0061
positions = (".init", ".medi", ".fina")
while unicode < rangeA[1] - 2:
    position = 0
    while position < 3:
        if unicode != unusedValues[unusedValueInd]:
            create_char(current_font, unicode, chr(letter_unicode) + positions[position])
        else:
            unusedValueInd += 1
        position += 1
        unicode += 0x1
    letter_unicode += 0x1

create_char(current_font, 0xe04f, "xy_kashida")
create_char(current_font, 0xe051, "x.long")
create_char(current_font, 0xe052, "z.long")


print('Add Sections B ("Traditional CJK-style punctuation") and C ("Historical Alternates")')
unicode = rangeB[0]
names = (
    "xy_fullstop", "xy_comma", "xy_commacn", "xy_exclamdown",
    "xy_questiondown", "xy_colon", "xy_semicolon", "xy_period",
    "xy_ellipsis", "xy_apos", "xy_apos.isol", "xy_apos.init",
    "xy_apos.medi", "xy_apos.fina", "xy_kome", "xy_lentleft",
    "xy_lentright", "xy_lentwhiteleft", "xy_lentwhiteright",
    "xy_kagileft", "xy_kagiright", "xy_kagiwhiteleft",
    "xy_kagiwhiteright", "xy_kikkoleft", "xy_kikkoright",
    "xy_kikkowhiteleft", "xy_kikkowhiteright", "xy_yamaleft",
    "xy_yamaright","xy_yamadblleft", "xy_yamadblright", "xy_wakai",
    "xy_wasou", "ampersand.lat"
)
for name in names:
    # print(unusedValues[unusedValueInd])
    # print(unicode)
    # print(name)
    # print()
    if unicode != unusedValues[unusedValueInd]:
        create_char(current_font, unicode, name)
    else:
        unusedValueInd += 1
    unicode += 0x1
    # Skip to Section C after reaching the end of Section B.
    if unicode == rangeB[1]:
        unicode = rangeC[0]


print('Add E Fishhook (italic fonts only)')
if current_font.italicangle != 0:
    create_char(current_font, unicode, "e.fishhook")
else:
    print("Italic angle was 0. Fishhook E not added.")
unicode += 0x1;


print('Add Xymyric historical numerals')
number_names = (
    'zero', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine'
)
for number_name in number_names:
    create_char(current_font, unicode, 'xy_' + number_name)
    unicode += 0x1;


print('Add Section D ("Xymyric Special")')
unicode = rangeD[0]
punctuation_names = (
    'period', 'comma', 'exclam', 'question', 'colon',
    'semicolon',' ellipsis', 'quoteleft', 'quotesingle',
    'quoteright', 'quotedblleft', 'quotedbl', 'quotedblright'
)
for punctuation_name in punctuation_names:
    create_char(current_font, unicode, punctuation_name + '.override')
    unicode += 0x1;


current_font.save()
current_font.close()

input("Finished, press enter to exit."); exit()
