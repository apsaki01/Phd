# Rehearsal feedback — iteration 207 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.19, 'seg_timeout': 27.71}
  role0 prep: (none) | play: chase then grab box to door_block[yaw0,direct] lock
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.563
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 41.0
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.28
- seekers entered quadrant: 0.68, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.58, 2.47] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.5, 0.97] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.88, 0.82] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.65, 0.58] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.62, 1.93] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.4, 1.24] | seeker 3 saw hider 0 at play step 73 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.86, 0.22] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.27, 0.91] | seeker 3 saw hider 1 at play step 77 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed