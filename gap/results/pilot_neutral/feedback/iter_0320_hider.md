# Rehearsal feedback — iteration 320 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.41, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 38.08}
  role0 prep: grab box to door_block[target,door] lock release -> grab box to ramp_inside[yaw2,door] | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.727
- hider win-rate: 0.72
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 37.9
- doors sealed+locked at prep end: 0.76, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.12, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.67, 2.12] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; prep0/1:dropped@23; prep1/0:no_target@15; prep1/1:dropped@16; prep1/1:done@22
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.54, 1.84] | seeker 3 saw hider 1 at play step 45 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:no_object@21
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.06, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@2; prep0/1:dropped@3; prep0/1:done@11
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 1.34] | hiders never seen | segments: prep1/0:no_target@5; prep1/1:dropped@6; prep1/1:done@10
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.22, 0.02] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 1.05] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@23
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.7, 0.85] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@7; prep1/0:dropped@4
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.92, 1.51] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep0/1:dropped@22; prep0/1:no_object@22; prep1/0:no_target@11; prep1/1:dropped@12