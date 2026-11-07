# Rehearsal feedback — iteration 336 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 38.08}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,direct] lock -> grab ramp to quadrant_interior[align,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,direct] lock -> to quadrant_interior[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.716
- hider win-rate: 0.72
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.7
- doors sealed+locked at prep end: 0.75, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.25, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.24, 0.84] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@11; prep1/1:dropped@12
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.15, 0.88] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep0/1:dropped@19; prep1/0:done@19; prep1/1:dropped@20; prep1/1:dropped@31
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.56, 0.1] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; prep0/1:no_target@21; prep1/0:done@6; prep1/1:dropped@7
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.05, 0.21] | seeker 2 saw hider 1 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep0/1:done@27; prep1/0:done@15; prep1/1:dropped@16; prep1/1:no_target@25
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.85, 1.92] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep0/1:no_target@26; prep1/0:done@14; prep1/1:dropped@15; prep1/1:done@24
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.63, 0.86] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep0/1:dropped@19; prep0/1:dropped@21; prep0/1:dropped@29; prep1/0:dropped@16; prep1/0:done@18; prep1/1:dropped@19; prep1/1:no_target@20
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.21, 0.38] | seeker 3 saw hider 1 at play step 44 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@5; prep0/1:dropped@6; prep1/0:done@28; prep1/1:dropped@29; prep1/1:no_target@30
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.49, 1.49] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@23; prep0/0:dropped@26; prep1/0:dropped@18; prep1/0:done@25; prep1/1:dropped@26