# Rehearsal feedback — iteration 345 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.53, 'tol': 0.35, 'offset': 0.21, 'seg_timeout': 26.66}
  role0 prep: (none) | play: chase
  role1 prep: (none) | play: chase then grab ramp to wander[yaw0,door] lock release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.687
- hider win-rate: 0.72
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.5
- doors sealed+locked at prep end: 0.74, ramp inside quadrant at prep end: 0.07
- seekers entered quadrant: 0.28, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.1, 0.45] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.14, 0.69] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.39, 1.17] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.93, 2.07] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.32, 0.68] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.26, 2.57] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.12, 2.16] | seeker 2 saw hider 0 at play step 50 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.65, 2.14] | seeker 3 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed