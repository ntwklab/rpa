import rpa as r
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Change scaling to 100% (Retnia on Mac)
# Take Screenshots
r.init(visual_automation = True, chrome_browser = False)
r.hover('start.png')
r.click('start.png')
r.hover('sublime.png')
r.click('sublime.png')
r.wait(2.5)
r.keyboard('type something here[enter]')
r.wait(2.5)
r.dclick('sublime_text.png')
r.wait(1.5)
r.keyboard('changing the word "something" to this')
r.keyboard('[end][enter]')
r.keyboard('Adding a new line')
r.keyboard('[win]m')
r.close()
