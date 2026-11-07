# Rehearsal feedback — iteration 30 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 6.0, 'damp': 0.4, 'tol': 0.32, 'offset': 0.4, 'seg_timeout': 36.09}
  role0 prep: [when doors_sealed] grab box to box[align,direct] lock | play: search
  role1 prep: grab ramp to ramp_inside[yaw3,direct] release -> [when doors_sealed] grab box to box[align,direct] lock | play: search then grab box to door_block[yaw3,door] lock release -> [when teammate_inside] grab box to teammate[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.182
- hider win-rate: 0.05
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.23}
- mean first-seen play step: 33.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.42
- seekers entered quadrant: 0.68, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.6, 1.16] | seeker 2 saw hider 1 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.71] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@26
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.37] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@28
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@12
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.14) | segments: no segments executed