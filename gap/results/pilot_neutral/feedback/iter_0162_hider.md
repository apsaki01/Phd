# Rehearsal feedback — iteration 162 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.8, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to teammate[align,door] release -> [when teammate_inside] grab box to quadrant_corner[yaw3,door] lock | play: segments then to stay[yaw0,door] release -> grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to teammate[align,door] release | play: segments then grab box to outside_wall[yaw2,door] -> [when ramp_inside] grab box to quadrant_interior[yaw3,direct] lock -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.321
- hider win-rate: 0.33
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.1
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.65, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.74, 1.39] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:dropped@76; play1/0:timeout@70
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.3, 1.59] | seeker 2 saw hider 1 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@20; prep1/0:dropped@22; prep1/0:dropped@25; prep1/0:dropped@29; play1/0:dropped@66; play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.04, 1.21] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@79; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.2, 0.77] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@7; play0/0:timeout@70; play0/1:dropped@71; play1/0:done@59
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.06, 0.72] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.39, 1.17] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.16, 0.3] | seeker 2 saw hider 1 at play step 38 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:dropped@34; play0/0:done@34; play0/1:timeout@73; play0/2:dropped@74; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.69, 1.0] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:dropped@32; play0/0:done@32; play0/1:timeout@71; play0/2:dropped@72; play1/0:timeout@70