# Rehearsal feedback — iteration 160 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.68, 'tol': 0.33, 'offset': 0.24, 'seg_timeout': 38.83}
  role0 prep: grab box to teammate[align,door] release | play: segments then to stay[yaw0,door] release -> grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to teammate[align,door] release | play: segments then grab box to outside_wall[yaw2,door] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.255
- hider win-rate: 0.20
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 35.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.75, mean max seeker z: 0.23

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.86, 0.65] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; play0/0:timeout@70; play0/1:dropped@71; prep1/0:dropped@14; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.29, 1.28] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@15; play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.4, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:timeout@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.42, 1.35] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@32; play0/1:dropped@33; play0/1:dropped@37; play0/1:done@43; play0/2:done@44; play1/0:done@62
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.95, 0.33] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@16; prep0/0:dropped@18; play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.17, 0.59] | seeker 2 saw hider 0 at play step 37 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.72, 0.48] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:done@57
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.5, 2.39] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:done@35; play1/1:timeout@74