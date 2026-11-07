# Rehearsal feedback — iteration 134 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.52, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 38.83}
  role0 prep: grab box to climb[yaw3,door] release -> [when ramp_inside] grab ramp to climb[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[yaw3,door] release -> [when ramp_inside] grab ramp to climb[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.256
- hider win-rate: 0.17
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.8
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.85, mean max seeker z: 0.22

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.14, 1.17] | seeker 2 saw hider 1 at play step 45 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@3; prep0/1:dropped@4; prep0/1:dropped@10; prep0/1:done@15; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@18; prep1/1:dropped@19; prep1/1:done@28; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.6, 0.89] | seeker 3 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@15; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 1.05] | seeker 2 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@16; play1/0:dropped@32; play1/0:done@44
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.62, 0.0] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@4; play0/0:dropped@32; play0/0:done@59; prep1/0:done@24; play1/0:dropped@32; play1/0:done@44
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.82, 1.71] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@24; play0/0:dropped@32; play0/0:done@48; prep1/0:done@17; play1/0:dropped@32; play1/0:dropped@38; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.95, 0.26] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@8; play1/0:dropped@32; play1/0:done@39; play1/1:dropped@42; play1/1:done@42; play1/2:dropped@47; play1/2:dropped@52; play1/2:dropped@56
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.91, 0.76] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@12; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.81, 0.83] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@4; play0/0:dropped@32; play0/0:done@51; prep1/0:done@17; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71