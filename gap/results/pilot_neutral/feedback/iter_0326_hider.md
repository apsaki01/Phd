# Rehearsal feedback — iteration 326 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.41, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 38.08}
  role0 prep: grab box to door_block[target,door] lock release -> grab box to ramp_inside[yaw2,door] | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to stay[yaw3,door] lock -> grab ramp to quadrant_interior[yaw2,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.667
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.75, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.8
- doors sealed+locked at prep end: 0.78, ramp inside quadrant at prep end: 0.28
- seekers entered quadrant: 0.23, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.61, 0.0] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:no_object@12
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.77, 1.2] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; prep0/1:no_object@17; prep1/0:dropped@12; prep1/0:done@21; prep1/1:dropped@22; prep1/1:no_object@22
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.35, 1.21] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@17
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.0, 0.55] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@12; prep1/1:dropped@13; prep1/1:no_object@13
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.14, 1.45] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@17; prep1/0:no_target@22; prep1/1:dropped@23; prep1/1:done@28
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[2.6, 0.84] | seeker 2 saw hider 0 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@17; prep0/1:dropped@18; prep1/0:done@22; prep1/1:dropped@23
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.69, 1.25] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; prep0/1:dropped@24; prep0/1:no_object@24; prep1/0:dropped@15; prep1/0:done@27; prep1/1:dropped@28; prep1/1:no_object@28
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.29, 2.39] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@11; prep0/0:done@23; prep0/1:dropped@24; prep1/0:no_target@15; prep1/1:dropped@16; prep1/1:dropped@19; prep1/1:done@23