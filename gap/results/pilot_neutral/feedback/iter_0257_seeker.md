# Rehearsal feedback — iteration 257 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.49, 'damp': 0.38, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then grab ramp to teammate[yaw3,door] lock -> [when ramp_inside] to teammate[yaw1,door] release
  role1 prep: (none) | play: search then grab ramp to teammate[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.587
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 37.1
- doors sealed+locked at prep end: 0.65, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.35, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.95, 2.24] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.84, 1.62] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.15, 1.39] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.53, 0.95] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.23, 1.89] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.44, 0.64] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.65, 0.66] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.06, 0.94] | hiders never seen | segments: no segments executed