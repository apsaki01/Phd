# Rehearsal feedback — iteration 176 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.94, 'damp': 0.8, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then [when ramp_inside] grab box to quadrant_interior[yaw3,direct] lock -> grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.530
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.47, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.0, 0.52] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.52, 1.72] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@18; play1/0:dropped@32; play1/0:dropped@35; play1/0:done@39; play1/1:timeout@78
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.64, 1.69] | seeker 2 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@24; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@19; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.11, 0.33] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.38, 1.06] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@10; prep0/0:done@15; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@14; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.21, 1.91] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@23; play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.41, 1.51] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; play0/0:dropped@32; play0/0:done@44; prep1/0:no_target@26; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71