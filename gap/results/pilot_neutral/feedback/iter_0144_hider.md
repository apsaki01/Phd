# Rehearsal feedback — iteration 144 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.65, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 38.83}
  role0 prep: (none) | play: segments then to stay[yaw0,door] release -> grab box to outside_wall[align,door] -> grab box to stay[yaw3,door] lock
  role1 prep: (none) | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.283
- hider win-rate: 0.30
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.8
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.82, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play0/2:dropped@72; play1/0:dropped@43; play1/0:done@55
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play0/2:dropped@72; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:dropped@44; play0/1:timeout@71; play0/2:dropped@72; play1/0:done@48
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:done@62; play1/0:done@46
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:done@42; play1/0:dropped@55; play1/0:done@57
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:done@50; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play0/2:dropped@72; play1/0:dropped@41; play1/0:dropped@43; play1/0:done@63