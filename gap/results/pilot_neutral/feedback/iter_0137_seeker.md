# Rehearsal feedback — iteration 137 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 5.43, 'damp': 0.7, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase then grab box to opponent[target,door]
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.317
- hider win-rate: 0.28
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.09}
- mean first-seen play step: 37.0
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.78, mean max seeker z: 0.20

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.68, 0.1] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.56] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.34, 0.6] | seeker 3 saw hider 0 at play step 72 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.65, 0.89] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.43, 0.97] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.21, 0.76] | seeker 3 saw hider 1 at play step 64 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed