# Rehearsal feedback — iteration 342 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 38.08}
  role0 prep: grab box to climb[yaw1,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,direct] lock -> grab ramp to quadrant_interior[align,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.567
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.5
- doors sealed+locked at prep end: 0.66, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.28, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.19, 0.57] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:dropped@22; prep1/0:done@27; prep1/1:dropped@28
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.28, 0.16] | seeker 2 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@24; prep0/1:dropped@25; prep0/1:no_target@26; prep1/0:done@21; prep1/1:dropped@22; prep1/1:dropped@25
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.89, 1.06] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; prep0/1:dropped@7; prep0/1:done@15; prep1/0:done@6; prep1/1:dropped@7; prep1/1:no_target@8
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.9, 0.97] | seeker 3 saw hider 1 at play step 48 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@27; prep0/0:done@28; prep0/1:dropped@29; prep1/0:done@26; prep1/1:dropped@27; prep1/1:dropped@30
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.28, 0.09] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; prep0/1:dropped@7
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.8, 1.3] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; prep0/1:dropped@11; prep1/0:done@9; prep1/1:dropped@10
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.49, 1.02] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep1/0:done@13; prep1/1:dropped@14
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.74, 1.98] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep0/1:dropped@22; prep1/0:done@4; prep1/1:dropped@5; prep1/1:done@23