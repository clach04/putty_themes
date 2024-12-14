# Putty Themes

Also see https://github.com/clach04/terminal_style_toolkit



## Overview

  * themes - Putty themes in Microsoft Windows Registry format - colors ONLY
  * raw_themes - raw (various) format themes, probably not present in themes
  * images - preview PNG images/pictures/screenshots of themes

## Putty Settings

As of 2024, by default under "Connections", "Data" PuTTY defaults "Terminal-type string" to "xterm" but also defaults to enabling 256 color mode.
However many Linux systems will then treat $TERM=xterm as an 8 color display (not 16, not 256, and defintely not 24-bit true color).
Either:
1. change terminal declaration in putty, e.g. "xterm-256color" (other possiblities are "putty" and "putty-256color") and assume Linux/Unix system will understand
2. change your login scripts, for example; .bashrc, $HOME/.bash_profile, etc. to detect putty in another way. By default putty answer back under settings "Terminal" is set to PuTTY

Getting this wrong can severly impact vim and vim colorschemes. For example https://github.com/noahfrederick/vim-noctu (as of 2024-09-22) does not check t_Co and assumes 16 colors available, vim will deny access to any of the bright colors (colors 8-15) and default to foreground color.

A dirty hack for vim ~/.vimrc is:

    "if &term == "xterm"
    if &term =~ "xterm"
        set t_Co=256
        "set t_Co=16
        " etc. confirm setting with;    echo &t_Co
    endif

terminfo database (tools infocmp and tic)

    $ infocmp -1L xterm | grep max_colors
            max_colors#8,
    $ infocmp -1L xterm-256color | grep max_colors
            max_colors#0x100,
    $ infocmp -1L putty | grep max_colors
            max_colors#8,
    $ infocmp -1L putty-256color | grep max_colors
            max_colors#0x100,
    $ infocmp -1L $TERM | grep max_colors
            max_colors#0x100,
    $ infocmp -1L | grep max_colors
            max_colors#0x100,



### Font

For newish servers, color as bold default in Putty is reasonable.
For older Unix servers that only support black and white with bold (and maybe italic), need to decide if keep color as bold or may want to enable bold text in font for those older environments.

Do not use the default font Putty picks! Consolas as shipped with Windows for a long time (see https://github.com/vim/vim/issues/12919 comments) is reasonable but there are better (free) fonts available that could be installed.

### Behavior

Window, Selection, Copy - worth enabling "Copy to clipboard in RTF as well as plain text"


## Themes


### Default Putty and Variations

#### DefaultPuttySettings-dark

Out of box default colors for Putty from 2024-01, unchanged for at least 10 years.
Putty defaults are dark.

See fixed blue variants.

#### Default_fixed_blue-dark

Default Putty colors but with fixed blue shade for readability. See https://web.archive.org/web/20191231204120/http://dag.wiee.rs/blog/content/improving-putty-settings-on-windows by Dag Wieers.

#### Default_fixed_blue-dark_inverted

Same as fixed blue but inverted color scheme to make a lighter (a dark, light ;-p) color scheme.

### AdwaitaTango

#### mySettingsAdwaitaTango

Tweaked Adwaita Tango colors.

### Farmhouse

Based on https://github.com/mattly/iterm-colors-farmhouse

Which is in turn based on https://github.com/emacsorphanage/farmhouse-themes

See raw_themes/farmhouse_colors.txt

Also see https://github.com/mattly/colors-farmhouse which has both emacs and iterm2 files.

#### farmhouse-dark
#### farmhouse-light

## Also See

  * https://lospec.com/palette-list/
  * http://mkweb.bcgsc.ca/color/
      * http://mkweb.bcgsc.ca/colorsummarizer/ - perl (Windows exe available) and online
      * http://mkweb.bcgsc.ca/colornames/ - color name database/lists
