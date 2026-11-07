# Rehearsal feedback — iteration 178 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.75, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.454
- hider win-rate: 0.40
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 40.7
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.57, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.05, 2.56] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@10; prep0/0:done@13; play0/0:dropped@32; play0/0:dropped@48; play0/0:done@53; prep1/0:no_target@6; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.94, 0.49] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@4; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@13; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.64, 0.85] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; play0/0:dropped@32; play0/0:done@39; play0/1:timeout@78; prep1/0:done@11; play1/0:dropped@32; play1/0:dropped@34; play1/0:done@35; play1/1:timeout@74
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.62, 1.95] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@22; prep0/0:done@29; play0/0:dropped@32; play0/0:done@38; play0/1:timeout@77; prep1/0:done@22; play1/0:dropped@32; play1/0:done@36; play1/1:timeout@75
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play1/0:timeout@70
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.22, 0.43] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; play0/0:dropped@32; play0/0:dropped@41; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@14; prep1/0:done@25; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.34, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; prep1/0:done@22; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.78, 0.44] | seeker 3 saw hider 1 at play step 48 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; play0/0:dropped@32; play0/0:done@38; play0/1:timeout@77; prep1/0:no_target@15; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71