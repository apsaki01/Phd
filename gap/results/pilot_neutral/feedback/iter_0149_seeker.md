# Rehearsal feedback — iteration 149 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.43, 'damp': 0.7, 'tol': 0.37, 'offset': 0.12, 'seg_timeout': 29.06}
  role0 prep: (none) | play: chase then grab box to opponent[target,door] lock -> grab ramp to ramp[yaw2,door] release
  role1 prep: (none) | play: chase then grab box to opponent[target,door] lock -> grab ramp to ramp[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.272
- hider win-rate: 0.28
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 33.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.57, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.5, 1.57] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.41, 1.09] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.04, 1.73] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.77, 0.0] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[4.28, 0.29] | seeker 2 saw hider 1 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.65, 0.08] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 1.7] | hiders never seen | segments: no segments executed