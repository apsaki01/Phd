# Rehearsal feedback — iteration 334 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 38.08}
  role0 prep: grab box to door_block[target,door] lock release -> grab box to ramp_inside[yaw2,door] | play: chase then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to ramp_inside[yaw2,door] lock -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to stay[yaw3,direct] lock -> grab ramp to quadrant_interior[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.544
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.3
- doors sealed+locked at prep end: 0.74, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.25, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.78, 0.49] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@16; prep0/1:dropped@17; prep1/0:dropped@19
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[0.59, 1.04] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:no_object@15
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.0, 1.39] | seeker 3 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@8; prep0/0:done@20; prep0/1:dropped@21; prep0/1:no_object@21; prep1/0:dropped@17; prep1/0:done@25; prep1/1:dropped@26; prep1/1:no_object@26
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.31, 1.02] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; prep0/1:dropped@18; prep0/1:no_object@18; prep1/0:no_target@19; prep1/1:dropped@20; prep1/1:done@26
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.62] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@8
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.54, 0.0] | seeker 2 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@15; prep1/1:dropped@16; prep1/1:no_object@16
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.32, 1.39] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@22; prep0/1:dropped@23; prep0/1:dropped@27; prep1/0:dropped@12; prep1/0:done@20; prep1/1:dropped@21; prep1/1:no_object@21
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.8, 1.25] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@18; prep0/1:dropped@19; prep0/1:done@27; prep1/0:dropped@13; prep1/0:done@22; prep1/1:dropped@23; prep1/1:no_object@23