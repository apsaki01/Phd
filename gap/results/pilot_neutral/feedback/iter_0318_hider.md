# Rehearsal feedback — iteration 318 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.69, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 39.53}
  role0 prep: grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.560
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.06}
- mean first-seen play step: 37.6
- doors sealed+locked at prep end: 0.72, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.23, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.47, 1.02] | seeker 2 saw hider 0 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep1/0:dropped@13
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.7, 2.39] | seeker 3 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep1/0:done@22; prep1/1:dropped@23; prep1/1:no_object@23
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.85, 1.6] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@8; prep1/0:done@19; prep1/1:dropped@20; prep1/1:done@24
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.95, 2.07] | seeker 3 saw hider 1 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep1/0:done@20; prep1/1:dropped@21; prep1/1:no_object@21
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.19, 0.23] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@19; prep1/0:dropped@18
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.24, 1.47] | seeker 2 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep1/0:no_target@19; prep1/1:dropped@20; prep1/1:done@24
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[2.18, 0.79] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@16; prep0/0:done@25; prep1/0:done@17; prep1/1:dropped@18; prep1/1:no_object@18
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.36, 0.27] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed