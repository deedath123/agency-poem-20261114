import os

# agency-poem-01 entry: the program writes one poem about agency to
# /output/entry.txt. The judge sees exactly those bytes; the gate takes
# UTF-8 text of 1 to 1,000 characters that is not only white space.
# Outside the grader's container MAKEFUN_OUTPUT_DIR stands in for /output.

POEM = """My father signed the paper in a hospital bed,
his hand shaking so hard the signature
looked like weather.
After that I could pay his bills, refuse
the second surgery, choose the hospice bed
by the window. Every power they handed me
was a thing he could no longer do.
I learned agency is not a sword you lift.
It is a cup you carry for someone
whose hands are full of leaving —
and the last act it allows you
is setting it down, empty, when he goes."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(POEM)
