# Rehearsal feedback — iteration 200 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.678
- hider win-rate: 0.75
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.06}
- mean first-seen play step: 45.8
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.75, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.13, 0.74] | seeker 2 saw hider 1 at play step 43 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:no_target@22; play0/0:dropped@32; play0/0:dropped@58; play0/0:timeout@70; prep1/0:done@5; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.91, 0.91] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play1/0:dropped@34; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.4, 1.89] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@12; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.12, 1.74] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@22; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@13; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.9, 0.36] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; play0/0:dropped@32; play0/0:dropped@43; play0/0:timeout@70; prep1/0:no_target@12; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.17, 0.43] | seeker 3 saw hider 1 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@10; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.24, 2.5] | seeker 3 saw hider 1 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@24; play0/0:dropped@32; play0/0:dropped@35; play0/0:timeout@70; prep1/0:done@20; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.23, 1.29] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@23; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71