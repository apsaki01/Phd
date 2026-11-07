# Rehearsal feedback — iteration 247 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 3.5, 'damp': 0.38, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw1,door]
  role1 prep: (none) | play: chase then grab box to door_block[yaw0,direct] lock release -> [when ramp_inside] to teammate[yaw1,door]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.572
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.7, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.7
- doors sealed+locked at prep end: 0.75, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.17, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.31, 1.35] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.09, 1.31] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.96, 1.01] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[2.21, 0.56] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.81, 2.39] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.94, 2.38] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.18, 1.19] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.33, 0.24] | hiders never seen | segments: no segments executed