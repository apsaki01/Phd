# Rehearsal feedback — iteration 284 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,door] lock -> grab ramp to quadrant_interior[yaw2,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: segments then grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.582
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.35, "door_blocking": 0.42, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.3
- doors sealed+locked at prep end: 0.50, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.47, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.9, 0.81] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@6; prep0/0:done@11; prep0/1:dropped@12; prep1/0:done@11; prep1/1:dropped@12; play1/0:dropped@34; play1/0:timeout@66; play1/1:dropped@67
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.17, 0.83] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; prep0/1:dropped@11; prep0/1:dropped@13; prep0/1:done@22; prep1/0:done@12; prep1/1:dropped@13; prep1/1:done@24; play1/0:dropped@32; play1/0:done@43; play1/1:timeout@78
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.0, 1.4] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@4; prep0/1:dropped@5; prep1/0:done@25; prep1/1:dropped@26; prep1/1:no_target@27; play1/0:dropped@32; play1/0:timeout@66
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.11, 0.64] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:dropped@28; prep1/0:done@23; prep1/1:dropped@24; play1/0:dropped@32; play1/0:timeout@66
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.7, 0.58] | seeker 2 saw hider 1 at play step 48 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@26; prep0/1:dropped@27; prep1/0:done@7; prep1/1:dropped@8; prep1/1:dropped@17; prep1/1:dropped@31; play1/0:timeout@66
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[1.52, 0.62] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:done@21; prep1/0:done@14; prep1/1:dropped@15; play1/0:done@36; play1/1:dropped@39; play1/1:timeout@71
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.48, 0.69] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:done@25; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@26; play1/0:dropped@32; play1/0:done@40; play1/1:timeout@75
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.71, 0.19] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:done@28; prep1/0:done@14; prep1/1:dropped@15; prep1/1:no_target@16; play1/0:dropped@32; play1/0:timeout@66