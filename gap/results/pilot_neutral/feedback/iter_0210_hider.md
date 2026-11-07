# Rehearsal feedback — iteration 210 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.77, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[target,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[target,door] | play: segments then grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.580
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.03, "ramp_defense": 0.04}
- mean first-seen play step: 41.1
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.33
- seekers entered quadrant: 0.82, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.61, 1.33] | seeker 3 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@17; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@15; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.11, 0.41] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@30; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; prep1/0:done@14; play1/0:dropped@32; play1/0:dropped@38; play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.73, 0.0] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:dropped@42; play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.08, 0.41] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.8, 1.28] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@10; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; prep1/0:done@10; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.36, 0.57] | seeker 2 saw hider 1 at play step 62 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@76; prep1/0:done@11; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.97, 1.46] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@24; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@30; play1/0:dropped@32; play1/0:dropped@35; play1/0:dropped@41; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.87, 1.79] | seeker 2 saw hider 1 at play step 53 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@14; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@17; prep1/0:dropped@21; prep1/0:done@30; play1/0:dropped@32; play1/0:timeout@70