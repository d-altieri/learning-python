import re

text = '''A Better Modding Menu: https://mod.io/g/drg/m/a-better-modding-menu
Armor Framework + Paintjob Unlocker: https://mod.io/g/drg/m/armor-paintjob-unlocker1
Better Bolt Indicator: https://mod.io/g/drg/m/better-bolt-indicator
Bosco + Weapon Paintjob Unlocker: https://mod.io/g/drg/m/stock-and-bosco-weapon-paintjob-unlocker
Bosco Retooled: https://mod.io/g/drg/m/bosco-retooled
Brighter Objects: https://mod.io/g/drg/m/brighter-objects
Custom Vanity Framework: https://mod.io/g/drg/m/custom-vanity-framework
Doretta 50% Damage Resistance: https://mod.io/g/drg/m/doretta-50-damage-resistance
Equipment x2 but not so x2: https://mod.io/g/drg/m/equipment-x2-but-not-so-x2
Health and Shield Numbers: https://mod.io/g/drg/m/health-and-shield-numbers
Live Mission Stat Tracker: https://mod.io/g/drg/m/live-mission-stat-tracker
Remove Mineral Scatter: https://mod.io/g/drg/m/remove-mineral-scatter

10 Waypoints: https://mod.io/g/drg/m/10-waypoints
40 Nitra Resupply Pods: https://mod.io/g/drg/m/40-nitra-resupply-pods
AJN's Minehead Turrets: https://mod.io/g/drg/m/ajns-minehead-turrets
Abnormal Anomalies: https://mod.io/g/drg/m/abnormal-anomalies
Advanced Darkness: https://mod.io/g/drg/m/advanced-darkness-reloaded
Air Control: https://mod.io/g/drg/m/air-control
All Biomes More Missions: https://mod.io/g/drg/m/all-biomes-more-missions
All the Rares: https://mod.io/g/drg/m/all-the-rares
Ashless Radioactive Exclusion Zone: https://mod.io/g/drg/m/ashless-radioactive-exclusion-zone
Bar Bobble -> Gnome Chompski: https://mod.io/g/drg/m/gnomechompski
Better Beers, Extra Strength Underhills: https://mod.io/g/drg/m/better-beers-extra-strength-underhills
Better Mining - Gold Edition: https://mod.io/g/drg/m/better-mining-gold-edition
Better Mining Laser: https://mod.io/g/drg/m/better-mining-laser
Better Pickaxe: https://mod.io/g/drg/m/better-pickaxe
Better Plague Cleaning Tools: https://mod.io/g/drg/m/better-plague-cleaning-tools
Better Post Processing: https://mod.io/g/drg/m/better-post-processing-reloaded
Better Time Control: https://mod.io/g/drg/m/better-time-control
Black Dark Descent + Chasm-Borne: https://mod.io/g/drg/m/black-dark-descent-chasm-borne
Boomstick Classic: https://mod.io/g/drg/m/boomstick-classic
Bot Gradient: https://mod.io/g/drg/m/bot-gradient
Brighter Objects [Add-on]: https://mod.io/g/drg/m/brighter-objects-add-on
Bring Back Best Wurst Beer: https://mod.io/g/drg/m/bring-back-wurst-beer
Buffed-C: https://mod.io/g/drg/m/buffed-c
Bulldog Classic: https://mod.io/g/drg/m/bulldog-classic
Buyable Missions: https://mod.io/g/drg/m/buyable-missions
Class Icons Default: https://mod.io/g/drg/m/class-icons-default
Clear Weakspot Hit Sounds: https://mod.io/g/drg/m/clear-weakspot-hit-sounds
Cosmetic Restriction Remover: https://mod.io/g/drg/m/cosmetic-restriction-remover
Custom Killfeed: https://mod.io/g/drg/m/custom-killfeed
Custom Re-Engineered: https://mod.io/g/drg/m/custom-re-engineered
Customizable Ally Outlines: https://mod.io/g/drg/m/customizable-ally-outlines
Customizable Weapon Viewmodel FOV: https://mod.io/g/drg/m/customizable-weapon-fov
DRGLib: https://mod.io/g/drg/m/drglib
Dancer: https://mod.io/g/drg/m/dancer
Dark Future Pickaxe: https://mod.io/g/drg/m/dark-future-pickaxe
Dark Future Tools: https://mod.io/g/drg/m/dark-future-tools
Deep Coaster Tycoon: https://mod.io/g/drg/m/deep-coaster-tycoon
Deep Dive Secondaries on Normal Missions (Season2): https://mod.io/g/drg/m/deep-dive-secondaries-for-normal-missions-season2
Display Events: https://mod.io/g/drg/m/displayevents
Disruptive Audio Removal Pack Plus: https://mod.io/g/drg/m/disruptive-audio-removal-pack-plus
Dreadful Ending: https://mod.io/g/drg/m/dreadful-ending
Escort Flying Rocks 50% Health: https://mod.io/g/drg/m/escort-flying-rocks-50-health
Even Better Digging: https://mod.io/g/drg/m/even-better-digging
Fabulously Fast Lootbugs for U36: https://mod.io/g/drg/m/fabulously-fast-lootbugs-for-u36
Fancy Hats: https://mod.io/g/drg/m/fancy-hats
Fat Boy Massive Blast: https://mod.io/g/drg/m/fat-boy-massive-blast
Fix Grenade Collision: https://mod.io/g/drg/m/fix-grenade-collision
Give Gunner His Cigar: https://mod.io/g/drg/m/cigar
Glowing Equipment: https://mod.io/g/drg/m/glowing-equipment
Grenade Rework - All Grenades Hold 8: https://mod.io/g/drg/m/8-grenade-rework
Half the supply time: https://mod.io/g/drg/m/half-the-supply-time
Hazard Persistence Enjoyer: https://mod.io/g/drg/m/hazard-persistence-enjoyer
Horde Minigun Turrets (repacked only): https://mod.io/g/drg/m/horde-minigun-turrets-repacked
Inspect Animations when pressing R: https://mod.io/g/drg/m/inspect-animations-when-pressing-r
Karl Class Season 03 (All Classes + U37 Weapons): https://mod.io/g/drg/m/karl-class
Louder Equipment Audio Cues: https://mod.io/g/drg/m/louder-equipment-audio-cues
M1000 Classic Classic: https://mod.io/g/drg/m/m1000-classic-classic
MK2 Rocket Turret: https://mod.io/g/drg/m/mk2-rocket-turret
Marcus Personality Module for Bosco: https://mod.io/g/drg/m/marcus-personality-module-for-bosco
Mineral Bandits Mod: https://mod.io/g/drg/m/mineral-bandits-mod
Miracle Mod Manager: https://mod.io/g/drg/m/miracle-mod-manager
Mission Content Randomizer: https://mod.io/g/drg/m/mission-content-randomizer
Mission Control Text Remover (Demake): https://mod.io/g/drg/m/mission-control-text-remover-remake
Mod Hub: https://mod.io/g/drg/m/mod-hub
Molly Lights the Way: https://mod.io/g/drg/m/molly-lights-the-way
More FOV: https://mod.io/g/drg/m/more-fov
More Gunsling Animations: https://mod.io/g/drg/m/more-gunsling-animations
More Transparent shield and blood overlays: https://mod.io/g/drg/m/more-transparent-shield-and-blood-overlays
Nightmare Spiders: https://mod.io/g/drg/m/nightmarespiders
No Camera Shake: https://mod.io/g/drg/m/no-camera-shake
No Hot Rock Shouts: https://mod.io/g/drg/m/no-hot-rock-shouts
No Mission Control Ducking: https://mod.io/g/drg/m/no-mission-control-ducking
No Remorse For Loot Bugs: https://mod.io/g/drg/m/no-remorse-for-loot-bugs
Pettable Maggots: https://mod.io/g/drg/m/pettable-maggots
Profanity Booster: https://mod.io/g/drg/m/profanity-booster
Random Refinery Breakdowns: https://mod.io/g/drg/m/random-refinery-breakdowns
Ravager Minigun Model Swap: https://mod.io/g/drg/m/ravager-minigun-model-swap
Real Weapon Stats (Abandoned) (Backup Mod): https://mod.io/g/drg/m/real-weapon-stats
Real Weapon Stats Classic: https://mod.io/g/drg/m/real-weapon-stats-classic
Reduced Carry Speed Penalty: https://mod.io/g/drg/m/reduced-carry-speed-penalty
Reduced Cloud Opacity remake: https://mod.io/g/drg/m/reduced-cloud-opacity-remake
Reduced E Holding: https://mod.io/g/drg/m/reduced-e-holding
Reduced Movement Penalties: https://mod.io/g/drg/m/reduced-movement-penalties
Remove Jump Weapon Bobbing: https://mod.io/g/drg/m/remove-jump-weapon-bobbing
Removed Fire Death Particles: https://mod.io/g/drg/m/removed-fire-death-particles
Removed Frozen Death & Impact Particles: https://mod.io/g/drg/m/removed-frozen-death-impact-particles
Removed Terrain Destruction Particles: https://mod.io/g/drg/m/removed-terrain-destruction-particles
Retrograde Mod Spawner: https://mod.io/g/drg/m/retrograde-mod-spawner
Rival Tech Turrets Less Health: https://mod.io/g/drg/m/rival-tech-turrets-less-health
SFX: Less Repetitive Voice Lines: https://mod.io/g/drg/m/sfx-less-repetitive-voice-lines
SUGAR DADDY: https://mod.io/g/drg/m/sugar-daddy
Seasonal Space Rig: https://mod.io/g/drg/m/seasonal-space-rig
Showable Legs In First Person View: https://mod.io/g/drg/m/showable-legs-in-first-person-view
Silence of The Crumbs: https://mod.io/g/drg/m/silence-of-the-crumbs
Silent Sprinting: https://mod.io/g/drg/m/silent-sprinting
Simpler Azure Weald: https://mod.io/g/drg/m/simpler-azure-weald
Simpler Hollow Bough: https://mod.io/g/drg/m/simpler-hollow-bough
Slight Weapon Tweaks: https://mod.io/g/drg/m/slightweapontweaks
Smooth Dark Future Textures: https://mod.io/g/drg/m/smooth-dark-future-textures
Smooth Rival Tech Textures: https://mod.io/g/drg/m/smooth-rival-tech-textures
Speedster: https://mod.io/g/drg/m/speedster
Sprint by Default, Hold to Walk: https://mod.io/g/drg/m/sprint-by-default-hold-to-walk
Sugar Babies: https://mod.io/g/drg/m/sugar-babies
Supply Pods Keep Grab Progress: https://mod.io/g/drg/m/supply-pods-keep-grab-progress
Supporter Gold Vanity: https://mod.io/g/drg/m/supporter-gold-vanity
Swarm Control (AKA Swarm Size Control): https://mod.io/g/drg/m/swarm-size-control
Tactical Nukes: https://mod.io/g/drg/m/tactical-nukes
Tweaks, Tweaks and more Tweaks: https://mod.io/g/drg/m/tweaks-tweaks-and-more-tweaks
Unique Status Effect Icons + HUD Elements: https://mod.io/g/drg/m/unique-status-effect-icons-hud-elements
Voltaic SMG Model Change to PDW: https://mod.io/g/drg/m/voltaic-smg-model-change
Weapons In Space Rig: https://mod.io/g/drg/m/weapons-in-space-rig
Wheel's Miner Perks: https://mod.io/g/drg/m/wheels-miner-perks
White Throwing Flares: https://mod.io/g/drg/m/white-throwing-flares
Who Done It?: Button Mod: https://mod.io/g/drg/m/who-done-it-button-mod
[Season 2/3 Fix] Molly Respects Boundaries: https://mod.io/g/drg/m/season-2-fix-molly-respects-boundaries
rancor's Rig HUD: https://mod.io/g/drg/m/rancors-rig-hud
'''

lines = text.splitlines()
re_pattern = r"(?P<mod_name>.*): (?P<mod_url>https.*)"
compiled_re_pattern = re.compile(re_pattern)

for line in lines:
    result = re.match(compiled_re_pattern, line)

    if result:
        mod_name = result["mod_name"]
        mod_url = result["mod_url"]

        print(f"{mod_name:<50}\t{mod_url}")