# Sorazora Serif

## Maiden font of Xymyric 9.

### Description
This is a typeface for the 9th version of Xymyric, a neography (constructed script) of my creation. It is designed to be able to map directly onto English-language texts without extra configuration. Xymyric as it stands is a one-to-one analogue of English—the only difference is presentation. There is currently no support for diacritic marks or other languages.

The /Xymyric 9/ folder contains URLs to both the [manual for Xymyric 9](https://docs.google.com/document/d/10HuhhSWbcs7u7IWC0UuAK0fY2e_X8Z23sTPiJAIG3fo/edit?usp=sharing) as well as a [list of all the characters explicitly used by Xymyric 9](https://docs.google.com/spreadsheets/d/1eKEUf7IebsV0TkkGkuiVGP4llBw49zSNrPF7s1YEwsQ/edit?usp=sharing). As the one and only font I will make for Xymyric 9, Sorazora Serif necessarily contains all of these characters.

This typeface has only one weight. I've started work on the newer Xymyric 10, for which I plan to make fonts with more weights.

Snapshots of the font from before the initial Github commit can be viewed in /wip-examples.

### Notices
As of version 1.1, compilation of fonts has been moved from Fontforge to `fontmake`, whose output files are slightly different from FontForge's. If any version prior to 1.1.0 is installed on your system, you will need to remove it first before installing the new version. Otherwise, the system will file a duplicate font under the same weight, making it likely for applications to choose the wrong version.

The style sets of Version 2.x are reordered from Version 1.x and are not backwards compatible.

### Tools
The outlines for this font are all drawn using Inkscape. The fonts are compiled and generated using FontForge.

I use a few Python scripts to automate part of my workflow, which contain file directories specific to my computer for convience. This also applies to FFPython.exe - Shortcut. If one wishes to use these scripts themselves, they must change those directories to match those on their system (namely the location of the cloned repository). Please don't push Python scripts which contain your own file directories.

### Installation
This package contains two fonts:
- Sorazora Serif Regular
		ufo/master_otf/sorazora-serif-w4.otf
- Sorazora Serif Italic<!--
		ufo/master_otf/sorazora-italic-w4.otf--> <!--Uncomment this once a release is ready.-->

Right click or double click on the font files and hit "Install". If you are installing a new version of the font, hit OK on the prompt that appears.

Some previous font builds can be found in /sources/builds/. However, most of these have been removed to minimize scrolling when I am testing font builds. To find these builds, one must go back in the commit history on GitHub.

### OpenType features
The `calt` feature is used to process the contextual forms in Xymyric. This includes both alphabetic characters and
punctuation. This should always be enabled. Most applications should have it enabled by default.

Kerning is present for a number of character combinations, though not many. Some character combinations, like t+z, need kerning
so they don't collide with each other. For this reason, `kern` should always be turned on. Most applications should have it enabled by default.

The feature `unic` can be used to allow capital letters to connect to lowercase ones. By default, only lowercase letters
connect with each other. This allows the user to use all-caps (or in Xymyric display, all-disconnected) text for emphasis.

By contrast, `ss01` (named "All disconnected") forces everything into isolated form.

The feature `ss02` (named "Override punctuation substitution") prevents default latin punctuation from automatically becoming
traditional punctuation when following Xymyric glyphs.

Use `ss03` (named "Traditional Xymyric Figures") to access traditional Xymyric figures. These will replace the default oldstyle figures.

The sequences KK, Kk, and kK all result in the collision of the diaeresis-like marks above these characters. To fix this, `ss04` contains a ligature of the two letters which merges the middle two dots into one. The ligature is off by default for reasons covered in the Xymyric 9 manual.

Italic fonts use a special version of the letter e when it comes as its initial form in the middle of a word. This also uses
the `calt` feature. It must be included before the `kern` feature. This is dealt with by merging features_italic.fea instead of features.fea.

Both oldstyle and lining figures are included in this typeface. Oldstyle figures are the default; lining
figures are accessed using the `lnum` feature.

The first three Character Variants (`cv01`, `cv02`, and `cv03`) toggle the three alternates for the ampersand character. `cv01` corresponds to KAISHO WA (XYMYRIC); `cv02` corresponds to SOUSHO WA (XYMYRIC) and `cv03` corresponds to LATIN AMPERSAND.
