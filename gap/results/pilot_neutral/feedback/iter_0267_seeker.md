# Rehearsal feedback — iteration 267 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 3.49, 'damp': 0.38, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then to quadrant_interior[target,door] lock release -> grab ramp to teammate[yaw3,door] lock release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.610
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 39.4
- doors sealed+locked at prep end: 0.65, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.28, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.38, 0.57] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.12, 1.06] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.72, 2.55] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.0, 1.66] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.3, 0.61] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.01, 1.42] | seeker 3 saw hider 1 at play step 50 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.18, 0.79] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.56, 0.93] | hiders never seen | segments: no segments executed