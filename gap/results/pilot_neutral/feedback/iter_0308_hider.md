# Rehearsal feedback — iteration 308 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 39.53}
  role0 prep: grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.639
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 39.6
- doors sealed+locked at prep end: 0.75, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.25, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[2.09, 3.7] | seeker 3 saw hider 0 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.27, 0.59] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep1/0:done@17; prep1/1:dropped@18
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.22, 0.0] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.62, 0.34] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:no_target@16; prep1/0:done@1; prep1/1:dropped@2; prep1/1:dropped@6; prep1/1:done@18
- p_door=0.75 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.31, 1.24] | seeker 2 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@13; prep0/0:done@21; prep1/0:done@12; prep1/1:dropped@13
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[0.83, 0.13] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@10; prep0/0:dropped@21; prep1/0:done@18; prep1/1:dropped@19; prep1/1:done@29
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.96, 1.41] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep1/0:done@17; prep1/1:dropped@18; prep1/1:no_target@19
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.56, 0.32] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@11; prep1/1:dropped@12