# Rehearsal feedback — iteration 263 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.49, 'damp': 0.38, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then grab ramp to teammate[yaw3,door] lock
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.535
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.7
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.33, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.75 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.31, 2.18] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[2.0, 1.83] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.34, 1.81] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.7, 0.69] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.48, 0.73] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.35, 0.76] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.34, 1.04] | seeker 3 saw hider 0 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.35, 2.04] | hiders never seen | segments: no segments executed