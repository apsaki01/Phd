# Rehearsal feedback — iteration 314 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.69, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 39.53}
  role0 prep: grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.616
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.28, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.7
- doors sealed+locked at prep end: 0.79, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.28, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.58, 2.31] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.96, 1.53] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:no_target@10; prep1/1:dropped@11
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.44, 1.28] | seeker 3 saw hider 1 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep1/0:done@13; prep1/1:dropped@14; prep1/1:no_object@14
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.76, 0.74] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; prep1/0:dropped@15
- p_door=0.75 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.46, 0.34] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep1/0:dropped@10
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 1.03] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@3
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.47, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.26, 0.76] | seeker 2 saw hider 1 at play step 60 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@24; prep1/0:done@13; prep1/1:dropped@14; prep1/1:no_object@14