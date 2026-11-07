# Rehearsal feedback — iteration 259 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.49, 'damp': 0.38, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then grab ramp to teammate[yaw3,door] lock -> [when ramp_inside] to teammate[yaw1,door] release
  role1 prep: (none) | play: search then grab ramp to teammate[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.616
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.68, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.2
- doors sealed+locked at prep end: 0.74, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.33, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.92, 1.67] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.83, 0.6] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.26, 0.41] | seeker 2 saw hider 0 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[3.0, 0.44] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.42, 0.62] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.69, 1.85] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.25, 1.53] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.99, 1.85] | hiders never seen | segments: no segments executed