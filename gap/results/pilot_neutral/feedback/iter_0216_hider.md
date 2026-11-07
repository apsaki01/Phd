# Rehearsal feedback — iteration 216 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.77, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[target,door] lock -> [when opponent_visible] to opponent[yaw2,door] release | play: segments
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.594
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.33, "door_blocking": 0.62, "ramp_use": 0.03, "ramp_defense": 0.0}
- mean first-seen play step: 36.8
- doors sealed+locked at prep end: 0.68, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.17, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.09, 2.13] | seeker 3 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@4; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@13
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.82, 0.14] | seeker 3 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@12; prep1/1:dropped@14
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.72, 2.19] | seeker 2 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; prep1/0:done@24
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.19, 2.23] | seeker 3 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@11; play0/0:timeout@70; play0/1:dropped@71; prep1/0:no_target@19; prep1/1:dropped@20
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.04] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@79; prep1/0:no_target@5
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.87, 2.03] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@13; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:no_target@71; prep1/0:dropped@7; prep1/0:dropped@12; prep1/0:dropped@15; prep1/0:done@29
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.72] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.16, 1.27] | seeker 2 saw hider 1 at play step 53 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@31; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@79; prep1/0:dropped@14