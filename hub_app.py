#!/usr/bin/env python3.13
"""Bryan's Hub — native Mac window, frameless with custom controls."""
import subprocess
import time
import urllib.request
import webview

HUB_URL = "http://localhost:8765"

def wait_for_server(timeout=30):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            urllib.request.urlopen(HUB_URL, timeout=1)
            return True
        except Exception:
            time.sleep(0.5)
    return False

class Api:
    def close(self):
        import os, signal
        os.kill(os.getpid(), signal.SIGTERM)

    def minimize(self):
        window.minimize()

    def maximize(self):
        window.toggle_fullscreen()

    def open_external(self, url):
        if url.startswith("ms-outlook://"):
            subprocess.Popen(["open", "-a", "Microsoft Outlook"])
        else:
            subprocess.Popen(["open", url])

wait_for_server()

api = Api()

window = webview.create_window(
    "Bryan's Hub",
    HUB_URL,
    width=1280,
    height=820,
    resizable=True,
    frameless=True,
    easy_drag=True,
    js_api=api,
)

webview.start()
