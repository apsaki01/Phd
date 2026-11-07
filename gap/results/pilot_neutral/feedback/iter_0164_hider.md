# Rehearsal feedback — iteration 164 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.8, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to teammate[align,door] release -> [when teammate_inside] grab box to quadrant_corner[yaw3,door] lock | play: segments then to stay[yaw0,door] release -> grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to teammate[align,door] release | play: segments then grab box to outside_wall[yaw2,door] -> [when ramp_inside] grab box to quadrant_interior[yaw3,direct] lock -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.298
- hider win-rate: 0.30
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 37.0
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.80, mean max seeker z: 0.20

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.38, 1.71] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@7; prep1/0:dropped@11; prep1/0:dropped@17; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.69, 0.2] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.29, 0.52] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.76, 1.19] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:done@52
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.63, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.69, 1.32] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.67, 0.99] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@18; prep0/0:dropped@21; play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.66, 0.47] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:dropped@7; play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70