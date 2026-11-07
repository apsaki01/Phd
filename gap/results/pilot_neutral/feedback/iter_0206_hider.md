# Rehearsal feedback — iteration 206 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.497
- hider win-rate: 0.47
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.05
- seekers entered quadrant: 0.70, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.89, 0.63] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@7; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@21; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.2, 0.4] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@19; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@13; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.13, 0.55] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:dropped@18; prep0/0:done@25; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@21; play1/0:dropped@32; play1/0:dropped@37; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.83, 0.76] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@4; prep0/0:done@13; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@12; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.1, 1.67] | seeker 2 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@26; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.82, 1.3] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@16; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.17, 1.14] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@18; play0/0:timeout@70; prep1/0:done@26; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@77
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.48, 0.36] | seeker 3 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@27; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@27; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71