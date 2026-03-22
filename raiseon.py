from gajim.plugins import GajimPlugin
from gajim.common import app, ged
import logging
import gi
import ctypes
from ctypes import wintypes
from gi.repository import Gtk, GLib

gi.require_version('Gtk', '4.0')

log = logging.getLogger("gajim.p.raiseon")
log.setLevel(logging.DEBUG)  # Ensure debug messages appear

# Win32 API
user32 = ctypes.WinDLL('user32', use_last_error=True)
IsWindowVisible = user32.IsWindowVisible
IsWindowVisible.argtypes = [wintypes.HWND]
IsWindowVisible.restype = wintypes.BOOL
IsIconic = user32.IsIconic
IsIconic.argtypes = [wintypes.HWND]
IsIconic.restype = wintypes.BOOL

class Raiseon(GajimPlugin):

    def init(self):
        self.events_handlers = {
            'message-received': (ged.PREGUI2, self._on_gc_message),
        }
        GLib.timeout_add(150, self._check_window_visible)

    def _on_gc_message(self, event):
        win = app.window
        if not win:
            return

        title = win.get_title()
        if not title.startswith('[NEW] '):
            win.set_title('[NEW] ' + title)


    def _check_window_visible(self):
        win = app.window
        if not win:
            return True

        gtk_win = win.get_native()
        if not gtk_win:
            return True

        gdk_surface = gtk_win.get_surface()
        if not gdk_surface:
            return True

        # Get the actual Win32 HWND handle
        try:
            hwnd = gdk_surface.get_handle()  # returns int
        except AttributeError:
            return True

        # Win32 visibility/minimized checks
        visible = IsWindowVisible(hwnd)
        minimized = IsIconic(hwnd)
        title = win.get_title()

        log.debug(f"Check: hwnd={hwnd} visible={visible} minimized={minimized} title='{title}'")

        if visible and not minimized and title.startswith('[NEW] '):
            win.set_title(title.replace('[NEW] ', '', 1))
            log.debug(f"Title cleared: {win.get_title()}")

        return True
