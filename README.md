

# Inactivity Task :Auto Bing Search Bot

This project automates Bing searches to earn Microsoft Rewards points. It checks for user inactivity and performs searches during idle time. The bot uses the `pyautogui` library for GUI automation and `keyboard` library for detecting key presses.
Medium Post : 

## Prerequisites

- Python 3.x
- `pyautogui`
- `keyboard`
- `schedule`
- `open_edge`

Install the required libraries using pip:

```bash
pip install pyautogui keyboard schedule
```

## Usage

1. **Clone the Repository**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Prepare the `words_list` Module**

    Ensure you have a `words_list.py` file with a list of words to be used for searching. For example:

    ```python
    words = ["example", "word", "list", "search", "terms"]
    ```

3. **Run the Script**

    Execute the script:

    ```bash
    python auto_bing_search.py
    ```

## Features

- **Inactivity Detection**: The script detects user inactivity. If the system is idle for 5 seconds, it starts the automated search task.
- **Automated Searches**: Performs Bing searches using a list of predefined words.
- **Safety Exit**: Press the `Esc` key to stop the bot during inactivity.  // 
Currently not working
## Files

- `auto_bing_search.py`: Main script for running the Bing search bot.
- `words_list.py`: List of words for the search terms.
- `open_edge.py`: Module for opening and closing Microsoft Edge browser (must be implemented).

## Code Explanation

### Main Components

- **Inactivity Checker**: Checks for system inactivity using the `GetLastInputInfo` Windows API.
- **Task Function**: Automates Bing searches by simulating key presses and mouse clicks.
- **Exit Handler**: Listens for the `Esc` key press to safely terminate the bot.

### Functions

- `get_idle_duration()`: Returns the idle duration in seconds.
- `check_inactivity()`: Checks if the system is inactive for 5 seconds.
- `check_esc_press()`: Listens for the `Esc` key to terminate the bot.
- `task()`: Performs automated Bing searches during inactivity.
- `inactiviity_checker()`: Scheduler that runs the inactivity check.

### Threads

- `inactivity_thread`: Runs the inactivity checker.
- `task_thread`: Runs the automated search task.

## Example

To see the bot in action, run the script and leave the system idle for 5 seconds. The bot will start performing searches automatically. Press `Esc` to stop the bot.


Feel free to modify the `README.md` file according to your needs and add any additional information relevant to your project.
