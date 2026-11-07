# Rehearsal feedback — iteration 182 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.75, 'tol': 0.26, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.465
- hider win-rate: 0.45
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.0
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.55, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.2, 1.39] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@10; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.95, 0.52] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@18; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@8; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.13, 0.54] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@11; prep0/0:done@12; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@4; prep1/0:done@15; play1/0:dropped@32; play1/0:dropped@42; play1/0:done@46
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.81, 0.58] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@15; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@13; prep1/0:done@20; play1/0:dropped@32; play1/0:dropped@36; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.49, 1.75] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@12; prep0/0:done@21; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@8; prep1/0:done@21; play1/0:dropped@32; play1/0:dropped@50; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.34, 0.04] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@15; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@12; prep1/0:done@19; play1/0:dropped@32; play1/0:done@52
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.37, 2.0] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.16, 1.21] | seeker 3 saw hider 1 at play step 46 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@18; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71