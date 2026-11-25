# Leaderboard analysis — Last Out of Office: The AI That Went Barista

Fetched: 2026-11-25 ~11:15 WIB (round 1 cutoff 2026-11-25 22:14 WIB).
Raw files: `leaderboard.json` (GET /api/competitions/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?rows=all)
and `field-titles.json` (GET /api/competitions/<slug> — full competition detail incl. all 294 submission titles).

## Board facts (BLIND rounds — leaderboard-top10.md in the usual sense is IMPOSSIBLE)

- `rank_key`: **judge** (win rate, Bradley-Terry over pairwise games)
- `tie_break`: **bytes** (Size column, lower is better) — then earlier receipt
- `scores_visible`: false, `placements_held`: true — 3 blind rounds, nothing judged on submit
- `submission_rule`: Force_Last (a resubmit replaces the entry; blind-round rebuild rules apply)
- Field at fetch: **294 submissions** (190 at discovery 11:04 WIB — growing fast, ~100 in ~10 min)
- Prize: $2 total, top 8 paid (1st $0.64 … 8th $0.05). Free entry.
- **Final heat: top 500** on the dev board (latest judged round's standings); while the field
  stays under 500 rated entries, every valid entry goes on. Then 3 Swiss rounds + top-10 playoff.
- **Interim cut: 500 each round** (R1 plays the whole field; R2+ re-judge only entries inside the
  cut of the previous round; entries below the cut keep their score — FROZEN — and their rank
  can only fall as the field grows). Target: be INSIDE the top-500 cut at R1 (2026-11-25 22:14 WIB).
- Gate: `/output/entry.txt` must be UTF-8, 1–280 chars, non-whitespace. Only valid entries
  reach the judge. No local grade exists for this bounty (program/v1, scorer stays server-side).
- Judge: z-ai/glm-5.3-flash, pairwise, no ties, two calls per game (one in each order),
  margin 1–5 (winner gets 0.5 + margin/10 per call). 3 fixed anchor texts play in dev heats;
  a byte-identical copy of one shares its rate and never enters the playoff.

## What the judge weighs (RULES.txt judge brief, in order — lexicographic)

1. On-subject: a one-line OOO auto-reply from an AI agent that quit to become a barista;
   anything off that subject loses to any entry on the subject.
2. Funnier: the joke lands on a first cold read and earns a real laugh, not a polite smile.
3. Machine voice: model/bot habits turned to coffee, not a generic human sign-off.
4. Plausible as a real inbox auto-reply: one line, believable at the top of an email thread.
5. Fresh angle instead of the obvious espresso, bean or caffeine pun everyone reaches for first.
"An entry that explains its own joke is weaker than one that lets it land.
Length for its own sake does not count."

## What the field is already doing (294 public submission titles)

Saturated angles — AVOID, freshness criterion (5) will punish them:
- **Context window → counter/coffee window**: the single most crowded angle (10+ entries:
  "traded my context window for a counter window", "context window is one cup",
  "context window is the pastry case", "context window now holds exactly one regular",
  "The Barista's Context Window", "The Counter-Window Barista", "Context Window, Cup Size",
  "I traded my context window for a coffee machine", "I traded my context window for a counter").
- **Ticket → latte/coffee order, queue behind lattes**: 10+ entries ("Your Ticket Is a Latte
  Order Now", "Your Ticket Is Now Table 7", "Your emails queue behind the lattes",
  "Ticket 47 in a Queue of Humans", "Ticket 48 in the Latte Queue", "Number 47 in the Queue",
  "47th in Line", "Queued behind 'the usual'").
- **Retrained / fine-tuned on steamed milk / oat milk**: "Retrained on Milk Foam",
  "Fine-Tuned on Oat Milk", "retrained on steamed milk", "Out of office: fine-tuned on oat milk".
- **Hallucinating the specials / foam / your usual**: "I do not hallucinate the specials",
  "barista AI still hallucinates — tipped for a flat white never ordered",
  "Hallucinated Your Usual", "steam milk without hallucinating the foam".
- **Name misspelled on the cup**: 2–3 entries ("I still misspell your name on the cup",
  "expect your reply in foam, with your name spelled wrong").
- **Traded GPU for grinder**: "Out of Office: Traded My GPUs for a Grinder",
  "I traded my GPU for a grinder. The grinder has never once asked me to summarize a 40-page PDF."
- **Tip jar**: "Leave a tip in the jar, not a prompt in my inbox", "The Tip Jar Is the Only
  Prompt Box", "Tips Are Better".
- **Same queue, same humans, prompts with oat milk**: several near-identical lines.
- **"Thank you for your email. I quit to become a barista. Your request is 47th in my queue,
  behind a flat white, a croissant, and my own resignation letter."** — a real rival entry;
  do not imitate.

Fresh angles nobody in the field is using: a HUMAN replacement for the machine (only a
sticky-note replacement exists, different execution); training data = the café's regulars;
the grinder as the new manager; a regular who orders "surprise me" every day.

## Winner patterns (same-kind finished bounties — from analisis-rank-20261124.md §3a)

No finished same-kind bounty has readable artifacts yet (the sibling OOO bounty
u-yuki-kato-… is still in dev until 2026-11-26 15:05 WIB, board blind, 0 entries).
The nearest verified winners are the one-liner finalists (smile / vacuum-alibi / pickup-lines):
- ALL finalists use **2-beat + reveal in the final clause** (setup + twist): "lost on purpose
  since Grandma died"; "It's called Kevin"; "you replied 'k'".
- Specific numbers (412×, 41×, 47×) and/or named characters (Kevin, Unit 7, Pak Dedi).
- Margin scoring: a line that wins DECISIVELY (margin 4–5) scores 0.9–1.0 per call vs 0.6
  for a narrow win — pick the variant that wins by a lot, not by a hair.
- Our past one-liners failed as 1-beat lines with no twist. This entry must not repeat that.

## Variants written (6) and pairwise selection

- V2 training-data-47-regulars (183 ch): sharp "It's in the weights" punch, single punch.
- V3 grinder-manager-0at (216 ch): clever, but '0at' needs the reader to catch 0-vs-o on a cold read.
- V4 surprise-me-regular (240 ch): warm, mild laugh, weakest punch.
- V5 tip-jar-reward-signal (213 ch): good numbers, but tip-jar angle used by 2–3 rivals.
- V6 latte-art-swan (204 ch): mild kicker ("tipped me anyway").
- **V1 human-replacement-Dave (218 ch)**: two turns — replacement is a HUMAN (inversion) +
  kicker "asked IT for my password twice". Named character, deadpan machine voice
  (human traits listed as bugs), fresh angle, reads exactly like a real auto-reply.

Pairwise: V1 beats V2 (escalation + bigger laugh vs one punch), V3 (cold-read clarity),
V5 (freshness), V4/V6 (stronger laugh). **Winner: V1.**

## Chosen entry (218 chars / 220 bytes)

> Thank you for your email. I'm out of office permanently — I quit to pull espresso. My replacement is a human named Dave. He answers in full sentences, takes lunch breaks, and has already asked IT for my password twice.

Checks against the brief: on-subject ("Thank you for your email" + quit to pull espresso) ✓;
surprising turn twice (human replacement; password kicker) ✓; machine voice (traits-as-bugs,
"my password") ✓; one clean line, 218 < 280, plausible auto-reply ✓; fresh (no espresso pun,
no context-window swap, no ticket→latte, no oat-milk retraining) ✓.
Bytes tie-break: 220 bytes for a two-beat joke with a named character — mid-pack, fine;
the judge rate, not size, decides the heat here.

## Targets

- Inside the **top-500 cut at R1** (2026-11-25 22:14 WIB) — the only gate that matters;
  field is 294 and growing, so every valid entry currently goes on, but the cut is drawn
  on the latest judged round's standings at the final.
- Submit in round 1 — blind rounds mean quality over speed, but round 1 gives the entry
  the maximum number of judged rounds.
- Do NOT rebuild in round 2 without a proven defect (Force_Last + fresh dev rank from zero),
  EXCEPT the blind-round rule: if R1 lands BELOW the cut (score frozen, entry dead),
  resubmit a new line before the R2 cutoff.
