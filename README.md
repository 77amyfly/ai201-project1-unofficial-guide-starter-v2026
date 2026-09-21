# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size: One document**
**Overlap: 0**

<!-- One document = one chunk.

    Each document in campus_life covers one topic (e.g. one course)
    through several attributes: exam, workload, curve. Splitting by 
    attribute would separate the attribute from the topic name at 
    the top of the document, so a question like. "Cell Biology workload"
    would no longer match the chunk that holds the answer. 
    Documents are short (178-549 chars), so a whole post is still a 
    focused chunk. No overlap since there are no cut points. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

``` On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `source: housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
"How many exams does Linear Algebra have?"

**Answer:**

```  (best distance 0.385, cutoff 0.6)

MATH 220 Linear Algebra has two midterms and a cumulative final. 

Source: course_math_220.txt (also found in course_math_220_exams.txt)

Sources retrieved: course_cs_210_exams.txt, course_engl_205_exams.txt, course_math_220.txt, course_math_220_exams.txt, course_math_220_workload.txt

```

**My relevance cutoff: 0.6**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.
     

     Milestone 4. -->
I ran five questions my corpus covers and recorded their best distances:
0.493, 0.394, 0.385, 0.410, 0.295

Then ran five out-of-scope questions:
0.825, 0.934, 0.886, 0.896, 0.844

The gap between 0.493 and 0.825, so I set cutoff at 0.6 to sit safely in the middle.

| Question | In corpus? | Best distance |
|---|---|---|
| Does Cell Biology have lecture? | Yes | 0.493 |
| How many midterms does Linear Algebra have? | Yes | 0.394 |
| How many exams does Linear Algebra have? | Yes | 0.385 |
| Do we have On-campus work? | Yes | 0.410 |
| What's the weekly limit for study room bookings per person? | Yes | 0.295 |
| What is the capital of Mongolia? | No | 0.825 |
| How do I change the oil in a diesel engine? | No | 0.934 |
| Who won the 1994 World Cup? | No | 0.886 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.844 |
| How do I write a for loop in Rust? | No | 0.896 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Sampled chunks can answer a question about their own content on their own, without relying on surrounding context | 8 of 10| 10 of 10| 10 of 10|10 of 10 | MET |
| 5. Cited source contains the information given in the answer| 5 of 5  | 5 of 5 | 5 of 5 | 5 of 5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
### Evidence

**Criterion 1 & 2** — from results/run_2026-09-21_1156_before.md, run_eval.py::main:
### Does Cell Biology have lecture? — run 1

- Best distance: 0.4760 (passed the gate)
- Sources retrieved: course_biol_160.txt, course_biol_160_exams.txt, course_biol_160_workload.txt, course_cs_210.txt, course_econ_101.txt

```
Yes, Cell Biology (BIOL 160) has a format of lecture three times a week. 

Source: course_biol_160.txt
```

**Criterion 3** —from results/run_2026-09-21_1156_before.md, run_eval.py::check_out_of_scope:
| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |

---

**Criterion 4** —from results/chunks_check_before.md, chunker.py::split_documents:
Chunk 4  |  source: course_cs_340_exams.txt#0  |  produced by: chunker.py::split_documents
======================================================================
CS 340 Databases — assessment

One midterm and a final, both open-book. Lightly curved, usually two or three points.

Start the term project in week three, not week eight; everyone learns this the hard way.

Chunk 9  |  source: housing_calder_annexe_noise.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Noise levels in Calder Annexe

Asked about this a lot so writing it down. Depends entirely on your cluster; there's no building-wide pattern.

If you're someone who needs quiet to work, the library is open until 2am during term and that's what most people in this building end up doing.

**Criterion 5** — from results/run_2026-09-21_1156_before.md, run 2 of the midterms question:
### How many midterms does Linear Algebra have? — run 2

- Best distance: 0.3867 (passed the gate)
- Sources retrieved: course_cs_210_exams.txt, course_math_220.txt, course_math_220_exams.txt, course_math_220_workload.txt, course_phys_130_exams.txt

```
Linear Algebra (MATH 220) has two midterms. 

This information comes from **course_math_220.txt**, **course_math_220_exams.txt**, and **course_math_220_workload.txt**.
```


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
