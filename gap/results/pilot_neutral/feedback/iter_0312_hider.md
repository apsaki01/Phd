# Rehearsal feedback — iteration 312 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 39.53}
  role0 prep: grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.639
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.5
- doors sealed+locked at prep end: 0.66, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.30, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.02, 2.02] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep1/0:done@22; prep1/1:dropped@23
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.3, 0.16] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.01, 1.1] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@15
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.79, 1.93] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; prep1/0:done@15; prep1/1:dropped@16; prep1/1:dropped@28
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.26, 0.87] | seeker 3 saw hider 1 at play step 46 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:no_target@17; prep1/0:done@9; prep1/1:dropped@10
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.12, 1.15] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep1/0:dropped@6; prep1/0:done@14; prep1/1:dropped@15; prep1/1:done@26
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.07, 1.12] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@24; prep1/0:done@16; prep1/1:dropped@17
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.8, 1.24] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@17; prep1/0:done@10; prep1/1:dropped@11