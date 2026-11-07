# Rehearsal feedback — iteration 261 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.49, 'damp': 0.38, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then grab ramp to teammate[yaw3,door] lock
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.549
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.57, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 41.7
- doors sealed+locked at prep end: 0.62, ramp inside quadrant at prep end: 0.05
- seekers entered quadrant: 0.28, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.9, 2.64] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.39, 2.06] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.3, 1.93] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.41, 1.89] | seeker 3 saw hider 0 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.89, 1.46] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.53, 1.92] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.41, 1.85] | seeker 2 saw hider 0 at play step 64 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.36, 1.07] | hiders never seen | segments: no segments executed