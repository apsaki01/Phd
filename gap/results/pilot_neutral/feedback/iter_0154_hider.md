# Rehearsal feedback — iteration 154 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.68, 'tol': 0.33, 'offset': 0.19, 'seg_timeout': 38.83}
  role0 prep: (none) | play: go(ramp_inside,door) then grab box to outside_wall[align,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to teammate[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.349
- hider win-rate: 0.35
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 35.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.80, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.96, 0.42] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@39; play1/1:timeout@78; play1/2:dropped@79
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.16, 1.62] | seeker 2 saw hider 0 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@39; play1/1:timeout@78; play1/2:dropped@79
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.66, 0.54] | seeker 3 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.19, 1.73] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.08, 0.25] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@14; play1/0:done@62
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.72, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 2.08] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: play1/0:dropped@34; play1/0:dropped@38; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.83, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:done@50