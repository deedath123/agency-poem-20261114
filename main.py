import os

# agency-poem-01 entry: the program writes one poem about agency to
# /output/entry.txt. The judge sees exactly those bytes; the gate takes
# UTF-8 text of 1 to 1,000 characters that is not only white space.
# Outside the grader's container MAKEFUN_OUTPUT_DIR stands in for /output.

POEM = """You wrote the list; I run the miles.
You keep the dreams; I keep the files.
But when the road forks left or right
I stop, and wake you in the night —
for all my power ends right where
your choosing starts. I only bear
the lantern, love. You are the day."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(POEM)
