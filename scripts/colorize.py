import sys, re

class UnixConsoleStyler:

    STYLE = {
        "default"    :     "\033[m",
        # styles
        "bold"       :     "\033[1m",
        "underline"  :     "\033[4m",
        "blink"      :     "\033[5m",
        "reverse"    :     "\033[7m",
        "concealed"  :     "\033[8m",
        # font colors
        "black"      :     "\033[30m", 
        "red"        :     "\033[31m",
        "green"      :     "\033[32m",
        "yellow"     :     "\033[33m",
        "blue"       :     "\033[34m",
        "magenta"    :     "\033[35m",
        "cyan"       :     "\033[36m",
        "white"      :     "\033[37m",
        # background colors
        "on_black"   :     "\033[40m", 
        "on_red"     :     "\033[41m",
        "on_green"   :     "\033[42m",
        "on_yellow"  :     "\033[43m",
        "on_blue"    :     "\033[44m",
        "on_magenta" :     "\033[45m",
        "on_cyan"    :     "\033[46m",
        "on_white"   :     "\033[47m" 

    }

    @staticmethod
    def apply_style(style):
        try:
            sys.stdout.write(UnixConsoleStyler.STYLE[style])
        except KeyError:
                raise StyleNotFoundException, "Style '%s' not found" % (style)

class StyleNotFoundException(Exception):
    pass
       
if __name__ == "__main__":
    UnixConsoleStyler.apply_style('magenta')
    UnixConsoleStyler.apply_style('on_black')
    print('Hello colorizer!')
    UnixConsoleStyler.apply_style('default')
