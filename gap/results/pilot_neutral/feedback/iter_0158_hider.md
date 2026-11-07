# Rehearsal feedback — iteration 158 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.68, 'tol': 0.33, 'offset': 0.19, 'seg_timeout': 38.83}
  role0 prep: grab box to teammate[align,door] release | play: segments then grab box to outside_wall[yaw2,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to teammate[align,door] release | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.322
- hider win-rate: 0.23
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.9
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.65, mean max seeker z: 0.21

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.88, 1.01] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 1.96] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@38; play0/1:timeout@77; play0/2:dropped@78; play1/0:done@57
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.54, 0.14] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:dropped@13; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.43, 1.47] | seeker 2 saw hider 0 at play step 51 (hider inside quadrant, seeker outside, seeker z=0.17) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:done@44
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.75] | seeker 3 saw hider 0 at play step 42 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@41; play1/0:dropped@42; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.1, 0.75] | seeker 3 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@18; play0/0:done@40; play0/1:timeout@79; prep1/0:dropped@30; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.14, 1.64] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.65, 0.41] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@42; play1/0:timeout@70; play1/1:dropped@71