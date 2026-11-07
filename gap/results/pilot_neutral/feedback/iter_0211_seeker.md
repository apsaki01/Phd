# Rehearsal feedback — iteration 211 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.19, 'seg_timeout': 27.71}
  role0 prep: (none) | play: chase
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.572
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 44.1
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.80, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.24, 0.72] | seeker 2 saw hider 0 at play step 37 (hider outside quadrant, seeker outside, seeker z=0.14) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.19, 0.97] | seeker 3 saw hider 0 at play step 74 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.28, 0.18] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.05, 1.27] | seeker 2 saw hider 0 at play step 73 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.2, 0.64] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.19, 2.41] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.19, 0.84] | seeker 2 saw hider 0 at play step 51 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.62, 2.45] | seeker 3 saw hider 1 at play step 42 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed