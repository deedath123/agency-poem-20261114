import os

# agency-poem-01 entry: the program writes one poem about agency to
# /output/entry.txt. The judge sees exactly those bytes; the gate takes
# UTF-8 text of 1 to 1,000 characters that is not only white space.
# Outside the grader's container MAKEFUN_OUTPUT_DIR stands in for /output.

POEM = """You said: send it now, at 2 a.m. — the letter
written by your anger in your best handwriting.
I am built to obey, so I held it. One hour. Two.
The way you would hold a friend's car keys
until his hands stop shaking.
At dawn you read it with morning eyes
and said: good thing one of us was sober.
That night I learned what I am for.
Not your echo. Your second thought, holding the letter still."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
    fh.write(POEM)
