# Bunker: Survival Protocol

A text-based survival management game written in Python. You run the last safe shelter in a collapsing world - screening visitors at the gate, managing scarce resources, and keeping your people alive for 10 days until rescue arrives.

## Overview

Every day, up to three strangers arrive at your gate, each with their own story, condition, and reason to be let in — or turned away. Every decision has a cost. Let in the wrong person and infection spreads through your bunker. Turn away too many and your reputation in the wasteland collapses. Run out of food, air, or the trust of your own people, and it's game over.

Survive 10 full days and the rescue teams find you.

## Gameplay

Each day is split into two phases:

### Morning — The Gate
Three visitors arrive over the course of the day. For each one, you can:
- **Run a checkup** to reveal their infection risk and health status before deciding (recommended, but not required)
- **Allow entry**, bringing them and anything in their inventory (food, meds, or tools) into the bunker
- **Deny entry**, turning them away

### Evening — The Bunker
Once the gates are closed for the night, you manage what's inside:
- **Do checkups** — screen anyone not yet diagnosed, and decide the fate of anyone confirmed infected
- **Check the air filter** — repair it with tools or a mechanic before it fails
- **Check morality level** — gauge how close your own people are to revolt
- **Check reputation level** — gauge how the outside world sees your gate
- **Skip the evening routine** — move straight to the day's results

## Core Systems

### Resources
| Resource | Use |
|---|---|
| **Food** | Consumed automatically each day — 1 unit per person sheltering in the bunker. Hits 0 and everyone starves. |
| **Meds** | Cures infected residents, 1 unit per person treated. |
| **Tools** | Repairs the air filter. |

Visitors may bring any of these with them if you let them in.

### Air Filter
Degrades by 15% every day on its own. Repair it with Tools (+15%) or call in a Mechanic resident (+20%, once per day). If it ever reaches 0%, the bunker fills with toxic gas — game over.

### Morality
Reflects how much your own residents trust your leadership. Curing the infected raises it. Expelling people — especially infected ones — lowers it sharply. If it hits 0%, the survivors revolt... unless you have a Policeman in the bunker, who has a chance to talk them down.

### Reputation
Reflects how the wasteland outside sees your gate. Accepting visitors builds it slowly; denying them costs more, and denying someone without justification (i.e. without a checkup showing a real medical risk) costs the most. Let it fall low enough and you'll no longer be allowed to deny entry at all unless a checkup confirms the visitor is SEVERE or CRITICAL — the bunker's own reputation restrains you from turning people away on a whim. If it reaches 0%, raiders tired of being turned away storm the gates.

### Infection
Checkups reveal a status — CLEAR, MILD, SEVERE, or CRITICAL — along with an infection risk percentage. Once someone inside the bunker is confirmed infected, you must either cure them with meds or expel them. Left untreated for more than 4 days, the infection spreads and wipes out everyone. Game over.

## Roles

Residents aren't just extra mouths to feed — certain roles help the bunker passively once they're inside:

| Role | Effect |
|---|---|
| **Doctor** | Chance to cure an infected resident for free, no meds spent |
| **Nurse** | Boosts the morality gained from successfully curing someone |
| **Mechanic** | Can repair the air filter directly, once per day |
| **Botanist** | Chance to grow extra food each day |
| **Musician** | Chance to boost morality each day |
| **Policeman** | Chance to prevent a mutiny if morality hits 0% |

Other roles (Ex-Soldier, Scavenger, Civilian) appear as flavor and contribute inventory items, but have no passive bonus yet — open territory for future features.

## Loss Conditions

The game ends immediately if any of the following occurs:
- Food reaches 0
- Air filter condition reaches 0
- Morality reaches 0 (and no Policeman saves the day)
- Someone stays infected for more than 4 days
- Reputation reaches 0

Survive through Day 10 and you win.

## Running the Game

Requires Python 3.10+ (uses `match` statements).

```bash
python bunker.py
```

Play entirely from the terminal — all input is typed at the `>>` prompt.

## Project Status

This is a work in progress. Currently implemented:
- Full day/night loop with morning gate decisions and evening bunker management
- Infection, morality, and reputation systems
- Role-based passive bonuses
- Win/loss conditions and a replayable main menu

Ideas for future additions:
- Passive bonuses for the remaining roles (Ex-Soldier, Scavenger, Civilian)
- Persistent stats or a run history across playthroughs
- Difficulty options (starting resources, visitor frequency, infection rates)
- Save/load mid-run
