# Rehearsal feedback — iteration 126 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.52, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 38.83}
  role0 prep: [when ramp_inside] grab ramp to climb[align,door] release | play: segments then to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
  role1 prep: [when ramp_inside] grab ramp to climb[align,door] release | play: segments then to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.306
- hider win-rate: 0.28
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.2
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.90, mean max seeker z: 0.21

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.42] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; play0/0:dropped@32; play0/0:done@32; play0/1:timeout@71; prep1/0:no_object@0; play1/0:done@32; play1/1:timeout@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 39 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play1/0:done@32; play1/1:timeout@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play1/0:done@32; play1/1:timeout@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play1/0:done@32; play1/1:timeout@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play1/0:done@32; play1/1:dropped@50; play1/1:timeout@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play1/0:done@32; play1/1:timeout@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.04, 1.14] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; play0/0:dropped@32; play0/0:done@32; play0/1:timeout@71; prep1/0:no_object@0; play1/0:done@32; play1/1:done@38
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:dropped@41; play0/1:dropped@44; play0/1:timeout@71; play1/0:done@32; play1/1:timeout@71