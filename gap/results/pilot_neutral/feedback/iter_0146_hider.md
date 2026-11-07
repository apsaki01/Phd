# Rehearsal feedback — iteration 146 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.65, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 38.83}
  role0 prep: grab box to teammate[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to teammate[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.297
- hider win-rate: 0.25
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 35.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.62, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.69, 0.64] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:done@55
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.38, 1.26] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.07, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@36; play0/1:timeout@75; play0/2:dropped@76; play1/0:timeout@70; play1/1:done@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.95, 1.15] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.2, 1.76] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play0/2:dropped@76; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.89, 1.23] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@41; play1/0:done@41
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.79, 1.36] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:dropped@34; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:done@41
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.05, 0.2] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71