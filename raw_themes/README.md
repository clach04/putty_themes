Themes in various formats that have not been converted into a Putty theme.

To generate:

    cd ..\themes
    py -3 FULL_PATH\terminal_style_toolkit\putty\batch_build.py ..\raw_themes FULL_PATH\terminal_style_toolkit\putty\putty_reg.mustache .reg

AKA the TODO list ;-)

Tango-Palette.gpl from https://web.archive.org/web/20230329090429/http://tango.freedesktop.org/static/cvs/tango-art-tools/palettes/Tango-Palette.gpl

  * http://tango.freedesktop.org/Tango_Icon_Theme_Guidelines
  * http://tango.freedesktop.org/static/cvs/tango-art-tools/palettes/Tango-Palette.gpl
  * http://tango.freedesktop.org/static/cvs/tango-art-tools/palettes/Tango-Palette.svg


tango_putty.json created by converting script from https://winterdom.com/2009/05/03/configuring-putty-with-tango
and now converted into `themes/Tango_Putty-dark.reg`.

https://github.com/piousdeer/vscode-adwaita

https://www.google.com/search?q=putty+adwaita+tango&oq=putty+adwaita+tango&aqs=chrome..69i57j33i160.4529j0j7&sourceid=chrome&ie=UTF-8

https://www.pierov.org/tag/adwaita/

## Check out

### Catppuccin

looks like 2024 new theme update expected to handle ansi 16 colors properly.

https://github.com/catppuccin/catppuccin/issues/1961#issuecomment-2229047020

### Nord theme

See (untested) ericvw_nord.json - for use with json2putty_reg.py from https://github.com/clach04/terminal_style_toolkit

https://www.nordtheme.com/docs/colors-and-palettes
  * https://github.com/ItzSwirlz/nord-lapce
  * https://github.com/nordtheme/putty - been broken for over a year as of 2024-08-31 16:46  https://github.com/nordtheme/putty/pull/11
  * https://github.com/mbadolato/iTerm2-Color-Schemes?tab=readme-ov-file#nord
      * https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/putty/nord.reg
      * https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/putty/nord-light.reg
  * https://github.com/nordtheme/iterm2/pull/16

From Synchronize RGB Hex values from official Nord palette https://github.com/nordtheme/iterm2/pull/16

which fixes RGB Hex values don't match Nord palette values https://github.com/nordtheme/iterm2/issues/15

    Align the ANSI and other iTerm2 colors to the Nord color palette.

    The following values have changed in the iTerm2 Settings > Profiles >
    Colors panel, noting changes in colors:

    Basic Colors
    ------------
    - Foreground    (nord4): #d8dde8 -> #d8dee9
    - Background    (nord0): #2e333f -> #2e3440
    - Bold          (nord6): #eceef3 -> #eceff4
    - Links         (nord5): #e5e8ef -> #e5e9f0
    - Selection     (nord2): #4c5569 -> #434c5e
                             (nord3) -> (nord2)
    - Selected text (nord4): #d8dde8 -> #d8dee9
    - Tab color     (nord1): #3b4151 -> #3b4252

    Cursor Colors
    -------------
    - Cursor       (nord4): #d8dde8 -> #d8dee9
    - Cursor text  (nord1): #3b4151 -> #3b4252
    - Cursor guide (nord2): #3b4151 -> #434c5e
                            (nord1)    (nord2)

    ANSI Colors
    -----------
    - Normal Black     (nord1): #3b4151  -> #3b4252
    - Bright Black     (nord3): #4c5569  -> #4c566a
    - Normal Red      (nord11): #be6069  -> #bf616a
    - Bright Red      (nord11): #be6069  -> #bf616a
    - Normal Green    (nord14): #a3bd8b  -> #a3be8c
    - Bright Green:   (nord14): #a3bd8b  -> #a3be8c
    - Normal Yellow:  (nord13): #ebca8a  -> #ebcb8b
    - Bright Yellow:  (nord12): #ebca8a  -> #d08770
                                (nord13)    (nord12)
    - Normal Blue:     (nord9): #81a0c0  -> #81a1c1
    - Bright Blue:    (nord10): #81a0c0  -> #5e81ac
                                (nord9)     (nord10)
    - Normal Magenta: (nord15): #b48dac  -> #b48ead
    - Bright Magenta: (nord15): #b48dac  -> #b48ead
    - Normal Cyan:     (nord8): #88bfcf  -> #88c0d0
    - Bright Cyan:     (nord7): #8fbbba  -> #8fbcbb
    - Normal White:    (nord5): #e5e8ef  -> #e5e9f0
    - Bright White:    (nord6): #eceef3  -> #eceff4

    The text selection and cursor guide uses nord2 now to align with
    "currently active text editor line as well as selection."

    Bright Blue uses nord10, the next accent level, for tertiary UI
    elements. Using nord12 may be a stretch for Bright Yellow. With both
    these changes, all of Frost and Aurora are available.

### Selenized (Solarized)

  * https://github.com/jan-warchol/selenized
      * https://github.com/clach04/selenized/branches/
      * https://codeberg.org/dnkl/foot/src/branch/master/themes/selenized-dark

  * https://swijaya.com/solarized-selenized-cheatsheet - comparing Solarized & Selenized
      * https://swijaya.com/jekyll/solarized
  * https://www.zovirl.com/2011/07/22/solarized_cheat_sheet/
  * https://github.com/bhdicaire/solarized
  * https://ericnormand.me/article/solarized-cheat-sheet


### Tango

  * https://github.com/mbadolato/iTerm2-Color-Schemes#iterm2-tango-dark
  * https://github.com/mbadolato/iTerm2-Color-Schemes#iterm2-tango-light
  * https://github.com/mbadolato/iTerm2-Color-Schemes#tango-adapted
  * https://github.com/mbadolato/iTerm2-Color-Schemes#tango-half-adapted

From https://github.com/mbadolato/iTerm2-Color-Schemes

> [_iTerm2 Tango Dark_](#iterm2-tango-dark), and [_iTerm2 Tango Light_](#iterm2-tango-light)
> are ports from the built-in color schemes of iTerm2 (current source is iTerm2 v3.4.19).


### Misc / Random

  * https://github.com/Matsuuu/pinkmare
