# Rehearsal feedback — iteration 229 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.22, 'damp': 0.4, 'tol': 0.3, 'offset': 0.25, 'seg_timeout': 35.0}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock -> [when doors_sealed] to door_block[align,door] release
  role1 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock -> [when doors_sealed] to door_block[align,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.680
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.7
- doors sealed+locked at prep end: 0.68, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.23, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.65, 0.57] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.88, 1.64] | seeker 3 saw hider 1 at play step 45 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.93, 2.03] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.92, 0.91] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.26, 0.87] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.6, 2.07] | seeker 3 saw hider 0 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.48, 1.17] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.64, 0.35] | hiders never seen | segments: no segments executed