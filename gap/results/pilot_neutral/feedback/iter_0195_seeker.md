# Rehearsal feedback — iteration 195 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.19, 'seg_timeout': 27.71}
  role0 prep: (none) | play: search then grab ramp to opponent[yaw0,direct] lock
  role1 prep: (none) | play: chase then grab ramp to opponent[yaw0,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.381
- hider win-rate: 0.30
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.2
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.95, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.11, 2.19] | seeker 2 saw hider 0 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.21, 1.36] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.66, 0.78] | seeker 3 saw hider 0 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.06, 0.14] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.61, 0.73] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.53, 0.92] | seeker 2 saw hider 1 at play step 52 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.65, 1.45] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.73, 1.8] | seeker 2 saw hider 1 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed