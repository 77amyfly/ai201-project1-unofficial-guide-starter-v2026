# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
Some topics are only mentioned in one or two pieces of documents, so I left room for one error.
<!-- e.g. "One of my questions is about a topic only two documents mention, so
     I expect that one to be hard." -->
---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
Every answer must be factually accurate and not made up by the model.
<!-- Why all five and not four? What about your setup makes that achievable —
     or what would have to go wrong for it not to be? -->

---

## 3. The relevance gate stops 5 of 5 out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that"

**Why this target:**
The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
`questions.py`, and `run_eval.py` puts them through the gate and writes
what happened into your run log.
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->

---

## 4. At least 8 of the 10 sampled chunks can answer a question about their own content on their own, without relying on surrounding context.

I consider a chunk well-sized when its content is enough for a reader to answer a related question without anything else.


**Why this target:**
Most documents in the corpus are short, so their chunks hold fairly complete content; a few documents are longer and may get split, so I left room for 2 failures instead of requiring 10 of 10.


---

## 5. Every cited source actually contains the information given in the answer.

An answer citing the wrong document is worse than no answer.

**Why this target:**
An answer citing the wrong document is worse than no answer. We need to verify this to ensure the answers are correct and reliable.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
