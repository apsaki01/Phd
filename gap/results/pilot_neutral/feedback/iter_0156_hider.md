# Rehearsal feedback — iteration 156 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.68, 'tol': 0.33, 'offset': 0.19, 'seg_timeout': 38.83}
  role0 prep: (none) | play: go(ramp_inside,door) then grab box to outside_wall[align,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to teammate[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.264
- hider win-rate: 0.17
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.4
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.82, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.34, 0.0] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.62, 2.25] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.99, 0.85] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@18; play1/0:dropped@34; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.11, 1.92] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@42
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 2.16] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.87, 0.26] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@39; play1/1:timeout@78; play1/2:dropped@79
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.44, 0.0] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.81] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@57