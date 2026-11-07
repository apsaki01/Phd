# Rehearsal feedback — iteration 237 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.63, 'damp': 0.4, 'tol': 0.3, 'offset': 0.25, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock
  role1 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.549
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 35.8
- doors sealed+locked at prep end: 0.59, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.20, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.23, 0.77] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.64, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.16, 0.92] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.96, 0.87] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 1.89] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.71, 1.52] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.11, 1.81] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.52, 1.17] | hiders never seen | segments: no segments executed