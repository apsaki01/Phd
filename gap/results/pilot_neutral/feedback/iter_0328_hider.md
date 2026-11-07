# Rehearsal feedback — iteration 328 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.41, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 38.08}
  role0 prep: grab box to door_block[target,door] lock release -> grab box to ramp_inside[yaw2,door] | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to stay[yaw3,door] lock -> grab ramp to quadrant_interior[yaw2,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.520
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.7
- doors sealed+locked at prep end: 0.68, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.35, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.01, 0.75] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.03, 0.41] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.12, 0.38] | seeker 2 saw hider 0 at play step 42 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@6; prep1/0:no_target@28; prep1/1:dropped@29
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.28] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.25, 1.15] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:no_target@10; prep1/1:dropped@11; prep1/1:done@15
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.93, 2.19] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; prep0/1:dropped@23; prep0/1:no_object@23; prep1/0:dropped@13
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.65, 2.35] | seeker 2 saw hider 0 at play step 51 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@12; prep0/1:dropped@13; prep1/0:done@17; prep1/1:dropped@18; prep1/1:no_object@18
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.01, 0.0] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed