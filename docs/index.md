# Neuromorphic Computing Game Spec

## Product Goal
Build a Neo-led, neuromorphic-themed strategy/idle game where players design efficient neural systems, earn progression rewards, and unlock narrative/community content tied to the `$NEURO` ecosystem.

## Core Loop
1. Build or upgrade a node cluster in the network map.
2. Route synapses and tune spike behavior for current mission goals.
3. Run simulation cycles to generate outputs and measure efficiency.
4. Spend earned resources on upgrades, unlocks, and new mission tiers.
5. Publish progress to social/community modules (optional), then repeat at higher complexity.

## Resources And Economy
- `Charge`: baseline energy input used by all active nodes.
- `Spikes`: event output produced by neuron nodes; used for most progression steps.
- `Insights`: earned from optimization targets, challenge clears, and mission completions.
- `$NEURO Credits` (in-game): premium progression currency for cosmetics, faster unlock paths, and special events.
- `Reputation`: social/community score from Learn-to-Earn missions, outreach quests, and seasonal participation.

Economy rules:
- Charge is abundant but inefficient at scale unless optimized.
- Spikes and Insights are bottlenecks for mid/late-game upgrades.
- $NEURO Credits are optional accelerators, not required for core progression.

## Progression And Unlocks
- Tier 1 (`Bootstrap`): basic neuron + simple synapse routing + tutorial missions.
- Tier 2 (`Adaptive Network`): threshold tuning, inhibitory control, and multi-objective missions.
- Tier 3 (`Edge Intelligence`): low-power constraints, burst workloads, and resilience challenges.
- Tier 4 (`Cognitive Fabric`): large network orchestration, rare node variants, and seasonal boss simulations.

Unlock channels:
- Mission completion (primary).
- Efficiency milestones (secondary).
- Learn-to-Earn achievements (community-linked).
- Seasonal events and lore chapters (comics/podcast tie-ins).

## Node And Synapse Types
Node types:
- `Sensor Node`: converts external input to spike trains.
- `Compute Neuron`: core processing node with configurable threshold.
- `Inhibitory Node`: suppresses noisy traffic and stabilizes routing.
- `Memory Node`: stores short-term state for temporal tasks.
- `Edge Gateway`: boosts local efficiency and handles burst events.
- `Oracle Node` (late game): injects mission modifiers and rare bonuses.

Synapse types:
- `Excitatory`: increases downstream firing probability.
- `Inhibitory`: decreases downstream firing probability.
- `Plastic`: adjusts weight via use-dependent learning.
- `Long-Range`: high throughput with higher Charge cost.
- `Resonant`: combo-link that amplifies synchronized spike bursts.

## Efficiency Scaling
- Target metric: `Output Efficiency = Useful Spikes / Charge Used`.
- Diminishing returns: each repeated upgrade on the same node family gives reduced gains.
- Heat/noise penalties increase when networks over-fire without inhibition.
- Event-driven bonus: idle-efficient configurations receive multiplier rewards.
- Late-game mastery focuses on balancing throughput, latency, and power budget rather than raw output.

## UI Layout And Screens
- `Home / Network Map`: main playable graph canvas and mission HUD.
- `Node Lab`: per-node tuning, synapse inspector, and comparative metrics.
- `Missions`: campaign, weekly challenges, and Learn-to-Earn tasks.
- `Progression`: unlock tree, milestones, and season track.
- `Marketplace`: cosmetics, gallery assets, and optional premium exchanges.
- `Community`: announcements, outreach quests, and featured creator content.
- `Settings`: accessibility, audio, controls, and performance mode.

Mobile-first adaptation:
- Bottom-tab navigation for core screens.
- Compact graph interaction mode with tap-to-focus node editing.

## Art And Audio Asset Plan
Art direction:
- Cyber-neural sci-fi with high contrast circuitry, synapse pulse FX, and Neo character motifs.
- Visual layers: network core, city-scale holographic backdrop, mission-specific overlays.

Asset categories:
- UI kit (panels, graphs, node icons, status states).
- Node/synapse VFX packs (spike pulses, inhibitory dampening, resonance bursts).
- Character/lore assets (Neo portraits, comic panels, seasonal banners).
- Marketing/media assets (podcast covers, teaser stills, short-form clip templates).

Audio direction:
- Adaptive electronic score that grows with network complexity.
- Distinct audio cues for spike events, instability warnings, and unlock moments.
- Podcast-ready stingers and social clip stems for marketing reuse.

## Scope Notes
- This spec treats the game as the primary product surface and keeps token integration optional/in-game to avoid hard dependency.
- Conversations under `docs/chats/` are treated as ideation source material; implementation should follow this document as canonical scope.
