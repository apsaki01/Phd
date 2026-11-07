# Rehearsal feedback — iteration 332 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 38.08}
  role0 prep: grab box to door_block[target,door] lock release -> grab box to ramp_inside[yaw2,door] | play: chase then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to stay[yaw3,door] lock -> grab ramp to quadrant_interior[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.468
- hider win-rate: 0.40
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.7
- doors sealed+locked at prep end: 0.79, ramp inside quadrant at prep end: 0.30
- seekers entered quadrant: 0.23, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.0, 0.38] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@10; prep0/0:done@18; prep0/1:dropped@19; prep0/1:no_object@19
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.94, 0.82] | seeker 3 saw hider 1 at play step 56 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@12; prep1/0:no_target@15; prep1/1:dropped@16
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.27, 1.33] | hiders never seen | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:no_object@21; prep1/0:dropped@12; prep1/0:done@31
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.42, 1.49] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.63, 2.04] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@23; prep0/1:dropped@24; prep0/1:no_object@24; prep1/0:done@24; prep1/1:dropped@25; prep1/1:no_object@25
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[2.29, 0.6] | seeker 2 saw hider 0 at play step 50 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:no_object@12; prep1/0:done@20; prep1/1:dropped@21; prep1/1:no_object@21
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.05, 1.75] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@5; prep0/1:dropped@6; prep1/0:done@12; prep1/1:dropped@13; prep1/1:no_object@13