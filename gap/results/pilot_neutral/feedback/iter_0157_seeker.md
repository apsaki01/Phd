# Rehearsal feedback — iteration 157 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.0, 'damp': 0.6, 'tol': 0.3, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase then [when ramp_inside] to ramp[yaw2,door] release
  role1 prep: (none) | play: chase then [when doors_sealed] grab box to opponent[target,door] lock -> [when ramp_inside] grab ramp to ramp[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.367
- hider win-rate: 0.35
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.70, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.87, 1.3] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.09, 1.17] | seeker 2 saw hider 0 at play step 78 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.98, 0.16] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.26, 1.26] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.47, 1.1] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.36, 0.52] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.95, 0.22] | seeker 2 saw hider 1 at play step 52 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.68, 0.76] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed