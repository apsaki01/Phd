# Rehearsal feedback — iteration 132 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.52, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 38.83}
  role0 prep: grab box to climb[yaw3,door] release -> [when ramp_inside] grab ramp to climb[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[yaw3,door] release -> [when ramp_inside] grab ramp to climb[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.252
- hider win-rate: 0.20
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.4
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.85, mean max seeker z: 0.23

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.83, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; play0/0:dropped@32; play0/0:dropped@36; play0/0:dropped@46; play0/0:done@54; prep1/0:done@13; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.46] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; play0/0:dropped@32; play0/0:done@39; play0/1:timeout@78; play0/2:dropped@79; prep1/0:done@10; play1/0:dropped@32; play1/0:done@52
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.59] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@14; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.19, 0.28] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@16; prep0/0:done@19; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@13; play1/0:dropped@32; play1/0:dropped@36; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.17, 0.61] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; play0/0:dropped@32; play0/0:dropped@38; play0/0:done@54; prep1/0:done@18; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.7, 0.76] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@11; play0/0:dropped@32; play0/0:done@39; play0/1:timeout@78; play0/2:dropped@79; prep1/0:done@16; play1/0:dropped@32; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.58, 1.93] | seeker 3 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; play0/0:dropped@32; play0/0:dropped@40; play0/0:dropped@44; play0/0:dropped@67; play0/0:done@68; prep1/0:done@21; play1/0:dropped@32; play1/0:dropped@35; play1/0:done@39; play1/1:timeout@78; play1/2:dropped@79
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.87, 0.83] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; play0/0:dropped@32; play0/0:dropped@37; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; prep1/0:done@12; play1/0:dropped@32; play1/0:done@63