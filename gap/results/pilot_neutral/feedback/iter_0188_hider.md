# Rehearsal feedback — iteration 188 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.26, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock -> grab box to outside_wall[yaw2,door]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.517
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 41.4
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.65, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.67, 0.52] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@3; prep0/0:done@18; play0/0:dropped@32; play0/0:dropped@37; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@15; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.07, 0.14] | seeker 2 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; play0/0:dropped@32; play0/0:dropped@37; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@20; play1/0:dropped@32; play1/0:dropped@35; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.09, 1.14] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@9; prep0/0:done@14; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@17; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.71, 0.9] | seeker 2 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@21; play0/0:dropped@32; play0/0:dropped@50; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@9; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.42, 1.87] | seeker 2 saw hider 0 at play step 49 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep0/0:done@15; play0/0:dropped@32; play0/0:dropped@35; play0/0:dropped@38; play0/0:done@42; prep1/0:dropped@13; prep1/0:dropped@16; prep1/0:done@26; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.01, 1.26] | seeker 3 saw hider 1 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:done@37; play0/1:timeout@76; prep1/0:done@12; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.65, 0.15] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:dropped@36; play0/0:timeout@70; play0/1:dropped@71; play1/0:dropped@36; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.79, 0.24] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:done@55; prep1/0:no_target@26; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:dropped@74; play1/1:dropped@77