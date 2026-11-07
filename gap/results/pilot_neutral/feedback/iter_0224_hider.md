# Rehearsal feedback — iteration 224 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.612
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.62, "ramp_use": 0.03, "ramp_defense": 0.0}
- mean first-seen play step: 35.1
- doors sealed+locked at prep end: 0.66, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.35, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.49, 1.79] | seeker 2 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@11; prep0/0:done@23; prep0/1:dropped@24; prep0/1:done@30; play0/0:dropped@32; play0/0:no_object@32; play0/1:timeout@67; prep1/0:done@24; prep1/1:dropped@25; prep1/1:done@31; play1/0:timeout@66; play1/1:dropped@67; play1/1:done@68
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.96, 1.18] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@19; prep0/1:dropped@20; prep0/1:no_target@21; play0/0:dropped@32; play0/0:timeout@66; play0/1:dropped@67; play0/1:no_target@67; prep1/0:done@17; prep1/1:dropped@18; play1/0:timeout@66; play1/1:dropped@67; play1/1:done@70
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.75, 0.28] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@66; play0/1:dropped@67; play0/1:done@75; play1/0:dropped@34; play1/0:timeout@66
- p_door=0.75 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.53, 0.78] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:done@24; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; prep1/0:dropped@21; prep1/0:dropped@24; play1/0:timeout@66; play1/1:dropped@67
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.77, 0.46] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@66; play0/1:dropped@67; play0/1:done@78; prep1/0:dropped@19; play1/0:timeout@66; play1/1:dropped@67; play1/1:done@78
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.58, 2.12] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; prep0/1:dropped@23; prep0/1:done@26; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@36; prep1/0:done@21; prep1/1:dropped@22; prep1/1:done@27; play1/0:dropped@32; play1/0:no_object@32; play1/1:done@39
- p_door=0.25 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.69, 1.52] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@16; prep0/1:dropped@17; play0/0:timeout@66; play0/1:no_target@67; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@17; play1/0:dropped@32; play1/0:timeout@66; play1/1:dropped@67
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.53, 0.69] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:done@18; play0/0:dropped@32; play0/0:timeout@66; play0/1:dropped@67; prep1/0:no_target@10; prep1/1:dropped@11; prep1/1:no_target@12; play1/0:dropped@32; play1/0:timeout@66; play1/1:dropped@67; play1/1:no_target@67