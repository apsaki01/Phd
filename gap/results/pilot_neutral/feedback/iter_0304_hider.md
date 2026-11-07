# Rehearsal feedback — iteration 304 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 39.53}
  role0 prep: grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.687
- hider win-rate: 0.72
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.75, "ramp_use": 0.03, "ramp_defense": 0.03}
- mean first-seen play step: 39.6
- doors sealed+locked at prep end: 0.79, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.28, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.65, 1.18] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep1/0:done@16; prep1/1:dropped@17; prep1/1:done@27
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.33, 2.56] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep0/0:done@20; prep1/0:done@14; prep1/1:dropped@15
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.25, 2.22] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep0/0:done@22; prep1/0:done@15; prep1/1:dropped@16; prep1/1:done@27
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.01, 2.01] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@9; prep1/0:done@16; prep1/1:dropped@17; prep1/1:no_target@18
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.5, 1.76] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.69) | segments: prep0/0:done@21; prep1/0:done@6; prep1/1:dropped@7; prep1/1:done@20
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.16, 1.78] | hiders never seen | segments: prep0/0:dropped@18; prep0/0:no_object@18; prep1/0:done@10; prep1/1:dropped@11; prep1/1:dropped@23; prep1/1:no_object@23
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.66, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.16, 0.76] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed