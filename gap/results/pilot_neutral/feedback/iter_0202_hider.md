# Rehearsal feedback — iteration 202 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.563
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 40.3
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.85, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.77, 1.05] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@20; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.24, 1.27] | seeker 2 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@18; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.82, 0.05] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@21; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@14; prep1/0:done@27; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@78
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.48, 2.39] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; play0/0:dropped@32; play0/0:dropped@43; play0/0:timeout@70; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.87, 2.0] | hiders never seen | segments: prep0/0:done@17; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@15; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.72, 2.16] | seeker 3 saw hider 1 at play step 50 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@22; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.89, 1.56] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@21; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.5, 0.81] | seeker 2 saw hider 0 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:no_target@22; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@16; prep1/0:dropped@19; play1/0:timeout@70; play1/1:dropped@71