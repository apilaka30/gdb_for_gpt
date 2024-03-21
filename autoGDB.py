import gdb
import sys

# if len(sys.argv) == 1:
#     print("invalid arguments: source autoGDB.py break")
#     exit()
breakpoints = [13]

REPORT_TAG = "[GPTREPORT]"

# Define a function to print variable values
def print_variable(var):
    try:
        value = gdb.parse_and_eval(var)
        print(f"{REPORT_TAG}{var} = {value}")
    except gdb.error:
        print(f"Error: Unable to evaluate {var}")

# Define a function to filter and log variable print statements
def log_prints(event):
    frame = gdb.selected_frame()
    block = frame.block()
    while block:
        for sym in block:
            if sym.is_argument:
                print_variable(sym.name)
        block = block.superblock

# Register the log_prints function as a hook for 'stop' events
gdb.events.stop.connect(log_prints)

for breakp in breakpoints:
    gdb.execute(f"break {breakp}", True, False)
open("gpt_log", "w").close()
gdb.execute("run", True, False)


# print_variable("n")

