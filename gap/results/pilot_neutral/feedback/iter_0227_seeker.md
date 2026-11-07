# Rehearsal feedback — iteration 227 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 5.0, 'damp': 0.4, 'tol': 0.3, 'offset': 0.25, 'seg_timeout': 35.0}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock -> [when teammate_inside] grab box to box[yaw0,direct] lock release -> [when doors_sealed] to door_block[align,door] release
  role1 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock -> [when teammate_inside] grab box to box[yaw0,direct] lock release -> [when doors_sealed] to door_block[align,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.745
- hider win-rate: 0.80
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.62, "ramp_use": 0.03, "ramp_defense": 0.0}
- mean first-seen play step: 35.4
- doors sealed+locked at prep end: 0.69, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.23, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.39, 0.55] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.33, 1.47] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.68, 0.84] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.26, 0.69] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.19, 1.78] | seeker 3 saw hider 1 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.07, 2.07] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.41, 0.72] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.25, 1.77] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed