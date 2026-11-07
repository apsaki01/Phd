# Rehearsal feedback — iteration 174 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.94, 'damp': 0.8, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then [when ramp_inside] grab box to quadrant_interior[yaw3,direct] lock -> grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.512
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.2
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.60, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.27, 2.22] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@11; prep1/0:done@16; play1/0:dropped@32; play1/0:done@42
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.62, 1.19] | seeker 3 saw hider 1 at play step 36 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep0/0:dropped@19; prep0/0:done@23; play0/0:dropped@32; play0/0:done@45; prep1/0:dropped@17; prep1/0:done@23; play1/0:dropped@32; play1/0:done@35; play1/1:timeout@74
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.37, 0.86] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@15; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@76; prep1/0:done@20; play1/0:dropped@32; play1/0:done@42
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.56, 0.21] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@15; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@14; prep1/0:dropped@19; prep1/0:dropped@23; prep1/0:done@29; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.51, 0.26] | seeker 3 saw hider 1 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@7; prep0/0:done@18; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@23; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.69, 2.17] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@7; play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:dropped@75
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.93, 1.55] | seeker 3 saw hider 1 at play step 47 (hider inside quadrant, seeker outside, seeker z=0.58) | segments: prep0/0:done@12; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@12; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.72, 0.63] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71