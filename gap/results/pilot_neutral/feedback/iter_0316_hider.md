# Rehearsal feedback — iteration 316 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.69, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 39.53}
  role0 prep: grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.616
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.23, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.9
- doors sealed+locked at prep end: 0.70, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.28, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.82, 0.77] | seeker 3 saw hider 0 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@10; prep0/0:done@18; prep1/0:no_target@9; prep1/1:dropped@10; prep1/1:done@13
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.01, 0.97] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.77, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@12
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.54, 0.34] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.99, 2.59] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.56, 1.73] | hiders never seen | segments: prep0/0:done@21; prep1/0:dropped@15; prep1/0:done@27; prep1/1:dropped@28; prep1/1:no_object@28
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.47, 2.22] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; prep1/0:dropped@14; prep1/0:done@24; prep1/1:dropped@25; prep1/1:no_object@25
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.73, 0.78] | seeker 3 saw hider 0 at play step 55 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@25; prep1/0:done@26; prep1/1:dropped@27; prep1/1:no_object@27