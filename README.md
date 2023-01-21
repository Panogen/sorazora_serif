# Sorazora Serif

## Maiden font of Xymyric 9.

### Description
This is a typeface for the 9th version of Xymyric, a neography (constructed script) of my creation. It is designed to map directly onto English text without extra configuration. Xymyric as it stands is a one-two-one analogue of English—the only difference is presentation. There is currently no support for diacritic marks or other languages.

The \/Xymyric 9/ folder contains URLs to both the manual for Xymyric \9 as well as a list of all the characters explicitly used by Xymyric \9. As the one and only font I will make for Xymyric 9, Sorazora Serif necessarily contains all of these characters.

This typeface has only one weight. This is because I've already started work on Xymyric 10, which will have more weights. I don't want to waste time making more weights for this font, and have elected to only complete the regular weight.

### Tools
The outlines for this font are all drawn using Inkscape. The fonts are compiled and generated using FontForge.

I use a few Python scripts to automate part of my workflow, which contain file directories specific to my computer for convience. This also applies to FFPython.exe - Shortcut. If one wishes to use these scripts themselves, they must change those directories to match those on their system (namely the location of the cloned repository). Please don't push Python scripts which contain your own file directories.

### Installation
This package contains two fonts:
- Sorazora Serif Regular<!--
		sorazora-serif-w4.otf-->
- Sorazora Serif Italic<!--
		sorazora-serif-italic-w4.otf-->

Right click or double click on the font files and hit "Install". If you are installing a new version of the font, hit OK on the prompt that appears.

Some previous font builds can be found in \/sources/builds/. However, most of these have been removed to minimize scrolling when I am testing font builds. To find these builds, one must go back in the commit history on GitHub.

All font builds with a version number less than 1.0.0 are considered 'alpha' or 'beta' and don't contain all of the features.

### OpenType features
The `calt` feature is used to process the contextual forms in Xymyric. This includes both alphabetic characters and
punctuation. This should always be enabled. Most applications should have it enabled by default.

Kerning is present for a number of character combinations, though not many. Some character combinations, like f+z, need kerning
so they don't collide with each other. For this reason, `kern` should always be turned on. Most applications should have it enabled by default.

The feature `unic` can be used to allow capital letters to connect to lowercase ones. By default, only lowercase letters
connect with each other. This allows the user to use all-caps (or in Xymyric display, all-disconnected) text for emphasis.

By contrast, `ss01` (named "All disconnected") forces everything into isolated form.

The feature `ss02` (named "Override punctuation substitution") prevents default latin punctuation from automatically becoming
traditional punctuation when following Xymyric glyphs.

Italic fonts use a special version of the letter e when it comes as its initial form in the middle of a word. This also uses
the `calt` feature.

Both oldstyle and lining figures are included in this typeface. Oldstyle figures are the default; lining
figures may be accessed using the `lnum` feature.
I won't dive into much detail on Xymyric here because all of that is contained with the Xymyric 9 specification, the URL to which
is found in the \/Xymyric 9/ folder.
