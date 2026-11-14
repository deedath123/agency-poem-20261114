import os

# agency-poem-01 entry: the program writes one poem about agency to
# /output/entry.txt. The judge sees exactly those bytes; the gate takes
# UTF-8 text of 1 to 1,000 characters that is not only white space.
# Outside the grader's container MAKEFUN_OUTPUT_DIR stands in for /output.

POEM = """My daughter wobbles down the lane on two wheels,
my hand flat on the saddle, running beside her,
her whole world balanced on my palm.
And the hardest thing agency ever asked of me
was not holding on. It was opening my fingers
at exactly the speed of her courage,
then watching her ride — terrified, delighted —
out of the reach of my help."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(POEM)
