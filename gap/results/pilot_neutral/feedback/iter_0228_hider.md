# Rehearsal feedback — iteration 228 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: go(ramp_inside,door) then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[align,door] -> grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.710
- hider win-rate: 0.75
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.72, "ramp_use": 0.03, "ramp_defense": 0.0}
- mean first-seen play step: 37.0
- doors sealed+locked at prep end: 0.74, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.25, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.03, 2.0] | seeker 3 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.70) | segments: prep0/0:done@21; prep0/1:dropped@22; prep0/1:done@25; prep1/0:done@10; prep1/1:done@13; play1/0:dropped@32; play1/0:no_object@32; play1/1:done@34
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.6, 0.71] | seeker 2 saw hider 0 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:done@24; prep1/0:no_target@18; prep1/1:dropped@19; prep1/1:no_target@20; play1/0:dropped@32; play1/0:timeout@66; play1/1:dropped@67; play1/1:no_target@67
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.84, 0.3] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:no_target@7; prep1/1:dropped@8; prep1/1:no_target@11; play1/0:dropped@32; play1/0:timeout@66; play1/1:dropped@67; play1/1:no_target@67
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.26, 1.5] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:done@12; prep1/0:done@18; prep1/1:done@21; play1/0:dropped@32; play1/0:no_object@32; play1/1:timeout@67
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.55, 1.15] | seeker 2 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep1/0:no_target@17; prep1/1:dropped@18; prep1/1:no_target@19; play1/0:dropped@32; play1/0:timeout@66; play1/1:dropped@67; play1/1:no_target@67
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.07, 0.9] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; prep1/0:no_target@21; prep1/1:dropped@22; prep1/1:no_target@27; play1/0:dropped@32; play1/0:timeout@66; play1/1:dropped@67; play1/1:no_target@67
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.08, 0.0] | seeker 2 saw hider 0 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@66; play1/1:dropped@67; play1/1:done@75
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.08, 0.04] | seeker 3 saw hider 1 at play step 55 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play1/0:timeout@66; play1/1:dropped@67