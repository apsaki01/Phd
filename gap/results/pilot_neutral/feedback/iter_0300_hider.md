# Rehearsal feedback — iteration 300 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.75, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 39.53}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.542
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.28, "door_blocking": 0.47, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.3
- doors sealed+locked at prep end: 0.59, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.50, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.33, 2.44] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@1; prep0/1:dropped@2
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.92, 1.62] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@21; prep0/0:done@27; prep0/1:dropped@28; prep0/1:no_target@29; prep1/0:done@18; prep1/1:dropped@19
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.1, 1.05] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@5; prep0/1:dropped@6; prep0/1:dropped@9
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.73, 2.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:dropped@12; prep1/0:done@3; prep1/1:dropped@4; prep1/1:done@19
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.03, 1.55] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@4; prep0/0:done@6; prep0/1:dropped@7; prep0/1:dropped@15; prep0/1:done@28; prep1/0:done@15; prep1/1:dropped@16
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.64, 1.68] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@4; prep1/1:dropped@5; prep1/1:dropped@7
- p_door=0.75 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.86, 1.16] | seeker 3 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep0/1:dropped@19; prep0/1:dropped@22; prep1/0:done@15; prep1/1:dropped@16; prep1/1:done@24
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.88, 1.18] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; prep0/1:dropped@7; prep1/0:done@6; prep1/1:dropped@7; prep1/1:no_target@17