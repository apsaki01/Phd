# Rehearsal feedback — iteration 208 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[target,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[target,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.509
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 45.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.75, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.07, 1.19] | seeker 3 saw hider 1 at play step 74 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@7; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@7; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.94, 0.7] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@15; play1/0:dropped@32; play1/0:dropped@43; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.1, 1.6] | seeker 2 saw hider 1 at play step 45 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:no_target@14; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; prep1/0:dropped@10; prep1/0:done@22; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.16, 0.15] | seeker 2 saw hider 1 at play step 46 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:no_target@2; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@5; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:no_target@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.74, 0.41] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@28; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; prep1/0:done@28; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.46, 0.04] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@76; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.33, 0.75] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@7; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; prep1/0:done@23; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@79
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.74, 1.61] | seeker 2 saw hider 1 at play step 51 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@20; prep0/0:done@31; play0/0:dropped@36; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@10; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71