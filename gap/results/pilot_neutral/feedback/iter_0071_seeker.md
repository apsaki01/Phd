# Rehearsal feedback — iteration 71 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 5.0, 'damp': 0.6, 'tol': 0.3, 'offset': 0.2, 'seg_timeout': 20.0}
  role0 prep: (none) | play: segments then [when door] to door_block[yaw0,door] lock -> grab box to ramp[yaw2,direct] lock release -> [when doors_sealed] grab box to ramp[yaw3,door] lock release -> [when ramp_inside] to quadrant_corner[target,direct]
  role1 prep: (none) | play: chase then [when door] to door_block[yaw0,door] lock -> [when doors_sealed] grab box to ramp[yaw3,door] lock release -> [when ramp_inside] to quadrant_corner[target,direct] -> [when opponent_visible] to outside_wall[yaw0,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.359
- hider win-rate: 0.33
- behaviour detection rates: {"chasing": 0.23, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.28}
- mean first-seen play step: 34.4
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.42
- seekers entered quadrant: 0.85, mean max seeker z: 0.20

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@33; play0/1:timeout@54; play0/2:timeout@75; play0/3:dropped@76
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@46; play0/1:done@61
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 45 (hider outside quadrant, seeker inside, seeker z=0.15) | segments: play0/0:done@44; play0/1:timeout@65
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@46; play0/1:timeout@67
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.07, 0.3] | seeker 3 saw hider 1 at play step 36 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@42; play0/1:timeout@63
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@46; play0/1:timeout@67
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.06, 0.76] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@47; play0/1:dropped@51; play0/1:dropped@62; play0/1:timeout@68
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@52; play0/1:timeout@73