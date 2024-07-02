import subprocess
import time
import pygetwindow as gw


def open_edge_browser():
    # Path to Microsoft Edge
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    # Open Microsoft Edge
    subprocess.Popen([edge_path])

    # Give some time for the Edge window to open
    time.sleep(5)

    # Print all available window titles for debugging
    window_titles = gw.getAllTitles()
    ##print("Available window titles:", window_titles)

    # Find the Edge window by title (adjust if necessary)
    edge_window_titles = [title for title in window_titles if 'Edge' in title]
    ##print("Edge window titles:", edge_window_titles)
    time.sleep(1)

    if edge_window_titles:
        edge_window = gw.getWindowsWithTitle(edge_window_titles[0])[0]
        # Maximize the window
        edge_window.maximize()
    else:
        print("No Edge window found.")


def close_edge_browser():
    # Get all window titles
    window_titles = gw.getAllTitles()
   ##s print("Available window titles:", window_titles)

    # Find the Edge window by title (adjust if necessary)
    edge_window_titles = [title for title in window_titles if 'Edge' in title]
    ##print("Edge window titles:", edge_window_titles)

    if edge_window_titles:
        edge_window = gw.getWindowsWithTitle(edge_window_titles[0])[0]
        # Close the window
        edge_window.close()
    else:
        print("No Edge window found.")

# open_edge_browser()