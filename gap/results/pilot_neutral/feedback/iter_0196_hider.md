# Rehearsal feedback — iteration 196 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.552
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.05, "ramp_defense": 0.0}
- mean first-seen play step: 43.9
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.88, mean max seeker z: 0.20

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.47, 0.57] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.57) | segments: prep0/0:dropped@13; prep0/0:done@21; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@16; play1/0:dropped@32; play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.94, 0.41] | seeker 2 saw hider 0 at play step 43 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@15; play1/0:dropped@32; play1/0:dropped@37; play1/0:timeout@70
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.24, 2.03] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.55) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@4; prep1/0:done@15; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.25, 2.38] | seeker 2 saw hider 0 at play step 53 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@15; prep1/0:done@31; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.12, 2.08] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; play0/0:dropped@32; play0/0:dropped@35; play0/0:timeout@70; prep1/0:done@26; play1/0:dropped@32; play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.8, 2.39] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@17; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@21; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.13, 1.34] | seeker 2 saw hider 1 at play step 73 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep0/0:done@25; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@19; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.13, 2.13] | seeker 2 saw hider 0 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@18; play1/0:dropped@32; play1/0:timeout@70