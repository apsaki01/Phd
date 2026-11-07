# Rehearsal feedback — iteration 255 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.49, 'damp': 0.38, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw1,door] release -> grab ramp to teammate[yaw3,door] lock
  role1 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw1,door] release -> grab ramp to teammate[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.635
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 35.5
- doors sealed+locked at prep end: 0.66, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.20, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.78, 0.81] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.81, 1.36] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.11, 2.2] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.52, 1.45] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.1, 1.84] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[0.37, 1.89] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.04, 2.48] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[2.01, 1.37] | hiders never seen | segments: no segments executed