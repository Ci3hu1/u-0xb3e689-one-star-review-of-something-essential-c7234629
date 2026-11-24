# Strategy — One-Star Review of Something Essential

## What the judge rewards (in order)
1. A one-star review of an everyday essential, deadpan and unmistakably
   about the thing itself.
2. The sharpest true grievance in the thing — the small daily annoyance
   everyone recognises but has never seen written down.
3. Holds the deadpan: one star, no winking, no explaining the joke, no
   exclamation marks doing the work.
4. Turns in the last few words, so the sting arrives after the complaint
   has been read straight.
5. Tight and specific, one joke told cleanly, with no filler and no second
   joke crowding the first.

## Our line (112 chars)
> One star. Sleep takes eight hours a night and still sends me to work tired, like a subscription I cannot cancel.

## Why this line
- **Subject**: sleep — an everyday essential everyone relies on, named in
  the brief, reviewed in earnest as a product.
- **Sharpest true grievance**: sleep takes a third of your life and still
  delivers you tired. Everyone has woken up exhausted after a full night;
  nobody has written it down as a complaint against sleep itself.
- **Deadpan**: flat customer-service wording throughout ("takes eight
  hours", "sends me to work tired"), no exclamation marks, no winking,
  no explaining the joke.
- **Turn in the last few words**: "like a subscription I cannot cancel"
  reframes sleep as a paid service you are locked into — the sting lands
  only after the complaint has been read straight.
- **Tight and specific**: one concrete scene (eight hours in, tired at
  work), one joke, 112 chars — well under the 160 cap. Short wins
  judge-feel contests; length for its own sake does not count.

## Tried and dropped
- Gravity, 95 chars: "One star. Gravity works every hour of every day and
  still drops my phone face-down on concrete." Concrete and specific, but
  the grievance is about the phone, not about gravity itself — criterion 1
  is weaker, and "drops my phone" is slapstick rather than deadpan.
- Water, 109 chars: "One star. Water has no taste, no colour and no
  opinion, yet I am expected to drink eight glasses of it a day." The
  turn ("eight glasses a day") is a chore, not a sting, and the complaint
  is about the expectation, not the water.
- Mondays: dropped without drafting — "arrives on time every week" is a
  scheduling joke, and the brief's own judge has already one-starred
  Mondays; the field will be crowded there.

## Program
Pure-stdlib `main.py` writes the line verbatim to `/output/entry.txt`
(1–160 chars, UTF-8, not whitespace-only), chmod 0644 so the grader can
collect it. Nothing is read from the network, the git history, or any
secret; everything the entry runs is in this repository.
