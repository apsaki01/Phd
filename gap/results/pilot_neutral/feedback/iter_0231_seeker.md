# Rehearsal feedback — iteration 231 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.63, 'damp': 0.4, 'tol': 0.3, 'offset': 0.25, 'seg_timeout': 35.0}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock -> grab box to teammate[target,door] lock -> [when doors_sealed] to door_block[align,door] release
  role1 prep: (none) | play: chase then [when doors_sealed] to door_block[align,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.504
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.23, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.7
- doors sealed+locked at prep end: 0.72, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.25, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.17, 0.39] | seeker 3 saw hider 0 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.31, 0.71] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.64, 1.51] | seeker 3 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.94, 1.64] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.78, 0.7] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[3.1, 1.47] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.25, 0.38] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.8, 3.0] | hiders never seen | segments: no segments executed