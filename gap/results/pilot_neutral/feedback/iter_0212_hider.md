# Rehearsal feedback — iteration 212 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.77, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[target,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[target,door] | play: segments then grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.537
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 44.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.70, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.32, 2.28] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@21; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.94, 0.65] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@7; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@15; prep1/0:done@21; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.62, 0.01] | seeker 3 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.48, 2.45] | seeker 3 saw hider 1 at play step 47 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:no_target@17; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; prep1/0:dropped@17; prep1/0:done@30; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.31, 2.3] | seeker 3 saw hider 1 at play step 43 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@29; play1/0:dropped@32; play1/0:dropped@35; play1/0:timeout@70
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[2.48, 2.27] | seeker 2 saw hider 1 at play step 53 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@13; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.07, 0.56] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@2; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@9; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.16, 2.33] | seeker 2 saw hider 0 at play step 41 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@14; prep1/0:dropped@17; prep1/0:done@30; play1/0:dropped@32; play1/0:timeout@70