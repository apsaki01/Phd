# Rehearsal feedback — iteration 298 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.75, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 39.53}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.683
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 41.0
- doors sealed+locked at prep end: 0.75, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.17, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.93, 0.3] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:done@26; prep1/0:done@24; prep1/1:dropped@25; prep1/1:no_target@26
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.7, 1.9] | seeker 2 saw hider 0 at play step 49 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; prep0/1:dropped@24; prep1/0:done@23; prep1/1:dropped@24
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.29, 0.89] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep1/0:done@9; prep1/1:dropped@10
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.79, 1.35] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:no_target@14; prep1/0:done@4; prep1/1:dropped@5; prep1/1:done@21
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.48, 0.59] | seeker 3 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@8; prep0/0:done@11; prep0/1:dropped@12; prep0/1:done@31; prep1/0:done@18; prep1/1:dropped@19; prep1/1:no_target@25
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.33, 0.53] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep0/1:dropped@22; prep0/1:no_target@27; prep1/0:dropped@14; prep1/0:done@16; prep1/1:dropped@17; prep1/1:done@30
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.83, 0.68] | seeker 2 saw hider 0 at play step 49 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep0/1:done@29; prep1/0:done@3; prep1/1:dropped@4; prep1/1:done@23
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.88, 1.81] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep0/1:done@28; prep1/0:done@21; prep1/1:dropped@22; prep1/1:no_target@23