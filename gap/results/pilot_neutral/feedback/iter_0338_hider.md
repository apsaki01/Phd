# Rehearsal feedback — iteration 338 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 38.08}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,direct] lock -> grab ramp to quadrant_interior[align,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,direct] lock -> to quadrant_interior[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.546
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.45, "ramp_use": 0.03, "ramp_defense": 0.0}
- mean first-seen play step: 36.7
- doors sealed+locked at prep end: 0.51, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.47, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.78, 1.62] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep0/1:dropped@19; prep1/0:dropped@18; prep1/0:dropped@28
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.6, 0.49] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; prep0/1:dropped@11
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.06, 1.13] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@11; prep0/1:dropped@12
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.27, 1.36] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:dropped@21; prep0/0:done@23; prep0/1:dropped@24; prep0/1:done@29; prep1/0:done@25; prep1/1:dropped@26; prep1/1:no_target@27
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.54, 1.6] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep1/0:done@12; prep1/1:dropped@13
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.33, 1.16] | hiders never seen | segments: prep0/0:done@10; prep0/1:dropped@11; prep0/1:done@18; prep1/0:done@14; prep1/1:dropped@15; prep1/1:dropped@22; prep1/1:done@28
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.68, 0.11] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@5; prep0/0:dropped@14; prep0/0:done@18; prep0/1:dropped@19; prep0/1:dropped@23; prep1/0:done@14; prep1/1:dropped@15; prep1/1:dropped@17
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.47, 1.11] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10