# Rehearsal feedback — iteration 194 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 4.94, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] | play: segments then grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.543
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 43.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.75, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.81, 0.11] | seeker 3 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@17; play1/0:dropped@32; play1/0:timeout@70
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.56, 0.9] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@26; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.04, 0.58] | seeker 2 saw hider 1 at play step 36 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@5; play0/0:dropped@32; play0/0:dropped@52; play0/0:timeout@70; play1/0:timeout@70
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.72, 1.72] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@8; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.76, 0.04] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play1/0:timeout@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.87, 0.43] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; play0/0:dropped@32; play0/0:timeout@70; prep1/0:done@22; play1/0:dropped@32; play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.47, 0.76] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@21; play0/0:dropped@32; play0/0:timeout@70; prep1/0:dropped@18; prep1/0:dropped@28; play1/0:timeout@70
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.07, 0.78] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; play0/0:dropped@32; play0/0:timeout@70; prep1/0:no_target@25; play1/0:dropped@32; play1/0:timeout@70