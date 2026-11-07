# Rehearsal feedback — iteration 322 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.41, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 38.08}
  role0 prep: grab box to door_block[target,door] lock release -> grab box to ramp_inside[yaw2,door] | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.553
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.6
- doors sealed+locked at prep end: 0.79, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.25, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.36, 0.38] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@4; prep0/1:dropped@5; prep0/1:done@14; prep1/0:done@17; prep1/1:dropped@18; prep1/1:no_object@18
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.81, 0.0] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@9
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.73, 0.63] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep0/1:no_object@14
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.75, 1.37] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; prep0/1:dropped@18; prep0/1:no_object@18; prep1/0:done@20; prep1/1:dropped@21; prep1/1:no_object@21
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.54, 0.0] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@7
- p_door=0.25 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.06, 1.79] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@18; prep0/1:dropped@19; prep1/0:done@22; prep1/1:dropped@23; prep1/1:no_object@23
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.39, 0.0] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.11, 0.77] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@13; prep1/1:dropped@14; prep1/1:no_object@14