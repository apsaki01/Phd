# Rehearsal feedback — iteration 166 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.8, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to teammate[align,door] release -> [when teammate_inside] grab box to quadrant_corner[yaw3,door] lock | play: flee then to stay[yaw0,door] release -> grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to teammate[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> [when ramp_inside] grab box to quadrant_interior[yaw3,direct] lock -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.235
- hider win-rate: 0.12
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 36.4
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.75, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.32, 1.06] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@24; play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.85, 0.14] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@14; play1/0:timeout@70
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.85, 0.84] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@8; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.84, 1.04] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@43
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.53, 0.54] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.33, 0.93] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70; play1/1:dropped@71; play1/1:done@77
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.98, 0.28] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@18; prep0/0:dropped@22; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.75, 0.05] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@8; play1/0:done@37; play1/1:timeout@76; play1/2:dropped@77