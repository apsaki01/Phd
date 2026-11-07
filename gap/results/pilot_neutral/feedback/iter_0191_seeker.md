# Rehearsal feedback — iteration 191 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.15, 'seg_timeout': 27.71}
  role0 prep: (none) | play: chase then grab ramp to opponent[yaw0,direct] lock
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.693
- hider win-rate: 0.70
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 45.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.53, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.41, 0.79] | seeker 3 saw hider 1 at play step 75 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.11, 1.5] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.48, 1.32] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.85, 0.39] | seeker 2 saw hider 0 at play step 57 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.71, 1.23] | seeker 3 saw hider 1 at play step 46 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.09, 0.63] | seeker 3 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.96, 0.62] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.97, 0.85] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed