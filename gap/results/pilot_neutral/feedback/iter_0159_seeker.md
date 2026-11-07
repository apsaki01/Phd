# Rehearsal feedback — iteration 159 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.0, 'damp': 0.6, 'tol': 0.3, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase then [when ramp_inside] to ramp[yaw2,door] release
  role1 prep: (none) | play: chase then [when ramp_inside] grab ramp to ramp[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.240
- hider win-rate: 0.20
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.0
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.72, mean max seeker z: 0.21

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.54, 0.99] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.62, 0.42] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.49, 0.47] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.34] | seeker 2 saw hider 0 at play step 46 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.16, 0.49] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.77, 1.38] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.42, 1.93] | seeker 3 saw hider 0 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.83, 0.54] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed