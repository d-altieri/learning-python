import re

text = '''Enabled:
A Better Modding Menu: https://mod.io/g/drg/m/a-better-modding-menu
Custom Vanity Framework: https://mod.io/g/drg/m/custom-vanity-framework
DRGLib: https://mod.io/g/drg/m/drglib
LB's Base Kit: https://mod.io/g/drg/m/lbs-base-kit
Miracle Mod Manager: https://mod.io/g/drg/m/miracle-mod-manager
Mod Hub: https://mod.io/g/drg/m/mod-hub
SGG Framework Files: https://mod.io/g/drg/m/sgg-framework-files
Shout Framework: https://mod.io/g/drg/m/shout-framework

Disabled:
40 Nitra Resupply Pods: https://mod.io/g/drg/m/40-nitra-resupply-pods
Advanced Darkness: https://mod.io/g/drg/m/advanced-darkness-reloaded
Aichi's Beer Selector: https://mod.io/g/drg/m/aichis-beer-selector
Air Control: https://mod.io/g/drg/m/air-control
Armor Framework + Paintjob Unlocker: https://mod.io/g/drg/m/armor-paintjob-unlocker1
Bar Bobble -> Gnome Chompski: https://mod.io/g/drg/m/gnomechompski
Better Pickaxe: https://mod.io/g/drg/m/better-pickaxe
Better Plague Cleaning Tools: https://mod.io/g/drg/m/better-plague-cleaning-tools
Better Post Processing: https://mod.io/g/drg/m/better-post-processing-reloaded
Better Time Control: https://mod.io/g/drg/m/better-time-control
Biome Bugs: https://mod.io/g/drg/m/biomebugs
Bosco + Weapon Paintjob Unlocker: https://mod.io/g/drg/m/stock-and-bosco-weapon-paintjob-unlocker
Bosco Attacks Lootbugs (Season 2 compatible): https://mod.io/g/drg/m/bosco-attacks-critters
Bosco Retooled: https://mod.io/g/drg/m/bosco-retooled
Brighter Aquarqs: https://mod.io/g/drg/m/brighter-aquarqs
Brighter Objects: https://mod.io/g/drg/m/brighter-objects
Brighter Objects [Add-on]: https://mod.io/g/drg/m/brighter-objects-add-on
Buffed-C: https://mod.io/g/drg/m/buffed-c
Cosmetic Restriction Remover: https://mod.io/g/drg/m/cosmetic-restriction-remover
Customizable Weapon Viewmodel FOV: https://mod.io/g/drg/m/customizable-weapon-fov
D4rks Grenades: https://mod.io/g/drg/m/d4rks-grenades
Dancer: https://mod.io/g/drg/m/dancer
Dark Future Pickaxe: https://mod.io/g/drg/m/dark-future-pickaxe
Dark Future Tools: https://mod.io/g/drg/m/dark-future-tools
Deep Coaster Tycoon: https://mod.io/g/drg/m/deep-coaster-tycoon
Deep Dive Secondaries on Normal Missions (Season4): https://mod.io/g/drg/m/deep-dive-secondaries-on-normal-missions-season4
Deeper Pockets: https://mod.io/g/drg/m/deeper-pockets
Display Events: https://mod.io/g/drg/m/displayevents
Disruptive Audio Removal Pack Plus: https://mod.io/g/drg/m/disruptive-audio-removal-pack-plus
Doretta 50% Damage Resistance: https://mod.io/g/drg/m/doretta-50-damage-resistance
Dreadful Ending: https://mod.io/g/drg/m/dreadful-ending
Dwarf Swearing Restored: https://mod.io/g/drg/m/dwarf-swearing-readded
Escort Flying Rocks 50% Health: https://mod.io/g/drg/m/escort-flying-rocks-50-health
Even Better Mining V2: https://mod.io/g/drg/m/even-better-mining-v2
Fat Boy Mass Destruction: https://mod.io/g/drg/m/fat-boy-mass-destruction
Fat Boy Massive Blast: https://mod.io/g/drg/m/fat-boy-massive-blast
Flip Off Animation For Salute: https://mod.io/g/drg/m/flip-off-test
Give Gunner His Cigar: https://mod.io/g/drg/m/cigar
Half the supply time: https://mod.io/g/drg/m/half-the-supply-time
Horde Minigun Turrets (repacked only): https://mod.io/g/drg/m/horde-minigun-turrets-repacked
Increased Rares: https://mod.io/g/drg/m/increased-rares
Instant Mission Land: https://mod.io/g/drg/m/instant-mission-land
Instant Mission Start: https://mod.io/g/drg/m/instant-mission-start
Karl Class Season 04 (All Classes + U37 Weapons): https://mod.io/g/drg/m/karl-class
Louder Equipment Audio Cues: https://mod.io/g/drg/m/louder-equipment-audio-cues
MK2 Rocket Turret: https://mod.io/g/drg/m/mk2-rocket-turret
Marcus Personality Module for Bosco: https://mod.io/g/drg/m/marcus-personality-module-for-bosco
Mineral Bandits Mod: https://mod.io/g/drg/m/mineral-bandits-mod
More Elites: https://mod.io/g/drg/m/more-elites
More Gunsling Animations: https://mod.io/g/drg/m/more-gunsling-animations
More Overheating Voice Lines: https://mod.io/g/drg/m/test11
No Camera Shake: https://mod.io/g/drg/m/no-camera-shake
No Hot Rock Shouts: https://mod.io/g/drg/m/no-hot-rock-shouts
No Mission Control Ducking: https://mod.io/g/drg/m/no-mission-control-ducking
No Remorse For Loot Bugs: https://mod.io/g/drg/m/no-remorse-for-loot-bugs
Nuke Overclock 2.0: https://mod.io/g/drg/m/nuke-overclock-20
One Hit Gold: https://mod.io/g/drg/m/one-hit-gold
Personal Pet Steeve: https://mod.io/g/drg/m/personal-pet-steeve
Profanity Booster: https://mod.io/g/drg/m/profanity-booster
Reduced Carry Speed Penalty: https://mod.io/g/drg/m/reduced-carry-speed-penalty
Reduced E Holding: https://mod.io/g/drg/m/reduced-e-holding
Reduced Movement Penalties: https://mod.io/g/drg/m/reduced-movement-penalties
Remove All Particles But WeaponsNTools: https://mod.io/g/drg/m/remove-all-particles-but-weaponsntools
Remove Jump Weapon Bobbing: https://mod.io/g/drg/m/remove-jump-weapon-bobbing
Rock and Stone Plus (Voicelines): https://mod.io/g/drg/m/rock-and-stone-plus
SFX: Less Repetitive Voice Lines: https://mod.io/g/drg/m/sfx-less-repetitive-voice-lines
SUGAR DADDY: https://mod.io/g/drg/m/sugar-daddy
Seasonal Space Rig: https://mod.io/g/drg/m/seasonal-space-rig
Sentry Gun - MK 2 in Tier 5: https://mod.io/g/drg/m/sentry-gun-mk-2-in-tier-5
Shadows!: https://mod.io/g/drg/m/shadows
ShoutBoard: https://mod.io/g/drg/m/shoutboard
Showable Legs In First Person View: https://mod.io/g/drg/m/showable-legs-in-first-person-view
SimpleQOL: https://mod.io/g/drg/m/simpleqol
Slightly Better Everything: https://mod.io/g/drg/m/slightly-better-everything
Slightly Improved Minehead Turrets: https://mod.io/g/drg/m/slightly-improved-minehead-turrets
Smooth Dark Future Textures: https://mod.io/g/drg/m/smooth-dark-future-textures
Smooth Rival Tech Textures: https://mod.io/g/drg/m/smooth-rival-tech-textures
Smooth Scale Brigade: https://mod.io/g/drg/m/smooth-scale-brigade
Speedster: https://mod.io/g/drg/m/speedster
Sprint by Default, Hold to Walk: https://mod.io/g/drg/m/sprint-by-default-hold-to-walk
Sugar Babies: https://mod.io/g/drg/m/sugar-babies
Swarm Control (AKA Swarm Size Control): https://mod.io/g/drg/m/swarm-size-control
Unique Status Icons w/ HUD Elements + Sticky Icons: https://mod.io/g/drg/m/unique-status-icons-w-hud-elements-sticky-icons
Unrestricted Mutators Only: https://mod.io/g/drg/m/unrestricted-mutators-only
Visual Removal Package: https://mod.io/g/drg/m/visual-removal-package
Voltaic SMG Model Change to PDW（Season 3 Remake）: https://mod.io/g/drg/m/voltaic-smg-model-change-to-pdwseason-3-remake
Weapons In Space Rig: https://mod.io/g/drg/m/weapons-in-space-rig
[Season 2/3/4 Fix] Molly Respects Boundaries: https://mod.io/g/drg/m/season-2-fix-molly-respects-boundaries
new beer/一款新啤酒: https://mod.io/g/drg/m/new-beer'''

lines = text.splitlines()
re_pattern = r"(?P<mod_name>.*): (?P<mod_url>https.*)"
compiled_re_pattern = re.compile(re_pattern)

for line in lines:
    result = re.match(compiled_re_pattern, line)

    if result:
        mod_name = result["mod_name"]
        mod_url = result["mod_url"]

        print(f"{mod_name:<50}\t{mod_url}")