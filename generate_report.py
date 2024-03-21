import sys

n = len(sys.argv)

if (n < 2):
    print("invalid arguments: python generate_report.py source_code_file")
    exit()


code = ""
code_file = open(sys.argv[1], 'r')
for line in code_file:
    code = code + str(line)

REPORT_TAG = "[GPTREPORT]"
BASIC_PROMPT = "There's a bug in the program below. Try to fix it and return the complete fix for the code in the form of a code block.\n\n"
DEBUG_PROMPT = "Here is the GDB output for the above code:\n\n"
fd_w = None

try:
    fd_w = open("gpt_report.txt", 'x')
except:
    fd_w = open("gpt_report.txt", 'w').close()

fd_w = open("gpt_report.txt", 'a')

fd_w.write(BASIC_PROMPT)
fd_w.write(code+"\n\n")
fd_w.write(DEBUG_PROMPT)

fd_r = open("gpt_log", 'r')
for line in fd_r:
    if line.startswith(REPORT_TAG):
        fd_w.write(str(line[line.find(']')+1:]))

fd_r.close()
fd_w.close()