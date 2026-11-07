# Rehearsal feedback — iteration 170 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.94, 'damp': 0.8, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to teammate[align,door] release -> [when teammate_inside] grab box to quadrant_corner[yaw3,door] lock | play: flee then to stay[yaw0,door] release -> grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to teammate[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> [when ramp_inside] grab box to quadrant_interior[yaw3,direct] lock -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.364
- hider win-rate: 0.35
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.7
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.75, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.82, 0.92] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.3, 0.82] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:dropped@34; play1/0:done@59
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.56, 0.35] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@39; play1/1:timeout@78; play1/2:dropped@79
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.74, 0.54] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@29; play1/0:dropped@41; play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.25, 0.54] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.04, 0.38] | seeker 2 saw hider 0 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@17; play1/0:done@41
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.5, 0.71] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.96, 1.13] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@11; prep0/0:dropped@15; play1/0:timeout@70; play1/1:dropped@71