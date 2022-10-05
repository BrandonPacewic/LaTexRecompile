# Copyright (c) Brandon Pacewic
# SPDX-License-Identifier: MIT

import os
import sys
import time

COMPILE_COMMAND = "pdflatex -interaction=nonstopmode"


class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'


def main() -> None:
    if len(sys.argv) != 2:
        print(f"{Colors.RED}Usage: python3 {sys.argv[0]} <filename>{Colors.ENDC}")
        sys.exit(1)
    
    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"{Colors.RED}File '{filename}' does not exist.{Colors.ENDC}")
        sys.exit(1)
    
    print(f"{Colors.YELLOW}Recompiling '{filename}'...{Colors.ENDC}")

    last_waiting_message = 0

    while True:
        last_modified = os.path.getmtime(filename)
        try:
            last_compiled = os.path.getmtime(f"{filename.split('.tex')[0]}.pdf")
        except FileNotFoundError:
            last_compiled = 0

        if last_modified > last_compiled:
            os.system(f"{COMPILE_COMMAND} {filename}")
            print(f"{Colors.GREEN}Recompiled '{filename}' successfully.{Colors.ENDC}")

        time.sleep(0.7)

        if time.time() - last_waiting_message > 5:
            print(f"{Colors.YELLOW}Waiting for changes to '{filename}'...{Colors.ENDC}")
            last_waiting_message = time.time()


if __name__ == "__main__":
    main()
