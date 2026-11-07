# Rehearsal feedback — iteration 205 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.19, 'seg_timeout': 27.71}
  role0 prep: (none) | play: chase then grab box to door_block[yaw0,direct] lock
  role1 prep: (none) | play: chase then grab ramp to opponent[yaw0,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.517
- hider win-rate: 0.47
- behaviour detection rates: {"chasing": 0.23, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 44.1
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.72, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.23, 2.63] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.51, 1.92] | seeker 3 saw hider 0 at play step 46 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.51, 0.75] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.39, 1.24] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.29, 1.55] | seeker 3 saw hider 1 at play step 75 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.39, 0.88] | seeker 3 saw hider 1 at play step 76 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.27, 0.45] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.47, 1.04] | seeker 3 saw hider 0 at play step 77 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed