# Sorazora Serif

## Maiden font of Xymyric 9.

### Description
This is a typeface for the 9th version of Xymyric, a neography (constructed script) of my creation. It is designed to be able to map directly onto English-language texts without extra configuration. Xymyric as it stands is a one-to-one analogue of English—the only difference is presentation. There is currently no support for diacritic marks or other languages.

The /Xymyric 9/ folder contains URLs to both the [manual for Xymyric 9](https://docs.google.com/document/d/10HuhhSWbcs7u7IWC0UuAK0fY2e_X8Z23sTPiJAIG3fo/edit?usp=sharing) as well as a [list of all the characters explicitly used by Xymyric 9](https://docs.google.com/spreadsheets/d/1eKEUf7IebsV0TkkGkuiVGP4llBw49zSNrPF7s1YEwsQ/edit?usp=sharing). As the one and only font I will make for Xymyric 9, Sorazora Serif necessarily contains all of these characters.

This typeface has only one weight—I've started work on the newer Xymyric 10, for which I plan to make fonts with more weights.

Snapshots of the font from before the initial Github commit can be viewed in /wip-examples.

### Installation
This package contains two fonts:
- Sorazora Serif Regular
	- ufo/master_otf/sorazora-serif-w4.otf
- Sorazora Serif Italic
	- ufo/master_otf/sorazora-italic-w4.otf

Right click or double click on the font files and hit "Install". If you are installing a new version of the font, hit OK on the prompt that appears.

### Notices
As of version 1.1 of Sorazora Serif Regular, font generation has been moved from Fontforge to `fontmake`, whose output files vary slightly from FontForge's. If any version prior to 1.1.0 is installed on your system, you will need to remove it first before installing the new version. Otherwise, the system will file a duplicate font under the same weight, making it likely for applications to choose the wrong version.

The style sets of Version 2.x and onward of Sorazora Serif Regular are reordered from Version 1.x and are not backwards compatible.

### Tools
The outlines for this font are drawn using Inkscape. The fonts are compiled using FontForge and generated using `fontmake`.

A few Python scripts and batch files automate parts of the workflow.

### OpenType features
|Feature tag|Feature name|Feature description|Usage|
|---|---|---|---|
|calt|Contextual alternates|Substitute default forms with contextual ones|Always required|
|kern|Kerning|Enable custom spacing of certain glyph pairs|Always required|
|unic|Unicase|Disable isolate forms|Discretionary|
|ss01|Stylistic set 01|Isolate forms only|Discretionary|
|ss02|Stylistic set 02|Force ideographic comma|Discretionary|
|ss03|Stylistic set 03|Force dot period|Discretionary|
|ss04|Stylistic set 04|Keep default punctuation|Discretionary|
|ss05|Stylistic set 05|Force all Xymyric punctuation|Discretionary|
|ss06|Stylistic set 06|Force traditional Xymyric figures|Discretionary|
|ss07|Stylistic set 07|Enable ligature of double isolate K|Discretionary|
|cv01|Character Variants 01|Use kaisho wa ampersand|Discretionary|
|cv02|Character Variants 02|Use sousho wa ampersand|Discretionary|
|cv03|Character Variants 03|Use latin ampersand|Discretionary|
