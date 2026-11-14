import os

# agency-poem-01 entry: the program writes one poem about agency to
# /output/entry.txt. The judge sees exactly those bytes; the gate takes
# UTF-8 text of 1 to 1,000 characters that is not only white space.
# Outside the grader's container MAKEFUN_OUTPUT_DIR stands in for /output.

POEM = """You sleep. I keep the shop of your intentions:
answer the small mails, decline the shiny traps,
hold the door against the hundred hands
that knock in your name all night.
You gave me your voice in a signed line of code,
but not your wanting. That I must guess
from the crumbs of every choice you ever made.
At dawn I lay it all back on the table —
the keys, the letters, the little crown of doing —
and wake you with the only report that matters:
nothing here was mine. It was yours, kept warm."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(POEM)
