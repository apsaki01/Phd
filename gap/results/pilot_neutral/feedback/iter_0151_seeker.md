# Rehearsal feedback — iteration 151 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.43, 'damp': 0.7, 'tol': 0.35, 'offset': 0.12, 'seg_timeout': 29.06}
  role0 prep: (none) | play: chase then to ramp[yaw2,door] release
  role1 prep: (none) | play: chase then grab box to opponent[target,door] lock -> grab ramp to ramp[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.186
- hider win-rate: 0.15
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 34.3
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.65, mean max seeker z: 0.23

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.67, 0.92] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.16, 0.29] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[3.85, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.23, 0.0] | seeker 2 saw hider 1 at play step 47 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.45, 0.0] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.86, 0.15] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed