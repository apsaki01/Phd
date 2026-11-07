# Rehearsal feedback — iteration 180 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.75, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.451
- hider win-rate: 0.47
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.55, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.68, 0.68] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@7; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@12; play1/0:dropped@32; play1/0:dropped@52; play1/0:timeout@70; play1/1:dropped@71; play1/1:dropped@74
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.76, 1.06] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@15; prep0/0:done@21; play0/0:dropped@32; play0/0:done@62; prep1/0:done@18; play1/0:dropped@32; play1/0:done@38; play1/1:timeout@77
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.41, 0.47] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@7; prep0/0:done@8; play0/0:dropped@32; play0/0:done@49; prep1/0:done@8; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.79, 2.35] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; play0/0:dropped@32; play0/0:dropped@58; play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@19; play1/0:dropped@32; play1/0:done@39; play1/1:timeout@78
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.55, 0.0] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: play0/0:dropped@34; play0/0:done@42; prep1/0:done@21; play1/0:dropped@32; play1/0:done@65
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.25, 0.49] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:done@42; prep1/0:done@18; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.76, 2.1] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; play0/0:dropped@32; play0/0:done@38; play0/1:timeout@77; prep1/0:dropped@9; prep1/0:done@18; play1/0:dropped@32; play1/0:done@39; play1/1:timeout@78
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.03, 1.11] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:done@38; play0/1:timeout@77; prep1/0:no_target@14; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71