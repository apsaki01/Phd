# Rehearsal feedback — iteration 204 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.413
- hider win-rate: 0.40
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.12}
- mean first-seen play step: 38.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.82, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.02, 1.92] | seeker 2 saw hider 1 at play step 54 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@31; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.32, 2.36] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@20; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@12; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.68, 3.22] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@14; prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@2; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.52, 0.5] | seeker 2 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:no_target@11; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@11; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.11, 1.9] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@21; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@22; prep1/0:dropped@25; prep1/0:dropped@29; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.83, 0.58] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@17; prep0/0:done@27; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@28; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.32, 1.46] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@18; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play1/0:timeout@70; play1/1:no_target@71