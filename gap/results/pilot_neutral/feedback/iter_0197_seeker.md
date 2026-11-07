# Rehearsal feedback — iteration 197 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.19, 'seg_timeout': 27.71}
  role0 prep: (none) | play: search then grab ramp to opponent[yaw0,direct] lock
  role1 prep: (none) | play: chase then grab ramp to opponent[yaw0,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.606
- hider win-rate: 0.70
- behaviour detection rates: {"chasing": 0.0, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 41.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.95, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.2, 1.58] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.63, 0.88] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.25, 0.08] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.88, 0.44] | seeker 2 saw hider 1 at play step 44 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[2.09, 0.16] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.57, 2.21] | seeker 3 saw hider 1 at play step 50 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.82, 1.97] | seeker 2 saw hider 0 at play step 47 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.75, 1.42] | seeker 2 saw hider 1 at play step 47 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed